# Diseño del módulo

Cómo se diseñó *Hands-on VNA*: la necesidad que aborda, los principios en los
que se basa, cómo se corresponden sus resultados de aprendizaje con las
actividades y por qué las lecciones siguen este orden. La
[validación técnica](validation.md) describe cómo se ha comprobado el
material.

```{admonition} Estado
:class: note
Versión 0.1.0. El diseño descrito aquí se ha comprobado técnicamente, no
pedagógicamente: el módulo todavía no se ha usado con estudiantes, así que
nada de esta página es una afirmación sobre lo que el alumnado aprende con él.
```

## 1. La necesidad

Un analizador vectorial de redes (VNA) mide cómo refleja y transmite un
dispositivo una onda, en módulo y fase. Usarlo bien depende de una idea fácil
de enunciar y difícil de asimilar: el instrumento no muestra el dispositivo,
sino el dispositivo visto a través de sus propios errores sistemáticos, y esos
errores hay que medirlos y eliminarlos mediante la calibración.

Tres obstáculos prácticos hacen difícil enseñar esa idea:

- **Acceso.** Los VNA de laboratorio son caros y compartidos. Los
  instrumentos de bajo coste como el NanoVNA han hecho posible un instrumento
  por estudiante {cite}`derickson2021, caverly2021`, pero una asignatura sigue
  necesitando una sesión de laboratorio para cada medida.
- **La calibración es un menú.** En el instrumento, calibrar son tres
  pulsaciones de botón. Lo que ocurre detrás, un pequeño sistema lineal por
  frecuencia, queda invisible.
- **Los datos reales no tienen solucionario.** Quien calibra una medida real
  no puede distinguir un resultado correcto de uno erróneo de aspecto
  verosímil.

El módulo los aborda con un enfoque computacional: el alumnado construye el
modelo de error y la calibración en cuadernos Jupyter, primero sobre un
instrumento sintético cuya respuesta se conoce y después sobre medidas reales
de un NanoVNA incluidas con el módulo. No se necesita el instrumento.

## 2. Principios de diseño

| Principio | Qué significa en el material |
|---|---|
| **Programar para aprender, no aprender a programar** | El alumnado solo escribe el código que lleva la idea (unas diez líneas: el modelo de error, el resolvedor, la corrección). Las gráficas y la carga de datos se proporcionan. |
| **Predecir, ejecutar, explicar** | Antes de cada celda clave, una indicación «Predice antes de ejecutar» pide un compromiso; el texto posterior explica el resultado. Sigue la estrategia predecir–observar–explicar {cite}`white1992`. Hay 17 indicaciones de este tipo. |
| **Primero sintético, después real** | Cada método se verifica primero en un instrumento inventado con errores conocidos (respuesta exacta) y después se aplica a datos medidos (solo comprobaciones de coherencia). |
| **Sin hardware** | Todas las lecciones se ejecutan con datos simulados o con medidas reales incluidas en el repositorio. El cuaderno con hardware previsto (04) es opcional. |
| **Bibliotecas después de entender** | El alumnado escribe la calibración a mano y después comprueba que `scikit-rf` {cite}`scikitrf` da la misma respuesta. La biblioteca pasa a ser una herramienta cuyo comportamiento conoce. |
| **Honestidad sobre los límites** | Cada lección dice lo que no cubre; la guía docente enumera las limitaciones conocidas; el estado del módulo (todavía sin uso en aula) se declara en todas partes. |
| **Abierto y reproducible** | Código bajo BSD-3-Clause; contenido y datos bajo CC BY 4.0. Los cuadernos se guardan sin salidas y se ejecutan en integración continua. |

## 3. Público y requisitos previos

- Estudiantes de grado de Ingeniería Biomédica, Electrónica o de
  Telecomunicación, tras una primera asignatura de circuitos; estudiantes de
  máster y de TFG/TFM; autodidactas que empiezan con un NanoVNA.
- **Requisitos previos:** fasores e impedancia compleja; Python básico con
  NumPy y Matplotlib.
- **No se necesita:** ninguna asignatura previa de RF ni de líneas de
  transmisión; ningún hardware.
- **Idiomas:** inglés y español, con el mismo contenido y el mismo código.

## 4. De los resultados de aprendizaje a las actividades

El módulo tiene seis resultados de aprendizaje (sección 2 de la
[guía docente](../instructor/guia_docente.md#2-qué-aprende-el-alumnado)). La
tabla relaciona cada uno con los conceptos implicados, las actividades que lo
trabajan y la evidencia que puede buscar el profesorado. Solo se incluyen
actividades que existen en el material.

| Resultado de aprendizaje | Conceptos | Cuaderno y actividad | Evidencia del resultado |
|---|---|---|---|
| 1. Explicar una medida de reflexión en términos de ondas; convertir entre Γ y Z | ondas incidente y reflejada, parámetros S, pérdidas de retorno, Γ ↔ Z | 00 §2–4 (ondas estacionarias, una resistencia tras un cable); 01 §1 (escribir `z_to_gamma`, `gamma_to_z`); ejercicios 00.1–00.4, 01.1 | Conversiones correctas; explicación de por qué la tensión total no basta para separar dos ondas (00, pregunta 4) |
| 2. Leer una carta de Smith; reconocer circuitos por sus trazas | circunferencias de resistencia y reactancia, circunferencias de conductancia, resonancia, retardo | 01 §2 (construir la carta), §3 (trazas de RL, RC, RLC, línea), §4 (adivinar tres circuitos misteriosos); ejercicios 01.2–01.4 | Topología elegida por la forma antes de calcular; valores de componentes con un error de unos pocos por ciento |
| 3. Describir los tres términos de error sistemático y predecir su efecto | directividad, desadaptación de fuente, seguimiento de reflexión; modelo de tres términos | 02 §1–2 (un defecto cada vez), §3 (los tres a lo largo de la frecuencia), §4 (datos reales en bruto); ejercicios 02.1–02.4 | Predicción de qué dispositivo distorsiona cada término; explicación del rizado y de la lectura en bruto del abierto \|Γ\| = 2.1 |
| 4. Deducir, implementar y aplicar la calibración SOL | linealización, sistema 3×3 por frecuencia, fórmula de corrección | 03 §1–3 (deducir y escribir el resolvedor, verificarlo con datos sintéticos), §4–5 (datos reales, comparación con `scikit-rf`); ejercicios 03.1, 03.3, 03.4 | Resolvedor que coincide con `scikit-rf`; resistencias corregidas a unos 2 Ω de su valor por debajo de 10 MHz |
| 5. Juzgar un resultado calibrado | prueba con datos reservados, plano de referencia, estándares imperfectos, repetibilidad, pasividad | 03 §4.2–4.3, §6; 05 §2–4; ejercicios 03.2, 03.5, 05.1–05.3 | Calibración probada con repeticiones no vistas; violaciones de la pasividad interpretadas, no recortadas |
| 6. Comunicar un resultado con incertidumbre, limitaciones y contexto | incertidumbre de tipo A, estado de validación con evidencia, procedencia | 05 §3, §5–6; ejercicio 05.4; práctica evaluable | Incertidumbre declarada con lo que incluye y excluye; registro trazable de datos y procesado |

Cada cuaderno termina además con preguntas «Comprueba lo que has entendido»
(19 en total, con la respuesta a un clic) y ejercicios abiertos (21 en total,
con soluciones resueltas). La práctica evaluable y su rúbrica están en la
[guía docente](../instructor/guia_docente.md#9-evaluación-sumativa).

## 5. Secuenciación

```
00 ──► 01 ──► 02 ──► 03 ──► 05        (04: opcional, con hardware, previsto)
```

| Etapa | Cuaderno | Por qué va aquí |
|---|---|---|
| Fundamentos de parámetros S y análisis de redes | 00 | Todo lo posterior es una afirmación sobre Γ; hacen falta ondas, no tensiones, antes de poder definir ningún error. |
| Interpretación de medidas y representaciones gráficas | 01 | Los errores y la calibración se muestran en la carta de Smith; antes hay que saber leerla. La sección 3.4 (un retardo dibuja una circunferencia) se siembra aquí porque reaparece en los datos reales del 03. |
| Introducción a los errores sistemáticos | 02, §1–3 | Cada término de error se presenta solo, en un instrumento sintético, para que su efecto sea inequívoco antes de combinar los tres. |
| Datos reales, sin corregir | 02, §4 | La lectura en bruto del abierto \|Γ\| = 2.1 crea la necesidad de calibrar antes de presentar la calibración. |
| Modelo de error y calibración SOL | 03, §1–5 | Se deduce como la inversa del modelo construido en el 02; se verifica exactamente con datos sintéticos y después se aplica a datos reales. |
| Comparación de resultados ideales, simulados y reales | 03, §4–6 | El plano de referencia y los estándares imperfectos aparecen como aparentes fallos de la calibración y se resuelven a partir de los datos. |
| Interpretación de resultados y discusión de limitaciones | 05 | La repetibilidad, la pasividad y la trazabilidad convierten un número corregido en un resultado comunicable. Marcado como «avanzado» para poder eliminarlo sin romper la secuencia. |

Los tres itinerarios del módulo (completo, sin validación, solo calibración) y
un plan de sesiones con tiempos estimados están en las secciones 3 y 4 de la
[guía docente](../instructor/guia_docente.md#3-cómo-dependen-los-cuadernos-entre-sí).

## 6. Teoría, simulación y datos reales

| Cuaderno | Teoría analítica | Datos sintéticos | Datos medidos con el NanoVNA | Implementación de referencia |
|---|---|---|---|---|
| 00 | ondas en una línea, parámetros S | cable y resistencia ideales | — | conexión en cascada de redes con `scikit-rf` |
| 01 | correspondencia Γ ↔ Z, carta de Smith | RL, RC, RLC, línea; circuitos misteriosos | — | — |
| 02 | modelo de error de tres términos | `synthetic_error_terms` (errores exagerados) | cortocircuito, abierto y carga en bruto | — |
| 03 | sistema SOL linealizado, corrección | instrumento sintético, estándares imperfectos | estándares (10 repeticiones), resistencias de 33 Ω y 75 Ω (3 cada una) | `skrf.calibration.OnePort` |
| 05 | incertidumbre de tipo A, pasividad | — | los mismos datos medidos | reglas de validación de `rfmeasurement` {cite}`rfmeasurement` |

Los datos simulados y los medidos nunca se mezclan en una figura sin una
etiqueta: los sintéticos proceden de funciones de `vnacourse.errormodel` y
`vnacourse.puzzles`; los medidos se cargan siempre con
`vnacourse.data.load_repetitions` desde `data/`, cuya procedencia está
documentada en [`data/README.md`](../data/README.md) {cite}`nanovnacal`.

## 7. Hardware y tiempo

| Actividad | Hardware | Tiempo (estimación) |
|---|---|---|
| Cuadernos 00, 01, 02, 03, 05 y sus ejercicios | ninguno | 10–14 h en total |
| Práctica evaluable | ninguno (datos medidos) | 2–3 h |
| Cuaderno 04, adquisición con un NanoVNA | NanoVNA, cables, kit SOL (opcional) | todavía no disponible |
| Sesión práctica sugerida en la guía (§10) | NanoVNA (opcional) | una sesión |

Los tiempos son estimaciones a partir de la extensión del material y se
sustituirán por tiempos medidos tras el primer uso en el aula.

## 8. Decisiones de diseño

- **Solo un puerto.** Una medida de un puerto tiene tres términos de error que
  el alumnado puede deducir y resolver a mano. La calibración de dos puertos
  (doce términos) queda como referencia en la guía.
- **Python y Jupyter.** Gratuitos, ejecutables en el navegador mediante Binder
  y Colab, y el formato en el que suelen compartirse los módulos abiertos de
  ingeniería {cite}`barba2019, barba2020`.
- **Un paquete auxiliar pequeño.** `vnacourse` contiene lo que el alumnado no
  necesita escribir (estilo de las gráficas, carga de datos) y, una vez que lo
  ha escrito, las funciones de los cuadernos 02 y 03, para que los siguientes
  puedan reutilizarlas.
- **Datos reales de una fuente documentada.** Las medidas proceden de un
  repositorio de investigación archivado en Zenodo, copiadas byte a byte. Sus
  lagunas (kit de calibración, utillaje) se declaran y se usan como lección
  sobre trazabilidad.
- **Bilingüe.** La edición en español (`es/`) replica la inglesa celda a
  celda; un test comprueba que ambas ejecutan el mismo código.

## Referencias

```{bibliography}
:filter: docname in docnames
```
