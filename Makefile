# Makefile — root of repo
TEX      := lualatex
BUILD    := build

MASTER_TEX := whitebook.tex
OUTPDF     := whitebook.pdf

VOL2_TEX := Volume_II_Onu_Calculus.tex
VOL2_PDF := $(BUILD)/Volume_II_Onu_Calculus.pdf

.PHONY: all clean xelatex

all: $(VOL2_PDF) $(OUTPDF)

$(BUILD):
	@mkdir -p $(BUILD)

$(VOL2_PDF): $(VOL2_TEX) | $(BUILD)
	$(TEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(VOL2_TEX)
	# run twice if your Volume II creates a ToC
	$(TEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(VOL2_TEX) || true

$(OUTPDF): $(MASTER_TEX) $(VOL2_PDF)
	$(TEX) -interaction=nonstopmode -halt-on-error $(MASTER_TEX)
	$(TEX) -interaction=nonstopmode -halt-on-error $(MASTER_TEX) # ToC pass

xelatex:
	$(MAKE) TEX=xelatex

clean:
	rm -rf $(BUILD) *.aux *.log *.out *.toc *.pdf *.lof *.lot *.bbl *.blg *.run.xml *.bcf
