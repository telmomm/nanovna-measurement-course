# Changelog

All notable changes to this learning module are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project follows [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-10-26

First public release, archived on Zenodo
([doi:10.5281/zenodo.23669895](https://doi.org/10.5281/zenodo.23669895)). The core module is complete in
English and Spanish; it has not yet been used in a classroom.

### Added

- Spanish edition in `es/`: the five lessons, their worked solutions, the
  instructor guide, the rubric and the data description, plus `README.es.md`,
  `CONTRIBUTING.es.md` and `CODE_OF_CONDUCT.es.md`. The code of each Spanish
  notebook is the same as in its English twin; `tests/test_translations.py`
  checks it.
- One book per language (`book/en/`, `book/es/`), each also built as a PDF
  with XeLaTeX; `tools/build_book.sh` builds both and assembles the site.
- Visual identity in `assets/brand/` (mark, banners, social preview and the
  script that draws them), applied to the README, the web book
  (`book/_static/brand.css`), the PDF (`book/latex/handsonvna.sty`) and the
  figures (IBM Plex Sans when installed).
- `docs/design.md` and `docs/validation.md` (and Spanish versions): design
  methodology with the map from learning outcomes to activities and evidence,
  and the technical validation of the module, with references in
  `docs/references.bib`.
- `tests/test_reference_values.py`: every number the lessons and the
  instructor guide quote about the data, recomputed, including the expected
  results of the assignment for all 120 choices of repetitions.
- `plotting.draw_error_adapter(lang=...)` draws its labels in English or
  Spanish.

### Changed

- Notebook 03, section 4.2: the residual variation of the 75 Ω resistor after
  removing the line delay is "between about −8 Ω and +15 Ω", not "roughly
  ±10 Ω" as stated before.
- The book configuration moved from `book/` to `book/en/`; the book workflow
  builds both editions and their PDFs and deploys `_site/`.
- CI executes the Spanish notebooks too.

- Notebook `00_introduccion_vna.ipynb`: waves on a line, incident and
  reflected waves, S-parameters, and what a VNA measures.
- Notebook `01_reflexion_smith.ipynb`: the Γ–Z mapping, the Smith chart built
  from scratch, traces of RL, RC and RLC circuits, and a "guess the circuit"
  activity.
- Notebook `05_validacion_calidad.ipynb`: repeatability and Type A
  uncertainty, passivity as a physical test, structured validation and a
  traceable report with `rfmeasurement`.
- Worked solutions for every lesson in `exercises/solutions/`, executed in CI.
- `vnacourse.puzzles` with the mystery circuits of notebook 01.
- Optional dependency on `rfmeasurement` (extra `validation`), used only by
  notebook 05.
- Instructor material in `instructor/`: a guide with session plan, time
  estimates, notes on each notebook and a summative assignment on real data,
  and a rubric to mark it.
- "Classroom experience" issue template for reports from instructors.
- Jupyter Book in `book/`: lessons, solutions, instructor material and data
  description as a website, built in CI and deployed to GitHub Pages.

- Repository scaffolding: dual licence (BSD-3-Clause for code, CC BY 4.0 for
  content), `CITATION.cff`, contribution guide and code of conduct.
- `vnacourse` helper package skeleton and `environment.yml` / `postBuild`
  for Binder.
- CI that executes every notebook with nbmake, both from a pip install and
  from the Binder conda environment.
- Notebook `02_errores_sistematicos.ipynb`: the three-term error model, built
  one term at a time on a synthetic instrument and then observed in real data.
- Notebook `03_calibracion_sol.ipynb`: SOL calibration derived and solved by
  hand, applied to synthetic and real measurements, checked on held-out
  repetitions and against `skrf.calibration.OnePort`.
- `data/`: recorded NanoVNA-F V2 measurements of the short, open and load
  standards and of two resistors, from `nanovna-calibration`.
- `vnacourse` modules `reflection`, `errormodel`, `calibration`, `data` and
  `plotting`, with tests.
