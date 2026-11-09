# figures/EDITS.md -- edits to copies of figure files (Override O6). Originals in figures/abdou/ are untouched.

## W3b (Appendix C, figures fig:elimlfp and fig:elimlfp_health)
- `abdou/frot_weld1_paper.tex`, `abdou/frot_weld1_0_paper.tex`, `abdou/frot_weld1_1_paper.tex`: copies of `frot_weld1.tex`, `frot_weld1_0.tex`, `frot_weld1_1.tex` with two label edits and no data edits:
  (i) legend entry `(D2) Full Medicare Ins.` -> `(D2) Full coverage after 65` (BLUEPRINT 7, C.4; dossier 03 section 7.2);
  (ii) `ylabel={}` -> `ylabel={Participation rate (\%)}` (left-hand panels only; the right-hand panels `frot_weld2*.tex` are input unchanged).
- `abdou/frot_weld1_2_paper.tex`: copy of `frot_weld1_2.tex` with edit (ii) and the same relabel applied to a commented-out legend line (its active legend already reads `(D2)`).
- Not used anywhere: `frot_weld*_ssb*.tex`, `frot_weld*_slides.tex`, `hlfprs*`, `ulfprs*`, `lfprs`, `*_reform_policy` (dossier 03 section 7.3).

## W1b (Section 4, Figure fig:firststep; Appendix B, Figure fig:fitlnc)
- `abdou/frot_wageselection_n800_edit_paper.tex`: copy of `frot_wageselection_n800_edit.tex` with one label edit and no data edits: line 14 `ylabel={Hourly Wages in \$1,000}` -> `ylabel={Dollars per hour}` (the plotted values are dollars per hour; dossier 02 Flag F8; BLUEPRINT 2.4). Input as panel (D) of `fig:firststep`.
- `abdou/h800_lnc_meana_paper.tex`: copy of `h800_lnc_meana.tex` with the duplicate first `ylabel={Short label\phantom{(extra)}},` line (line 7 of the original) deleted; the remaining `ylabel={Assets $\times10^5$}` is unchanged, as are all data (dossier 02 §10 figure-file quirk; BLUEPRINT 7, B.4). Input as panel (C) of `fig:fitlnc`.
- Input unchanged: `frot_disab0_edit.tex`, `frot_mortal7_edit2.tex`, `frot_oopmedical_2016_edit.tex` (Figure 1); `h800_l0_edit_c.tex`, `h800_l1_edit_c.tex`, `h800_h0_edit_c.tex`, `h800_h1_edit_c.tex` (Figure 2); `h800_meana_edit_c.tex`, `h800_mediana_edit_c.tex`, `h800_reentry_edit.tex` (Figure B1); `h800_l0_lnc_edit.tex`, `h800_l1_lnc_edit.tex`, `h800_lnc_mediana.tex` (Figure B2); `frot_target_l2.tex`, `frot_target_h.tex`, `frot_target_a.tex`, `frot_target_r.tex` (Figure A1). Not used: `frot_target_l.tex` (mislabeled), `frot_mortal7_edit.tex` (superseded), `figures/excel/wage.tex` (no data).

## Fixer, model group (audit round; Appendix A Figure fig:targets, Appendix B Figures fig:fitassets and fig:fitlnc)
- `abdou/frot_target_a_paper.tex`: copy of `frot_target_a.tex` with one label edit and no data edits: line 14 `ylabel={Assets $\times10^5$}` -> `ylabel={Assets (\$100{,}000s)}` (same label as `h800_meana_edit_c.tex`; layout audit 14). Input as panel (C) of `fig:targets`.
- `abdou/h800_lnc_mediana_paper.tex`: copy of `h800_lnc_mediana.tex` with the same ylabel edit (line 14) and no data edits. Input as panel (D) of `fig:fitlnc`.
- `abdou/h800_lnc_meana_paper.tex`: the same ylabel edit applied to the existing copy (line 16); no data edits.
- `abdou/frot_target_r_paper.tex` and `abdou/h800_reentry_edit_paper.tex`: copies of `frot_target_r.tex` and `h800_reentry_edit.tex` with axis edits and no data edits: `ymin=-5, ymax=100` -> `ymin=0, ymax=10` (the plotted series lie between 0.39 and 5.51; layout audit 15) and the legend moved from `(axis cs:32,50)`, anchor south west, to `(axis cs:31,9.7)`, anchor north west, so that it stays inside the new axis. Input as panel (D) of `fig:targets` and panel (C) of `fig:fitassets`.
- Originals `frot_target_a.tex`, `frot_target_r.tex`, `h800_reentry_edit.tex`, `h800_lnc_mediana.tex` are untouched and no longer input anywhere.
