# REFERENCE — Completion Rules

Activity- and course-level completion settings for FIDA Moodle courses.

## Global Defaults

- **Activity completion:** enabled for every graded activity
- **Course completion:** enabled for every course
- **Completion tracking display:** shown to student on dashboard

## Radiography for Dental Personnel (FAC 64B5-9.011)

### Per-module completion
A student completes a module when all of the following are true:
1. All lesson pages viewed
2. Module quiz score ≥ 80%
3. Any H5P practice activity marked attempted

### Course completion
A student completes the course when:
1. All 16 modules complete
2. Final competency assessment score ≥ 80%
3. Minimum time-in-course met (if FDOE requires clock-hour verification)

### Certificate trigger
Auto-issue customcert PDF on course completion, including:
- Student full legal name (pulled from profile)
- Course name + FAC 64B5-9.011 reference
- Clock hours (total)
- Completion date
- Unique certificate ID (for verification)
- FIDA logo + instructor signature image

## Assessment Thresholds

| Item | Passing | Retake policy |
|---|---|---|
| Module quiz | 80% | Unlimited attempts, highest score counts |
| Final competency | 80% | Max 3 attempts; 4th requires instructor contact |
| Practical demonstration (if required) | Instructor sign-off | Unlimited until proficient |

## Grade Book

- Gradebook shows: module quizzes (weighted by topic — see `/radiography/REFERENCE-assessment-weights.md`), final exam, overall grade.
- Students can see their own grades only.
