# REFERENCE — Completion Rules (Generic)

Cross-course guidance for Moodle completion rules. For course-specific rules, see the course folder.

## Global defaults

- **Activity completion:** enabled for every graded activity
- **Course completion:** enabled for every course
- **Completion tracking display:** shown to student on the dashboard
- **Gating:** sequential — each topic restricted by the prior topic's quiz completion

## Typical patterns across FIDA courses

### Per-module completion
Module completes when all true:
1. All lesson pages viewed
2. Module quiz score ≥ 80%
3. Any required interactive activity marked attempted

### Course completion triggers certificate
Requires (at minimum):
- All modules complete
- Final assessment ≥ 80% (if course has one)
- Any in-person / clinical components signed off
- Post-course survey submitted

## Course-specific completion rules

| Course | Where the full rules live |
|---|---|
| Radiography for Dental Personnel | [`/courses/radiography-dental-personnel/03-moodle-build/REFERENCE-completion-rules.md`](../courses/radiography-dental-personnel/03-moodle-build/REFERENCE-completion-rules.md) |
| Expanded Functions | (TBD when course is built) |
| Dental Assisting | (TBD when course is built) |

## Assessment thresholds (common)

| Item | Passing | Retake |
|---|---|---|
| Module quiz | 80% | 2 attempts, highest score kept; some courses require instructor reset after 2 failures |
| Final exam | 80% | Typically 2 attempts with cooling period (course-specific) |
| Clinical / skill demonstration | Per rubric | Remediation window per course (typically 30 days) |

## Gradebook

- Student sees own grades only
- Staff with `grader` role sees all grades for their cohort

## Changing rules

Any change to completion rules requires updating:
- The course's Moodle course completion configuration
- The course's `REFERENCE-completion-rules.md`
- The course syllabus and student welcome copy
