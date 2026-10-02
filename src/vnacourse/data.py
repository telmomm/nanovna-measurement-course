"""Access to the recorded measurements shipped with the course."""

from pathlib import Path

import numpy as np
import skrf as rf

# In a clone of the repository the data lives in <repo>/data. In a regular
# (non-editable) install the build copies it next to this module instead.
_REPO_DATA = Path(__file__).resolve().parents[2] / "data"
_PACKAGED_DATA = Path(__file__).resolve().parent / "_data"


def data_dir():
    """Folder that holds the course data."""
    for candidate in (_REPO_DATA, _PACKAGED_DATA):
        if (candidate / "standards").is_dir():
            return candidate
    raise FileNotFoundError(
        "Course data not found. Clone the repository or reinstall the vnacourse package."
    )


def load_repetitions(*parts):
    """Load every repetition of one measurement, e.g. ``("standards", "open")``.

    Returns the frequency axis in Hz, shape ``(n_freq,)``, and the measured
    reflection coefficients, shape ``(n_repetitions, n_freq)``.
    """
    folder = data_dir().joinpath(*parts)
    files = sorted(folder.glob("*.s1p"))
    if not files:
        raise FileNotFoundError(f"No .s1p files in {folder}")

    networks = [rf.Network(str(path)) for path in files]
    f_hz = networks[0].f
    for path, network in zip(files, networks, strict=True):
        if network.f.shape != f_hz.shape or not np.allclose(network.f, f_hz):
            raise ValueError(f"{path.name} does not share the frequency grid of {files[0].name}")
    return f_hz, np.stack([network.s[:, 0, 0] for network in networks])
