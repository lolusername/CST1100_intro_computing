# Logic Gates Module: Full Curriculum

## Overview
- Purpose: give students a practical grasp of digital logic as the foundation for computing hardware and software decisions.
- Length: 3 sessions (90 minutes each) with optional extension lab time.
- Format: mini-lectures, whiteboard/tablet demos, guided practice, and a short reflection assignment.

## Learning Outcomes
- Describe how binary signals flow through NOT, AND, OR, NAND, NOR, XOR, and XNOR gates.
- Build and read truth tables for single gates and small compositions (e.g., half/full adders).
- Draw or interpret simple gate diagrams that map inputs to outputs.
- Connect real-world computing scenarios (authentication, alerts, arithmetic) back to gate logic.
- Debug logical errors by comparing expected truth tables to observed behavior.

## Prerequisites and Materials
- Students: basic binary familiarity (0/1 meaning) and boolean operators.
- Instructor: projector + whiteboard/tablet; optional breadboard/LED demo if available.
- Files: `logic_gates_module/Logic_Gates_Deep_Dive.pptx` slide deck; `logic_gates_module/Reflection_Assignment.md` prompt.

## Session Plan (3 x 90 minutes)
### Session 1 – Digital Signals and Core Gates
- **Topics**: analog vs digital, voltage as 0/1, NOT/AND/OR truth tables, gate symbols.
- **Flow (minutes)**: 0–10 warm-up (binary recap); 10–35 mini-lecture with deck slides 2–6; 35–55 board/tablet truth table building; 55–75 partner practice sketching gates; 75–90 recap + exit ticket.
- **Activities**: predict gate outputs before revealing; use simple two-switch light demo for AND/OR.
- **Checks**: 3-question quick poll on NOT/AND/OR outputs.

### Session 2 – Derived Gates and Compositions
- **Topics**: NAND/NOR (universality), XOR/XNOR, multi-input gates, combining gates into adders.
- **Flow**: 0–15 review quiz; 15–40 mini-lecture slides 7–11; 40–70 guided build of half-adder then full-adder truth tables; 70–85 practice drawing compositions; 85–90 wrap.
- **Activities**: have students implement XOR with only NAND on paper; relate carry/ sum bits to arithmetic.
- **Checks**: table-completion worksheet; peer check of adder diagrams.

### Session 3 – Real-World Applications and Software Tie-Ins
- **Topics**: gate logic inside CPUs (instruction decode), input validation, feature flags, bitwise operators.
- **Flow**: 0–15 review; 15–45 application demos (slides 12–15); 45–70 small-group case studies mapping scenarios to gates; 70–85 reflection assignment launch; 85–90 exit poll.
- **Activities**: students diagram a two-factor login gate, an alarm OR chain, and a rate limiter AND/NOT combo.
- **Checks**: group share-out of diagrams; quick bitwise exercise (`mask = 0b1010` examples).

## Assessments and Deliverables
- In-class: exit tickets after Sessions 1 and 3; worksheet from Session 2.
- Reflection: submit `logic_gates_module/Reflection_Assignment.md` prompts (350–500 words) due next class.
- Optional extension: code a truth-table generator (Python/JS) and compare against manual tables.

## Differentiation and Accessibility
- Provide printed truth table templates; narrate diagrams verbally.
- Allow pairs to check each other’s tables before turning in.
- Offer alternate contexts (hardware or software-heavy) so students can connect to prior knowledge.

## Instructor Preparation
- Rehearse slide speaker notes (embedded in deck) to stay within timeboxes.
- If using hardware demos, pre-test power, LED polarity, and resistor values.
- Keep a high-contrast marker palette for board work; photograph tables for students who need copies.
