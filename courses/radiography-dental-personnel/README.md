# Radiography for Dental Personnel

Florida Continuing-Education course in dental radiography. Built for the **Florida Institute of Dental Assisting (FIDA)** under contract by **WorldTeachPathways (dba WorldTeachESL / Atticus™)**. Live in MoodleCloud at https://fldentalassisting.moodlecloud.com (Sandbox course id=14).

**Status as of 2026-05-02:** architecture stable, course open for review by Debbie Sanders (clinical/compliance lens) and Ashley Sanders (admin/student-experience lens). Nothing is locked.

> **The single source of truth for current state is [`ARCHITECTURE_SNAPSHOT_2026-05-02.md`](./ARCHITECTURE_SNAPSHOT_2026-05-02.md).** Read it first if you're new to this repo.

---

## At a glance — canonical facts

| | |
|---|---|
| Format | 6-week structured program · LMS instruction + simulation + workplace verification |
| Total contact hours | **14** (8 theory + 6 lab + 0 externship) |
| Required textbook | Bird & Robinson, *Essentials of Dental Assisting*, 7th ed. (Elsevier, ISBN 9780323764025) |
| Authority chain | FAC 64B5-9.011 · FDOE Std 17 · §466.024(6), F.S. |
| Pass threshold | **≥75%** on graded assessments |
| Final Exam | 25 scenario MCQs · 50 marks · 30-min timer · 2 attempts · ≥75% pass |
| Capstone Project | 2-phase artifact (6 lab hours total) · 50 marks · 5-criterion rubric · 3 student-choice format options |
| Gradebook | **100 points** = 50 Final Exam + 50 Capstone Final · self-checks weight = 0 |
| Records retention | 4 years minimum |
| Cohort model | Manual + cohort-based; Florida-licensed-dentist supervision required |

## Program breakdown by RHS course

| Course | Title | Hrs | Theory | Lab |
|---|---|---|---|---|
| RHS101 | Foundations of Radiography, Equipment, and Radiation Safety | 2 | 1 | 1 |
| RHS102 | Dental Imaging, Dental Film, and Processing Radiographs | 3 | 2 | 1 |
| RHS103 | Legal Issues, Quality Assurance, and Infection Prevention | 3 | 2 | 1 |
| RHS104 | Intraoral Imaging | 4 | 2 | 2 |
| RHS105 | Extraoral Imaging | 2 | 1 | 1 |
| Week 6 | Final Competency & Evaluation (Final Exam + Verification + Capstone + Cert) | — | — | — |
| **Total** | | **14** | **8** | **6** |

## Three-layer competency-validation system

1. **LMS instruction (theory)** — Bird & Robinson chapter readings + WTP-styled Moodle Pages with original commentary and scenario examples
2. **Simulation-based practice (lab)** — typodont positioning + the 2-phase Capstone Project + Pressbook H5P interactives (CC BY-NC-ND 4.0, Confederation College via eCampus Ontario)
3. **Workplace clinical verification** — radiographic procedures performed at the student's place of employment under a Florida-licensed supervising dentist, attested via the Clinical Verification Form (Week 6)

The course does **not** provide direct clinical supervision. Clinical competency is validated by the supervising dentist on the Clinical Verification Form. The contractor (WorldTeachPathways) is not Florida-licensed; the Instructor of Record is Debbie Sanders.

---

## Folder map

| Folder | Purpose |
|---|---|
| [`00-overview/`](./00-overview) | Architecture snapshot · cmid map · current state reference |
| [`01-curriculum/`](./01-curriculum) | Week-by-week scope · FAC 64B5-9.011 citation · FDOE Standard 17 crosswalk |
| [`02-assessments/`](./02-assessments) | Gradebook (50/50) · Capstone Rubric · Self-Reflection prompts |
| [`03-moodle-build/`](./03-moodle-build) | WTP design system · page templates · TinyMCE editing caveat |
| [`04-delivery/`](./04-delivery) | 14-hour pacing calendar reflecting the current architecture |
| `05-project-mgmt/` | (Currently empty; legacy four-phase build process archived) |
| [`_archive-2026-04-21/`](./_archive-2026-04-21) | Legacy design artifacts from the original 64-hour / 13-module / 80%-pass concept (April 2026). Preserved for design-history archeology only. **Not authoritative.** |

## Key files

- [`ARCHITECTURE_SNAPSHOT_2026-05-02.md`](./ARCHITECTURE_SNAPSHOT_2026-05-02.md) — comprehensive single source of truth
- [`CHANGELOG.md`](./CHANGELOG.md) — what changed and why (notes the 2026-05-02 major restructure)
- [`00-overview/REFERENCE-current-state-2026-05-02.md`](./00-overview/REFERENCE-current-state-2026-05-02.md) — every cmid mapped to its activity
- [`02-assessments/REFERENCE-gradebook-current.md`](./02-assessments/REFERENCE-gradebook-current.md) — 50/50 gradebook structure
- [`02-assessments/REFERENCE-capstone-rubric.md`](./02-assessments/REFERENCE-capstone-rubric.md) — 5-criterion analytic rubric
- [`02-assessments/REFERENCE-self-reflection-prompts.md`](./02-assessments/REFERENCE-self-reflection-prompts.md) — canonical 18 prompts (3 per week × 6 weeks)
- [`03-moodle-build/REFERENCE-wtp-design-system.md`](./03-moodle-build/REFERENCE-wtp-design-system.md) — design tokens, component patterns, TinyMCE caveat

---

**Repo updated:** 2026-05-03 — root README rewritten to mirror live Moodle state. Legacy artifacts moved to `_archive-2026-04-21/`. See `CHANGELOG.md` for the full restructure narrative.
