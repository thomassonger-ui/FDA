# REFERENCE — Completion Rules

Course completion fires only when **all six** conditions below are true. Only then does the certificate auto-issue.

## The 6 completion conditions

1. **All 13 module quizzes** (M0–M12) marked complete with score ≥ 80%
2. **Final written exam** (Topic 13) passed with score ≥ 80%
3. **Clinical Day attendance** marked "Present" via `mod_attendance`
4. **Clinical rubric** shows ≥ 3/4 on every one of the 7 competencies
5. **All required videos** ≥ 90% watched (enforced per activity completion rule)
6. **Post-course survey** submitted (Topic 15 feedback activity)

Moodle configuration: `Course completion → All of the conditions below`, each listed as a required activity.

## Certificate auto-issue

On course completion, `mod_customcert` auto-issues a PDF with:

- Student legal name (from profile)
- Course title + FAC 64B5-9.011 citation
- Hours: "56 online + 8 clinical = 64"
- Completion date
- Unique certificate ID
- QR code linking to verification URL (see open decision #6)
- Instructor signature image
- FIDA logo + seal

## Re-issuance / lost certificate

- Students may re-download from Moodle as long as the enrollment is active.
- Post-access-window requests: Instructor of Record confirms identity, then re-issues from `mod_customcert` admin interface.
- Re-issued certificates retain the original certificate ID (do not renumber).

## Reporting

Per cohort (monthly):
- CSV export of all completions (`report_trainingrecord`)
- Certificate issuance log (audit-ready)

Retained: minimum 4 years. See [`REFERENCE-moodle-config.md`](./REFERENCE-moodle-config.md).
