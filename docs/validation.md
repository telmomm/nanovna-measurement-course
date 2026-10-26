# Technical validation

What has been checked to establish that the module works as specified: the
code computes what the text says, the notebooks run from a clean
installation, the numbers quoted in the lessons come from the code and the
data, and the two language editions stay in step. The [design](design.md)
page describes what the module is meant to do.

```{admonition} What this page does not claim
:class: warning
Technical validation shows that the material is correct and reproducible. It
is not evidence that students learn from it: the module has not yet been used
in a classroom, and no learning outcome has been measured.
```

## 1. Environment

The module needs Python 3.10 or newer and three libraries (NumPy, Matplotlib,
scikit-rf); notebook 05 adds `rfmeasurement`. Versions are pinned only from
below, in [`pyproject.toml`](https://github.com/telmomm/nanovna-measurement-course/blob/main/pyproject.toml)
and [`environment.yml`](https://github.com/telmomm/nanovna-measurement-course/blob/main/environment.yml).

The validation reported here was run on 2026-10-24 in a new virtual
environment created from `pyproject.toml` (`pip install -e ".[book,dev]"`):

| Component | Version |
|---|---|
| Operating system | macOS 26.6.2, arm64 |
| Python | 3.12.9 |
| NumPy / SciPy / Matplotlib | 2.5.4 / 1.18.1 / 3.11.2 |
| scikit-rf | 2.2.0 |
| rfmeasurement | 0.3.0 |
| Jupyter Book / Sphinx | 1.0.4.post1 / 7.4.7 |
| TeX (PDF edition) | XeTeX, TeX Live 2026 |

The continuous-integration workflows in `.github/workflows/` run the same
checks on Ubuntu with Python 3.10, 3.12 and 3.13, and in the conda
environment used by Binder. Their results for this version are not part of
this report: they will be recorded here after the first run on GitHub.

## 2. Checks

| Check | Method | Automated | Result (2026-10-24) |
|---|---|---|---|
| Code style | `ruff check`, `ruff format --check` on the package, tests and all notebooks | yes (CI) | pass |
| Package functions | unit tests in `tests/test_calibration.py`, `test_puzzles.py`, `test_package.py` | yes (CI) | 12 pass |
| Analytic reference cases | `tests/test_reference_values.py`: Γ ↔ Z examples, return loss, wavelength and delay, resonant frequency, a resistor behind a line | yes (CI) | pass |
| Exact recovery on synthetic data | SOL solver recovers the error terms of the synthetic instrument and the true device to rounding error, with ideal and non-ideal standard definitions | yes (CI) | pass |
| Independent implementation | error terms and corrected Γ compared with `skrf.calibration.OnePort` on the recorded data | yes (CI, and in notebook 03) | identical to rounding error |
| Numbers quoted in the text | every number the lessons and the guide state about the data (table in section 3) is recomputed by `tests/test_reference_values.py` | yes (CI) | pass, after one correction (section 4) |
| Expected values of the assignment | the instructor guide's table of expected results, recomputed for all 120 choices of three repetitions out of ten | yes (CI) | all 120 within the stated ranges |
| Notebook execution | all 10 English and 10 Spanish notebooks (lessons and solutions) executed top to bottom with `nbmake` | yes (CI) | 20 pass, 37 s in total |
| Figures and outputs | both books built with `jupyter-book build -W`, which executes every notebook and fails on any warning (broken link, missing figure, failed cell); PDF edition built with XeLaTeX | yes (book workflow) | HTML: no warnings; PDF: built |
| Language parity | `tests/test_translations.py`: each Spanish notebook has the same cells as the English one, and its code is token-for-token the same once comments, strings and layout are removed | yes (CI) | 10 pairs pass |
| Simulated and real data kept apart | inspection: synthetic data only from `vnacourse.errormodel` and `vnacourse.puzzles`; recorded data only through `vnacourse.data.load_repetitions` | no | consistent in every notebook |
| Data provenance | `data/README.md` states that the files are a byte-for-byte copy of the archived source | no | not re-verified against the source in this validation |
| Binder and Colab | launch badges in every notebook | no | not tested in this validation |

To reproduce the automated checks:

```bash
python -m pip install -e ".[book,dev]"
ruff check . && ruff format --check .
pytest                                            # unit, reference and parity tests
pytest --nbmake notebooks exercises es            # all 20 notebooks
tools/build_book.sh                               # both books, HTML and PDF
```

## 3. Numbers quoted in the lessons

| Where | Statement | Recomputed |
|---|---|---|
| 00 | wavelength in the cable at 300 MHz; delay of 20 cm | 0.70 m; 0.95 ns |
| 01 | Γ of 50 − j50 Ω; Z at Γ = j0.5; series RLC resonance | 0.2 − 0.4j; 30 + j40 Ω; 503 MHz |
| 01 | 75 Ω behind 20 cm of cable looks like 33 Ω to 75 Ω | 33.3 Ω to 75.0 Ω |
| 02, `data/README.md` | raw open reads up to \|S11\| = 2.1 | 2.13 |
| 03 | raw 75 Ω on the synthetic instrument ripples between about 0.09 and 0.27 | 0.086 to 0.266 |
| 03 | above 150 MHz the tracking is within a few percent of 1 | 0.994 to 1.015 |
| 03 | held-out residual: a few thousandths (short, open), a few ten-thousandths (load) | medians 0.0015, 0.0016, 0.0003 |
| 03 | about 1 ns of line between calibration plane and resistors | 1.05 ns (33 Ω), 1.01 ns (75 Ω) |
| 03 | after removing it, 75 Ω varies by about −8 Ω to +15 Ω in the upper band | 66.6 Ω to 89.5 Ω |
| 05 | typical scatter 0.003 (short, open), 0.0005 (load), about six times better | 0.0029, 0.0031, 0.0005 |
| 05 | noisy points cluster after multiples of 100 | 43 of 53 |
| 05 | 75 Ω below 10 MHz: 74.0 Ω, standard uncertainty about 0.2 Ω | 73.99 Ω, 0.18 Ω |
| 05 | calibrated open above 1 at a little under half of the points | 43 % |
| Guide §9 | assignment: R below 10 MHz 32.3–32.5 Ω; delay about 1.05 ns; held-out open 0.0015–0.0018; u about 0.09 Ω | 32.34–32.47 Ω; 1.048 ns; 0.0015–0.0018; 0.084–0.089 Ω |

## 4. Findings

- **Corrected:** notebook 03 (section 4.2) said that, after removing the
  line delay, the 75 Ω resistor varied by "roughly ±10 Ω" at the top of the
  band. The recomputed range is −8.4 Ω to +14.5 Ω, with the maximum near
  1.41 GHz. The text now says "between about −8 Ω and +15 Ω" in both
  languages, and a test fixes the value.
- No other statement in the lessons, solutions or guide disagreed with the
  code or the data.

## 5. Known issues and limitations

- **`rfmeasurement` 0.3.0 and one-port data.** Its built-in passivity rule
  returns a failure for every one-port network. Notebook 05 excludes it and
  has students write a one-port rule; if the library is fixed, that section
  should be revisited.
- **Naming in the source repository.** The `er` term of
  [nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
  equals $e_{10}e_{01} - e_{00}e_{11}$, not the reflection tracking. Notebook
  03 explains the difference and exercise 03.3 checks that the corrected Γ is
  unaffected.
- **Gaps in the data record.** The calibration kit and its definition, the
  fixture of the resistors, whether the instrument's internal calibration was
  active, and the acquisition settings were not recorded. The lessons treat
  the standards as ideal and infer the line delay from the data.
- **Citation metadata.** `CITATION.cff` gives the DOI of the source data as
  `10.5281/zenodo.22722704`, while `data/README.md` and the lessons use
  `10.5281/zenodo.22722703`. One of them needs correcting.
- **Notebook 04** (acquisition with a NanoVNA) does not exist yet.
- **Third-party output in English.** In the Spanish edition, messages and the
  report generated by `rfmeasurement` remain in English; notebook 05 says so.
- **Typeface of the figures.** Figures use IBM Plex Sans when it is installed
  (the book workflow installs it) and fall back to Matplotlib's default
  otherwise; content is unaffected.

## 6. Data: simulated or recorded

| Source | Where it comes from | Used in |
|---|---|---|
| Ideal cable and resistor | formulas in the notebook | 00, 01 |
| Mystery circuits | `vnacourse.puzzles` (closed-form circuits) | 01 |
| Synthetic instrument | `vnacourse.errormodel.synthetic_error_terms`, exaggerated on purpose and labelled as such | 02, 03 |
| Imperfect standards | formulas in notebook 03, section 6 | 03 |
| Recorded NanoVNA-F V2 sweeps | `data/` via `vnacourse.data.load_repetitions`, provenance in `data/README.md` | 02, 03, 05 |
