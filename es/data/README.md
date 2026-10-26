# Datos

Medidas reales de reflexión de un puerto que usan los cuadernos. Los ficheros
son [Touchstone](https://en.wikipedia.org/wiki/Touchstone_file) `.s1p`, con la
parte real e imaginaria de S11 referidas a 50 Ω, y pueden abrirse con
cualquier herramienta de RF o leerse como texto.

Los datos son los mismos para las dos versiones del curso y están en la
carpeta [`data/`](https://github.com/telmomm/nanovna-measurement-course/tree/main/data) de la raíz del repositorio; esta página solo
los describe en español. En los cuadernos se cargan con
`vnacourse.data.load_repetitions`, por ejemplo
`load_repetitions("standards", "open")`.

## Contenido

| Carpeta | Dispositivo medido | Repeticiones |
|---|---|---|
| `standards/short/` | estándar de calibración de cortocircuito | 10 |
| `standards/open/` | estándar de calibración de circuito abierto | 10 |
| `standards/load/` | estándar de calibración de carga de 50 Ω | 10 |
| `dut/load_33ohm/` | resistencia de 33 Ω | 3 |
| `dut/load_75ohm/` | resistencia de 75 Ω | 3 |

Cada repetición es un barrido independiente guardado en su propio fichero,
`rep_01.s1p`, `rep_02.s1p`, etc.

## Adquisición

| | |
|---|---|
| Instrumento | NanoVNA-F V2 |
| Intervalo de frecuencias | de 50 kHz a 1.45 GHz |
| Puntos por barrido | 1001, espaciados linealmente (unos 1.45 MHz) |
| Impedancia de referencia | 50 Ω |
| Corrección aplicada | ninguna por parte del software de adquisición: el repositorio de origen registra estos barridos como «sin calibrar / en bruto» |

Lo que muestran los propios datos, y en lo que se apoyan los cuadernos:

- Las lecturas de los tres estándares están lejos de lo ideal por debajo de
  unos 150 MHz (el abierto llega a |S11| = 2.1) y a unos pocos por ciento de
  lo ideal por encima.
- Tras una calibración SOL calculada a partir de `standards/`, las dos
  resistencias leen a unos 2 Ω de sus valores nominales por debajo de 10 MHz.
- En toda la banda, el coeficiente de reflexión corregido de ambas
  resistencias gira como lo haría tras aproximadamente 1 ns de línea de
  transmisión. Por tanto, las resistencias no estaban en el plano de
  calibración. El cuaderno 03 lo usa para hablar del plano de referencia.

No se registró con los datos: el modelo y la definición del kit de
calibración, el utillaje o cable usado para las resistencias, el par de
apriete de los conectores, la temperatura ni el tiempo de calentamiento. Los
cuadernos tratan los estándares como ideales.

## Procedencia

Los ficheros están copiados, byte a byte, del repositorio de investigación
[telmomm/nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
(commit `0d0cb62`), archivado en Zenodo:
[doi:10.5281/zenodo.22722703](https://doi.org/10.5281/zenodo.22722703).
Solo cambian las rutas:

| Aquí | En nanovna-calibration |
|---|---|
| `standards/<estándar>/rep_NN.s1p` | `data/calibration/<estándar>/test_N.s1p` |
| `dut/load_33ohm/rep_NN.s1p` | `data/measures/load 33 (5)/test_N.s1p` |
| `dut/load_75ohm/rep_NN.s1p` | `data/measures/load 75 (6)/test_N.s1p` |

Ese repositorio contiene más medidas (otros juegos de estándares,
atenuadores, una red LC y versiones de dos puertos `.s2p` de cada barrido).

## Licencia

[Creative Commons Reconocimiento 4.0 Internacional](../../LICENSE-CONTENT). Si
usas los datos, cita el registro de Zenodo anterior.
