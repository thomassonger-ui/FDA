# REFERENCE — Gradebook Weights

## Weighting model

Moodle gradebook aggregation: **Weighted mean of grades**

| Component | Weight | Detail |
|---|---|---|
| Module quizzes (M0–M12) | **30%** | 13 quizzes equally weighted inside this pool |
| Final written exam (Topic 13) | **30%** | 100-item exam |
| Clinical competency rubric (Topic 14) | **40%** | 7-competency 4-point rubric |

**Course passing criteria (all must be true):**
1. Overall weighted grade ≥ 80%
2. Final exam ≥ 80% (non-negotiable)
3. Clinical rubric ≥ 3/4 on every competency (non-negotiable)
4. All content modules complete (quiz ≥ 80% + required activities)

## Why these weights

- Quizzes at 30% keep continuous accountability across 12 topics.
- Final at 30% rewards integrated didactic mastery.
- Clinical at 40% — the heaviest single component — reflects that radiography is ultimately a hands-on competency. A student who passes didactic content but cannot perform the technique cannot be certified.

## Module-quiz pool mechanics

- Each of the 13 module quizzes contributes 1/13 of the 30% pool.
- Passing score per module: 80%.
- Attempts: 2; Moodle keeps the **highest** score.
- Failing a module quiz twice relocks the module; student must request a reset.

## Changing the weights

Any change to 30/30/40 requires updating:
- Moodle gradebook setup
- [`/03-moodle-build/REFERENCE-completion-rules.md`](../03-moodle-build/REFERENCE-completion-rules.md)
- Course syllabus and student welcome copy
- Certificate language if it references assessment structure
