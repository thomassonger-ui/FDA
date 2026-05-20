# FDA — Florida Institute of Dental Assisting Project

Central reference repo for the FIDA Moodle build, its courses, and supporting marketing + compliance documentation.

**Client:** Florida Institute of Dental Assisting (Jacksonville, FL) — https://fldentalassisting.com/
**Contractor:** WorldTeachPathways dba WorldTeachESL / Atticus™
**Updated:** 2026-05-19

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

## Design system (canonical)

All Moodle course pages, READMEs, and branded artifacts in this project must use the **WorldTeachPathways production design system**. The live Welcome page in the Sandbox course is the established baseline.

### Typography
- **Body:** `'Inter', system-ui, sans-serif`
- **Headings:** `'Playfair Display', serif`, bold

### Palette
- Navy (primary): `#1B365D`
- Navy (deep): `#122748`
- Teal (accent): `#2D6F73`
- Teal (light): `#7EC9CD`
- Border (cool gray): `#E0E4EA`
- Panel background: `#F5F7FA`
- Body text: `#1A1F2C`
- Muted body text: `#5A6B7C`

### Required components (in this order on top-level pages)
1. **Hero block** — linear gradient (navy → deep navy → teal), white text, uppercase eyebrow, Playfair H1, rounded `12px` corners
2. **Pillar cards** — responsive grid, white bg, `1px solid #E0E4EA`, `4px solid #2D6F73` top border
3. **Expectations block** — bg `#F5F7FA`, `5px solid #1B365D` left rail, check chips (teal circle, white check)
4. **Path-forward block** — dark navy gradient (`#1B365D → #122748`), white text, Playfair heading
5. **Nav block** — bordered white card, "Next up →" eyebrow, navy bold page title
6. **Footer** — centered, 13px, color `#5A6B7C`, copy: `Designed by WorldTeachPathways™ (dba WorldTeachESL LLC).`

### Layout defaults
- Page container: `max-width: 980px`, centered
- All blocks: `border-radius: 12px`
- Eyebrow text: 13–14px Inter, bold, uppercase, letter-spacing 1.5–2.5px

### Do NOT
- Default to Arial/Helvetica or "simple bordered box" layouts
- Skip the hero or footer
- Invent accent colors outside this palette

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

Production system in active delivery phase.

### Live cohorts (Summer 2026)

- **EFDA — Summer 2026** — `EFDA-S26` — `course id=21` — built 2026-05-19, content-complete clone of EFDA master, in Professional Development, visible, open-ended (self-paced)
- **RDP-CE — Summer 2026** — `RDP-CE-S26` — `course id=22` — built 2026-05-19, content-complete clone of RDP-CE master, in Professional Development, visible, open-ended (self-paced)

### Master blueprints

- `EFDA` master is now **Expanded Functions Dental Assisting Master Blueprint v1.0** (`course id=16`), hidden from students, source-of-truth for all future EFDA cohorts
- `RDP-CE` master is now **Radiography for Dental Personnel Master Blueprint v1.0** (`course id=14`), hidden from students, source-of-truth for all future RDP cohorts

### Cohort build pattern (validated 2026-05-19)

Future cohort builds should use **Course Import** (not Course Copy / Backup-Restore):

1. Create empty shell in Professional Development with desired full name + shortname, visibility Show, end date disabled
2. Open shell → More → Course reuse → Import → select the relevant Master Blueprint → import all defaults
3. Re-role instructors as Teacher on cohort, no role on Master Blueprint

Detailed build session memory: `memory/2026-05-19_moodle_cohorts_built.md`
