"""Mystery circuits for the "guess the circuit" activity of notebook 01.

Reading this file gives the answers away. Try the activity first.
"""

import numpy as np

from vnacourse.reflection import z_to_gamma


def mystery_trace(name, f_hz):
    """Reflection coefficient of mystery circuit ``"A"``, ``"B"`` or ``"C"``."""
    omega = 2 * np.pi * np.asarray(f_hz, dtype=float)
    if name == "A":
        z = 30 + 1 / (1j * omega * 8e-12)
    elif name == "B":
        z = 1 / (1 / 120 + 1 / (1j * omega * 15e-9))
    elif name == "C":
        z = 60 + 1j * omega * 30e-9 + 1 / (1j * omega * 2e-12)
    else:
        raise ValueError(f"Unknown mystery circuit {name!r}: choose 'A', 'B' or 'C'")
    return z_to_gamma(z)
