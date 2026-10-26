# Hands-on vector network analysis with a NanoVNA

An open, computational learning module on S-parameter measurement and
calibration. You derive the error model of a vector network analyzer (VNA),
simulate it, and calibrate real measurements taken with a low-cost NanoVNA.

The guiding idea is *coding to learn*, not *learning to code*: the code is
the means to understand the measurement, not the goal.

```{admonition} Status
:class: note
Version 0.1.0. The material is complete but has not yet been used in a
classroom. Corrections and reports of use are welcome on
[GitHub](https://github.com/telmomm/nanovna-measurement-course).
```

## Who it is for

- Undergraduate students in biomedical engineering (instrumentation and
  electronics courses).
- Undergraduate students in electronic or telecommunication engineering
  (introduction to RF and measurement).
- Self-learners: master's and final-year project students, and practitioners
  starting out with a NanoVNA.

You need sinusoidal steady-state circuits (phasors, complex impedance) and
basic Python with NumPy and Matplotlib. You do **not** need any previous RF
course, and you do **not** need the instrument: every lesson runs on
simulated data or on real measurements included with the module.

Allow 10 to 14 hours for the whole module.

## The lessons

| | Lesson | You will learn to… |
|---|---|---|
| 00 | [What does a VNA measure?](../../notebooks/00_introduccion_vna.ipynb) | explain incident and reflected waves, define S-parameters, and say what a VNA measures that other instruments do not |
| 01 | [Reflection coefficient and the Smith chart](../../notebooks/01_reflexion_smith.ipynb) | convert between Γ and Z, read the Smith chart, and recognise a circuit from its trace |
| 02 | [Systematic errors](../../notebooks/02_errores_sistematicos.ipynb) | identify directivity, source match and reflection tracking, and predict what each distorts |
| 03 | [SOL calibration](../../notebooks/03_calibracion_sol.ipynb) | solve the short–open–load system, correct a real measurement, and know what calibration does not fix |
| 05 | [Validation and measurement quality](../../notebooks/05_validacion_calidad.ipynb) | quantify repeatability, use passivity as a physical test, and record a traceable result |

Work through them in order: each one uses the previous. Lesson 04, on
acquiring your own measurements with a NanoVNA, is optional and not yet
available.

## Languages and formats

The module exists in **English** and **Spanish**, with the same lessons,
code and numbering: [leer en español](https://telmomm.github.io/nanovna-measurement-course/es/).
Each edition is also available as a
[PDF book](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-en.pdf)
([en español](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-es.pdf)),
convenient for reading offline or printing; the lessons are still meant to be
run.

## How to use this book

Reading is not enough. Each lesson is a Jupyter notebook, and it asks you to
**predict** what a piece of code will show, **run** it, and then read the
**explanation**. The pages of this book show the notebooks already executed,
which is convenient for reading and revising, but the learning happens when
you run them yourself:

- Use the rocket icon at the top of any lesson to open it in **Binder** or
  **Google Colab**. Nothing to install.
- Or [install the module on your computer](setup.md).

Each lesson ends with questions to check your understanding (answers one
click away) and with open exercises. Worked solutions to the exercises are in
this book; try each exercise before you read its solution.

## If you teach

The [instructor guide](../../instructor/guia_docente.md) has a session plan,
notes on each lesson and a summative assignment, and there is a
[rubric](../../instructor/rubrica.md) to mark it.

## About this resource

How the module was designed, from learning outcomes to activities, is
described in [Design of the module](../../docs/design.md), and what has been
checked to show that it works as described is in
[Technical validation](../../docs/validation.md).

## Licence and citation

The code is released under the BSD 3-Clause licence. The text, figures and
data are released under Creative Commons Attribution 4.0 International
(CC BY 4.0).

If you use the module, please cite the archived release,
[doi:10.5281/zenodo.23669895](https://doi.org/10.5281/zenodo.23669895), with the metadata in
[`CITATION.cff`](https://github.com/telmomm/nanovna-measurement-course/blob/main/CITATION.cff).
The real measurements come from the research repository
[nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
([doi:10.5281/zenodo.22722703](https://doi.org/10.5281/zenodo.22722703)).
