# Ejecutar las lecciones

## En el navegador

Abre cualquier lección y usa el icono del cohete de la parte superior de la
página:

- **Binder** arranca un entorno temporal con todo instalado. El primer
  arranque puede tardar unos minutos. El trabajo se pierde al cerrar la
  pestaña salvo que descargues el cuaderno.
- **Colab** abre el cuaderno en Google Colab (necesitas una cuenta de Google).
  La primera celda de código de cada lección instala el paquete del curso.
  Puedes guardar tu trabajo en tu Drive.

## En tu ordenador

Necesitas Python 3.10 o posterior.

Con conda (o mamba):

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

conda env create -f environment.yml
conda activate nanovna-measurement-course
python -m pip install --no-deps -e .
jupyter lab es/notebooks
```

Con pip y un entorno virtual:

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
python -m pip install -e ".[notebooks]"
jupyter lab es/notebooks
```

Para comprobar la instalación, ejecuta las primeras celdas de código de la
lección 00: muestran las versiones de las bibliotecas que usa el módulo.

## Qué se instala

| Paquete | Para qué se usa |
|---|---|
| NumPy, Matplotlib | cálculo y gráficas, en todas las lecciones |
| [scikit-rf](https://scikit-rf.org) | lectura de ficheros Touchstone, la retícula de la carta de Smith y como implementación de referencia de la calibración |
| [rfmeasurement](https://github.com/telmomm/rfmeasurement) | reglas de validación e informes, solo en la lección 05 (sus mensajes están en inglés) |
| `vnacourse` | el pequeño paquete auxiliar de este módulo: carga de datos, estilo de las gráficas y las funciones que escribes en las lecciones 02 y 03 |

## Construir este libro

```bash
python -m pip install -e ".[book]"
tools/build_book.sh            # las dos ediciones, HTML y PDF
tools/build_book.sh --html-only es
```

El script construye cada edición con Jupyter Book y monta el sitio web en
`_site/`: la edición inglesa en la raíz, la española en `_site/es/` y los PDF
en `_site/pdf/`. La construcción ejecuta todos los cuadernos, así que tarda
unos minutos. El PDF necesita XeLaTeX (TeX Live con las fuentes `plex`) y
`rsvg-convert`.

Para construir una edición a mano:

```bash
jupyter-book build . --config book/es/_config.yml --toc book/es/_toc.yml --path-output book/es
```
