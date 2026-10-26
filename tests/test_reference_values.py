"""Numbers quoted in the text of the course, recomputed from the code and the data.

Each test names where the number is quoted. If one fails after a change to the
data or the package, update the text in both languages (notebooks/ and es/)
and the instructor guide, not only the expected value here.
"""

import itertools

import numpy as np
import pytest

from vnacourse.calibration import correct, solve_error_terms
from vnacourse.data import load_repetitions
from vnacourse.errormodel import apply_error_model, synthetic_error_terms
from vnacourse.reflection import gamma_to_z, z_to_gamma

C0 = 299_792_458.0
V = 0.7 * C0


@pytest.fixture(scope="module")
def recorded():
    f_hz, short = load_repetitions("standards", "short")
    _, open_ = load_repetitions("standards", "open")
    _, load = load_repetitions("standards", "load")
    _, r33 = load_repetitions("dut", "load_33ohm")
    _, r75 = load_repetitions("dut", "load_75ohm")
    return {"f": f_hz, "standards": (short, open_, load), "r33": r33, "r75": r75}


def full_calibration(recorded):
    return solve_error_terms([reps.mean(axis=0) for reps in recorded["standards"]])


def line_delay(gamma, f_hz):
    """One-way delay from the slope of the unwrapped phase (notebook 03, section 4.2)."""
    return -np.polyfit(f_hz, np.unwrap(np.angle(gamma)), 1)[0] / (4 * np.pi)


def spread(repetitions):
    return np.sqrt(repetitions.real.var(axis=0, ddof=1) + repetitions.imag.var(axis=0, ddof=1))


# Analytic reference cases (notebooks 00 and 01) ------------------------------


def test_wave_basics_of_notebook_00():
    assert V / 300e6 == pytest.approx(0.70, abs=0.005)
    assert 0.20 / V * 1e9 == pytest.approx(0.95, abs=0.005)
    assert abs(z_to_gamma(75)) ** 2 == pytest.approx(0.04)
    assert -20 * np.log10(0.5) == pytest.approx(6.0, abs=0.05)


def test_smith_chart_examples_of_notebook_01():
    assert z_to_gamma(50 - 50j) == pytest.approx(0.2 - 0.4j)
    assert gamma_to_z(0.5j) == pytest.approx(30 + 40j)
    assert gamma_to_z(z_to_gamma(20 - 30j)) == pytest.approx(20 - 30j)
    f0 = 1 / (2 * np.pi * np.sqrt(20e-9 * 5e-12))
    assert f0 / 1e6 == pytest.approx(503, abs=1)


def test_resistor_behind_cable_of_notebook_01():
    f_hz = np.linspace(10e6, 1.45e9, 600)
    gamma = z_to_gamma(75) * np.exp(-4j * np.pi * f_hz * 0.20 / V)
    z = gamma_to_z(gamma).real
    assert z.min() == pytest.approx(33.3, abs=0.2)
    assert z.max() == pytest.approx(75.0, abs=0.1)


# Synthetic instrument (notebooks 02 and 03) -----------------------------------


def test_synthetic_ripple_quoted_in_notebook_03():
    f_hz = np.linspace(50e3, 1.45e9, 401)
    raw = np.abs(
        apply_error_model(z_to_gamma(75) * np.ones(f_hz.shape), synthetic_error_terms(f_hz))
    )
    assert raw.min() == pytest.approx(0.09, abs=0.01)
    assert raw.max() == pytest.approx(0.27, abs=0.01)


# Recorded NanoVNA data (notebooks 02, 03 and 05, data/README.md) --------------


def test_raw_open_exceeds_passivity(recorded):
    _, open_, _ = recorded["standards"]
    assert np.abs(open_.mean(axis=0)).max() == pytest.approx(2.1, abs=0.05)


def test_tracking_is_near_one_above_150_mhz(recorded):
    tracking = np.abs(full_calibration(recorded).tracking[recorded["f"] > 150e6])
    assert np.all(np.abs(tracking - 1) < 0.02)


def test_held_out_residuals_of_notebook_03(recorded):
    standards = recorded["standards"]
    terms = solve_error_terms([reps[:5].mean(axis=0) for reps in standards])
    medians = [
        np.median(np.abs(correct(reps[5:].mean(axis=0), terms) - target))
        for reps, target in zip(standards, (-1, 1, 0), strict=True)
    ]
    short, open_, load = medians
    assert 0.001 < short < 0.005 and 0.001 < open_ < 0.005  # "a few thousandths"
    assert 0.0001 < load < 0.0005  # "a few ten-thousandths"


def test_reference_plane_delay_of_notebook_03(recorded):
    f_hz, terms = recorded["f"], full_calibration(recorded)
    for name in ("r33", "r75"):
        corrected = correct(recorded[name].mean(axis=0), terms)
        assert line_delay(corrected, f_hz) * 1e9 == pytest.approx(1.0, abs=0.1)

    corrected = correct(recorded["r75"].mean(axis=0), terms)
    tau = line_delay(corrected, f_hz)
    z = gamma_to_z(corrected * np.exp(4j * np.pi * f_hz * tau)).real
    assert z.mean() == pytest.approx(75, abs=1)
    assert z.min() - 75 == pytest.approx(-8, abs=1)
    assert z.max() - 75 == pytest.approx(15, abs=1)


def test_repeatability_of_notebook_05(recorded):
    short, open_, load = (np.median(spread(reps)) for reps in recorded["standards"])
    assert short == pytest.approx(0.003, abs=0.0005)
    assert open_ == pytest.approx(0.003, abs=0.0005)
    assert load == pytest.approx(0.0005, abs=0.0001)
    assert 5 < open_ / load < 7  # "about six times better"


def test_noisy_points_follow_blocks_of_100(recorded):
    s = spread(recorded["standards"][1])
    noisy = np.flatnonzero(s > 5 * np.median(s))
    assert np.mean(noisy % 100 < 10) > 0.75


def test_resistance_and_uncertainty_of_notebook_05(recorded):
    f_hz, terms = recorded["f"], full_calibration(recorded)
    short, open_, load = recorded["standards"]
    r75 = recorded["r75"]
    low = f_hz < 10e6

    def resistance(raw, t):
        return gamma_to_z(correct(raw, t)).real[low].mean()

    per_sweep = np.array([resistance(raw, terms) for raw in r75])
    per_cal = np.array(
        [
            resistance(r75.mean(axis=0), solve_error_terms([short[i], open_[i], load[i]]))
            for i in range(len(open_))
        ]
    )
    u = np.hypot(per_sweep.std(ddof=1) / np.sqrt(3), per_cal.std(ddof=1) / np.sqrt(10))
    assert resistance(r75.mean(axis=0), terms) == pytest.approx(74.0, abs=0.05)
    assert u == pytest.approx(0.2, abs=0.05)


def test_calibrated_open_scatters_around_one(recorded):
    standards = recorded["standards"]
    terms = solve_error_terms([reps[:5].mean(axis=0) for reps in standards])
    magnitude = np.abs(correct(standards[1][5:].mean(axis=0), terms))
    assert 0.35 < np.mean(magnitude > 1) < 0.5  # "a little under half of the points"
    assert np.mean(magnitude > 1.01) < 0.01


def test_expected_values_of_the_assignment(recorded):
    """Instructor guide, section 9: every choice of three repetitions out of ten."""
    f_hz = recorded["f"]
    standards, r33 = recorded["standards"], recorded["r33"]
    low = f_hz < 10e6
    for chosen in itertools.combinations(range(10), 3):
        chosen = list(chosen)
        held_out = [i for i in range(10) if i not in chosen]
        terms = solve_error_terms([reps[chosen].mean(axis=0) for reps in standards])
        corrected = correct(r33.mean(axis=0), terms)

        assert 32.3 <= gamma_to_z(corrected).real[low].mean() <= 32.5
        assert line_delay(corrected, f_hz) * 1e9 == pytest.approx(1.05, abs=0.01)
        held_out_open = np.abs(correct(standards[1][held_out].mean(axis=0), terms) - 1)
        assert 0.0015 <= np.median(held_out_open) <= 0.0018
        per_sweep = np.array([gamma_to_z(correct(raw, terms)).real[low].mean() for raw in r33])
        assert per_sweep.std(ddof=1) / np.sqrt(3) == pytest.approx(0.09, abs=0.01)
