# Contributing to nanovna-measurement-course

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
pytest --nbmake notebooks exercises --ignore=notebooks/04_adquisicion_nanovna.ipynb
```

The last command executes every lesson and every solution notebook from top
to bottom and fails if any cell raises. Notebook 04 is skipped because it
needs a physical NanoVNA. `ruff format .` fixes formatting, including the
code cells of notebooks.

## Building the book

The website is a [Jupyter Book](https://jupyterbook.org) (version 1) built
from the notebooks and Markdown files where they are; `book/` only holds its
configuration, table of contents and two pages of its own.

```bash
python -m pip install -e ".[book]"
jupyter-book build . --config book/_config.yml --toc book/_toc.yml --path-output book -W
```

Open `book/_build/html/index.html`. The build executes every notebook, and
`-W` makes a warning (for example a broken link) fail it, as in CI. A new
notebook or page must be added to `book/_toc.yml` to appear.

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
  notebook itself.
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
