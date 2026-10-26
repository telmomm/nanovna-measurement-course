# Análisis vectorial de redes práctico con un NanoVNA

Un módulo de aprendizaje abierto y computacional sobre la medida y la
calibración de parámetros S. Deduces el modelo de error de un analizador
vectorial de redes (VNA), lo simulas y calibras medidas reales tomadas con un
NanoVNA de bajo coste.

La idea que lo guía es *programar para aprender*, no *aprender a programar*:
el código es el medio para entender la medida, no el objetivo.

```{admonition} Estado
:class: note
Versión 0.1.0. El material está completo, pero todavía no se ha usado en un
aula. Las correcciones y los informes de uso son bienvenidos en
[GitHub](https://github.com/telmomm/nanovna-measurement-course).
```

## Para quién es

- Estudiantes de grado de Ingeniería Biomédica (asignaturas de
  instrumentación y electrónica).
- Estudiantes de grado de Ingeniería Electrónica o de Telecomunicación
  (introducción a la RF y a la medida).
- Autodidactas: estudiantes de máster y de TFG/TFM, y profesionales que
  empiezan con un NanoVNA.

Necesitas circuitos en régimen sinusoidal permanente (fasores, impedancia
compleja) y Python básico con NumPy y Matplotlib. **No** necesitas ninguna
asignatura previa de RF ni **tampoco** el instrumento: todas las lecciones se
ejecutan con datos simulados o con medidas reales incluidas en el módulo.

Calcula entre 10 y 14 horas para todo el módulo.

## Las lecciones

| | Lección | Aprenderás a… |
|---|---|---|
| 00 | [¿Qué mide un VNA?](../../es/notebooks/00_introduccion_vna.ipynb) | explicar las ondas incidente y reflejada, definir los parámetros S y decir qué mide un VNA que no midan otros instrumentos |
| 01 | [Coeficiente de reflexión y carta de Smith](../../es/notebooks/01_reflexion_smith.ipynb) | convertir entre Γ y Z, leer la carta de Smith y reconocer un circuito por su traza |
| 02 | [Errores sistemáticos](../../es/notebooks/02_errores_sistematicos.ipynb) | identificar la directividad, la desadaptación de fuente y el seguimiento de reflexión, y predecir qué distorsiona cada uno |
| 03 | [Calibración SOL](../../es/notebooks/03_calibracion_sol.ipynb) | resolver el sistema cortocircuito–abierto–carga, corregir una medida real y saber lo que la calibración no arregla |
| 05 | [Validación y calidad de la medida](../../es/notebooks/05_validacion_calidad.ipynb) | cuantificar la repetibilidad, usar la pasividad como prueba física y registrar un resultado trazable |

Síguelas en orden: cada una usa la anterior. La lección 04, sobre la
adquisición de tus propias medidas con un NanoVNA, es opcional y todavía no
está disponible.

## Idiomas y formatos

El módulo existe en **español** y en **inglés**, con las mismas lecciones, el
mismo código y la misma numeración:
[read in English](https://telmomm.github.io/nanovna-measurement-course/). Cada
edición está también disponible como
[libro en PDF](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-es.pdf)
([in English](https://telmomm.github.io/nanovna-measurement-course/pdf/hands-on-vna-en.pdf)),
cómodo para leer sin conexión o imprimir; aun así, las lecciones están pensadas
para ejecutarse.

En la versión española se traducen el texto, los comentarios del código, las
etiquetas de las figuras y los mensajes; los nombres de variables y funciones
son los mismos que en la inglesa. Se usa el punto decimal, como en Python,
para que el texto coincida con lo que muestra el código.

## Cómo usar este libro

Leer no basta. Cada lección es un cuaderno Jupyter que te pide **predecir** lo
que mostrará un fragmento de código, **ejecutarlo** y después leer la
**explicación**. Las páginas de este libro muestran los cuadernos ya
ejecutados, lo que es cómodo para leer y repasar, pero el aprendizaje ocurre
cuando los ejecutas tú:

- Usa el icono del cohete de la parte superior de cualquier lección para
  abrirla en **Binder** o **Google Colab**. No hay que instalar nada.
- O [instala el módulo en tu ordenador](setup.md).

Cada lección termina con preguntas para comprobar lo que has entendido (con la
respuesta a un clic) y con ejercicios abiertos. Las soluciones resueltas de
los ejercicios están en este libro; intenta cada ejercicio antes de leer su
solución.

## Si das clase

La [guía docente](../../es/instructor/guia_docente.md) tiene un plan de
sesiones, notas sobre cada lección y una práctica evaluable, y hay una
[rúbrica](../../es/instructor/rubrica.md) para corregirla.

## Sobre este recurso

Cómo se diseñó el módulo, de los resultados de aprendizaje a las actividades,
se describe en [Diseño del módulo](../../es/docs/design.md), y lo que se ha
comprobado para mostrar que funciona como se describe está en
[Validación técnica](../../es/docs/validation.md).

## Licencia y cita

El código se publica bajo la licencia BSD de 3 cláusulas. El texto, las
figuras y los datos se publican bajo Creative Commons Reconocimiento 4.0
Internacional (CC BY 4.0).

Si usas el módulo, cita la versión archivada,
[doi:10.5281/zenodo.23669895](https://doi.org/10.5281/zenodo.23669895), con los metadatos de
[`CITATION.cff`](https://github.com/telmomm/nanovna-measurement-course/blob/main/CITATION.cff).
Las medidas reales proceden del repositorio de investigación
[nanovna-calibration](https://github.com/telmomm/nanovna-calibration)
([doi:10.5281/zenodo.22722703](https://doi.org/10.5281/zenodo.22722703)).
