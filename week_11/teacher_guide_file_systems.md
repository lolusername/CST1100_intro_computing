Title: Instructor Guide — Week 11 File Systems, Directories, and Disk Scheduling  
Audience: CST1100 instructors  
Total Class Time: 90 minutes (23 slides + labs)  

---

## 1. Session Goals
- Demystify how operating systems organise storage (file systems, directories, metadata).
- Contrast sequential and direct file access with tangible timing demos.
- Model disk scheduling algorithms (FCFS, SSTF, SCAN/C-SCAN) and discuss fairness vs. efficiency.
- Prompt students to connect technical ideas to personal file management via the writing log.

---

## 2. Pre-Class Setup Checklist
| Task | Details |
| --- | --- |
| Environment | Confirm Python 3, `pandas`, and `python-pptx` installed. Test lab notebooks (`file_systems_lab_student.ipynb`, `file_systems_lab_teacher.ipynb`). |
| Files | Open the Week 11 slide deck, student lab, teacher lab, and home lab. Print or share Daily Writing Log prompt. |
| Demo prep | Run the sequential vs. random read cells once to warm disk caches. Seed random module to keep timings consistent if you plan to screen-share results. |
| Room logistics | Ensure projector shows speaker notes view, blank sticky notes or polling tool ready for warm-up, index cards for exit ticket if needed. |

---

## 3. Slide-by-Slide Facilitation Notes
> A fully scripted narration for each slide (aiming at ~5 minutes) is embedded in the deck’s speaker notes. Use the summary below as a quick reference.

### Slide 1 — Welcome & Framing
- Set the tone: “Today we become storage librarians.”
- Connect to prior weeks (APIs, OOP): all that code lives on disk; data pipelines rely on orderly storage.

### Slide 2 — Today’s Flow
- Walk the class through the agenda; ask for a show of hands on current file habits to foreshadow later reflection.
- Emphasise the balance between conceptual lecture and hands-on lab work.

### Slide 3 — Why File Systems Matter
- Use library/library card analogy; highlight APIs (`open`, `read`, `write`).
- Stress metadata’s role in audits, backups, and security.

### Slide 4 — Four Layers to Watch
- Draw a stack on the board: physical → logical → virtual → user.
- Contrast HDD vs. SSD at the physical layer.

### Slide 5 — Directory Structures in Practice
- Demonstrate absolute vs. relative path navigation (`/Users/...` vs. `../Documents`).
- Address case sensitivity differences (macOS vs. Linux).

### Slide 6 — Naming Conventions & Hygiene
- Showcase good vs. bad filenames.
- Mention automation scripts breaking on spaces; propose consistent naming scheme (date prefixes).

### Slide 7 — Metadata: Beyond the Filename
- Display `ls -l` or Finder “Get Info” screenshot.
- Introduce extended attributes, magic numbers.

### Slide 8 — Extensions & Associations
- Categorise sample extensions; discuss suspicious ones (.exe, .bat, .ps1).
- Encourage students to think about default applications and MIME types.

### Slide 9 — Extension Detective Process
- Model the four-step classification process (inventory → cross-check → validate → decide).
- Explain how the lab mirrors professional incident response triage.

### Slide 10 — Sequential Access Essentials
- Use vinyl record or cassette analogy.
- Highlight OS prefetching and streaming scenarios (log analysis, backups).

### Slide 11 — Direct Access Essentials
- Compare to skipping tracks on Spotify; emphasise data structures enabling random jumps (indexes, B-trees).
- Connect to database query patterns.

### Slide 12 — Comparing Strategies
- Facilitate a think-pair-share: “Which workloads fit sequential vs. direct?”
- Record examples on whiteboard.

### Slide 13 — Caching & Buffers 101
- Introduce page cache, write-back buffers, SSD controller caches.
- Warn about sudden power loss and data in volatile buffers.

### Slide 14 — Disk Anatomy Refresher
- Display diagram (if available) of platters/heads vs. flash cells.
- Mention SMART monitoring and failure prediction.

### Slide 15 — Scheduling Goals & Metrics
- Define throughput, latency, total movement, variance.
- Ask: “Which matters most to a gamer? To a database admin?”

### Slide 16 — FCFS Algorithm
- Walk through 2–3 requests on the board; emphasise fairness and simplicity.
- Note inefficiency on long queues.

### Slide 17 — SSTF Algorithm
- Present benefits and starvation risk.
- Highlight real-world usage: OS schedulers often hybridise with aging/priority.

### Slide 18 — SCAN Family
- Use elevator metaphor; demonstrate LOOK and C-SCAN variants.
- Discuss fairness for outer cylinders.

### Slide 19 — Case Study Queue
- Work through numbers; compare movement and wait time.
- Encourage students to compute along in their notebooks.

### Slide 20 — Designing a Scheduling Policy
- Promote profiling and monitoring; tie to capacity planning.
- Suggest follow-up exploration: SSD vs. HDD tuning.

### Slide 21 — Lab Preview & Roles
- Assign pairs; define Driver/Navigator responsibilities.
- Set expectations for check-ins and pace (15 min per part).

### Slide 22 — Writing Log Prompts
- Preview reflection questions; remind students to jot notes during lab.
- Explain purpose: solidify habits and identify open questions.

### Slide 23 — Takeaway
- Recap key message: “Disks remember everything we ask of them.”
- Transition to live lab instructions; remind of final reflection timing.

---

## 4. Lab Facilitation Tips
- **Extension Detective:** ask each group to surface one suspicious filename; collect on board.
- **Sequential vs. Direct Benchmark:** have students predict results before running; compare HDD vs. SSD experiences.
- **Disk Scheduling Simulation:** ask volunteers to walk the “disk head” path on a printed tape or floor grid.
- Use the teacher notebook for quick reference answers and additional probing questions.

---

## 5. Post-Class Follow-Up
- Glance through writing logs to identify misconceptions (e.g., confusing sequential vs. direct).
- Review home-lab notebooks for consistent algorithm implementations.
- Queue up short videos or readings on file system internals (EXT4 journaling, NTFS MFT) for interested students.

---

## 6. Additional Resources
- “Operating Systems: Three Easy Pieces” — chapters on file systems and IO scheduling.
- Microsoft Docs: “File System Basics” for NTFS and ReFS.
- Linux Performance Tools (Brendan Gregg) slides for cache and IO insights.
