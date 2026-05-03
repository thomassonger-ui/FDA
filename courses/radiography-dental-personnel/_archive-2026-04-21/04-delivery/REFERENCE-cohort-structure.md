# REFERENCE — Cohort Structure

## Cohort model

- **Manual + cohort-based** enrollment
- **Self-enrollment:** disabled
- Students enroll in a cohort, not into the course directly
- Each cohort gets a fixed start date, 6-week online run, and a scheduled Clinical Day

## Cohort naming convention

`RAD-{{YYYY}}-{{MM}}`

Examples:
- `RAD-2026-05` — May 2026 cohort
- `RAD-2026-09` — September 2026 cohort

## Cadence

Quarterly cohorts by default (adjust per demand). Each cohort:

- Enrollment opens ~4 weeks before start
- Course runs 6 weeks
- Clinical Day in Week 6
- Certificates issue on completion (typically within a week of Clinical Day)
- 90-day access window ends ~90 days after cohort start

## Cohort size

- Open decision — see [`/00-overview/REFERENCE-open-decisions.md`](../00-overview/REFERENCE-open-decisions.md)
- Driven by Clinical Day supervision ratio (one supervising dentist can evaluate only so many students per day)

## Moodle setup per cohort

1. Create System cohort named `RAD-{{YYYY}}-{{MM}}`.
2. Populate cohort members (manual or via CSV).
3. Course enrollment method = Cohort sync, attached to that cohort.
4. Set course start date, enrollment end date = start + 90 days.
5. Update Topic 0 Welcome label with cohort-specific dates.
6. Schedule Clinical Day in `mod_attendance` for Week 6.

## Why cohort (not rolling)

- Clinical Day must be scheduled — requires site + supervising dentist logistics
- Live check-ins depend on a shared pace
- Cohort-level reporting is the audit expectation (FDOE and Board of Dentistry)

## Reporting

Monthly, per cohort:

- CSV export of completion status (`report_trainingrecord`)
- Certificate issuance log
- Any remediation records
- Exception log (extensions, deferrals)

Retain per [`/03-moodle-build/REFERENCE-moodle-config.md`](../03-moodle-build/REFERENCE-moodle-config.md).
