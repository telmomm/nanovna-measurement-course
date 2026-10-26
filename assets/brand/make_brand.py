"""Render the brand images of the course: README banners and the social preview.

The images are committed, so this only needs to run when the identity changes:

    python assets/brand/make_brand.py

It needs the IBM Plex Sans and IBM Plex Mono OpenType files. They ship with
TeX Live (package ``plex``); set ``PLEX_FONT_DIR`` to use another copy.

The motif on the right of every image is computed, not drawn: a 75 Ω
resistor seen by the synthetic instrument of notebooks 02 and 03 (orange,
raw reading) and the same resistor after SOL calibration (blue, one point).
"""

import os
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch  # noqa: E402

from vnacourse.calibration import correct, solve_error_terms  # noqa: E402
from vnacourse.errormodel import apply_error_model, synthetic_error_terms  # noqa: E402
from vnacourse.reflection import z_to_gamma  # noqa: E402

HERE = Path(__file__).resolve().parent

# Brand colours (see BRAND.md).
SCREEN = "#0e1116"
SCREEN_RAISED = "#1a2029"
PAPER = "#fcfcfb"
SHORT_BLUE = "#2a78d6"
OPEN_ORANGE = "#eb6834"
LOAD_GREEN = "#1baf7a"
GRID_LIGHT = "#e4e3df"
GRID_DARK = "#2a313c"
MUTED_LIGHT = "#52514e"
MUTED_DARK = "#9aa3ae"

# IBM Plex Mono has no Greek letters; fall back to Plex Sans for Γ and Ω.
MONO = ["IBM Plex Mono", "IBM Plex Sans"]

TEXT = {
    "en": {
        "tagline": "Learn to measure with a VNA.\nWithout owning one.",
        "raw": "raw 75 Ω",
        "calibrated": "after SOL",
    },
    "es": {
        "tagline": "Aprende a medir con un VNA.\nSin tener uno.",
        "raw": "75 Ω en bruto",
        "calibrated": "tras SOL",
    },
}


def load_plex():
    """Register IBM Plex with Matplotlib and return the font directory."""
    font_dir = os.environ.get("PLEX_FONT_DIR")
    if not font_dir:
        found = subprocess.run(
            ["kpsewhich", "IBMPlexSans-Regular.otf"], capture_output=True, text=True
        ).stdout.strip()
        font_dir = str(Path(found).parent) if found else ""
    if not font_dir or not Path(font_dir).is_dir():
        raise SystemExit("IBM Plex not found: install TeX Live's plex or set PLEX_FONT_DIR.")
    for path in Path(font_dir).glob("IBMPlex[SM]*-*.otf"):
        font_manager.fontManager.addfont(str(path))
    return font_dir


def motif_traces():
    """Raw and calibrated reflection of 75 Ω on the synthetic instrument."""
    f_hz = np.linspace(50e6, 1.45e9, 600)
    terms = synthetic_error_terms(f_hz)
    measured_standards = [apply_error_model(np.full_like(f_hz, g), terms) for g in (-1, 1, 0)]
    raw = apply_error_model(np.full(f_hz.shape, z_to_gamma(75.0)), terms)
    calibrated = correct(raw, solve_error_terms(measured_standards))
    return raw, calibrated


def smith_motif(ax, cx, cy, radius, dark, labels=None, lang="en"):
    """Smith chart with the raw spiral and the calibrated point, in pixels."""
    grid = GRID_DARK if dark else GRID_LIGHT
    rim = "#5b6573" if dark else MUTED_LIGHT
    ground = SCREEN if dark else PAPER
    chart = Circle((cx, cy), radius, transform=ax.transData)

    def gx(g):
        return cx + radius * np.real(g)

    def gy(g):
        return cy - radius * np.imag(g)

    ax.plot([cx - radius, cx + radius], [cy, cy], color=grid, lw=0.8)
    turn = np.linspace(0, 2 * np.pi, 400)
    for r in (0.2, 0.5, 1, 2, 5):
        c, rr = r / (1 + r), 1 / (1 + r)
        ax.plot(gx(c + rr * np.exp(1j * turn)), gy(c + rr * np.exp(1j * turn)), color=grid, lw=0.8)
    for x in (0.2, 0.5, 1, 2, 5):
        for sign in (1, -1):
            arc = 1 + 1j * sign / x + (1 / x) * np.exp(1j * turn)
            (line,) = ax.plot(gx(arc), gy(arc), color=grid, lw=0.8)
            line.set_clip_path(chart)
    ax.add_patch(Circle((cx, cy), radius, fill=False, ec=rim, lw=1.4))

    raw, calibrated = motif_traces()
    ax.plot(gx(raw), gy(raw), color=OPEN_ORANGE, lw=1.6, solid_joinstyle="round")
    ax.plot(
        gx(calibrated.mean()),
        gy(calibrated.mean()),
        "o",
        ms=radius * 0.075,
        color=SHORT_BLUE,
        mec=ground,
        mew=1.5,
    )
    ax.plot(gx(-1), gy(0), "o", ms=radius * 0.05, color=SHORT_BLUE)
    ax.plot(gx(1), gy(0), "o", ms=radius * 0.05, color=OPEN_ORANGE)

    if labels:
        text = TEXT[lang]
        color = "#c9d0d8" if dark else MUTED_LIGHT
        y = cy + radius + labels
        ax.plot([cx - 150, cx - 128], [y, y], color=OPEN_ORANGE, lw=2.4)
        ax.text(cx - 120, y, text["raw"], va="center", family=MONO, size=11.5, color=color)
        ax.plot(cx + 22, y, "o", ms=8, color=SHORT_BLUE)
        ax.text(cx + 34, y, text["calibrated"], va="center", family=MONO, size=11.5, color=color)


def mark(ax, x, y, size, dark):
    """The brand mark centred at (x, y), ``size`` pixels across."""
    ink = PAPER if dark else SCREEN
    r = size / 2.5
    ax.add_patch(Circle((x, y), r, fill=False, ec=ink, lw=r * 0.09 * 0.72))
    ax.plot([x - r, x + r], [y, y], color=ink, lw=r * 0.05 * 0.72)
    for dx, color in ((-r, SHORT_BLUE), (0, LOAD_GREEN), (r, OPEN_ORANGE)):
        ax.add_patch(Circle((x + dx, y), r * 0.2, color=color, lw=0))


def canvas(width, height, ground):
    """A figure whose data coordinates are pixels, origin at the top left."""
    fig = plt.figure(figsize=(width / 100, height / 100), dpi=100)
    fig.patch.set_facecolor(ground)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def px(size):
    """Font size in points for a size in pixels at 100 dpi."""
    return size * 0.72


def banner(lang, dark, path):
    width, height = 1280, 360
    ground = SCREEN if dark else PAPER
    ink = PAPER if dark else SCREEN
    muted = MUTED_DARK if dark else MUTED_LIGHT
    fig, ax = canvas(width, height, ground)
    if not dark:
        ax.add_patch(
            FancyBboxPatch(
                (1, 1),
                width - 2,
                height - 2,
                boxstyle="round,pad=0,rounding_size=16",
                fill=False,
                ec=GRID_LIGHT,
                lw=1.5,
            )
        )
    mark(ax, 104, 108, 84, dark)
    ax.text(
        160,
        108,
        "Hands-on VNA",
        va="center",
        family="IBM Plex Sans",
        weight="bold",
        size=px(60),
        color=ink,
    )
    ax.text(
        64,
        190,
        "nanovna-measurement-course",
        va="center",
        family="IBM Plex Mono",
        size=px(19),
        color=muted,
    )
    ax.text(
        64,
        272,
        TEXT[lang]["tagline"],
        va="center",
        family="IBM Plex Sans",
        weight="medium",
        size=px(29),
        color=ink,
        linespacing=1.3,
    )
    smith_motif(ax, 1060, 180, 140, dark)
    fig.savefig(path, dpi=200, facecolor=ground)
    plt.close(fig)


def social_preview(path):
    """GitHub social preview, 1280×640 (Settings › Social preview)."""
    width, height = 1280, 640
    fig, ax = canvas(width, height, SCREEN)
    mark(ax, 102, 138, 50, dark=True)
    ax.text(
        140,
        138,
        "telmomm / nanovna-measurement-course",
        va="center",
        family="IBM Plex Mono",
        size=px(20),
        color=MUTED_DARK,
    )
    ax.text(
        80,
        268,
        "Hands-on vector network\nanalysis with a NanoVNA",
        va="center",
        family="IBM Plex Sans",
        weight="bold",
        size=px(56),
        color=PAPER,
        linespacing=1.1,
    )
    subtitle = "Derive the error model, simulate it, and\ncalibrate real measurements in Jupyter."
    ax.text(
        80,
        400,
        subtitle,
        va="center",
        family="IBM Plex Sans",
        size=px(24),
        color="#c9d0d8",
        linespacing=1.35,
    )
    x = 80
    chips = (
        ("5 notebooks", "#3a4350", PAPER),
        ("EN · ES", "#3a4350", PAPER),
        ("no hardware needed", OPEN_ORANGE, "#f39a6f"),
        ("Binder · Colab", "#3a4350", PAPER),
    )
    for label, edge, color in chips:
        w = 18 + 10.2 * len(label)
        ax.add_patch(
            FancyBboxPatch(
                (x, 480), w, 38, boxstyle="round,pad=0,rounding_size=19", fill=False, ec=edge, lw=1
            )
        )
        ax.text(
            x + w / 2,
            499,
            label,
            ha="center",
            va="center",
            family="IBM Plex Mono",
            size=px(17),
            color=color,
        )
        x += w + 10
    smith_motif(ax, 1000, 300, 200, dark=True, labels=40)
    fig.savefig(path, dpi=100, facecolor=SCREEN)
    plt.close(fig)


def cover_motif(path):
    """The motif alone, as vector art for the cover of the PDF book."""
    size = 600
    fig, ax = canvas(size, size, SCREEN)
    smith_motif(ax, size / 2, size / 2, size * 0.46, dark=True)
    fig.savefig(path, facecolor=SCREEN)
    plt.close(fig)


def main():
    load_plex()
    for lang in TEXT:
        for dark in (False, True):
            banner(lang, dark, HERE / f"banner-{lang}-{'dark' if dark else 'light'}.png")
    social_preview(HERE / "social-preview.png")
    cover_motif(HERE.parents[1] / "book" / "latex" / "cover-motif.pdf")


if __name__ == "__main__":
    main()
