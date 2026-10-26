# Validación técnica

Qué se ha comprobado para establecer que el módulo funciona según lo
especificado: el código calcula lo que dice el texto, los cuadernos se
ejecutan desde una instalación limpia, las cifras que citan las lecciones
salen del código y los datos, y las dos ediciones lingüísticas avanzan a la
par. La página de [diseño](design.md) describe lo que el módulo pretende
hacer.

```{admonition} Lo que esta página no afirma
:class: warning
La validación técnica muestra que el material es correcto y reproducible. No
es evidencia de que el alumnado aprenda con él: el módulo todavía no se ha
usado en un aula y no se ha medido ningún resultado de aprendizaje.
```

## 1. Entorno

El módulo necesita Python 3.10 o posterior y tres bibliotecas (NumPy,
Matplotlib, scikit-rf); el cuaderno 05 añade `rfmeasurement`. Las versiones
solo se fijan por abajo, en
[`pyproject.toml`](https://github.com/telmomm/nanovna-measurement-course/blob/main/pyproject.toml)
y [`environment.yml`](https://github.com/telmomm/nanovna-measurement-course/blob/main/environment.yml).

La validación que se recoge aquí se ejecutó el 24 de octubre de 2026 en un
entorno virtual nuevo creado a partir de `pyproject.toml`
(`pip install -e ".[book,dev]"`):

| Componente | Versión |
|---|---|
| Sistema operativo | macOS 26.6.2, arm64 |
| Python | 3.12.9 |
| NumPy / SciPy / Matplotlib | 2.5.4 / 1.18.1 / 3.11.2 |
| scikit-rf | 2.2.0 |
| rfmeasurement | 0.3.0 |
| Jupyter Book / Sphinx | 1.0.4.post1 / 7.4.7 |
| TeX (edición PDF) | XeTeX, TeX Live 2026 |

Los flujos de integración continua de `.github/workflows/` ejecutan las
mismas comprobaciones en Ubuntu con Python 3.10, 3.12 y 3.13, y en el entorno
conda que usa Binder. Sus resultados para esta versión no forman parte de este
informe: se recogerán aquí tras la primera ejecución en GitHub.

## 2. Comprobaciones

| Comprobación | Método | Automatizada | Resultado (24-10-2026) |
|---|---|---|---|
| Estilo del código | `ruff check`, `ruff format --check` sobre el paquete, los tests y todos los cuadernos | sí (CI) | correcto |
| Funciones del paquete | tests unitarios en `tests/test_calibration.py`, `test_puzzles.py`, `test_package.py` | sí (CI) | 12 correctos |
| Casos de referencia analíticos | `tests/test_reference_values.py`: ejemplos Γ ↔ Z, pérdidas de retorno, longitud de onda y retardo, frecuencia de resonancia, una resistencia tras una línea | sí (CI) | correcto |
| Recuperación exacta con datos sintéticos | el resolvedor SOL recupera los términos de error del instrumento sintético y el dispositivo real hasta el error de redondeo, con definiciones de estándares ideales y no ideales | sí (CI) | correcto |
| Implementación independiente | términos de error y Γ corregido comparados con `skrf.calibration.OnePort` en los datos medidos | sí (CI, y en el cuaderno 03) | idénticos hasta el redondeo |
| Cifras citadas en el texto | cada cifra que las lecciones y la guía dan sobre los datos (tabla de la sección 3) se recalcula en `tests/test_reference_values.py` | sí (CI) | correcto, tras una corrección (sección 4) |
| Valores esperados de la práctica | la tabla de resultados esperados de la guía docente, recalculada para las 120 elecciones de tres repeticiones de diez | sí (CI) | las 120 dentro de los intervalos declarados |
| Ejecución de los cuadernos | los 10 cuadernos en inglés y los 10 en español (lecciones y soluciones), ejecutados de principio a fin con `nbmake` | sí (CI) | 20 correctos, 37 s en total |
| Figuras y salidas | los dos libros construidos con `jupyter-book build -W`, que ejecuta todos los cuadernos y falla ante cualquier aviso (enlace roto, figura ausente, celda fallida); edición PDF construida con XeLaTeX | sí (flujo del libro) | HTML: sin avisos; PDF: generado |
| Paridad entre idiomas | `tests/test_translations.py`: cada cuaderno en español tiene las mismas celdas que el inglés, y su código es idéntico token a token una vez eliminados comentarios, cadenas y formato | sí (CI) | 10 pares correctos |
| Datos simulados y reales separados | inspección: los datos sintéticos solo proceden de `vnacourse.errormodel` y `vnacourse.puzzles`; los medidos, solo de `vnacourse.data.load_repetitions` | no | coherente en todos los cuadernos |
| Procedencia de los datos | `data/README.md` declara que los ficheros son una copia byte a byte de la fuente archivada | no | no se ha vuelto a verificar contra la fuente en esta validación |
| Binder y Colab | insignias de arranque en cada cuaderno | no | no probado en esta validación |

Para reproducir las comprobaciones automatizadas:

```bash
python -m pip install -e ".[book,dev]"
ruff check . && ruff format --check .
pytest                                            # tests unitarios, de referencia y de paridad
pytest --nbmake notebooks exercises es            # los 20 cuadernos
tools/build_book.sh                               # los dos libros, HTML y PDF
```

## 3. Cifras citadas en las lecciones

| Dónde | Afirmación | Recalculado |
|---|---|---|
| 00 | longitud de onda en el cable a 300 MHz; retardo de 20 cm | 0.70 m; 0.95 ns |
| 01 | Γ de 50 − j50 Ω; Z en Γ = j0.5; resonancia del RLC serie | 0.2 − 0.4j; 30 + j40 Ω; 503 MHz |
| 01 | 75 Ω tras 20 cm de cable parecen de 33 Ω a 75 Ω | de 33.3 Ω a 75.0 Ω |
| 02, `data/README.md` | el abierto en bruto llega a \|S11\| = 2.1 | 2.13 |
| 03 | la resistencia de 75 Ω en bruto en el instrumento sintético oscila entre unos 0.09 y 0.27 | de 0.086 a 0.266 |
| 03 | por encima de 150 MHz el seguimiento está a unos pocos por ciento de 1 | de 0.994 a 1.015 |
| 03 | residuo con datos reservados: unas milésimas (cortocircuito, abierto), unas diezmilésimas (carga) | medianas 0.0015, 0.0016, 0.0003 |
| 03 | alrededor de 1 ns de línea entre el plano de calibración y las resistencias | 1.05 ns (33 Ω), 1.01 ns (75 Ω) |
| 03 | tras eliminarlo, la de 75 Ω varía entre unos −8 Ω y +15 Ω en la parte alta de la banda | de 66.6 Ω a 89.5 Ω |
| 05 | dispersión típica de 0.003 (cortocircuito, abierto), 0.0005 (carga), unas seis veces mejor | 0.0029, 0.0031, 0.0005 |
| 05 | los puntos ruidosos se agrupan tras los múltiplos de 100 | 43 de 53 |
| 05 | 75 Ω por debajo de 10 MHz: 74.0 Ω, incertidumbre típica de unos 0.2 Ω | 73.99 Ω, 0.18 Ω |
| 05 | el abierto calibrado supera 1 en algo menos de la mitad de los puntos | 43 % |
| Guía §9 | práctica: R por debajo de 10 MHz 32.3–32.5 Ω; retardo de unos 1.05 ns; abierto reservado 0.0015–0.0018; u de unos 0.09 Ω | 32.34–32.47 Ω; 1.048 ns; 0.0015–0.0018; 0.084–0.089 Ω |

## 4. Hallazgos

- **Corregido:** el cuaderno 03 (sección 4.2) decía que, tras eliminar el
  retardo de la línea, la resistencia de 75 Ω variaba «aproximadamente
  ±10 Ω» en lo alto de la banda. El intervalo recalculado es de −8.4 Ω a
  +14.5 Ω, con el máximo cerca de 1.41 GHz. El texto dice ahora «entre unos
  −8 Ω y +15 Ω» en ambos idiomas, y un test fija el valor.
- Ninguna otra afirmación de las lecciones, las soluciones o la guía
  discrepaba del código o de los datos.

## 5. Problemas conocidos y limitaciones

- **`rfmeasurement` 0.3.0 y los datos de un puerto.** Su regla de pasividad
  integrada devuelve un fallo para toda red de un puerto. El cuaderno 05 la
  excluye y pide al alumnado escribir una regla de un puerto; si se corrige la
  biblioteca, habría que revisar esa sección.
- **Nombres en el repositorio de origen.** El término `er` de
  [nanovna-calibration](https://github.com/telmomm/nanovna-calibration) es
  $e_{10}e_{01} - e_{00}e_{11}$, no el seguimiento de reflexión. El cuaderno 03
  explica la diferencia y el ejercicio 03.3 comprueba que el Γ corregido no se
  ve afectado.
- **Lagunas en el registro de los datos.** No se registraron el kit de
  calibración y su definición, el utillaje de las resistencias, si estaba
  activa la calibración interna del instrumento ni la configuración de
  adquisición. Las lecciones tratan los estándares como ideales e infieren de
  los datos el retardo de la línea.
- **Metadatos de citación.** `CITATION.cff` da como DOI de los datos de origen
  `10.5281/zenodo.22722704`, mientras que `data/README.md` y las lecciones usan
  `10.5281/zenodo.22722703`. Hay que corregir uno de los dos.
- **El cuaderno 04** (adquisición con un NanoVNA) todavía no existe.
- **Salidas de terceros en inglés.** En la edición española, los mensajes y el
  informe que genera `rfmeasurement` siguen en inglés; el cuaderno 05 lo
  advierte.
- **Tipografía de las figuras.** Las figuras usan IBM Plex Sans cuando está
  instalada (el flujo del libro la instala) y, si no, la fuente por defecto de
  Matplotlib; el contenido no cambia.

## 6. Datos: simulados o medidos

| Fuente | De dónde procede | Se usa en |
|---|---|---|
| Cable y resistencia ideales | fórmulas en el cuaderno | 00, 01 |
| Circuitos misteriosos | `vnacourse.puzzles` (circuitos en forma cerrada) | 01 |
| Instrumento sintético | `vnacourse.errormodel.synthetic_error_terms`, exagerado a propósito y etiquetado como tal | 02, 03 |
| Estándares imperfectos | fórmulas en el cuaderno 03, sección 6 | 03 |
| Barridos medidos con el NanoVNA-F V2 | `data/` mediante `vnacourse.data.load_repetitions`, procedencia en `data/README.md` | 02, 03, 05 |
