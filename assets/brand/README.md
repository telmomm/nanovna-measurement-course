<img src="mark.svg" width="72" alt="Hands-on VNA mark">

# Visual identity

**English** · [Español](README.es.md)

The visual identity of *Hands-on VNA*, applied to the README, the web book,
the PDF book and the figures of the notebooks. It comes from a design canvas
kept by the author, which also holds the launch material (social posts, A4
poster, LinkedIn banner, launch copy).

## The mark

The Smith chart reduced to its essentials: the unit circle, the real axis,
and the three SOL calibration standards where they really are. **Short** at
Γ = −1 (blue), **Load** at Γ = 0 (green), **Open** at Γ = +1 (orange). The
three colours are the first three series colours of the notebooks' figures,
so the mark and the material speak the same language.

| File | Use |
|---|---|
| [`mark.svg`](mark.svg) | on light grounds (web book logo in light mode, PDF) |
| [`mark-dark.svg`](mark-dark.svg) | on dark grounds (web book logo in dark mode) |
| [`favicon.svg`](favicon.svg) | browser tab: the mark on a paper tile |
| `banner-{en,es}-{light,dark}.png` | README header, one per language and colour scheme |
| `social-preview.png` | GitHub *Settings › Social preview*, 1280×640 |

## Colour

| Name | Hex | Role |
|---|---|---|
| Screen | `#0E1116` | ink; dark grounds (cover, announcement bar, dark mode) |
| Paper | `#FCFCFB` | light ground; text on Screen |
| Short · calibrated | `#2A78D6` | links, primary accent, the calibrated result |
| Open · raw | `#EB6834` | what the instrument reads before calibration; warnings. Use `#C4501F` for orange text on Paper (contrast) |
| Load | `#1BAF7A` | the third standard only |
| Grid | `#E4E3DF` | rules, borders, chart grid |
| Muted | `#52514E` | secondary text on Paper; `#9AA3AE` on Screen |

Orange is what the instrument reads; blue is what is left after
calibration. Keep green for the third standard.

## Type

- **IBM Plex Sans** for everything: headings at weight 700, text at 400/500.
- **IBM Plex Mono** for data, labels, file names and formulas in running
  text. It has no Greek letters: Γ and Ω fall back to Plex Sans.
- **IBM Plex Math** for equations in the PDF.

All three are open (SIL Open Font License). The web book loads them from
Google Fonts; the PDF uses the copies in TeX Live (`plex` package); figures
use Plex Sans when it is installed.

## The motif

A 75 Ω resistor seen by an uncalibrated instrument wanders around the centre
of the Smith chart (orange); after SOL calibration it is a single point at
Γ = 0.2 (blue). It tells the module in one glance. In this repository it is
computed, not drawn: [`make_brand.py`](make_brand.py) uses the synthetic
instrument of notebooks 02 and 03.

## Voice

- **Precise, not grandiose.** Real figures from the repository; never
  "revolutionary".
- **Invite a prediction.** A question before a promise: "what will you see
  before you run it?".
- **Honest about status.** Version 0.1.0, not yet used in a classroom: say so,
  and turn it into an invitation.

## Where it is applied

| Place | File |
|---|---|
| README (both languages) | `README.md`, `README.es.md` |
| Web book: fonts, colours, logo, announcement bar | [`book/_static/brand.css`](../../book/_static/brand.css), `book/*/_config.yml` |
| PDF book: cover, fonts, chapter headings, colours | [`book/latex/handsonvna.sty`](../../book/latex/handsonvna.sty) |
| Figures in the notebooks | `vnacourse.plotting.use_course_style` |

## Regenerating the images

```bash
python assets/brand/make_brand.py
```

It needs the IBM Plex OpenType files (TeX Live's `plex`, or set
`PLEX_FONT_DIR`). It writes the banners, the social preview and
`book/latex/cover-motif.pdf`.
