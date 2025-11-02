TEX      := lualatex
ROOT     := whitebook
SRC_DIR  := $(ROOT)/src
BUILD    := $(ROOT)/build
MASTER   := $(ROOT)/whitebook.tex
OUTPDF   := whitebook.pdf
VOL2_TEX := $(SRC_DIR)/Volume_II_Onu_Calculus.tex
VOL2_PDF := $(BUILD)/Volume_II_Onu_Calculus.pdf

.PHONY: all clean xelatex

all: $(VOL2_PDF) $(OUTPDF)

$(VOL2_PDF): $(VOL2_TEX)
	@mkdir -p $(BUILD)
	$(TEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(VOL2_TEX)
	$(TEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(VOL2_TEX)

$(OUTPDF): $(MASTER)
	$(TEX) -interaction=nonstopmode -halt-on-error $(MASTER)
	$(TEX) -interaction=nonstopmode -halt-on-error $(MASTER)

xelatex:
	$(MAKE) TEX=xelatex

clean:
	rm -rf $(BUILD) *.aux *.log *.out *.toc *.pdf
