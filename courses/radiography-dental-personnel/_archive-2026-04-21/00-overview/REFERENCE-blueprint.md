# REFERENCE — Master Blueprint

Governing specification for the Moodle course. Other files in this course elaborate or operationalize sections of this document.

## 1. Course Overview

| Field | Value |
|---|---|
| Title | Radiography for Dental Personnel |
| Short name | RAD-DENT-PERS |
| Version | 1.0 (April 2026) |
| Delivery | Hybrid — self-paced online + 1 day in-person clinical evaluation |
| Duration | 40–60 hours online + 8-hour clinical day (pacing calendar targets 56 + 8 = 64 hours) |
| Enrollment | Manual + cohort-based; self-enrollment disabled |
| Passing | ≥ 80% on final written exam AND satisfactory clinical competency sign-off |
| Authority | FAC 64B5-9.011 · §466.017(5), F.S. · Florida Board of Dentistry |
| FDOE alignment | Dental Assisting CIP 0351060108 — Standard 17 |

## 2. Admission requirements

- Florida-licensed-dentist affiliation
- Minimum 3 months experience in a dental setting
- Dentist attestation letter
- Government-issued photo ID
- Signed HIPAA and radiation-safety acknowledgments
- BLS / CPR (recommended — not required)

## 3. Course structure — 16 topics

See [`/01-curriculum/REFERENCE-topics.md`](../01-curriculum/REFERENCE-topics.md) for the authoritative topic list with hours and FDOE benchmarks.

## 4. Standard module template

Each content module (M0–M12) follows the same structure:

1. Learning Objectives (Label)
2. Required Reading (Book)
3. Video (≥ 90% watched to count)
4. H5P / SCORM interactive (≥ 70% — some modules raise this to ≥ 80%)
5. Optional Forum
6. Knowledge-Check Quiz — 10–15 items randomized from the module item bank, 2 attempts, ≥ 80% to unlock the next module
7. Resource Library (Folder)

Full per-module specs live in [`/01-curriculum/REFERENCE-module-specs.md`](../01-curriculum/REFERENCE-module-specs.md).

## 5. Final written exam (Module 13)

- 100 items drawn proportionally from all module item banks (composition in [`/02-assessments/REFERENCE-final-exam-spec.md`](../02-assessments/REFERENCE-final-exam-spec.md))
- 120-minute timer
- Safe Exam Browser required
- 80% to pass
- 2 attempts allowed; second attempt gated by 7-day cooling period + targeted review assignment

## 6. In-person clinical evaluation day (Module 14)

- 8-hour day at an affiliated clinical site
- 7 competencies on a 4-point rubric (3/4 = "Supervised" = passing threshold per competency)
- Any competency scored below 3 triggers a 30-day remediation re-test on that competency only
- Full detail: [`/02-assessments/REFERENCE-clinical-rubric.md`](../02-assessments/REFERENCE-clinical-rubric.md)

## 7. Moodle platform configuration

- Moodle 4.3+
- Plugins: mod_customcert, mod_h5p, mod_attendance, Safe Exam Browser, local_competency, report_trainingrecord, block_completion_progress
- Gradebook aggregation: Weighted mean of grades — module quizzes 30%, final exam 30%, clinical rubric 40%
- Course access window: 90 days from cohort start
- Records retention: minimum 4 years
- Backups: nightly off-site
- Audit export: CSV of gradebook, completion, certificates

Full config: [`/03-moodle-build/REFERENCE-moodle-config.md`](../03-moodle-build/REFERENCE-moodle-config.md).

## 8. FDOE Standard 17 mapping

See [`/01-curriculum/REFERENCE-fdoe-standard-17-map.md`](../01-curriculum/REFERENCE-fdoe-standard-17-map.md) — every module maps to at least one 17.0x benchmark.

## 9. Build checklist

Operationalized as a 4-phase plan with Contractor ↔ Client sign-offs. See [`/05-project-mgmt/REFERENCE-four-phase-build.md`](../05-project-mgmt/REFERENCE-four-phase-build.md).

## 10. Open decisions

Six items blocking final build. Tracked in [`REFERENCE-open-decisions.md`](./REFERENCE-open-decisions.md).

## Default textbook

Iannucci & Howerton, *Dental Radiography: Principles and Techniques* (specific edition TBD — see open decisions).
