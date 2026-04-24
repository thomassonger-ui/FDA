# REFERENCE — Moodle Plugins (Generic)

Cross-cutting plugin guidance for the FIDA Moodle. Course-specific plugin lists live in each course's `/03-moodle-build/REFERENCE-moodle-config.md`.

## Core (always installed)

| Plugin | Purpose |
|---|---|
| Quiz (core) | Primary assessment engine |
| Assignment (core) | File / submission-based tasks |
| Completion (core) | Activity + course completion tracking |
| SCORM (core) | SCORM content playback (enable only if needed) |

## Certification + compliance

| Plugin | Purpose |
|---|---|
| `mod_customcert` | Custom PDF certificates (FIDA logo, FAC citation, QR verification) |
| `report_trainingrecord` | Per-student training record export (audit) |
| `mod_attendance` | Document in-person session attendance (required for any course with live/clinical component) |

## Assessment + security

| Plugin | Purpose |
|---|---|
| Safe Exam Browser | Lockdown proctoring for high-stakes exams |
| `local_competency` | Rubric-based competency assessment (used for clinical rubrics) |

## Content + interactivity

| Plugin | Purpose |
|---|---|
| `mod_h5p` | Interactive practice activities (drag-drop, hotspot, branching) |
| `block_completion_progress` | Student-facing progress block in the sidebar |

## Theming

| Plugin | Purpose |
|---|---|
| Boost (core theme) + FIDA child theme | Brand tokens from `/marketing/REFERENCE-brand-spec.md` |

## Per-course plugin specifics

| Course | Plugin list |
|---|---|
| Radiography for Dental Personnel | [`/courses/radiography-dental-personnel/03-moodle-build/REFERENCE-moodle-config.md`](../courses/radiography-dental-personnel/03-moodle-build/REFERENCE-moodle-config.md) |

## Open questions (cross-cutting)

- [ ] FIDA self-hosts vs. Atticus-hosts the Moodle instance
- [ ] H5P licensing covered
- [ ] Which audit-specific reports Florida Board of Dentistry and FDOE expect at inspection
