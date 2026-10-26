"""The Spanish edition in es/ mirrors the English one cell by cell."""

import io
import json
import tokenize
from pathlib import Path

import matplotlib
import pytest

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

from vnacourse import plotting  # noqa: E402

REPO = Path(__file__).resolve().parents[1]
ENGLISH = sorted(
    path.relative_to(REPO)
    for folder in ("notebooks", "exercises/solutions")
    for path in (REPO / folder).glob("*.ipynb")
)
DOCUMENTS = ("instructor/guia_docente.md", "instructor/rubrica.md", "data/README.md")


def cells(path):
    return json.loads(path.read_text())["cells"]


@pytest.mark.parametrize("notebook", ENGLISH, ids=str)
def test_spanish_notebook_has_the_same_cells(notebook):
    english, spanish = cells(REPO / notebook), cells(REPO / "es" / notebook)
    assert [c["cell_type"] for c in spanish] == [c["cell_type"] for c in english]
    assert [c.get("id") for c in spanish] == [c.get("id") for c in english]


def code_tokens(source):
    """The tokens of a code cell, without comments, strings and layout."""
    # IPython magics such as "%pip install ..." are not Python: leave them out.
    lines = [line for line in source.splitlines() if not line.lstrip().startswith("%")]
    skip = {tokenize.COMMENT, tokenize.STRING, tokenize.NL, tokenize.NEWLINE}
    skip |= {tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}
    # Python 3.12+ splits f-strings into several tokens; a translated f-string may be
    # split in two to keep lines short.
    for name in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):
        skip.add(getattr(tokenize, name, tokenize.STRING))
    tokens = tokenize.generate_tokens(io.StringIO("\n".join(lines) + "\n").readline)
    kept = [token.string for token in tokens if token.type not in skip]
    # A trailing comma before a closing bracket is layout too.
    closing = (")", "]", "}")
    return [
        t for i, t in enumerate(kept) if not (t == "," and "".join(kept[i + 1 : i + 2]) in closing)
    ]


@pytest.mark.parametrize("notebook", ENGLISH, ids=str)
def test_spanish_notebook_runs_the_same_code(notebook):
    """Only comments, docstrings, labels and messages are translated."""
    english, spanish = cells(REPO / notebook), cells(REPO / "es" / notebook)
    for en, es in zip(english, spanish, strict=True):
        if en["cell_type"] == "code":
            assert code_tokens("".join(es["source"])) == code_tokens("".join(en["source"]))


@pytest.mark.parametrize("document", DOCUMENTS)
def test_spanish_document_exists(document):
    assert (REPO / "es" / document).is_file()


@pytest.mark.parametrize("lang", ["en", "es"])
def test_error_adapter_draws_in_both_languages(lang):
    fig, ax = plt.subplots()
    plotting.draw_error_adapter(ax, lang=lang)
    texts = " ".join(text.get_text() for text in ax.texts)
    assert ("directivity" if lang == "en" else "directividad") in texts
    plt.close(fig)
