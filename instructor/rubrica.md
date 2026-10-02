# Assessment rubric

Rubric for the summative assignment described in the
[instructor guide](guia_docente.md#9-summative-assessment), *Characterise a
resistor from raw data*, followed by a short scale for the weekly exercises.

> Like the rest of the instructor material, this rubric has not yet been used
> to mark real submissions. Treat the weights as a starting point.

## How to use it

- Six criteria, each marked on four levels. For each criterion compute
  weight × level ÷ 4 and add them up: the total is 100 when every criterion
  is at level 4, and 25 when every criterion is at level 1.
- The levels describe **what is in the submission**, not how much effort it
  shows. Mark the highest level whose description is fully met.
- Criteria B and D carry the understanding; A and C carry the execution. A
  submission can have every number right and still sit at level 2 in B and D.
- Share the rubric with students when you set the assignment.

| | Criterion | Weight | Assignment steps | Module outcomes |
|---|---|---|---|---|
| A | Calibration procedure | 25 | 1, 2 | 3, 4 |
| B | Interpretation of the calibrated result | 20 | 1, 3 | 1, 2, 4 |
| C | Validation | 20 | 4, 5 | 5 |
| D | Uncertainty and limitations | 15 | 6 | 5, 6 |
| E | Reproducibility and traceability | 10 | 7 | 6 |
| F | Communication | 10 | all | |

The module outcomes are numbered as in section 2 of the
[guide](guia_docente.md#2-what-students-learn).

## The rubric

### A. Calibration procedure (weight 25)

| Level | Description |
|---|---|
| **4 Excellent** | Error terms computed from the assigned repetitions only, with a solver the student can explain. Correction applied correctly. Resistance below 10 MHz within the expected range. The result is cross-checked, for example against `skrf.calibration.OnePort` or the closed form. |
| **3 Proficient** | Error terms and correction are correct and the resistance is within the expected range. No independent cross-check. |
| **2 Developing** | The procedure is recognisable but has an error that changes the result: wrong repetitions, standards in the wrong order, the correction formula misapplied, or raw and calibrated data confused. |
| **1 Beginning** | No working calibration, or library calls copied without evidence of understanding what they compute. |

### B. Interpretation of the calibrated result (weight 20)

| Level | Description |
|---|---|
| **4 Excellent** | Describes how the three error terms behave across the band and relates them to the raw readings. Recognises that the swing of the resistance with frequency is a rotation of Γ at nearly constant magnitude, attributes it to a length of line beyond the calibration plane, estimates the delay, removes it, and comments on what remains. |
| **3 Proficient** | Identifies the reference-plane effect and estimates the delay correctly, with little comment on the error terms or on the residual variation after removing the delay. |
| **2 Developing** | Shows the swing across the band and notes that something is wrong, but attributes it to a calibration error, to noise or to the resistor, or reports it without explanation. |
| **1 Beginning** | Reports only the low-frequency value, or presents the full-band result without noticing that it is not a constant resistance. |

### C. Validation (weight 20)

| Level | Description |
|---|---|
| **4 Excellent** | Tests the calibration on repetitions not used to compute it and summarises the residual with a robust statistic. Checks passivity for the resistor and for a calibrated standard, and interprets excursions above 1 by comparing their size with the repeatability. Notes what the held-out test cannot detect. |
| **3 Proficient** | Held-out test and passivity check both done and correctly reported, with a reasonable but brief interpretation. |
| **2 Developing** | Only one of the two checks, or the calibration is "validated" on the same data used to compute it, or a value above 1 is treated as a data error and clipped or discarded. |
| **1 Beginning** | No validation, or a statement that the result is correct because it is close to the nominal value. |

### D. Uncertainty and limitations (weight 15)

| Level | Description |
|---|---|
| **4 Excellent** | Gives a standard uncertainty with its derivation, distinguishing the scatter of single readings from the uncertainty of a mean. States which sources it includes and names the main ones it does not: the definition of the standards, the reference plane, the tolerance of the component. Compares the result with the nominal value in units of that uncertainty and draws a justified conclusion. |
| **3 Proficient** | A correctly computed standard uncertainty, with at least one limitation named. |
| **2 Developing** | A number is given as "the error" without a derivation, or the standard deviation of readings is reported as the uncertainty of the mean, or the uncertainty is presented as covering everything. |
| **1 Beginning** | No uncertainty, or the result is reported with meaningless digits. |

### E. Reproducibility and traceability (weight 10)

| Level | Description |
|---|---|
| **4 Excellent** | The notebook runs from top to bottom without changes. It records which data and repetitions were used, the instrument, the calibration and its assumptions, the processing steps and the software versions, and distinguishes what was measured from what was assumed. |
| **3 Proficient** | The notebook runs from top to bottom and states the data, repetitions and calibration used. |
| **2 Developing** | The notebook runs only after fixes (cells out of order, missing definitions), or the reader has to guess which data produced which result. |
| **1 Beginning** | The notebook does not run, or the results in the conclusion cannot be traced to any cell. |

### F. Communication (weight 10)

| Level | Description |
|---|---|
| **4 Excellent** | Every figure has labelled axes with units, a legend where there is more than one trace, and a sentence saying what it shows. Results are stated with units and a sensible number of digits. The conclusion answers the brief in at most one page and can be understood without reading the code. |
| **3 Proficient** | Figures are labelled and results have units. The conclusion is complete but relies on the reader inspecting the notebook. |
| **2 Developing** | Some figures lack labels or units, or the conclusion lists what was done without saying what was found. |
| **1 Beginning** | Figures unlabelled or missing; no conclusion. |

## Marking sheet

| Criterion | Weight | Level (1–4) | Weight × level ÷ 4 |
|---|---|---|---|
| A. Calibration procedure | 25 | | |
| B. Interpretation | 20 | | |
| C. Validation | 20 | | |
| D. Uncertainty and limitations | 15 | | |
| E. Reproducibility and traceability | 10 | | |
| F. Communication | 10 | | |
| **Total** | **100** | | |

A suggested reading of the total: 85 and above, outstanding; 70 to 84, good;
50 to 69, sufficient; below 50, not yet sufficient. Adjust the thresholds to
your institution's scale.

**Quick checks while marking.** The expected values are in the
[guide](guia_docente.md#9-summative-assessment). In practice:

- resistance below 10 MHz outside 32.3–32.5 Ω: look for an error in A;
- no mention of a delay or a line: B is at level 2 or below;
- residuals of exactly zero on the standards: the calibration was tested on
  its own data (C, level 2);
- an uncertainty well below 0.05 Ω or above 1 Ω: check what was computed (D).

## Weekly exercises

For the exercises at the end of each notebook a three-level scale is enough.
Its purpose is to keep students working between sessions, not to rank them.

| Level | Description |
|---|---|
| **Complete** | The exercise is attempted in full, the code runs, and the result comes with a sentence of interpretation: what it shows or why it comes out that way. |
| **Partial** | The exercise is attempted and the code runs, but there is no interpretation, or a part is missing. |
| **Not done** | Not attempted, or copied from the published solution without change. |

Worked solutions are public. An interpretation written in the student's own
words is what distinguishes work from copying, and it is the part worth
reading.

## Predictions

Do not mark the "Predict before you run" answers for correctness. If you
record them at all, record only that a prediction was made. A wrong
prediction followed by a good explanation of the difference is the best
outcome the module can produce.
