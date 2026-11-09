# Retirement Reforms That Pay for Themselves — Ndiaye and Yu

Companion paper to "Flexible Retirement and Optimal Taxation" (FROT). It contains the estimated life-cycle retirement economy (French–Jones nonseparable preferences, health/disability/mortality risk, US institutions), its data, targets, estimation and match of moments, and the welfare and MVPF analysis of 66 retirement reforms. All of this was taken out of FROT after the 2025 QJE round.

## Build
- Main file: `main.tex`. Compile with `latexmk -pdf main.tex` (pdflatex and BibTeX, style `aer`).
- In Overleaf (FROT project), choose Menu → Main document → `MVPF_paper/main.tex`. The preamble sets `\input@path`, so paths resolve whether the compiler runs from `MVPF_paper/` or from the project root. If BibTeX cannot find `references.bib` from the project root, compile this folder as its own Overleaf project.
- Structure:
  - `sections/`: 0 abstract, 1–8 main text, A–F appendices.
  - `tables/`: `*_body.tex` files are generated, do not edit by hand.
  - `figures/`: TikZ/pgfplots.
  - `references.bib`: FROT's `JMPreferences.bib` plus 24 added entries, each verified against publisher, RePEc, or SSA records. Non-ASCII characters were converted to LaTeX, and broken entries were repaired in this copy only.
- `tools/`: `gen_tables.py` regenerates `tables/tab_*_body.tex` from the original FROT tables (`../tables/welfare_*`); `gen_figs.py` regenerates `figures/mvpf_map.tex` and `figures/schedules_*.tex`. Run both from this folder. Note: `figures/mvpf_map.tex` was hand-tuned after generation (label and legend placement only), so re-running `gen_figs.py` overwrites those tweaks.

## Provenance of numbers
- Every reform number comes from the FROT 2025 tables:
  - `welfare_age_dependence_mvpfv5`
  - `welfare_progressivity_mvpfv7`
  - `welfare_medicare_mvpfv8`
  - `welfare_tax_mvpf_v8`
  - `welfare_savings_mvpf_v3`
  - `welfare_decomposition_gradient`
  - `DRC_visualization_4`
- The tables were parsed by script, and every cell was checked again against the source.
- Fit figures are the corrected (`*_c`) versions used in FROT v6. First-step figures, the parameter table, and the data tables are FROT originals.
- Derived quantities appear in the text only where marked `% Derived` in the source. Examples: the MVPF×Net/WTP factor, the ratio between the two consumption bases, and δ* at 65.
- LaTeX comments starting with `% AUTHORS` mark items the code must confirm.

## Before submission (author to-do; items need the code or simulation output)
1. **Rerun the reforms on the corrected code.** The reform and instrument-elimination results are from the May 2025 simulation. The fit figures are the 2026 corrected re-simulation, at the same parameter estimates.
2. **Why Social Security outlays fall under the DRC reforms (AD).** At the plotted first-step mortality, with r = 3.2% and T = 85, the actuarially fair credit at 65 is about 7.6% (7.3/7.5/8.8% by health). By Lemma 1, delays at credits of 8–10% would then raise outlays, yet the Direct column falls by 2.46–5.05%. Things to check:
   - (a) whether the claiming-age adjustment and the earnings-test crediting run through `aime_t` (French–Jones style), and whether the AIME cap binds;
   - (b) the survival probabilities actually used: the plotted mortality looks low next to SSA cohort life tables;
   - (c) which channel produces the saving.

   The text currently says only that the tables do not separate the channels.
3. **Consumption base of the dollar conversion.** WTP is a uniform change in consumption at every age. It is converted with consumption from 62 for reforms that start at 62, and with lifetime consumption for savings subsidies. Consider recomputing all MVPFs on the lifetime base, which the stored aggregates C̄⁰₃₀ and C̄⁰₆₂ allow. The tables imply a factor of about 5 between the two bases.
4. **Fiscal-column denominators.** Confirm them against the code, then report the baseline aggregates: SS, DI, transfers, income tax, payroll tax, G⁰, and the consumption bases. The inferred formulas sit in `% AUTHORS` comments (Section 4.3, Appendix D).
5. **Model details to confirm:**
   - how the claiming age is tracked in the state vector;
   - present values summed from age 30 and compounded to 62;
   - Medicare outlays excluded from G except in the Medicare reforms;
   - DI paid until the reformed NRA;
   - the income-tax reform formula λ_t + x(t−61) (the 2025 text said "after-tax income +x%");
   - Medicare expansion of "+20 percentage points" versus "by 20%";
   - the units and coding of the survival logit.
6. **Report N_s and common random numbers.** State the number of simulated individuals and whether common random numbers are used across reforms. Small non-monotonicities (L8 vs L9) are attributed in the text to simulation error.
7. **Simulated claiming-age distribution.** Tabulate it (status quo, AN2, AD1, AD5, AL4, AL9), and by health, against SSA award shares.
8. **Small fact checks:**
   - the price year of the $3,500 consumption floor, now attributed to French and Jones (2004);
   - the earnings-test exempt amount, $8,186 versus SSA's $8,160;
   - the PSID 70+ health shares, which sum to 99.0;
   - how the 57% income-tax share of P1.1's indirect effect was computed.
9. **Fixes made only in this paper's copies, not at the FROT source:**
   - The y-axis label of `figures/abdou/frot_wageselection_n800_edit.tex` reads "Hourly Wages in \$1,000"; the values are dollars per hour.
   - FROT's `JMPreferences.bib` has a stray `%@techreport{Grochulski2016` line and a missing brace.
