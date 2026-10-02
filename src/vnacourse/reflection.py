"""Conversions between reflection coefficient and impedance."""

import numpy as np

Z0 = 50.0


def z_to_gamma(z, z0=Z0):
    """Reflection coefficient of an impedance ``z`` seen from a ``z0`` port."""
    z = np.asarray(z, dtype=complex)
    return (z - z0) / (z + z0)


def gamma_to_z(gamma, z0=Z0):
    """Impedance that produces the reflection coefficient ``gamma`` on a ``z0`` port."""
    gamma = np.asarray(gamma, dtype=complex)
    return z0 * (1 + gamma) / (1 - gamma)
