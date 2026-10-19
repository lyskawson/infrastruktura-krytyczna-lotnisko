PYTHON ?= python3

.PHONY: pdf check figures overleaf clean

pdf: check
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	mkdir -p output/pdf
	cp build/main.pdf output/pdf/lotnisko-polnoc.pdf

check:
	$(PYTHON) tools/validate_design.py

figures:
	$(PYTHON) tools/generate_figures.py
	$(PYTHON) tools/validate_design.py

overleaf:
	$(PYTHON) tools/bundle_overleaf.py

clean:
	latexmk -C -outdir=build main.tex
