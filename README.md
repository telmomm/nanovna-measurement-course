<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/banner-en-dark.png">
  <img alt="Hands-on VNA · nanovna-measurement-course · Learn to measure with a VNA. Without owning one." src="assets/brand/banner-en-light.png">
</picture>

**English** · [Español](README.es.md)

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23669895-2a78d6?labelColor=0e1116)](https://doi.org/10.5281/zenodo.23669895)
[![CI](https://github.com/telmomm/nanovna-measurement-course/actions/workflows/ci.yml/badge.svg)](https://github.com/telmomm/nanovna-measurement-course/actions/workflows/ci.yml)
[![Book](https://img.shields.io/badge/book-EN%20·%20ES-2a78d6?labelColor=0e1116)](https://telmomm.github.io/nanovna-measurement-course/)
[![PDF](https://img.shields.io/badge/PDF-EN%20·%20ES-2a78d6?labelColor=0e1116)](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-en.pdf)
[![Binder](https://img.shields.io/badge/launch-Binder-eb6834?labelColor=0e1116)](https://mybinder.org/v2/gh/telmomm/nanovna-measurement-course/HEAD?labpath=notebooks)
[![Code: BSD-3-Clause](https://img.shields.io/badge/code-BSD--3--Clause-52514e?labelColor=0e1116)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-52514e?labelColor=0e1116)](LICENSE-CONTENT)

**Hands-on vector network analysis with a low-cost NanoVNA.** An open
computational learning module on S-parameter measurement and calibration:
you derive the error model of a vector network analyzer (VNA), simulate it,
and calibrate real measurements in Jupyter notebooks.

> **Status: version 0.1.0, not yet used in a classroom.** The five core
> notebooks, their exercises, worked solutions and the instructor guide are
> complete, in English and Spanish. The optional hardware notebook (04) is
> still to come.

The guiding idea is *coding to learn*, not *learning to code*: the code is
the means to understand the measurement, not the goal.

## Who is this for?

- Undergraduate students in biomedical engineering (instrumentation and
  electronics courses).
- Undergraduate students in electronic or telecommunication engineering
  (introduction to RF and measurement).
- Self-learners: master's and final-year project students, and practitioners
  starting out with a NanoVNA.

**Prerequisites:** sinusoidal steady-state circuits (phasors, complex
impedance) and basic Python (NumPy, Matplotlib). No previous RF experience is
needed.

**No hardware is required.** Every notebook runs on simulated data or on
real NanoVNA measurements shipped with the repository. Only notebook 04 will
use a physical NanoVNA, and it is optional.

**Estimated time:** 10–14 hours (5–7 two-hour sessions).

## Notebooks

| # | Notebook | You will learn to… | Solutions |
|---|---|---|---|
| 00 | [What does a VNA measure?](notebooks/00_introduccion_vna.ipynb) | explain incident and reflected waves, define S-parameters, and say what a VNA measures that other instruments do not | [00](exercises/solutions/00_solutions.ipynb) |
| 01 | [Reflection coefficient and the Smith chart](notebooks/01_reflexion_smith.ipynb) | convert between Γ and Z, read the Smith chart, and recognise a circuit from its trace | [01](exercises/solutions/01_solutions.ipynb) |
| 02 | [Systematic errors: the three-term model](notebooks/02_errores_sistematicos.ipynb) | identify directivity, source match and reflection tracking, and predict what each distorts | [02](exercises/solutions/02_solutions.ipynb) |
| 03 | [SOL calibration](notebooks/03_calibracion_sol.ipynb) | solve the short–open–load system, correct a real measurement, and know what calibration does not fix | [03](exercises/solutions/03_solutions.ipynb) |
| 04 | Acquisition with a NanoVNA (optional, needs hardware) | configure a sweep and export Touchstone files | *not yet available* |
| 05 | [Validation and measurement quality](notebooks/05_validacion_calidad.ipynb) (advanced) | quantify repeatability, use passivity as a physical test, and record a traceable result | [05](exercises/solutions/05_solutions.ipynb) |

Every notebook has the same shape: learning objectives, a short piece of
theory, guided code with "predict before you run" prompts, questions to check
your understanding, and open exercises.

## Two languages, three formats

| | English | Español |
|---|---|---|
| Notebooks | [`notebooks/`](notebooks/) | [`es/notebooks/`](es/notebooks/) |
| Web book | [telmomm.github.io/nanovna-measurement-course](https://telmomm.github.io/nanovna-measurement-course/) | […/es/](https://telmomm.github.io/nanovna-measurement-course/es/) |
| PDF book | [hands-on-vna-en.pdf](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-en.pdf) | [hands-on-vna-es.pdf](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-es.pdf) |
| Instructor guide | [`instructor/`](instructor/guia_docente.md) | [`es/instructor/`](es/instructor/guia_docente.md) |

The two editions have the same cells and run the same code; only text,
comments, figure labels and messages are translated. A test keeps them in
step.

## Getting started

### Read it

The web book shows every notebook already executed, and the PDF is
convenient offline. Both are good for reading and revising; to learn from the
module, run the notebooks.

### In the browser

Click the Binder badge above. Nothing to install; the first launch can take
a few minutes while the environment is built. Each notebook also has a Colab
badge.

### On your computer

With conda (or mamba):

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

conda env create -f environment.yml
conda activate nanovna-measurement-course
python -m pip install --no-deps -e .
jupyter lab notebooks          # or: jupyter lab es/notebooks
```

With pip and a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
python -m pip install -e ".[notebooks]"
jupyter lab notebooks
```

Python 3.10 or newer is required.

## For instructors

The [instructor guide](instructor/guia_docente.md) has a session plan with
time estimates, notes on each notebook, set-up advice and a summative
assignment on real data; the [rubric](instructor/rubrica.md) is for marking
it. If you teach with the module, please report how it went with a
["Classroom experience" issue](https://github.com/telmomm/nanovna-measurement-course/issues/new?template=classroom_report.yml).

## Design and validation

- [Design of the module](docs/design.md): the need it addresses, design
  principles, the map from learning outcomes to activities and evidence, and
  the reasons for the sequence.
- [Technical validation](docs/validation.md): what has been checked, how, and
  with what result, including every number the lessons quote; known issues
  and limitations.

Technical validation shows that the material is correct and reproducible; it
is not evidence of learning gains, which have not been measured.

## Repository layout

```
notebooks/      the lessons, in order (English)
exercises/      worked solutions to the exercises of each lesson
instructor/     instructor guide and assessment rubric
docs/           design and technical validation of the module, references
es/             Spanish edition: notebooks, exercises, instructor, docs, data notes
data/           real NanoVNA measurements used by both editions (see data/README.md)
book/           Jupyter Book configuration for each edition, web style, PDF style
assets/brand/   visual identity: mark, banners, social preview and the script that draws them
src/vnacourse/  small helper package used by the notebooks
tests/          tests for the package, the numbers quoted in the text, and language parity
tools/          build script for the books
```

## Contributing

Corrections, new exercises and reports from classroom use are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) and the
[code of conduct](CODE_OF_CONDUCT.md).

## Citing

If you use the module, please cite the archived release:

Miguel-Medina, T. (2026). *Hands-on VNA: an open learning module on vector
network analysis and calibration with a low-cost NanoVNA* (version 0.1.0)
[Computer software and learning materials]. Zenodo.
[https://doi.org/10.5281/zenodo.23669895](https://doi.org/10.5281/zenodo.23669895)

Citation metadata is in [CITATION.cff](CITATION.cff); GitHub shows a
"Cite this repository" button built from it.

The measurements and the calibration method come from the research
repository [nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
([doi:10.5281/zenodo.22722703](https://doi.org/10.5281/zenodo.22722703)).
Notebook 05 uses [rfmeasurement](https://github.com/telmomm/rfmeasurement)
([doi:10.5281/zenodo.22058515](https://doi.org/10.5281/zenodo.22058515)), and
all notebooks build on [scikit-rf](https://scikit-rf.org).

## Licence

- **Code** (the `vnacourse` package, tests, tools, and code cells in the
  notebooks): [BSD 3-Clause](LICENSE).
- **Content** (text, notebooks' narrative, figures, data and the visual
  identity in `assets/brand/`):
  [Creative Commons Attribution 4.0 International](LICENSE-CONTENT).
