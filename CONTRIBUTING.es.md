# Cómo contribuir a nanovna-measurement-course

[English](CONTRIBUTING.md) · **Español**

Gracias por plantearte contribuir. Esto es material docente, así que las
contribuciones más valiosas son las que ayudan a un estudiante a entender
algo: una explicación más clara, un ejercicio mejor, una ecuación corregida o
un informe de cómo funcionó el módulo en tu aula.

## Formas de contribuir

- **Informar de un problema.** Una errata, una ecuación equivocada, un
  cuaderno que no se ejecuta, un paso que te confundió a ti o a tu alumnado.
  Abre una incidencia e indica de qué cuaderno y celda se trata (y en qué
  idioma).
- **Compartir tu experiencia en el aula.** Si usaste el módulo en una
  asignatura, abre una incidencia
  [«Classroom experience»](https://github.com/telmomm/nanovna-measurement-course/issues/new?template=classroom_report.yml)
  describiendo el contexto (asignatura, número de estudiantes, tiempo
  necesario) y qué funcionó y qué no. Puedes escribirla en español. Estos
  comentarios dan forma a la siguiente versión y son los que convierten los
  tiempos estimados de la [guía docente](es/instructor/guia_docente.md) en
  medidas.
- **Mejorar o añadir contenido.** Explicaciones, figuras, ejercicios,
  soluciones, traducciones. Para cualquier cosa mayor que una corrección
  pequeña, abre antes una incidencia para que el cambio pueda discutirse antes
  de que inviertas tiempo en él.

## Para empezar

Usa un entorno virtual en lugar de instalar en el Python del sistema. Nunca
se sube al repositorio (ya está en `.gitignore`) y puede borrarse y recrearse
en cualquier momento.

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

python -m pip install -e ".[dev,notebooks]"
```

Después ejecuta lo mismo que la integración continua:

```bash
ruff check .
ruff format --check .
pytest
pytest --nbmake notebooks exercises es --ignore=notebooks/04_adquisicion_nanovna.ipynb
```

`pytest` ejecuta los tests del paquete, los que recalculan todas las cifras
que cita el texto (`tests/test_reference_values.py`) y los que mantienen
sincronizadas las dos ediciones (`tests/test_translations.py`). La última
orden ejecuta de principio a fin todas las lecciones y soluciones, en los dos
idiomas, y falla si alguna celda da error. El cuaderno 04 se omite porque
necesita un NanoVNA físico. `ruff format .` corrige el formato, también el de
las celdas de código de los cuadernos.

## Construir el libro

El sitio web es un [Jupyter Book](https://jupyterbook.org) (versión 1)
construido a partir de los cuadernos y ficheros Markdown allí donde están. Hay
un libro por idioma: `book/en/` y `book/es/` contienen cada configuración,
índice y páginas propias; `book/_static/` y `book/latex/` contienen los
estilos web y PDF que comparten ambos.

```bash
python -m pip install -e ".[book]"
tools/build_book.sh                  # las dos ediciones, HTML y PDF, en _site/
tools/build_book.sh --html-only es   # una edición, solo web
```

La construcción ejecuta todos los cuadernos, y la de HTML usa `-W`, así que un
aviso (por ejemplo, un enlace roto) la hace fallar, como en la integración
continua. Un cuaderno o página nuevos deben añadirse al `_toc.yml` de las dos
ediciones para aparecer. El PDF necesita XeLaTeX con las fuentes IBM Plex (el
paquete `plex` de TeX Live) y `rsvg-convert`.

## Dos idiomas

La edición inglesa está en la raíz del repositorio y la española en `es/`, con
los mismos nombres de fichero. Todo cambio en una lección, una solución o el
material docente debe hacerse en las dos:

- **Mismas celdas, mismo código.** Un cuaderno en español tiene las mismas
  celdas, en el mismo orden y con los mismos identificadores, que su gemelo en
  inglés. Su código es el mismo salvo comentarios, cadenas de documentación,
  etiquetas de las figuras y mensajes impresos. `tests/test_translations.py`
  comprueba ambas cosas.
- **Números.** Las dos ediciones usan el punto decimal, como Python. Si
  cambias una cifra citada en el texto, actualiza
  `tests/test_reference_values.py`.
- **Si solo puedes escribir en un idioma**, abre igualmente la solicitud de
  cambios y dilo: alguien del equipo añadirá el otro.

## Identidad visual

Los colores, la tipografía y el símbolo se describen en
[`assets/brand/README.es.md`](assets/brand/README.es.md). Las figuras nuevas
deben usar `vnacourse.plotting.use_course_style()` y los colores `SERIES` en
orden.

## Pautas para los cuadernos

- **Todo cuaderno debe ejecutarse sin hardware**, con datos simulados o con
  las medidas registradas en `data/`. El cuaderno 04 es la única excepción.
- **Declara los objetivos de aprendizaje** al principio (tres o cuatro
  puntos) y mantén el contenido centrado en ellos.
- **Sigue la estructura común:** objetivos, teoría breve, código guiado,
  preguntas de comprobación («¿qué esperas ver antes de ejecutar esto?»),
  ejercicios abiertos, resumen y enlace al siguiente cuaderno.
- **El código está al servicio del concepto.** Prefiere unas pocas líneas
  legibles de NumPy a una abstracción ingeniosa; lleva lo reutilizable a
  `src/vnacourse/`.
- **Sube los cuadernos sin salidas** (en JupyterLab: *Edit → Clear Outputs of
  All Cells*). Mantiene los cambios revisables; la integración continua los
  vuelve a ejecutar.
- **Conserva las insignias de Binder y Colab** en la primera celda,
  apuntando al propio cuaderno (`es/notebooks/...` en la edición española).
- **Un ejercicio necesita una solución.** Si añades o cambias un ejercicio,
  actualiza el cuaderno correspondiente en `exercises/solutions/` (y en
  `es/exercises/solutions/`). Un texto que da una cifra debe coincidir con lo
  que imprime el código.

## Antes de abrir una solicitud de cambios

1. Centra el cambio en un único asunto.
2. Ejecuta las órdenes anteriores.
3. Si cambiaste una ecuación o un método, cita la fuente (libro de texto,
   artículo o norma).
4. Actualiza `CHANGELOG.md` cuando el cambio sea visible para estudiantes o
   docentes.

## Licencia de las contribuciones

Al contribuir aceptas que tu código se publique bajo la
[licencia BSD de 3 cláusulas](LICENSE) y tus textos, figuras y datos bajo
[CC BY 4.0](LICENSE-CONTENT).

## Reconocimiento

Quienes contribuyen reciben el reconocimiento adecuado. Cuando una
contribución es sustancial, la autoría o un agradecimiento formal se
discutirán con transparencia con la persona que contribuye.
