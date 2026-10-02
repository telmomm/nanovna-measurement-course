import numpy as np
import skrf as rf

from vnacourse.calibration import correct, solve_error_terms
from vnacourse.data import load_repetitions
from vnacourse.errormodel import ErrorTerms, apply_error_model, synthetic_error_terms
from vnacourse.reflection import gamma_to_z, z_to_gamma

F_HZ = np.linspace(50e3, 1.45e9, 51)
ONES = np.ones(F_HZ.shape)


def test_perfect_instrument_reports_the_truth():
    perfect = ErrorTerms(directivity=0, source_match=0, tracking=1)
    assert np.allclose(apply_error_model(0.2 + 0.1j, perfect), 0.2 + 0.1j)


def test_impedance_conversions_are_inverse():
    z = np.array([10, 50, 75 + 20j])
    assert np.allclose(gamma_to_z(z_to_gamma(z)), z)
    assert np.isclose(z_to_gamma(75), 0.2)


def test_sol_recovers_synthetic_terms_and_dut():
    terms = synthetic_error_terms(F_HZ)
    measured = [apply_error_model(g * ONES, terms) for g in (-1, 1, 0)]
    found = solve_error_terms(measured)
    for a, b in zip(found, terms, strict=True):
        assert np.allclose(a, b)

    dut = z_to_gamma(75) * ONES
    assert np.allclose(correct(apply_error_model(dut, terms), found), dut)


def test_sol_accepts_non_ideal_standard_definitions():
    terms = synthetic_error_terms(F_HZ)
    omega = 2 * np.pi * F_HZ
    actual = [z_to_gamma(1j * omega * 0.3e-9), z_to_gamma(1 / (1j * omega * 0.1e-12)), 0.015]
    measured = [apply_error_model(g * ONES, terms) for g in actual]
    found = solve_error_terms(measured, actual)
    for a, b in zip(found, terms, strict=True):
        assert np.allclose(a, b)


def test_sol_agrees_with_scikit_rf_on_recorded_data():
    f_hz, short = load_repetitions("standards", "short")
    _, open_ = load_repetitions("standards", "open")
    _, load = load_repetitions("standards", "load")
    measured = [reps.mean(axis=0) for reps in (short, open_, load)]
    ours = solve_error_terms(measured)

    frequency = rf.Frequency.from_f(f_hz, unit="Hz")

    def network(gamma):
        return rf.Network(frequency=frequency, s=gamma * np.ones(len(f_hz), dtype=complex), z0=50)

    cal = rf.calibration.OnePort(
        measured=[network(m) for m in measured],
        ideals=[network(g) for g in (-1, 1, 0)],
    )
    cal.run()
    assert np.allclose(cal.coefs["directivity"], ours.directivity)
    assert np.allclose(cal.coefs["source match"], ours.source_match)
    assert np.allclose(cal.coefs["reflection tracking"], ours.tracking)


def test_recorded_resistors_read_nominal_at_low_frequency():
    f_hz, short = load_repetitions("standards", "short")
    terms = solve_error_terms(
        [load_repetitions("standards", name)[1].mean(axis=0) for name in ("short", "open", "load")]
    )
    assert short.shape == (10, 1001)

    low = f_hz < 10e6
    for folder, nominal in (("load_33ohm", 33), ("load_75ohm", 75)):
        _, reps = load_repetitions("dut", folder)
        resistance = gamma_to_z(correct(reps.mean(axis=0), terms)).real[low]
        assert np.all(np.abs(resistance - nominal) < 2.5)
