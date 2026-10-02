import numpy as np
import pytest

from vnacourse.puzzles import mystery_trace
from vnacourse.reflection import gamma_to_z

F_HZ = np.linspace(10e6, 1.45e9, 50)


@pytest.mark.parametrize(("name", "resistance"), [("A", 30), ("C", 60)])
def test_series_mystery_circuits_have_constant_resistance(name, resistance):
    assert np.allclose(gamma_to_z(mystery_trace(name, F_HZ)).real, resistance)


def test_parallel_mystery_circuit_has_constant_conductance():
    assert np.allclose((1 / gamma_to_z(mystery_trace("B", F_HZ))).real, 1 / 120)


def test_mystery_traces_are_passive():
    for name in "ABC":
        assert np.all(np.abs(mystery_trace(name, F_HZ)) <= 1)


def test_unknown_mystery_circuit_is_rejected():
    with pytest.raises(ValueError, match="Unknown mystery circuit"):
        mystery_trace("D", F_HZ)
