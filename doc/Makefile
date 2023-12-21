# Minimal makefile for Sphinx documentation
#
SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = source
BUILDDIR = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" "$(SPHINXOPTS)" $(0)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" "$(SPHINXOPTS)" $(0)

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf source/images/auto-generated

