SRCS := $(wildcard *.tex)
MAIN_SRC = znasibov_research_proposal.tex
TARGET = znasibov_research_proposal.pdf

all: ${TARGET}

${TARGET}: ${SRCS}
	pdflatex -interaction=nonstopmode ${MAIN_SRC}

.PHONY: all 
