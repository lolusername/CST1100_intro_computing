---
title: CST1100 Midterm Review
subtitle: Weeks 1–7 • Binary • Python • SQL
---

# Session Goals

- Explain why computers rely on binary and ASCII encoding.
- Practice reading Python snippets for conversions, control flow, and loops.
- Review logic gates and the CPU instruction cycle.
- Refresh SQL query syntax and string concatenation.

::: notes
Connect goals to midterm expectations. Ask students to note personal focus areas.
:::

# Agenda

- Warm-Up Diagnostic (10 min)
- Data Representation Deep Dive (30 min)
- Logic & CPU Cycle Workshop (15 min)
- Python Practice Circuit (25 min)
- SQL Refresher (10 min)
- Synthesis & Exit Ticket (10 min)

::: notes
Preview the session flow and encourage questions at each transition.
:::

# Warm-Up: Binary Quick Check

- Poll: 1011₂ equals what in decimal?
- Thumbs check: A NOT gate outputs the same value.
- Pair share: Why do computers lean on base-2?

::: notes
Capture misconceptions for targeted reteaching later.
:::

# Data Representation Highlights

- Binary rationale: two stable hardware states (Q1).
- Place-value conversion for `1011₂` → 11 (Q2).
- Bits vs bytes; ASCII code 65 → `A` (Q3–Q5).
- Python helpers: `int(binary, 2)` and `ord()` (Q4 & Q6).

::: notes
Model a conversion live and encourage students to narrate the steps.
:::

# Color Depth & Images

- 8 bits per pixel → 2⁸ = 256 colors (Q7).
- Real-world tie-ins: grayscale photos, emoji palettes.
- Stretch question: What does 24-bit color yield?

::: notes
Ask for estimates before revealing the answer. Relate powers of two to storage.
:::

# Logic & CPU Cycle

- NOT gate flips inputs; AND outputs 1 only when both inputs are 1 (Q8–Q9).
- Collaboratively build a truth table.
- CPU cycle: Fetch → Decode → Execute (Q10).

::: notes
Invite volunteers to act out each stage using a simple recipe metaphor.
:::

# Python Essentials Refresher

- `5 // 2` vs `5 / 2`: floor division vs true division (Q11).
- `len('CityTech')` → 8; `#` starts comments (Q12–Q13).
- `True and not False` evaluates to `True` (Q14).

::: notes
Run each snippet live, soliciting predictions before execution.
:::

# Code Patterns & Logic

- Iterate through files with `for line in f:` (Q15).
- Pseudocode goal: human-readable plan (Q16).
- Repeat N times? Reach for a `for` loop (Q17).

::: notes
Show how `with open(...)` refines the file iteration pattern.
:::

# Loop Output Walkthrough

- `for i in range(3): print(i, end=' ')` outputs `0 1 2` (Q18).
- Off-by-one awareness: start at 0, stop before 3.
- Challenge: How to include 3 or count down?

::: notes
Have students refactor the loop and share solutions.
:::

# SQL Fundamentals

- `SELECT` retrieves columns (Q19).
- PostgreSQL concatenation: `firstname || ' ' || surname` or `concat(...)` (Q20).
- Why `+` fails in PostgreSQL.

::: notes
Demonstrate both concatenation approaches and compare with SQL Server syntax.
:::

# Wrap-Up & Exit Ticket

- Big ideas: binary, Python control flow, SQL verbs.
- Exit ticket prompts:
  - Convert 1101₂ to decimal.
  - Predict `len('binary')`.
  - Write SQL to select full names.
- Capture “muddiest point” feedback.

::: notes
Review responses before dismissing; note trends for follow-up resources.
:::

# Next Steps

- Target weak spots with extra practice.
- Form study pods to review tricky questions.
- Reach out during office hours or LMS forums.

::: notes
Encourage students to commit to one specific action before the midterm.
:::

