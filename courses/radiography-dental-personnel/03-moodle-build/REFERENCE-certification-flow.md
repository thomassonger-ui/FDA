# REFERENCE — Certification flow (RDP-CE)

Authoritative spec of how a student goes from "completed final exam" to "certificate PDF in hand" in Moodle. Effective 2026-05-16.

---

## TL;DR

A student earns the Radiography for Dental Personnel Florida CE certificate by:

1. Passing the Final Exam at ≥ 75%
2. Receiving any grade (≥ 0%) on the Capstone Project — Final Submission
3. Submitting the Clinical Verification Form, signed by their supervising Florida-licensed dentist (marked complete by staff)

When all three conditions are true, `mod_customcert` cmid 302 (`Download Your Certificate`) becomes accessible and the student downloads a PDF generated from the site-level Radiography Certificate template.

If any condition isn't met, the activity shows locked with the unmet conditions listed.

---

## Components

| Component | Type | cmid / id | Role |
|---|---|---|---|
| Final Exam — Radiography for Dental Personnel | quiz | cmid 205 / gradeitem 66 | Pass at ≥ 75% (canonical: Moodle gradebook) |
| Capstone Project — Final Submission | assignment | cmid 238 / gradeitem 80 | Instructor-graded |
| Clinical Verification Form | assignment | cmid 206 | Instructor marks complete after dentist sign-off |
| Certification — Course Complete | page | cmid 207 | Friendly "congrats" intro page pointing to the cert activity |
| Download Your Certificate | customcert | cmid 302 | Auto-issued PDF |
| Radiography Certificate template | site template | template id 6 | Reusable template loaded into cmid 302 |

---

## Access restrictions on cmid 302

```
Student MUST match ALL of the following:
  AND  Grade: Final Exam — Radiography for Dental Personnel  must be ≥ 75%
  AND  Grade: Capstone Project — Final Submission             must be ≥ 0%   (i.e. graded with any score)
  AND  Activity completion: Clinical Verification Form         must be marked complete
```

Notes:
- The Capstone "≥ 0%" condition triggers the moment the instructor enters any grade. Use a real pass threshold (e.g. ≥ 70%) only if FIDA decides cert eligibility should require capstone competence, not just instructor review. Current default = "graded".
- Hide-vs-greyed-out: defaults to **greyed-out / locked** so students see the unmet conditions. Toggle the eye icon on each restriction line in Edit certificate → Restrict access if FIDA prefers fully hidden.

---

## Certificate template

Loaded from site-level `Radiography Certificate` template (template id 6) on 2026-05-16.

Elements present:
- Background image (FIDA-branded landscape A4)
- Student name (dynamic — pulled from `users.firstname + lastname`)
- Date (dynamic — issuance date)

If FIDA wants additional fields (CIE institution #6501, verification code, signature line), edit at `/mod/customcert/edit.php?tid=10` → Add element. Available element types: Background image, Border, Category name, Code, Course field, Course name, Date, Date range, Digital signature, Expiry, Grade, Grade item name, Image, QR code, Student name, Teacher name, Text, User field, User picture.

---

## Instructor override path (Option A — Moodle gradebook)

Per role-split decision 2026-05-16: Moodle is canonical for grades + cert state. Atticus mirrors only.

To unlock a student's certificate manually:

1. Course → Grades → open the student's grade row
2. Edit the grade on whichever gating item needs adjustment:
   - Final Exam: bump score to ≥ 75% if you're approving a borderline performance
   - Capstone: enter any grade ≥ 0% (the act of grading is the gate, not the score itself)
   - Clinical Verification: mark complete on the assignment activity
3. Save. The restriction set on cmid 302 re-evaluates on the next page load and the certificate unlocks.

The grade override is automatically logged in `grade_grades_history` and the activity completion change is logged in `course_modules_completion` — both are visible to auditors via the gradebook history report.

---

## Page cmid 207 — what it now says

The legacy "we'll email your certificate" copy is gone. The new copy:

1. Navy gradient hero: "Course Complete · Congratulations — you've earned it."
2. Teal callout: "Your certificate is ready · Download → Download Your Certificate" (links to `/mod/customcert/view.php?id=302`)
3. Explainer: "Your certificate is auto-issued the moment your Final Exam, Capstone, and Clinical Verification are all on file."
4. Certification path checklist (same as before, includes Capstone now)
5. CE record note (institution #6501)
6. Practice with confidence closing line
7. Email fallback: `success@fldentalassisting.com`

---

## Atticus role (FIDA app)

Per the 2026-05-16 role split:

- Atticus is **downstream** for cert state. It mirrors what Moodle issues/revokes.
- Atticus stores cert PDF copies and audit trail metadata.
- Atticus does **not** override Moodle. It does not have a "revoke" action; only Moodle can revoke.

The webhook/poll pulling cert state from Moodle into Atticus is **not yet wired** — flagged for the integration session that will set `MOODLE_TOKEN` in the FIDA Vercel env vars.

---

## Verification checklist (smoke test)

Run as a non-admin student account:

1. Visit Week 6 — `Download Your Certificate` shows locked with all three conditions visible.
2. Complete only Final Exam at < 75% — cert stays locked, condition 1 shown unmet.
3. Bump Final Exam grade via instructor override to ≥ 75% — condition 1 resolves.
4. Enter any grade on Capstone — condition 2 resolves.
5. Mark Clinical Verification complete — condition 3 resolves.
6. `Download Your Certificate` is now unlocked. View → PDF renders with student name + date populated.

---

## Linked decisions

- 2026-05-16 — System role split locked: Moodle canonical for attendance, grades, cert issuance + revocation. Atticus is store/display/audit only.
- 2026-05-16 — Instructor override path: Option A (gradebook overrides), no separate override assignment.
- 2026-05-16 — Capstone gate: "graded with any score" (≥ 0%), not a pass threshold. Revisit if FIDA wants stricter.
