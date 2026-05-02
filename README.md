# Radiography for Dental Personnel — CE Course System

## Overview

This repository contains the full instructional, assessment, and compliance system for a **14-hour Radiography for Dental Personnel Continuing Education (CE) course**.

This is not a traditional course.

It is a:

> **Competency validation system combining LMS instruction, simulation-based practice, and workplace-based clinical verification.**

---

## Hours Breakdown

**Total Contact Hours: 14**

- Theory Hours (LMS Instruction): 8
- Lab Hours (Simulation-Based Practice): 6
- Externship Hours: 0

---

## Course Model (Core Architecture)

This program operates across three integrated layers:

### 1. Instruction (Moodle LMS)

- Scenario-based learning
- Time-limited knowledge checks
- Image-based and decision-based questions

### 2. Simulation (Project-Based)

- Typodont / shipped materials
- Positioning and technique practice
- Error creation and correction exercises
- Photo-based submissions + reflection

### 3. Workplace Clinical Validation

- Radiographic procedures performed at the student's place of employment
- Supervised by a **Florida-licensed dentist**
- Dentist verifies and attests to competency
- The course does NOT provide clinical supervision

---

## Compliance Model (Critical)

The course provides:

- Instruction
- Simulation-based practice
- Assessment of knowledge and technique understanding

The course does NOT provide:

- Clinical supervision
- Patient access
- Clinical competency validation

Clinical competency is:

- Performed at the student's place of employment
- Verified by a **Florida-licensed dentist**

---

## Instructor Role

**Instructor of Record:**

- Delivers instructional content
- Evaluates LMS-based and simulation-based work
- Provides feedback

**Instructor does NOT:**

- Supervise clinical procedures
- Validate clinical competency

---

## Course Structure

### Weeks 1–3 (Theory)

- LMS instruction
- Scenario-based knowledge checks
- Time-limited assessments

### Weeks 4–6 (Application & Validation)

- Simulation (typodont-based)
- Workplace radiographic procedures
- Clinical logs and verification
- Reflection-based assessment

### Week 6

- Final competency submission
- Final exam (≥75% required)

---

## Assessment System

### Knowledge Checks

- 5 questions per section
- Scenario-based
- Time-limited (AI-resistant)
- Includes short-answer prompts

### Project-Based Assessments

- Simulation submissions (photos + explanation)
- Error identification and correction
- Reflection-driven evaluation

### Clinical Validation

- Activity logs
- Dentist initials/sign-off
- Clinical verification form

### Final Exam

- 25 questions
- Time limit enforced
- Passing score: 75%

---

## Anti-Cheat Design

- Time-limited quizzes
- Randomized question banks
- Scenario-based questions
- Short-answer explanations
- Physical simulation requirements
- Workplace-based validation (cannot be faked)

---

## Pre-Course Verification (Required)

Students must complete BEFORE accessing Week 1:

- Proof of clinical site access
- Signed supervising dentist agreement
- 3-month chairside experience acknowledgment
- Equipment access confirmation
- Data privacy acknowledgment

---

## Data Privacy Policy

- No patient identifiers may be submitted
- All images must be anonymized
- Submissions with identifying information must be rejected and resubmitted

---

## Repository Scope

All course work exists within:

`courses/radiography-dental-personnel/`

---

## Legacy Repository Notes (Preserved)

> The content below reflects prior repository documentation, references, and internal notes.
> It is preserved for continuity and internal use.

---

# FDA — Florida Institute of Dental Assisting Project

Central reference repo for the FIDA Moodle build, its courses, and supporting marketing + compliance documentation.

**Client:** Florida Institute of Dental Assisting (Jacksonville, FL) — https://fldentalassisting.com/
**Contractor:** WorldTeachPathways dba WorldTeachESL / Atticus™
**Updated:** 2026-04-24

---

## Directory Map

```
FDA/
├── README.md                                    ← you are here
├── courses/
│   └── radiography-dental-personnel/            ← one full course, self-contained
│       ├── README.md
│       ├── 00-overview/          blueprint, gap analysis, open decisions
│       ├── 01-curriculum/        16 topics, module specs, FDOE map, FAC cite
│       ├── 02-assessments/       gradebook, question bank, final, clinical rubric
│       ├── 03-moodle-build/      plugins, layout, completion rules
│       ├── 04-delivery/          6-week pacing, clinical day, cohorts, welcome copy
│       └── 05-project-mgmt/      4-phase build checklist, sign-offs, QA
├── marketing/                    brand audit + spec + email/landing templates
├── moodle/                       generic Moodle reference
├── compliance/                   FDOE + Board of Dentistry + audit checklist
└── client/                       FIDA + WorldTeachPathways (Atticus) info
```

## How this repo is structured

**Courses are first-class.** Each course lives at `/courses/{slug}/` and is self-contained: everything needed to build, assess, deliver, and hand off that course is inside its folder, broken into six numbered stages (00–05).

Cross-course material — generic Moodle guidance, shared marketing templates, FDOE/Board-of-Dentistry references, client contacts — lives at the top level.

## Active courses

| Slug | Title | Regulatory | Status |
|---|---|---|---|
| [`radiography-dental-personnel`](./courses/radiography-dental-personnel/) | Radiography for Dental Personnel | FAC 64B5-9.011 · FDOE Std 17 | Blueprint complete · 6 open decisions |

**Planned (not started):**
- Expanded Functions Dental Assisting
- Dental Assisting entry-level (6-month)

## File naming convention (applies everywhere)

- `README.md` — overview of the folder and how to use it
- `REFERENCE-*.md` — source-of-truth facts (regs, standards, canonical lists). Treat as read-only authoritative.
- `TEMPLATE-*.md` / `.html` — starter files to copy when creating new artifacts

## Working files

Working drafts and in-progress Moodle exports live in the local workspace folder (`/FDA Moodle/`) — not committed here. Only finalized reference + template files belong in this repo.
