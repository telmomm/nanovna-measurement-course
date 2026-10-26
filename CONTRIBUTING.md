# Contributing to nanovna-measurement-course

**English** · [Español](CONTRIBUTING.es.md)

Thank you for considering a contribution. This is teaching material, so the
most valuable contributions are the ones that help a student understand
something: a clearer explanation, a better exercise, a corrected equation,
or a report of how the module worked in your classroom.

## Ways to contribute

- **Report a problem.** A typo, a wrong equation, a notebook that does not
  run, a step that confused you or your students. Open an issue and say which
  notebook and cell it is about.
- **Share classroom experience.** If you used the module in a course, open a
  ["Classroom experience" issue](https://github.com/telmomm/nanovna-measurement-course/issues/new?template=classroom_report.yml)
  describing the context (course, number of students, time needed) and what
  worked or did not. This feedback shapes the next version, and it is what
  turns the time estimates of the
  [instructor guide](instructor/guia_docente.md) into measurements.
- **Improve or add content.** Explanations, figures, exercises, solutions,
  translations. For anything larger than a small fix, open an issue first so
  the change can be discussed before you invest time in it.

## Getting started

Use a virtual environment rather than installing into your system Python. It
is never committed (already in `.gitignore`) and can be deleted and recreated
at any time.

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

python -m pip install -e ".[dev,notebooks]"
```

Then run what CI runs:

```bash
ruff check .
ruff format --check .
pytest
pytest --nbmake notebooks exercises es --ignore=notebooks/04_adquisicion_nanovna.ipynb
```

`pytest` runs the package tests, the tests that recompute every number the
text quotes (`tests/test_reference_values.py`) and the tests that keep the two
language editions in step (`tests/test_translations.py`). The last command
executes every lesson and every solution notebook, in both languages, from top
to bottom and fails if any cell raises. Notebook 04 is skipped because it
needs a physical NanoVNA. `ruff format .` fixes formatting, including the
code cells of notebooks.

## Building the book

The website is a [Jupyter Book](https://jupyterbook.org) (version 1) built
from the notebooks and Markdown files where they are. There is one book per
language: `book/en/` and `book/es/` hold each configuration, table of contents
and the pages of its own; `book/_static/` and `book/latex/` hold the web and
PDF styles shared by both.

```bash
python -m pip install -e ".[book]"
tools/build_book.sh                  # both editions, HTML and PDF, into _site/
tools/build_book.sh --html-only en   # one edition, web only
```

The build executes every notebook, and the HTML build uses `-W`, so a warning
(for example a broken link) fails it, as in CI. A new notebook or page must be
added to the `_toc.yml` of both editions to appear. The PDF needs XeLaTeX with
the IBM Plex fonts (TeX Live's `plex` package) and `rsvg-convert`.

## Two languages

The English edition lives at the root of the repository and the Spanish one
in `es/`, with the same file names. Every change to a lesson, a solution or
the instructor material must be made in both:

- **Same cells, same code.** A Spanish notebook has the same cells, in the
  same order and with the same cell ids, as its English twin. Its code is the
  same except for comments, docstrings, figure labels and printed messages.
  `tests/test_translations.py` checks both.
- **Numbers.** Both editions use the decimal point, as Python does. If you
  change a number quoted in the text, update `tests/test_reference_values.py`.
- **If you can only write one language**, open the pull request anyway and
  say so: a maintainer will add the other.

## Visual identity

Colours, type and the mark are described in
[`assets/brand/README.md`](assets/brand/README.md). New figures should use
`vnacourse.plotting.use_course_style()` and the `SERIES` colours in order.

## Guidelines for notebooks

- **Every notebook must run without hardware**, on simulated data or on the
  recorded measurements in `data/`. Notebook 04 is the only exception.
- **State the learning objectives** at the top (three or four bullets), and
  keep the content focused on them.
- **Follow the common structure:** objectives, short theory, guided code,
  check-your-understanding questions ("what do you expect to see before you
  run this?"), open exercises, summary and link to the next notebook.
- **The code serves the concept.** Prefer a few readable lines of NumPy over
  a clever abstraction; move reusable plumbing into `src/vnacourse/`.
- **Commit notebooks with outputs cleared** (in JupyterLab: *Edit → Clear
  Outputs of All Cells*). It keeps diffs reviewable; CI re-executes them.
- **Keep the Binder and Colab badges** in the first cell pointing at the
  notebook itself (`es/notebooks/...` in the Spanish edition).
- **An exercise needs a solution.** If you add or change an exercise, update
  the matching notebook in `exercises/solutions/`. Text that states a number
  must match what the code prints.

## Before opening a pull request

1. Keep the change focused on a single concern.
2. Run the commands above.
3. If you changed an equation or a method, cite the source (textbook, paper
   or standard).
4. Update `CHANGELOG.md` when the change is visible to students or
   instructors.

## Licensing of contributions

By contributing you agree that your code is released under the
[BSD 3-Clause licence](LICENSE) and your text, figures and data under
[CC BY 4.0](LICENSE-CONTENT).

## Attribution

Contributors receive appropriate credit. When a contribution is substantial,
authorship or formal acknowledgement will be discussed transparently with
the contributor.
