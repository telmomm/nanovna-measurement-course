# Instructor guide

How to teach with *nanovna-measurement-course*: what it covers, how long it
takes, how to run a session, where students are likely to struggle, and how
to assess them. The marking rubric is in [rubrica.md](rubrica.md).

> **This module has not yet been used in a classroom.** The session times
> below are estimates from the length of the material, and the "likely
> difficulties" are what we expect, not what we have observed. Both will be
> replaced by measured values after the first pilot. If you teach with it,
> please [tell us how it went](#12-tell-us-how-it-went).

## 1. At a glance

| | |
|---|---|
| Subject | One-port S-parameter measurement with a low-cost vector network analyzer: error model, SOL calibration, validation |
| Level | Undergraduate, after a first course on circuits; also suitable for master's and final-year project students |
| Degrees | Biomedical engineering, electronic engineering, telecommunication engineering |
| Prerequisites | Phasors and complex impedance; basic Python with NumPy and Matplotlib |
| Not required | Any previous RF or transmission-line course; any hardware |
| Format | Five Jupyter notebooks, each with guided code, questions and exercises; worked solutions |
| Time | 10–14 hours (estimate): about 7.5 h guided, plus 2.5 h to 4.5 h of exercises depending on how many you set. The assignment adds 2–3 h. |
| Assessment | One assignment on real data, marked with the [rubric](rubrica.md) |
| Runs on | A browser (Binder or Google Colab) or a local Python 3.10+ installation |
| Languages | English (repository root) and Spanish (`es/` folder), with the same content and numbering |

## 2. What students learn

By the end of the module a student can:

1. explain a reflection measurement in terms of incident and reflected waves, and convert between reflection coefficient and impedance;
2. read a Smith chart and recognise simple circuits from their traces;
3. describe the three systematic error terms of a one-port measurement and predict what each one distorts;
4. derive, implement and apply a short–open–load calibration;
5. judge a calibrated result: test it on independent data, check it against physical limits, and state its repeatability;
6. report a result with its uncertainty, its limitations and enough context to be reproduced.

| Outcome | Notebook | Learning objectives stated in the notebook |
|---|---|---|
| 1 | 00 · What does a VNA measure? | incident and reflected waves; S-parameters; reflected power and return loss; VNA versus multimeter and oscilloscope |
| 1, 2 | 01 · Reflection coefficient and the Smith chart | Γ ↔ Z; what the chart's circles and arcs are; inductive, capacitive and resonant behaviour; identify a circuit from its trace |
| 3 | 02 · Systematic errors | name the three error terms; write the error model; predict which devices each term distorts; recognise an untrustworthy raw measurement |
| 4, 5 | 03 · SOL calibration | linearise and solve the model; correct a measurement; test on held-out data; reference plane and imperfect standards |
| 5, 6 | 05 · Validation and measurement quality | repeatability and standard uncertainty; passivity as a physical test; integrity, physics and quality; context and traceability |

Notebook 04 (acquiring your own data with a NanoVNA) is planned, optional,
and not yet available. Nothing in the other notebooks depends on it.

## 3. How the notebooks depend on each other

```
00 ──► 01 ──► 02 ──► 03 ──► 05
```

Each notebook uses the previous ones. Three ways to cut the module:

| Path | Notebooks | Time (estimate) | For |
|---|---|---|---|
| Full | 00, 01, 02, 03, 05 | 10–14 h | Students new to RF. The default. |
| Without validation | 00, 01, 02, 03 | 8–11 h | When time is short. Notebook 05 is marked "advanced" and can be dropped without breaking anything. |
| Calibration only | 02, 03 | 4–5 h | Students who already know S-parameters and the Smith chart, for example after an RF or microwave course. |

Notebook 05 needs notebook 03. Notebook 01 can be shortened (skip section
3.2, parallel circuits) but not skipped by students who have never seen a
Smith chart: notebooks 02 and 03 show results on it.

## 4. Session plan

For two-hour sessions. "Guided" is the time to work through the notebook
with its predictions and questions; "exercises" is the time for the exercises
at the end, in class or as homework.

| Session | Content | Guided | Exercises |
|---|---|---|---|
| 1 | Notebook 00, complete. Notebook 01, sections 1–2 (Γ ↔ Z, building the chart). | 60 min + 35 min | 00: 30–45 min, homework |
| 2 | Notebook 01, sections 3–4 (traces, guess the circuit). | 40 min + 30 min for the mystery circuits | 01: 45 min |
| 3 | Notebook 02, complete. | 75 min | 02: 45 min |
| 4 | Notebook 03, sections 1–4.1 (the solver, synthetic data, first real result). | 60 min | 03, exercises 1–2: 30 min |
| 5 | Notebook 03, sections 4.2–6 (reference plane, held-out test, scikit-rf, imperfect standards). | 60 min | 03, exercises 3–5: 45 min |
| 6 | Notebook 05, complete. | 90 min | 05: 60 min, homework |
| 7 (optional) | Assignment workshop, or a hands-on session with the instrument. | | Assignment: 2–3 h |

Sessions 4 and 5 are the heart of the module. If you must compress, take the
time from session 1 (assign notebook 00 as preparation) and not from these.

## 5. How to run a session

The notebooks are built around one habit: **predict, run, explain.**

1. **Predict.** Before each key cell there is a "Predict before you run"
   prompt (17 in total). Ask students to commit to an answer first: written
   in a line, or agreed with a neighbour. Thirty seconds is enough. The
   prediction does not need to be right; it needs to exist.
2. **Run.** They run the cell and compare.
3. **Explain.** The text after the cell explains the result. Where
   prediction and result differ, that difference is the lesson: spend the
   class time there.

The second device is the order **synthetic first, real second**. Every idea
is first tried on a made-up instrument where the right answer is known
exactly, and then on real NanoVNA data where it is not. Point this out to
students: on synthetic data the method can be *verified*; on real data it can
only be *checked for consistency*.

Practical suggestions:

- **Pairs work well** for the predictions and for the mystery circuits.
- **Do not project the solved notebook.** Students should run the cells
  themselves; the outputs are deliberately not stored in the repository.
- **The code is a means.** Students do not need to be able to write the
  plotting code. They do need to be able to write `apply_error_model`,
  `solve_error_terms` and `correct` (about ten lines in total), and each
  notebook has them do so.
- **The "Check your understanding" questions** have their answers one click
  away. Use them as two-minute pauses in class, or as a self-test before the
  exercises.

## 6. Setting up

Three ways to run the notebooks, in order of how little can go wrong:

| Option | Students need | Notes |
|---|---|---|
| **Binder** | A browser | Click the badge at the top of a notebook. The first launch after the repository changes takes several minutes while the environment is built; later launches are faster. Sessions are temporary: work is lost when the tab closes unless downloaded. |
| **Google Colab** | A browser and a Google account | Click the Colab badge. The first code cell of each notebook installs the course package. Work can be saved to the student's Drive. |
| **Local** | Python 3.10+ | Instructions in [Running the lessons](../book/en/setup.md). Best for a course that lasts several weeks. |

Before the first session:

- [ ] Open one notebook on the platform your students will use and run it to
      the end. Do it the day before: it also warms up Binder.
- [ ] If you use Binder, have Colab ready as a fallback (or the reverse).
      Both are free services with no guarantee of availability.
- [ ] Check that notebook 05 runs. It is the only one that needs the extra
      library `rfmeasurement`, installed automatically on Binder and Colab.
- [ ] Decide what students hand in and tell them how to save their work.
- [ ] Decide how you will use the solutions, which are public (section 9).

No hardware is needed at any point. If you have NanoVNAs, see section 10.

## 7. Notes on each notebook

"Likely difficulties" are anticipated, not yet observed.

### 00 · What does a VNA measure?

- **The one idea:** at radio frequency a device is characterised by how it
  reflects a wave, and that takes a magnitude *and* a phase.
- **Likely difficulties:** treating the reflected wave as a loss or a defect
  when it is simply the consequence of a mismatch; the sign of Γ (a load
  below 50 Ω has a negative Γ); return loss being a positive number of
  decibels that is *better* when larger; believing that phase is a detail.
- **Worth discussing:** section 4 shows that a flat |S11| with a rotating
  phase looks, to an instrument that only sees total voltage, like a device
  that changes with frequency. Ask: "what would you conclude from the second
  plot alone?"
- **Exercises:** 3 (return loss to impedance) is the most useful if you can
  only set one. 4 prepares the reference-plane discussion of notebook 03.

### 01 · Reflection coefficient and the Smith chart

- **The one idea:** the Smith chart is the Γ plane with impedance grid lines
  drawn on it, nothing more.
- **Likely difficulties:** seeing the chart as a separate, mysterious kind of
  plot; reading resistance from the horizontal position alone (the point
  straight above the centre is not 50 Ω of resistance); parallel circuits and
  conductance circles; why traces turn clockwise.
- **Worth discussing:** section 2 has students draw the circles themselves.
  Give it time: it is what removes the mystery. Section 3.4 (a circle around
  the centre is a delay) returns as a surprise in real data in notebook 03.
- **Guess the circuit (section 4):** works well in pairs, with a short
  whole-class debrief on *how* each pair decided. The three circuits are a
  series RC, a parallel RL and a series RLC. Insist on choosing the topology
  from the shape before computing anything.
- **If time is short:** skip section 3.2 and mystery circuit B.

### 02 · Systematic errors

- **The one idea:** an uncalibrated instrument is not imprecise, it is
  consistently wrong, and the wrongness has exactly three parameters.
- **Likely difficulties:** confusing systematic error with noise (the
  strongest misconception of the module: "measure it again and average");
  the ripple, which requires thinking of Γm as a sum of rotating complex
  vectors; remembering which term is which.
- **Worth discussing:** the three "one flaw at a time" plots of section 2.
  The prediction "which device does not move?" has a clean answer in each
  case and builds the table that closes the section. In section 4, the raw
  open reading |Γ| = 2.1 is a good moment to ask "is the file broken?" (it is
  not), which notebook 05 answers properly.
- **Tell students:** the synthetic instrument's errors are invented and
  exaggerated so that every effect is visible. Real instruments are better.
- **Exercises:** 1 (which term is to blame) consolidates the notebook. 3
  (worst case in decibels) is quick and connects to how datasheets are read.

### 03 · SOL calibration

- **The one idea:** three known devices give three equations for the three
  error terms; solve, then invert the model.
- **Likely difficulties:** the linearisation step (multiplying by the
  denominator and renaming a product of unknowns as one unknown, Δe); why
  correcting the calibration measurements themselves proves nothing; and the
  reference plane, which students meet here as an apparent failure of the
  calibration.
- **Worth discussing:** section 4.2 is the most important moment of the
  module. After calibration the two resistors swing between 33 Ω and 75 Ω
  across the band. Let students believe for a minute that the calibration is
  wrong before showing the Smith chart. The resolution (about 1 ns of line
  between the calibration plane and the resistors) is inferred from the data
  itself.
- **Section 6** (imperfect standards) can be assigned as reading if time is
  short, but do not drop it: it is what stops students from believing that a
  calibrated result is exact.
- **Exercises:** 1 (closed form) for students who like algebra; 2 (fewer
  repetitions) for everyone; 4 (a fourth standard) is the hardest and suits
  stronger students or a project.

### 05 · Validation and measurement quality

- **The one idea:** a number becomes a result when it comes with its
  repeatability, its physical checks and its history.
- **Likely difficulties:** the standard deviation of a complex quantity; the
  difference between the scatter of single readings and the uncertainty of
  their mean; reading "uncertainty" as "error"; and wanting to "fix" a
  passivity violation by clipping.
- **Worth discussing:** section 3 ends with a result of 74.0 Ω ± 0.2 Ω for a
  nominal 75 Ω resistor. Ask what could explain the difference. Every
  candidate is something the uncertainty does not include, which is the
  point. Section 4's table (three meanings of |Γ| > 1) is worth reading aloud.
- **About `rfmeasurement`:** sections 5 and 6 use more library machinery than
  the rest of the module. Students do not need to memorise the API. What
  matters is the structure: a measurement with its context, rules that return
  a status *with evidence*, and a processing history.
- **Exercises:** 1 (mean or median) is short and convincing. 3 (write a rule)
  is the most open; its solution deliberately shows a rule raising false
  alarms and discusses why.

## 8. Formative assessment

Three sources of evidence need no marking effort:

- **Predictions.** Collect them occasionally (a line on paper, a show of
  hands, a poll). Mark participation, never correctness: the method only
  works if students feel free to be wrong.
- **Check-your-understanding questions.** Use two or three as an exit ticket.
- **Exercises.** A three-level scale is enough; see the
  [rubric](rubrica.md#weekly-exercises).

## 9. Summative assessment

### The assignment: characterise a resistor from raw data

Students receive nothing new: the task uses the measurements already in the
repository, but with a calibration of their own.

> **Brief for students.** You are given raw NanoVNA measurements of three
> calibration standards (ten repetitions each, in `data/standards/`) and of a
> resistor (three repetitions, in `data/dut/load_33ohm/`). Using only the
> three repetitions of the standards assigned to you:
>
> 1. Compute the error terms of the instrument and describe how they behave
>    across the band.
> 2. Calibrate the resistor measurement. Report its resistance below 10 MHz.
> 3. Show the calibrated result across the whole band, explain what you see,
>    and estimate the delay between the calibration plane and the resistor.
> 4. Test your calibration on the repetitions of the standards that you did
>    not use.
> 5. Check passivity for the calibrated resistor and for one calibrated
>    standard, and interpret the outcome.
> 6. Give a standard uncertainty for the resistance of step 2. State what it
>    includes and what it does not.
> 7. Record what someone else would need in order to reproduce your result.
>
> Hand in a notebook that runs from top to bottom, and a conclusion of at
> most one page.

**Personalising it.** Give each student or pair a different set of three
repetition numbers out of ten (there are 120 combinations). The numbers they
obtain differ slightly, so results cannot simply be copied, while the
expected values stay within a narrow range that you can check.

**What a correct submission finds** (verified over all 120 combinations):

| Quantity | Expected |
|---|---|
| Resistance below 10 MHz | 32.3 Ω to 32.5 Ω |
| One-way delay to the resistor | about 1.05 ns (roughly 22 cm of line at 0.7 c) |
| Resistance after removing the delay | about 34 Ω on average, varying between about 30 Ω and 40 Ω across the band |
| Held-out open, median distance from Γ = 1 | 0.0015 to 0.0018 |
| Uncertainty from the three resistor repetitions | about 0.09 Ω |
| Passivity | The resistor is far inside the limit (\|Γ\| below 0.25). A calibrated open or short lies slightly above 1 at a large fraction of points, by amounts comparable to the repeatability. |

A student who also includes the scatter of the calibration in the
uncertainty, as notebook 05 does, will report a slightly larger value. Both
are acceptable if the student says which sources were included.

**What to look for** beyond the numbers: whether the student *explains* the
swing of the resistance across the band instead of reporting it as an error,
and whether the stated uncertainty comes with its limitations. These two
items separate understanding from execution. The [rubric](rubrica.md) weights
them accordingly.

### About the public solutions

The worked solutions to the exercises are in the repository, and notebooks 03
and 05 already work through the 75 Ω resistor in full. This is deliberate:
the module is meant for self-study too. For graded work:

- use the assignment above with personalised repetitions, which is not solved
  anywhere;
- or change the numbers in an exercise (component values, cable length, the
  capacitance of the open);
- or grade the open-ended parts: an explanation, a design choice, a
  validation rule and its false alarms.

This guide is public too, including the expected values above. They tell a
student what a right answer looks like, not how to obtain or explain it.

## 10. Adapting the module

**Your own measurements.** `load_repetitions("standards", "open")` reads
every `.s1p` file in `data/standards/open/`. To use your own data, replace
the files, keeping one folder per device and one Touchstone file per
repetition, all on the same frequency grid. Update `data/README.md` with your
instrument and conditions. The explanatory text in notebooks 02, 03 and 05
quotes numbers from the supplied data, so check it against yours.

**With NanoVNAs in the laboratory.** A natural hands-on session after
notebook 03: students measure a short, an open, a load and a component of
their choice, save Touchstone files, and run their own data through the
notebook. Have them calibrate at the end of the cable they will use, and then
add an adapter afterwards to see the reference plane move.

**New mystery circuits.** For notebook 01, generate your own traces:

```python
import numpy as np
from vnacourse.reflection import z_to_gamma

f_hz = np.linspace(10e6, 1.45e9, 600)
omega = 2 * np.pi * f_hz
z = 40 + 1j * omega * 12e-9  # for example: 40 Ω in series with 12 nH
gamma = z_to_gamma(z)  # give students this array, not the line above
```

**A different audience.** For biomedical engineering students, connect
notebook 01 to electrode and tissue impedance and notebook 05 to the
reporting standards they will meet in instrumentation. For telecommunication
students, connect notebook 00 to antenna matching and notebook 03 to
two-port calibration, which extends the same idea to twelve error terms.

**Languages.** The material is available in English and in Spanish, with the
same content: the Spanish edition is in the `es/` folder of the repository and
has its own [book](https://telmomm.github.io/nanovna-measurement-course/es/). The code (variable names and the `vnacourse` package) is
the same in both; the Spanish edition translates the text, comments, figure
labels and messages.

## 11. Known limitations of the material

Be aware of these, and consider telling your students:

- **The supplied data has gaps in its record.** The calibration kit and its
  definitions, the fixture used for the resistors, and the acquisition
  settings were not recorded with the data (see
  [`data/README.md`](../data/README.md)). The notebooks treat the standards
  as ideal and infer the rest from the data. Notebook 05 turns this into a
  lesson on traceability, but it does limit how far the results can be
  interpreted.
- **One-port only.** Transmission measurements and two-port calibration are
  not covered.
- **Uncertainty is introduced, not treated in full.** Notebook 05 covers
  repeatability (Type A) and explains what it leaves out. It does not build a
  complete uncertainty budget.
- **Notebook 05 depends on an early-stage library.** `rfmeasurement` is at
  version 0.3 and its interface may change. Its built-in passivity rule does
  not handle one-port data in that version, so the notebook has students
  write their own.
- **No hardware notebook yet.** Notebook 04 is planned.

## 12. Tell us how it went

If you use the module, in whole or in part, please open a
["Classroom experience" issue](https://github.com/telmomm/nanovna-measurement-course/issues/new?template=classroom_report.yml).
A few lines are enough: the course, how many students, which notebooks, how
long they took, and what did not work. This is how the estimates in this
guide become measurements, and how the next version gets better.

Corrections and additions to this guide are welcome through the same
repository; see
[CONTRIBUTING.md](https://github.com/telmomm/nanovna-measurement-course/blob/main/CONTRIBUTING.md).
