# Design of the module

How *Hands-on VNA* was designed: the need it addresses, the principles behind
it, how its learning outcomes map to activities, and why the lessons come in
this order. The [technical validation](validation.md) describes how the
material has been checked.

```{admonition} Status
:class: note
Version 0.1.0. The design described here has been checked technically, not
pedagogically: the module has not yet been used with students, so nothing on
this page is a claim about what students learn from it.
```

## 1. The need

A vector network analyzer (VNA) measures how a device reflects and transmits
a wave, in magnitude and phase. Using one well depends on an idea that is
easy to state and hard to absorb: the instrument does not report the device,
it reports the device seen through its own systematic errors, and those
errors have to be measured and removed by calibration.

Three practical obstacles make that idea hard to teach:

- **Access.** Laboratory VNAs are expensive and shared. Low-cost instruments
  such as the NanoVNA have made one instrument per student possible
  {cite}`derickson2021, caverly2021`, but a course still needs a lab session
  for every measurement.
- **The calibration is a menu.** On the instrument, calibration is three
  button presses. What happens behind them, a small linear system per
  frequency, stays invisible.
- **Real data has no answer key.** A student who calibrates a real
  measurement cannot tell a correct result from a plausible-looking wrong one.

The module addresses these with a computational approach: students build the
error model and the calibration themselves in Jupyter notebooks, first on a
synthetic instrument whose answer is known and then on real NanoVNA
measurements shipped with the module. No instrument is needed.

## 2. Design principles

| Principle | What it means in the material |
|---|---|
| **Coding to learn, not learning to code** | Students write only the code that carries the idea (about ten lines: the error model, the solver, the correction). Plotting and data loading are provided. |
| **Predict, run, explain** | Before each key cell a "Predict before you run" prompt asks for a commitment; the text after the cell explains the outcome. This follows the predict–observe–explain strategy {cite}`white1992`. There are 17 such prompts. |
| **Synthetic first, real second** | Every method is first verified on a made-up instrument with known errors (exact answer), then applied to recorded data (consistency checks only). |
| **No hardware required** | All lessons run on simulated data or on real measurements included in the repository. The planned hardware notebook (04) is optional. |
| **Libraries after understanding** | Students write the calibration by hand, then confirm that `scikit-rf` {cite}`scikitrf` gives the same answer. The library becomes a tool whose behaviour they know. |
| **Honest about limits** | Each lesson says what it does not cover; the instructor guide lists known limitations; the status of the module (not yet used in a classroom) is stated everywhere. |
| **Open and reproducible** | Code under BSD-3-Clause, content and data under CC BY 4.0. Notebooks are stored without outputs and executed in continuous integration. |

## 3. Audience and prerequisites

- Undergraduate students of biomedical, electronic or telecommunication
  engineering, after a first course on circuits; master's and final-year
  project students; self-learners starting with a NanoVNA.
- **Prerequisites:** phasors and complex impedance; basic Python with NumPy
  and Matplotlib.
- **Not required:** any previous RF or transmission-line course; any
  hardware.
- **Languages:** English and Spanish, with identical content and code.

## 4. From learning outcomes to activities

The module has six learning outcomes (section 2 of the
[instructor guide](../instructor/guia_docente.md#2-what-students-learn)).
The table maps each one to the concepts involved, the activities that
address it, and the evidence an instructor can look for. Only activities that
exist in the material are listed.

| Learning outcome | Concepts | Notebook and activity | Evidence of the outcome |
|---|---|---|---|
| 1. Explain a reflection measurement in terms of waves; convert between Γ and Z | incident and reflected waves, S-parameters, return loss, Γ ↔ Z | 00 §2–4 (standing waves, a resistor behind a cable); 01 §1 (write `z_to_gamma`, `gamma_to_z`); exercises 00.1–00.4, 01.1 | Correct conversions; explanation of why total voltage alone cannot separate two waves (00, question 4) |
| 2. Read a Smith chart; recognise circuits from traces | resistance and reactance circles, conductance circles, resonance, delay | 01 §2 (build the chart), §3 (traces of RL, RC, RLC, line), §4 (guess three mystery circuits); exercises 01.2–01.4 | Topology chosen from the shape before computing; component values within a few percent |
| 3. Describe the three systematic error terms and predict their effect | directivity, source match, reflection tracking; three-term model | 02 §1–2 (one flaw at a time), §3 (all three across frequency), §4 (raw real data); exercises 02.1–02.4 | Prediction of which device each term distorts; explanation of ripple and of the raw open reading \|Γ\| = 2.1 |
| 4. Derive, implement and apply SOL calibration | linearisation, 3×3 system per frequency, correction formula | 03 §1–3 (derive and write the solver, verify on synthetic data), §4–5 (real data, comparison with `scikit-rf`); exercises 03.1, 03.3, 03.4 | Working solver that matches `scikit-rf`; corrected resistors within about 2 Ω below 10 MHz |
| 5. Judge a calibrated result | held-out testing, reference plane, imperfect standards, repeatability, passivity | 03 §4.2–4.3, §6; 05 §2–4; exercises 03.2, 03.5, 05.1–05.3 | Calibration tested on unseen repetitions; passivity violations interpreted, not clipped |
| 6. Report a result with uncertainty, limitations and context | Type A uncertainty, validation status with evidence, provenance | 05 §3, §5–6; exercise 05.4; summative assignment | Uncertainty stated with what it includes and excludes; traceable record of data and processing |

Each notebook also ends with "Check your understanding" questions (19 in
total, answers one click away) and open exercises (21 in total, with worked
solutions). The summative assignment and its rubric are in the
[instructor guide](../instructor/guia_docente.md#9-summative-assessment).

## 5. Sequencing

```
00 ──► 01 ──► 02 ──► 03 ──► 05        (04: optional, hardware, planned)
```

| Stage | Notebook | Why it comes here |
|---|---|---|
| Fundamentals of S-parameters and network analysis | 00 | Everything later is a statement about Γ; students need waves, not voltages, before any error can be defined. |
| Interpreting measurements and graphical representations | 01 | Errors and calibration are shown on the Smith chart; reading it must come first. Section 3.4 (a delay draws a circle) is planted here because it returns in real data in 03. |
| Introduction to systematic errors | 02, §1–3 | Each error term is introduced alone on a synthetic instrument, so its effect is unambiguous before the three are combined. |
| Real data, uncorrected | 02, §4 | The raw open reading \|Γ\| = 2.1 creates the need for calibration before it is introduced. |
| Error model and SOL calibration | 03, §1–5 | Derived as the inverse of the model built in 02; verified exactly on synthetic data, then applied to real data. |
| Ideal, simulated and real results compared | 03, §4–6 | The reference plane and imperfect standards are met as apparent failures of the calibration and resolved from the data. |
| Interpreting results and discussing limitations | 05 | Repeatability, passivity and traceability turn a corrected number into a reportable result. Marked "advanced" so it can be dropped without breaking the sequence. |

Three paths through the module (full, without validation, calibration only)
and a session plan with time estimates are in sections 3 and 4 of the
[instructor guide](../instructor/guia_docente.md#3-how-the-notebooks-depend-on-each-other).

## 6. Theory, simulation and real data

| Notebook | Analytic theory | Synthetic data | Recorded NanoVNA data | Reference implementation |
|---|---|---|---|---|
| 00 | waves on a line, S-parameters | ideal cable and resistor | — | `scikit-rf` cascade of networks |
| 01 | Γ ↔ Z mapping, Smith chart | RL, RC, RLC, line; mystery circuits | — | — |
| 02 | three-term error model | `synthetic_error_terms` (exaggerated errors) | raw short, open, load | — |
| 03 | linearised SOL system, correction | synthetic instrument, imperfect standards | standards (10 repetitions), 33 Ω and 75 Ω resistors (3 each) | `skrf.calibration.OnePort` |
| 05 | Type A uncertainty, passivity | — | same recorded data | `rfmeasurement` validation rules {cite}`rfmeasurement` |

Simulated and recorded data are never mixed in one figure without a label:
synthetic data comes from functions in `vnacourse.errormodel` and
`vnacourse.puzzles`; recorded data is always loaded with
`vnacourse.data.load_repetitions` from `data/`, whose provenance is
documented in [`data/README.md`](../data/README.md) {cite}`nanovnacal`.

## 7. Hardware and time

| Activity | Hardware | Time (estimate) |
|---|---|---|
| Notebooks 00, 01, 02, 03, 05 and their exercises | none | 10–14 h in total |
| Summative assignment | none (recorded data) | 2–3 h |
| Notebook 04, acquisition with a NanoVNA | NanoVNA, cables, SOL kit (optional) | not yet available |
| Hands-on session suggested in the guide (§10) | NanoVNA (optional) | one session |

The times are estimates from the length of the material and will be replaced
by measured times after the first classroom use.

## 8. Design decisions

- **One port only.** A one-port measurement has three error terms that a
  student can derive and solve by hand. Two-port calibration (twelve terms)
  is left as a pointer in the guide.
- **Python and Jupyter.** Free, runnable in a browser through Binder and
  Colab, and the format in which open engineering modules are commonly shared
  {cite}`barba2019, barba2020`.
- **A small helper package.** `vnacourse` holds what students do not need to
  write (plot style, data loading) and, after they have written them, the
  functions from 02 and 03, so later notebooks can reuse them.
- **Real data from a documented source.** The measurements come from a
  research repository archived on Zenodo, copied byte for byte. Their gaps
  (calibration kit, fixture) are stated and used as a lesson on traceability.
- **Bilingual.** The Spanish edition (`es/`) mirrors the English one cell by
  cell; a test checks that both run the same code.

## References

```{bibliography}
:filter: docname in docnames
```
