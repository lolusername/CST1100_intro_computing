Title: CST1100 Week 10 Cross-Language OOP Design
Audience: Intro to Computing students
Duration: 90 minutes (single session)
Instructor: ____________________
Date: ____________________

## Learning Goals
- Describe the four-stage OOP design process (brainstorming, filtering, scenarios, responsibility algorithms) and why it precedes coding.
- Compare how Python and JavaScript express classes, constructors, and method binding.
- Practice translating a class blueprint between Python and JavaScript while respecting encapsulation and state management.
- Evaluate when to favor objects over procedural functions for organizing code that models real-world entities.

## Materials
- `week_10/OOP_reading.pdf` plus slide deck summary (`week_10/oop_cross_language_comparison.pptx`)
- Live-coding Jupyter notebook (`week_10/oop_language_comparison.ipynb`)
- Whiteboard or collaborative doc for CRC card sketches
- Optional: printed cheat sheet highlighting Python vs. JavaScript class syntax
- Sticky notes or polling tool for exit reflections

## Session Agenda

| Time | Segment | Objectives & Facilitation Moves |
| --- | --- | --- |
| 0:00–0:08 | Warm-Up: Spot the Objects | Show a daily-life scenario (shared slide). Students list nouns (candidate classes) vs. verbs (methods). Surface prior knowledge about encapsulation. |
| 0:08–0:20 | Mini-Lecture: OOP Design Stages | Walk through brainstorming → filtering → scenarios → responsibility algorithms using the coffee shop example from the reading. Capture responsibilities on a CRC template. |
| 0:20–0:35 | Guided CRC Jam | Teams build a CRC card for a “Campus Study Group” object. Prompt: “What collaborations are required?” Circulate and coach on filtering redundant classes. |
| 0:35–0:50 | Python Live Coding | Translate the CRC card into a Python class (slides + notebook cell). Highlight constructor defaults, instance attributes, and method docstrings. Students run and tweak behavior. |
| 0:50–1:05 | JavaScript Translation | Mirror the same design in JavaScript (ES6 class). Emphasize `constructor`, method binding, and how `this` differs from Python’s `self`. Compare output, note language-specific idioms. |
| 1:05–1:18 | Pair Practice: Cross-Language Remix | Assign a new blueprint (e.g., “Habit Tracker”). Pairs author one method in Python, then refactor to JavaScript. Encourage using notebook guidance cells. |
| 1:18–1:25 | Reflection & Debrief | Discuss where OOP added clarity vs. overhead. Ask: “Which stage of the design cycle felt most valuable?” Collect one sticky: Python-only, JS-only, or both for future projects. |
| 1:25–1:30 | Exit Ticket | Quick poll: identify class component definitions and match design stages to their purpose. |

## Differentiation Strategies
- Provide partially completed CRC cards for students who need scaffolding; challenge advanced students to layer inheritance or mixins.
- Encourage language choice flexibility during practice: allow confident JavaScript students to lead JS translation while peers narrate Python logic.
- Offer syntax reference strips (Python vs. JS) and highlight debugging aids (e.g., `console.log`, `print`) for students needing extra support.
- Invite advanced learners to prototype a factory function alternative and justify trade-offs.

## Formative Assessment
- Listen to warm-up brainstorms to diagnose misconceptions about classes vs. instances.
- Use quick cold-calls during live coding to check understanding of constructor parameters and `self`/`this`.
- Collect pair-programming artifacts (code snippets or annotated CRC cards) for immediate feedback.
- Exit tickets inform whether to reteach design stages or re-emphasize language-specific syntax.

## Homework / Extension
- Reading response: summarize one insight from `OOP_reading.pdf` and apply it to a personal project idea.
- Coding prompt: implement the Habit Tracker class in both Python and JavaScript, including a method that returns aggregated stats.
- Optional: explore how JavaScript prototypes relate to `class` sugar by rewriting one method using `ClassName.prototype`.

## Instructor Reflection Notes
- Track which design stage students rush through; plan a follow-up mini-lesson if scenarios/responsibility algorithms feel weak.
- Note language preference trends to adapt future cross-language comparisons.
- Record effective student analogies that bridge Python and JavaScript for reuse in future cohorts.
