# REFERENCE — Cohort Structure (Generic)

Cross-course guidance for organizing students into cohorts in FIDA's Moodle.

## Cohort naming convention

`{program_code}-{start_year}-{start_month}-{cohort_letter_if_needed}`

Examples:
- `DA-2026-03-A` — Dental Assisting entry-level, March 2026 start, first cohort of that month
- `RAD-2026-05` — Radiography, May 2026 cohort
- `EFDA-2026-09-A` — Expanded Functions, September 2026 start

## Program cohort models

| Program | Cohort cadence | Enrollment model | Notes |
|---|---|---|---|
| Dental Assisting (6-month) | Scheduled starts (~every 3 months) | Closed cohort, synchronous | Entry-level program |
| Radiography for Dental Personnel | Scheduled cohorts | **Cohort-based, manual + sync** | Hybrid with 8-hr Clinical Day — see course folder for specifics |
| Expanded Functions | Scheduled starts | Closed cohort | TBD on cadence |

**Note:** Self-enrollment is disabled across all programs. Students are added to cohorts manually or via CSV import.

## Moodle cohort setup (general pattern)

1. Create a System-level cohort per intake (named per convention above).
2. Populate members manually or via CSV.
3. Course enrollment method = Cohort sync, linked to that cohort.
4. Course start date + enrollment end date = start + course length (e.g., 90 days for Radiography).
5. Cohort name surfaces on the completion certificate for audit traceability.

## Per-course cohort detail

Course-specific cohort rules (size, Clinical Day scheduling, etc.) live in that course's folder, e.g. [`/courses/radiography-dental-personnel/04-delivery/REFERENCE-cohort-structure.md`](../courses/radiography-dental-personnel/04-delivery/REFERENCE-cohort-structure.md).

## Reporting

Export per cohort monthly:
- Completion CSV (`report_trainingrecord`)
- Certificate issuance log
- Remediation / exception log

Retain minimum 4 years (confirm against current Board of Dentistry and FDOE requirements).
