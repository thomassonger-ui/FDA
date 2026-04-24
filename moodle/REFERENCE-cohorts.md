# REFERENCE — Cohort Structure

How students are organized across FIDA's Moodle programs.

## Cohort Naming Convention

`{program_code}-{start_year}-{start_month}-{cohort_letter}`

Examples:
- `DA-2026-03-A` — Dental Assisting, March 2026 start, first cohort
- `RAD-2026-Q2` — Radiography, rolling Q2 enrollment (self-paced)
- `EFDA-2026-09-A` — Expanded Functions, September 2026 start

## Program Cohort Rules

| Program | Cohort cadence | Enrollment model |
|---|---|---|
| Dental Assisting (6-month) | Scheduled start dates (~every 3 months) | Closed cohort, synchronous |
| Radiography for Dental Personnel | Rolling | Self-paced, quarterly cohort buckets for reporting |
| Expanded Functions | Scheduled start dates | Closed cohort |

## Moodle Cohort Setup

1. Create a system-level cohort for each bucket above.
2. Auto-enroll students into the appropriate cohort on registration via profile field `program`.
3. Course enrollment is cohort-sync based on the cohort.
4. Cohort name appears on the completion certificate for audit traceability.

## Reporting

- Export completion by cohort monthly for FDOE records (keep 5 years minimum).
- Tag all cohorts with the responsible instructor in cohort `description` for accountability.
