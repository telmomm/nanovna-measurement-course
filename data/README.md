# Data

Real one-port reflection measurements used by the notebooks. The files are
[Touchstone](https://en.wikipedia.org/wiki/Touchstone_file) `.s1p`, real and
imaginary parts of S11 referred to 50 Ω, and can be opened with any RF tool
or read as text.

In the notebooks, load them with `vnacourse.data.load_repetitions`, for
example `load_repetitions("standards", "open")`.

## Contents

| Folder | Device measured | Repetitions |
|---|---|---|
| `standards/short/` | short-circuit calibration standard | 10 |
| `standards/open/` | open-circuit calibration standard | 10 |
| `standards/load/` | 50 Ω load calibration standard | 10 |
| `dut/load_33ohm/` | 33 Ω resistor | 3 |
| `dut/load_75ohm/` | 75 Ω resistor | 3 |

Each repetition is a separate sweep saved to its own file, `rep_01.s1p`,
`rep_02.s1p`, and so on.

## Acquisition

| | |
|---|---|
| Instrument | NanoVNA-F V2 |
| Frequency range | 50 kHz to 1.45 GHz |
| Points per sweep | 1001, linearly spaced (about 1.45 MHz apart) |
| Reference impedance | 50 Ω |
| Correction applied | none by the acquisition software: the source repository records these sweeps as "uncalibrated / raw" |

What the data itself shows, and what the notebooks rely on:

- The readings of the three standards are far from ideal below about 150 MHz
  (the open reads up to |S11| = 2.1) and within a few percent of ideal above.
- After a SOL calibration computed from `standards/`, the two resistors read
  within about 2 Ω of their nominal values below 10 MHz.
- Over the full band the corrected reflection coefficient of both resistors
  rotates as it would behind roughly 1 ns of transmission line. The resistors
  were therefore not at the calibration plane. Notebook 03 uses this to
  discuss the reference plane.

Not recorded with the data: the model and definition of the calibration kit,
the fixture or cable used for the resistors, connector torque, temperature
and warm-up time. The notebooks treat the standards as ideal.

## Provenance

The files are copied, byte for byte, from the research repository
[telmomm/nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
(commit `0d0cb62`), archived on Zenodo:
[doi:10.5281/zenodo.22722703](https://doi.org/10.5281/zenodo.22722703).
Only the paths changed:

| Here | In nanovna-calibration |
|---|---|
| `standards/<standard>/rep_NN.s1p` | `data/calibration/<standard>/test_N.s1p` |
| `dut/load_33ohm/rep_NN.s1p` | `data/measures/load 33 (5)/test_N.s1p` |
| `dut/load_75ohm/rep_NN.s1p` | `data/measures/load 75 (6)/test_N.s1p` |

That repository holds more measurements (other standard sets, attenuators,
an LC network, and two-port `.s2p` versions of every sweep).

## Licence

[Creative Commons Attribution 4.0 International](../LICENSE-CONTENT). If you
use the data, cite the Zenodo record above.
