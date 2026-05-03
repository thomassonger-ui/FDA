# REFERENCE — Gradebook (current)

Final gradebook structure as of 2026-05-02. **This file supersedes the legacy `REFERENCE-gradebook-weights.md` (which described the old 30/30/40 split).**

---

## Course Total = 100 points

| Item | Max | Weight | Counts toward grade? | Pass mark |
|---|---|---|---|---|
| Final Exam | 50 | **50%** | YES | 37.5 (75%) |
| Capstone Project — Final Submission | 50 | **50%** | YES | 38 (76% per rubric) |
| Knowledge Check Week 1 | 5 | 0% | no — engagement gate only | 3.75 (75%) |
| Knowledge Check Week 2 | 5 | 0% | no — engagement gate only | 3.75 |
| Knowledge Check Week 3 | 5 | 0% | no — engagement gate only | 3.75 |
| Knowledge Check Week 4 | 5 | 0% | no — engagement gate only | 3.75 |
| Knowledge Check Week 5 | 10 | 0% | no — engagement gate only | 7.5 |
| Self-Reflection Week 1 | 100 | 0% | no — engagement gate only | n/a (complete on submission) |
| Self-Reflection Week 2 | 100 | 0% | no — engagement gate only | n/a |
| Self-Reflection Week 3 | 100 | 0% | no — engagement gate only | n/a |
| Self-Reflection Week 4 | 100 | 0% | no — engagement gate only | n/a |
| Self-Reflection Week 5 | 100 | 0% | no — engagement gate only | n/a |
| Self-Reflection Week 6 (Capstone Reflection) | 100 | 0% | no — engagement gate only | n/a |
| Capstone Project — Plan & Draft | 100 | 0% | no — engagement gate only | n/a |
| Clinical Verification Form | 100 | 0% | no — engagement gate only | n/a |
| HIPAA Acknowledgment | none | — | no — completion gate, no grade type | n/a |
| Radiation Safety Acknowledgment | none | — | no — completion gate, no grade type | n/a |
| 2 archived H5Ps (legacy) | 100 each | 0% | no — hidden + zeroed | n/a |
| **Course total** | **100.00** | — | — | **75.00 to pass overall** |

---

## Aggregation method

- Category aggregation on "All Sandbox" (top-level): Natural
- All non-counting items have `weightoverride = 1` and `aggregationcoef2 = 0`, so their weight contributes 0% to the course total
- All non-counting items are also marked **Hidden in gradebook** (gradebook eye toggle), so students don't see them in their personal gradebook view — only Final + Capstone

---

## Why this structure

Self-checks (KCs and Self-Reflections) are formative — they exist to reinforce learning and to act as engagement gates that unlock the Final Exam and Certification. Counting them toward the score would create incentives to game the timer or share answers across the cohort. By keeping them weight-zero, the gradebook stays an honest measure of summative competency:

- **50 points from the Final Exam** = knowledge measurement, time-pressured (1 minute per question), 2 attempts (higher score recorded)
- **50 points from the Capstone Final Submission** = synthesis measurement, evaluated against a 5-criterion rubric, Complete / Needs Revision
- **All other completed work** = required for advancement but not for the score

The 50/50 split mirrors the canonical balance between *what you know* (Final) and *what you can do with it* (Capstone), which is exactly the balance the Florida Board of Dentistry expects from a competency-equivalent CE provider.
