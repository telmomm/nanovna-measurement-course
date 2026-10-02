# Running the lessons

## In the browser

Open any lesson and use the rocket icon at the top of the page:

- **Binder** starts a temporary environment with everything installed. The
  first launch can take a few minutes. Work is lost when you close the tab
  unless you download the notebook.
- **Colab** opens the notebook in Google Colab (you need a Google account).
  The first code cell of each lesson installs the course package. You can
  save your work to your Drive.

## On your computer

You need Python 3.10 or newer.

With conda (or mamba):

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

conda env create -f environment.yml
conda activate nanovna-measurement-course
python -m pip install --no-deps -e .
jupyter lab notebooks
```

With pip and a virtual environment:

```bash
git clone https://github.com/telmomm/nanovna-measurement-course.git
cd nanovna-measurement-course

python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
python -m pip install -e ".[notebooks]"
jupyter lab notebooks
```

To check the installation, run the first code cells of lesson 00: they print
the versions of the libraries the module uses.

## What is installed

| Package | Used for |
|---|---|
| NumPy, Matplotlib | computing and plotting, in every lesson |
| [scikit-rf](https://scikit-rf.org) | reading Touchstone files, the Smith chart grid, and as a reference implementation of the calibration |
| [rfmeasurement](https://github.com/telmomm/rfmeasurement) | validation rules and reports, in lesson 05 only |
| `vnacourse` | the small helper package of this module: data loading, plot style, and the functions you write in lessons 02 and 03 |

## Building this book

```bash
python -m pip install -e ".[book]"
jupyter-book build . --config book/_config.yml --toc book/_toc.yml --path-output book
```

The site is written to `book/_build/html/`. Building executes every notebook,
so it takes a minute or two.
