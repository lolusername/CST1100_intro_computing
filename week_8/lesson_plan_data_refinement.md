Title: CST1100 Week 8 Data Refinement Workshop
Audience: Intro to Computing students
Duration: 90 minutes (single session)
Instructor: ____________________
Date: ____________________

## Learning Goals
- Diagnose messy real-world datasets by spotting inconsistent values, missing data, and extreme outliers.
- Practice Python and spreadsheet techniques to impute or flag NULLs, winsorize or cap outliers, and construct categorical bins.
- Reinforce SQL/Python joins and aggregations from Week 7 while layering in data-cleaning safeguards.
- Build compelling visual summaries (histograms, box plots, heatmaps) that highlight the impact of cleaning and transformation choices.

## Materials
- Week 7 quiz review dataset with added quality issues (CSV or spreadsheet)
- Instructor demo notebook or notebook template for students
- Projector with slide deck highlighting cleaning workflow
- Whiteboard or shared doc for group synthesis
- Optional: polling tool or shared workspace (Padlet, Jamboard) for exit reflections

## Session Agenda

| Time | Segment | Objectives & Facilitation Moves |
| --- | --- | --- |
| 0:00–0:10 | Warm-Up & Data Quality Check-In | Quick poll on Week 7 confidence; showcase a messy dataset excerpt. Have students identify at least three data quality issues in pairs. |
| 0:10–0:25 | Mini-Lecture: Cleaning Toolkit | Recap Week 7 SQL/Python review, extend to NULL handling, categorical recoding, and why order matters. Model audit checklist. |
| 0:25–0:45 | Guided Demo: NULLs & Outliers | Live-code strategies to flag NULLs, apply default values vs. imputation, and calculate z-scores/IQR fences to isolate outliers. Contrast spreadsheet formulas with Python code. |
| 0:45–1:05 | Collaborative Lab: Transformation & Binning | Small groups bin a numeric column (equal-width vs. quantile), compare results, and discuss implications for interpretation. Encourage version control of transformations and docstring-style notes. |
| 1:05–1:20 | Visualization Deep Dive | Use cleaned vs. raw data to create histograms, box plots, and grouped bar charts. Facilitate read-aloud of insights; emphasize labeling, scales, and storytelling. |
| 1:20–1:30 | Reflection & Exit Ticket | Students submit a two-sentence summary of a cleaning decision and share one visualization insight. Collect remaining questions for asynchronous follow-up. |

## Differentiation Strategies
- Provide leveled datasets: baseline (few NULLs) and stretch (compound issues with multiple columns).
- Pair confident coders with students who prefer spreadsheets to encourage cross-tool translation.
- Offer checklist templates and transformation logs for students who benefit from guided structure.
- Challenge advanced learners to automate binning or visualize IQR fences dynamically.

## Formative Assessment
- Monitor warm-up annotations to prioritize which cleaning techniques to revisit.
- Circulate during lab to probe reasoning: “Why this bin size?” or “What happens if we drop NULLs instead?”
- Use visualization share-out as a concept check—students must justify styling choices.
- Exit ticket responses inform whether to reteach imputation or visualization selection.

## Homework / Extension
- Assign a short cleaning project: students document one messy dataset, describe three issues, and implement two fixes with code or formulas.
- Optional: have students create a before/after visualization and reflect on how the story changes.
- Encourage exploring pandas `cut()`/`qcut()` or spreadsheet pivot charts for further practice.

## Instructor Reflection Notes
- Track how long students need for each transformation; adjust pacing for future cohorts.
- Note common misconceptions (e.g., deleting vs. imputing NULLs) to inform review materials.
- Record standout student examples to build a Week 9 gallery walk or resource bank.
