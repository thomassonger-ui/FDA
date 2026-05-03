# REFERENCE — Moodle Configuration

## Base platform

- **Moodle version:** 4.3 or newer (LTS strongly recommended)
- **Theme:** Boost (child theme applying FIDA brand tokens — see `/marketing/REFERENCE-brand-spec.md` in the repo root)
- **Course format:** Topics format (one Section per Topic 0–15)
- **Short name:** `RAD-DENT-PERS`
- **Cohort:** `RAD-2026-05` (example; update per intake)

## Required plugins

| Plugin | Purpose | Notes |
|---|---|---|
| `mod_customcert` | Issues the FAC 64B5-9.011 certificate of completion | Custom PDF template with FIDA logo + QR verification code |
| `mod_h5p` | Interactive practice activities | Required for holder-selection simulator, landmark ID, etc. |
| `mod_attendance` | Documents clinical-day presence | Triggered at 0800 on Clinical Day |
| Safe Exam Browser | Lockdown for the final written exam | Install SEB config on the Topic 13 quiz |
| `local_competency` | Rubric-based clinical assessment | Backs the 7-competency clinical rubric |
| `report_trainingrecord` | Per-student training record export | Supports FDOE / Board of Dentistry audit |
| `block_completion_progress` | Student-facing progress block | Sidebar on course homepage |

## Enrollment

- **Self-enrollment:** disabled
- **Cohort sync:** students enroll via cohort membership, not manual per-course assignment
- **Access window:** 90 days from cohort start date; Moodle enrollment end date configured accordingly
- **Manual enrollment:** admin only, for corrections

## Security

- 2FA required on all admin + instructor accounts
- Role permissions: student cannot access question banks or quiz previews
- SEB required for final exam
- No password sharing; admin audit log reviewed per-cohort

## Data & backups

- **Retention:** minimum 4 years for completion records and certificates
- **Backups:** nightly off-site, tested quarterly for restoration
- **Audit export:** CSV of gradebook, completion status, and certificate issue log available on demand

## Gradebook

- Aggregation: **Weighted mean of grades**
- Categories + weights: see [`/02-assessments/REFERENCE-gradebook-weights.md`](../02-assessments/REFERENCE-gradebook-weights.md)

## Topic gating

Every topic restricted by prior topic's quiz completion:
```
Restrict access → Activity completion → {prior_quiz} must be marked complete
```

This enforces sequential progression.

## Environment stages

1. **Sandbox** — dev + contractor testing (Phase 1–2 of build)
2. **Client review** — client-facing review site (Phase 3)
3. **Production** — live cohorts (Phase 4 and beyond)

Pipeline: content authored in sandbox → exported → imported to review → approved → imported to production.
