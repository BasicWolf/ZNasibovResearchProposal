SRCS := $(wildcard *.tex) bibliography.bib
MAIN_SRC = znasibov_research_proposal.tex
TARGET = znasibov_research_proposal.pdf

all: ${TARGET}

${TARGET}: ${SRCS}
	latexmk -pdf -pdflatex="pdflatex -interactive=nonstopmode" -use-make ${TARGET}

.PHONY: all 
