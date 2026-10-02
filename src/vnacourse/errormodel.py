"""One-port, three-term error model of a reflection measurement.

The model is derived step by step in notebook 02; the functions here are the
same ones, kept in the package so later notebooks can reuse them.
"""

from typing import NamedTuple

import numpy as np


class ErrorTerms(NamedTuple):
    """The three systematic error terms, one complex value per frequency."""

    directivity: np.ndarray  # e00
    source_match: np.ndarray  # e11
    tracking: np.ndarray  # e10 * e01


def apply_error_model(gamma, terms):
    """What an imperfect instrument reports for a true reflection ``gamma``."""
    e00, e11, tracking = terms
    return e00 + tracking * gamma / (1 - e11 * gamma)


def synthetic_error_terms(f_hz):
    """Error terms of the made-up instrument used in notebooks 02 and 03.

    The values are exaggerated on purpose so that every effect is visible in
    a plot. They do not describe any real instrument.
    """
    f_hz = np.asarray(f_hz, dtype=float)
    x = f_hz / 1.45e9  # 0..1 over the band used in the course
    directivity = 0.08 * np.exp(1j * (0.6 + 2 * np.pi * f_hz * 0.4e-9))
    source_match = 0.20 * np.exp(1j * (1.0 - 2 * np.pi * f_hz * 2.0e-9))
    tracking = (0.95 - 0.15 * x) * np.exp(-2j * np.pi * f_hz * 1.2e-9)
    return ErrorTerms(directivity, source_match, tracking)
