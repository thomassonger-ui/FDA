# REFERENCE — End-of-Course Survey (cmid 303)

Anonymous 5-minute survey collected from every student before they can download the certificate. Created 2026-05-16.

URL: https://fldentalassisting.moodlecloud.com/mod/feedback/view.php?id=303

---

## Architecture

- **Tool:** Moodle Feedback activity (`mod_feedback`)
- **cmid:** 303
- **Position:** Week 6, after Self-Reflection (cmid 236), before Certification page (cmid 207)
- **Anonymity:** Anonymous — student names are not stored with answers
- **Required:** Yes — completion gates the certificate (cmid 302) via a 4th access restriction
- **Completion criteria:** Student must submit responses to be marked complete

---

## Questions (6 items, ~5 min)

| # | Label | Type | Question | Scale |
|---|---|---|---|---|
| 1 | `course_clarity` | Multiple choice (rated) | How clear was the course material and structure? | 1 Very unclear → 5 Very clear |
| 2 | `instructor_support` | Multiple choice (rated) | How supportive was the instructor in helping you succeed? | 1 Not supportive → 5 Extremely supportive |
| 3 | `workload_accuracy` | Multiple choice (rated) | How accurately did the stated workload (14 hours) match your actual time? | 1 Much less → 5 Much more |
| 4 | `hands_on_usefulness` | Multiple choice (rated) | How useful were the hands-on simulation and Capstone activities? | 1 Not useful → 5 Extremely useful |
| 5 | `confidence_applying` | Multiple choice (rated) | How confident do you feel applying these skills in clinical practice? | 1 Not confident → 5 Very confident |
| 6 | `suggestions` | Long-answer text | Suggestions for improvement (open-ended) | n/a |

All Likert questions use the "rated" multichoice type so Moodle computes per-question averages.

---

## Description (shown above questions, before student submits)

Brief framing + the Google review invite. Surfaces the FIDA Google review link in a yellow-tinted callout: `https://share.google/LPPVT68vxuslgXPfw`. Pitch: *"If you'd be willing to leave FIDA a Google review, please click here. It helps prospective students find us."*

---

## Completion message (shown after student submits)

Renders only after submission. Reads:

> **Thanks — that helps us improve.** Your feedback goes straight into our planning for the next Radiography cohort. We read every response.
>
> **One last ask:** if FIDA helped you, please consider leaving us a quick public review on Google. It is the single biggest thing that helps prospective students find FIDA over big-box programs.
>
> [Leave a Google review →](https://share.google/LPPVT68vxuslgXPfw)
>
> When you are ready, return to the course to download your certificate.

The "Completion message" heading shown in the admin overview is a Moodle built-in label — only visible to teachers/admins, not to students.

---

## Certificate gating

Per `03-moodle-build/REFERENCE-certification-flow.md`, the `Download Your Certificate` activity (cmid 302) now has **four** access restrictions (AND-joined):

1. Grade: Final Exam ≥ 75%
2. Grade: Capstone Project — Final Submission ≥ 0% (graded)
3. Activity completion: Clinical Verification Form
4. **Activity completion: End-of-Course Survey** ← NEW 2026-05-16

Until the student submits the survey, the certificate stays locked even if all three other conditions are met.

---

## Where staff view results

- **Aggregate analytics:** `/mod/feedback/view.php?id=303` → Responses tab → "Show responses" / "Analysis"
- **Per-response table (still anonymous):** `/mod/feedback/show_entries.php?id=303`
- **Export:** Excel / CSV from the Responses tab — useful for cohort-over-cohort comparison
- **Non-respondents list:** identifies who hasn't completed yet (so you can nudge if necessary). Cert restriction makes this somewhat self-enforcing.

---

## When to revise

- **Per cohort:** Don't change the question text mid-cohort (breaks longitudinal comparison)
- **End of each year:** Review for clarity, add or rotate one question if a specific concern needs deeper signal
- **After major course restructure:** Refresh question 3 (workload anchor) to reflect new total clock hours

---

## Linked decisions

- 2026-05-16 — Survey is REQUIRED (cert-gated). Expected response rate ~95%+ vs. ~30-50% if optional.
- 2026-05-16 — Anonymous over identifiable. Honest feedback wins over knowing who said what.
- 2026-05-16 — Multiple choice (rated) over plain multichoice. Lets Moodle compute averages without manual aggregation.
- 2026-05-16 — Single page (no pagebreaks). All 6 questions visible at once. Faster completion, lower abandon rate.
- 2026-05-16 — Google review link surfaced TWICE (description before, completion message after) for maximum touchpoint exposure.
