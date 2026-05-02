# FDA — Florida Institute of Dental Assisting Project

Central reference repo for the FIDA Moodle build, its courses, and supporting marketing + compliance documentation.

**Client:** Florida Institute of Dental Assisting (Jacksonville, FL) — https://fldentalassisting.com/
**Contractor:** WorldTeachPathways dba WorldTeachESL / Atticus™
**Updated:** 2026-04-24

---

## Directory Map

```
FDA/
├── README.md
├── courses/
│   └── radiography-dental-personnel/
│       ├── README.md
│       ├── 00-overview/
│       ├── 01-curriculum/
│       ├── 02-assessments/
│       ├── 03-moodle-build/
│       ├── 04-delivery/
│       └── 05-project-mgmt/
├── marketing/
├── moodle/
├── compliance/
└── client/
```

---

## How this repo is structured

Courses are first-class. Each course lives at:

`/courses/{slug}/`

Each course is fully self-contained. Everything required to design, assess, build, deliver, and hand off that course exists inside its folder, organized into six numbered stages (00–05).

Cross-course material lives at the root level.

---

## Active courses

- **Slug:** `radiography-dental-personnel`
- **Title:** Radiography for Dental Personnel
- **Regulatory:** FAC 64B5-9.011 · FDOE Std 17
- **Status:** Build in progress

---

## System model (Radiography course)

This course is a **competency validation system**.

It operates across three layers:

1. LMS instruction
2. Simulation-based practice
3. Workplace clinical verification

Clinical procedures:

- Occur at the student's place of employment
- Are supervised by a **Florida-licensed dentist**
- Are verified by that dentist

---

## Course hours

**Total Contact Hours: 14**

- Theory Hours (LMS Instruction): 8
- Lab Hours (Simulation-Based Practice): 6
- Externship Hours: 0

---

## Compliance model

The course provides:

- Instruction
- Simulation-based practice
- Assessment

The course does NOT provide:

- Clinical supervision
- Clinical competency validation

Clinical competency is verified by a **Florida-licensed dentist** at the student's workplace.

---

## File naming convention

- `README.md` — overview
- `REFERENCE-*.md` — authoritative documents
- `TEMPLATE-*.md` / `.html` — starter files

---

## Working files

Working drafts and Moodle exports live in:

`/FDA Moodle/`

Do NOT commit drafts to this repo.

---

## Key constraint

All course work must remain inside:

`/courses/{slug}/`

Do NOT create parallel structures.

---

## Status

Production system in build phase.
