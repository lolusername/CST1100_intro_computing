---
title: "Week 4: Hardware Logic + SQL Foundations"
subtitle: "CST1100 – Introduction to Computer Systems"
author: "Instructor"
---

# Agenda

- Why digital logic still matters in modern computing
- Truth tables and core gate behaviors
- From gates to adders: designing combinational circuits
- SQL origin story and relational thinking
- SQL syntax warm-up + lab expectations

# Warm-Up: Binary Refresh

- Recall: bits, voltage thresholds, binary digits (0/1)
- Encoding numbers and characters sets the stage for gates
- Quick check-in: convert 13 to binary and hex

# Digital Logic Basics

- Logic levels mapped to binary states (0 V vs. 5 V)
- Physical implementations: transistors enabling gates
- Deterministic outputs let us chain components safely

# Core Gates & Symbols

- NOT (inverter), AND, OR – building blocks
- Derived gates: NAND, NOR, XOR, XNOR
- Each gate described by truth table and circuit symbol diagram

# Truth Tables

- Enumerate all input combinations to verify behavior
- Example: XOR outputs 1 only when inputs differ
- Use tables to reason about larger circuits systematically

# Circuit Composition

- Wiring outputs to inputs forms combinational logic
- Propagation delay and fan-out considerations
- Software simulations mirror hardware wiring

# Lab Part 1: Python Gate Simulator

- Define gate functions that accept boolean/int inputs
- Generate truth tables programmatically for quick validation
- Build half-adder and full-adder from primitive gates
- Stretch goal: ripple-carry adder using function composition

# Bridging to Data Layers

- Hardware enables instruction execution and data storage
- Operating systems and databases depend on reliable logic
- Transition to abstracting data with relational models

# SQL Origins

- Early 1970s: IBM System R, Edgar F. Codd and relational theory
- SQL standardized by ANSI in 1986; vendors adopt dialects
- Designed to query data declaratively, not procedurally

# Why SQL Still Matters

- Portable knowledge across database systems
- Foundation for analytics, app backends, and Supabase labs
- Complements Python data pipelines you build in lab

# SQL Syntax Tour

- `CREATE TABLE` defines schema (columns + types)
- `INSERT` adds rows; `SELECT` retrieves filtered data
- Clauses: `WHERE`, `ORDER BY`, `LIMIT`
- Preview of joins to connect related tables next weeks

# Lab Part 2: SQLite Sandbox

- Use Colab/Notebook `sqlite3` module, no install required
- Create `components` table, insert sample hardware items
- Practice `SELECT` queries: filter by type, sort by price
- Reflect on how SQL describes data relationships

# Team Extension Ideas

- Log generated truth tables to CSV, load into Supabase
- Visualize adder outputs with matplotlib for debugging
- Document findings in lab README for portfolio credit

# Exit Ticket

- One insight about hardware logic
- One SQL command you can now write confidently
- Questions to explore before next session
