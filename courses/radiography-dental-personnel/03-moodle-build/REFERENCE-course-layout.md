# REFERENCE — Course Layout (Student + Instructor View)

Visual reference for what students and instructors see in Moodle. Use this as the "target state" when populating the course.

## Course homepage (student view)

Header displays: `Cohort: RAD-2026-05 · FAC 64B5-9.011 · 56 hrs online + 8 hr clinical`

Top of page: Completion Progress block (shows per-topic check marks).

Body: Topics 0–15 listed, with lock icons on any topic whose prior-topic quiz is not yet complete.

## Inside Topic 0 — Welcome

- Label: Welcome copy (tone document — see [`/04-delivery/TEMPLATE-welcome-copy.md`](../04-delivery/TEMPLATE-welcome-copy.md))
- Page: Syllabus
- Page: How this course works
- Page: Student expectations (Engage · Stay on Track · Prioritize Safety · Professionalism)
- Assignment: Student acknowledgment form (HIPAA + radiation safety)
- Quiz: Topic 0 knowledge check (gates Topic 1)

## Inside Topic 6 — Paralleling & Bisecting (exemplar topic)

7-activity structure, repeats as the pattern for every content topic:

1. **Label** — Learning Objectives
2. **Book** — Iannucci, Chapters 22–24 (or DALE equivalent)
3. **Video** — 18-minute FMX walkthrough (≥ 90% watched to count)
4. **H5P** — Holder Selection Simulator (≥ 70% — this module allows 70% threshold by design)
5. **Assignment** — Formative worksheet (ungraded, for practice)
6. **Forum** — Optional Q&A
7. **Quiz** — 15 items · 30-min timer · 2 attempts · 80% to pass

## Inside Topic 13 — Final Written Exam

- Label: Final exam instructions (including SEB setup)
- Quiz: final exam (100 items, 120-min timer, 80% pass, SEB required) — see [`/02-assessments/REFERENCE-final-exam-spec.md`](../02-assessments/REFERENCE-final-exam-spec.md)

## Inside Topic 14 — Clinical Evaluation Day

- Labels: what to bring; 0800–1700 schedule; station map (7 stations)
- Attendance: `mod_attendance` activity, triggered at 0800
- Assignment with rubric: Clinical Competency Rubric — 7 competencies on a 4-point scale
- Conditional Assignment: Remediation Log (visible only if any competency < 3)
- Detail: [`/02-assessments/REFERENCE-clinical-rubric.md`](../02-assessments/REFERENCE-clinical-rubric.md)

## Inside Topic 15 — Certificate & Survey

- Custom certificate: auto-issues when course completion conditions are met
- Feedback activity: post-course survey (for program improvement + FDOE feedback record)

## 10-step student journey (Day 1 → Week 6 Sunday)

| Day | Step |
|---|---|
| Day 1 | Enrollment email → login → Topic 0 Welcome + acknowledgment |
| Week 1 | Complete M0, M1, M2 quizzes |
| Week 2 | M3, M4 |
| Week 3 | M5, M6 |
| Week 4 | M7, M8 |
| Week 5 | M9, M10 |
| Week 6 — early | M11, M12 — all didactic complete |
| Week 6 — mid | Final written exam (SEB) |
| Week 6 — clinical day | In-person Clinical Evaluation Day |
| Week 6 — Sunday | Certificate auto-issued · post-course survey submitted |

Full pacing: [`/04-delivery/REFERENCE-6-week-pacing.md`](../04-delivery/REFERENCE-6-week-pacing.md).
