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
