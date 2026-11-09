# Health, Retirement, and the Fiscal Returns to Social Security Reform

Abdoulaye Ndiaye (NYU) and Zhixiu Yu (LSU). Companion paper to "Flexible Retirement and Optimal Taxation" (FROT).
Spun off from the May 2025 QJE submission of FROT (its Sections 5, 7, 8 and the MVPF tables), rebuilt as a standalone
quantitative life-cycle paper for the Review of Economic Studies.

## Build

    latexmk -pdf main.tex          # pdflatex + bibtex (aer.bst, natbib round)

Compiles with TeX Live 2023 (pdflatex). No custom .sty files are needed: `preamble.tex` loads standard packages only.
The bibliography is `references.bib` (the FROT bibliography, repaired, plus web-verified additions).

## Layout

    main.tex                 master file
    preamble.tex             FROT house style (12pt article, 1.5 spacing, pgfplots, natbib)
    references.bib           bibliography
    sections/                00 front matter, 01 intro ... 12 conclusion, macros.tex
    appendix/                A data, B estimation and fit, C reforms, D derivations
    tables/                  table sources (*.tex) used by the paper; *_paper.tex are edited copies; see tables/EDITS.md
    figures/abdou/           pgfplots figure sources with embedded data (from the FROT project); *_paper.tex edited copies; see figures/EDITS.md
    figures/new/             new pgfplots figures built from printed table cells (header comments list every cell)
    AUTHOR_NOTES.md          vintages, open questions, and every %TODO-AUTHORS comment (authors' decisions)
    BUILD_REPORT.md          last build report

## Overleaf

This folder lives inside the FROT Overleaf project (synced through Dropbox). Two ways to compile it:

1. (Recommended) Create a new Overleaf project and upload this folder's contents, with `main.tex` as the main document.
2. Inside the FROT project, set `main.tex` of this folder as the main document. Overleaf resolves `\input` paths
   relative to the project root, so add this folder's name to the input path in `preamble.tex`
   (the `\input@path` line) and to `\graphicspath`, or compile locally from this folder.

## Provenance

Every number in the text carries a `% src:` comment naming the table/figure file or source line it comes from.
Results tables are the May 2025 FROT files; the estimated-parameter table and the fit figures are the 2026 (v6)
recomputed versions; see AUTHOR_NOTES.md.
