"""Shared plot style and the few figure helpers the notebooks need."""

import matplotlib.pyplot as plt
import numpy as np
import skrf as rf
from cycler import cycler

# Categorical colours, always used in this order. The first three stay
# distinguishable under the common forms of colour blindness.
SERIES = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948")
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
GRID = "#e4e3df"
SURFACE = "#fcfcfb"


def use_course_style():
    """Apply the course plot style to every figure created afterwards."""
    plt.rcParams.update(
        {
            "figure.facecolor": SURFACE,
            "axes.facecolor": SURFACE,
            "savefig.facecolor": SURFACE,
            "figure.figsize": (7.5, 4.0),
            "figure.dpi": 110,
            "figure.constrained_layout.use": True,
            "axes.prop_cycle": cycler(color=SERIES),
            "axes.edgecolor": INK_SECONDARY,
            "axes.labelcolor": INK_SECONDARY,
            "axes.titlecolor": INK,
            "axes.titlesize": 11,
            "axes.titleweight": "bold",
            "axes.titlelocation": "left",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.axisbelow": True,
            "grid.color": GRID,
            "grid.linewidth": 0.8,
            "xtick.color": INK_SECONDARY,
            "ytick.color": INK_SECONDARY,
            "text.color": INK,
            "lines.linewidth": 1.6,
            "lines.markersize": 7,
            "legend.frameon": False,
        }
    )


def gamma_plane(ax, radius=1.0, title=None):
    """Turn ``ax`` into a reflection-coefficient plane.

    With ``radius=1`` the Smith chart grid is drawn. A larger ``radius``
    leaves room for (unphysical) raw readings outside the unit circle; then
    only the unit circle is drawn, over a plain grid.
    """
    if radius <= 1.0:
        rf.plotting.smith(ax=ax, draw_labels=False)
        ax.grid(False)
    else:
        ax.axhline(0, color=GRID, linewidth=0.8, zorder=0)
        ax.axvline(0, color=GRID, linewidth=0.8, zorder=0)
        ax.set_xlabel("Re Γ")
        ax.set_ylabel("Im Γ")
    turn = np.linspace(0, 2 * np.pi, 361)
    ax.plot(np.cos(turn), np.sin(turn), color=INK_SECONDARY, linewidth=1.0, zorder=1)
    ax.set_aspect("equal")
    ax.set_xlim(-radius * 1.05, radius * 1.05)
    ax.set_ylim(-radius * 1.05, radius * 1.05)
    if title:
        ax.set_title(title)
    return ax


def draw_error_adapter(ax=None):
    """Signal-flow graph of the three-term error model."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7.5, 3.0))

    left, right, top, bottom = 0.0, 3.0, 1.0, 0.0
    nodes = {
        "a": (left, top),
        "b": (left, bottom),
        "in": (right, top),
        "out": (right, bottom),
    }

    def arrow(start, end, label, offset, color=INK):
        (x0, y0), (x1, y1) = nodes[start], nodes[end]
        ax.annotate(
            "",
            xy=(x1, y1),
            xytext=(x0, y0),
            arrowprops={
                "arrowstyle": "-|>",
                "color": color,
                "linewidth": 1.6,
                "shrinkA": 7,
                "shrinkB": 7,
            },
        )
        ax.text(
            (x0 + x1) / 2 + offset[0],
            (y0 + y1) / 2 + offset[1],
            label,
            ha="center",
            va="center",
            fontsize=12,
            color=INK,
        )

    arrow("a", "in", "1", (0, 0.13))
    arrow("a", "b", "$e_{00}$\ndirectivity", (0.48, 0), SERIES[0])
    arrow("out", "in", "$e_{11}$\nsource match", (-0.55, 0), SERIES[1])
    arrow("out", "b", "$e_{10}e_{01}$   reflection tracking", (0, -0.15), SERIES[2])
    ax.annotate(
        "",
        xy=(right + 1.0, bottom),
        xytext=(right + 1.0, top),
        arrowprops={
            "arrowstyle": "-|>",
            "color": INK,
            "linewidth": 1.6,
            "shrinkA": 7,
            "shrinkB": 7,
        },
    )
    ax.plot([right, right + 1.0], [top, top], color=INK, linewidth=1.6)
    ax.plot([right, right + 1.0], [bottom, bottom], color=INK, linewidth=1.6)
    ax.text(right + 1.2, 0.5, "Γ\n(DUT)", ha="left", va="center", fontsize=12)

    for x, y in nodes.values():
        ax.plot(x, y, "o", color=INK, markersize=6, zorder=3)
    ax.text(left - 0.15, top, "sent", ha="right", va="center", color=INK_SECONDARY)
    ax.text(left - 0.15, bottom, "received", ha="right", va="center", color=INK_SECONDARY)
    ax.text(
        (left + right) / 2,
        top + 0.45,
        "error adapter (the imperfect instrument)",
        ha="center",
        color=INK_SECONDARY,
    )
    ax.axvline(right, color=GRID, linewidth=1.0, linestyle="--", zorder=0)
    ax.text(right, bottom - 0.42, "reference plane", ha="center", color=INK_SECONDARY)

    ax.set_xlim(left - 1.0, right + 2.0)
    ax.set_ylim(bottom - 0.55, top + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax
