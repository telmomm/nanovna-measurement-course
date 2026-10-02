"""One-port SOL (short-open-load) calibration.

Derived step by step in notebook 03; kept here so later notebooks can reuse it.
"""

import numpy as np

from vnacourse.errormodel import ErrorTerms

# Reflection coefficients of ideal standards, in the order short, open, load.
IDEAL_SOL = (-1.0, 1.0, 0.0)


def solve_error_terms(measured, actual=IDEAL_SOL):
    """Error terms from three standards.

    ``measured`` holds what the instrument reported for each standard: three
    arrays, one value per frequency. ``actual`` holds the true reflection
    coefficient of each standard, as scalars or as arrays of the same length.

    At each frequency the model ``m = e00 + g*m*e11 - g*delta`` is linear in
    the unknowns ``(e00, e11, delta)``, with ``delta = e00*e11 - e10e01``.
    """
    m = np.stack([np.asarray(x, dtype=complex) for x in measured], axis=-1)  # (n_freq, 3)
    g = np.stack(np.broadcast_arrays(*[np.asarray(x, dtype=complex) for x in actual]), axis=-1)
    g = np.broadcast_to(g, m.shape)

    matrix = np.stack([np.ones_like(m), g * m, -g], axis=-1)  # (n_freq, 3, 3)
    e00, e11, delta = np.moveaxis(np.linalg.solve(matrix, m[..., None])[..., 0], -1, 0)
    return ErrorTerms(directivity=e00, source_match=e11, tracking=e00 * e11 - delta)


def correct(gamma_measured, terms):
    """Remove the systematic errors from a measured reflection coefficient."""
    e00, e11, tracking = terms
    return (gamma_measured - e00) / (tracking + e11 * (gamma_measured - e00))
