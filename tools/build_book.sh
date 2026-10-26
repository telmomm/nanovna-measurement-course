#!/usr/bin/env bash
# Build both editions of the book and assemble the website in _site/:
#
#   _site/                         English edition (HTML)
#   _site/es/                      Spanish edition (HTML)
#   _site/pdf/hands-on-vna-en.pdf  English edition (PDF)
#   _site/pdf/hands-on-vna-es.pdf  Spanish edition (PDF)
#
# Usage: tools/build_book.sh [--html-only] [en|es]...
# With no language, both are built. The PDF needs XeLaTeX, latexmk and the
# IBM Plex fonts (TeX Live package "plex"). Run from the repository root.
set -euo pipefail

# Stop at the first LaTeX error instead of waiting for input.
export LATEXOPTS="${LATEXOPTS:--interaction=nonstopmode -halt-on-error}"

html_only=false
langs=()
for arg in "$@"; do
  case "$arg" in
    --html-only) html_only=true ;;
    en|es) langs+=("$arg") ;;
    *) echo "unknown argument: $arg" >&2; exit 2 ;;
  esac
done
[ ${#langs[@]} -eq 0 ] && langs=(en es)

for lang in "${langs[@]}"; do
  echo "==> HTML ($lang)"
  jupyter-book build . --config "book/$lang/_config.yml" --toc "book/$lang/_toc.yml" \
    --path-output "book/$lang" -W
  if [ "$html_only" = false ]; then
    echo "==> PDF ($lang)"
    jupyter-book build . --config "book/$lang/_config.yml" --toc "book/$lang/_toc.yml" \
      --path-output "book/$lang" --builder pdflatex
  fi
done

echo "==> assembling _site"
rm -rf _site
mkdir -p _site/pdf
[ -d book/en/_build/html ] && cp -R book/en/_build/html/. _site/
[ -d book/es/_build/html ] && mkdir -p _site/es && cp -R book/es/_build/html/. _site/es/
for lang in en es; do
  pdf="book/$lang/_build/latex/hands-on-vna-$lang.pdf"
  [ -f "$pdf" ] && cp "$pdf" _site/pdf/
done
touch _site/.nojekyll
echo "Site in _site/"
