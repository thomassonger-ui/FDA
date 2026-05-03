# Changelog — Radiography for Dental Personnel

## 2026-05-02 — Major architecture restructure

The course was restructured from the original 64-hour / 13-module design to a leaner, fully Florida-CE-aligned 14-hour / 6-week / RHS101–RHS105 architecture. **The single source of truth for current state is `ARCHITECTURE_SNAPSHOT_2026-05-02.md` at this folder's root.** Files dated before this snapshot describe the legacy design and are retained for historical reference only.

### Architecture
- **Total contact hours:** 14 (8 theory + 6 lab + 0 externship). Was: 64 hours (56 online + 8 clinical).
- **Course count:** 5 RHS courses (RHS101–RHS105) + Week 6 Final Competency. Was: 13 modules (M0–M12).
- **Pass threshold:** ≥75% on graded assessments. Was: ≥80%.
- **Required textbook:** Bird & Robinson, *Essentials of Dental Assisting*, 7th ed. (Elsevier, ISBN 9780323764025). Was: Iannucci & Howerton.
- **Authority chain (now cited consistently):** FAC 64B5-9.011 · FDOE Std 17 · §466.024(6), F.S.

### New components
- 18 external-practice lesson pages (3 per week) linking out to Confederation College Pressbook activities (CC BY-NC-ND 4.0)
- 6 Self-Reflection assignments (200-word individual reflections, gating engagement)
- 2-phase Capstone Project (Week 5 Plan & Draft 2.5 hr + Week 6 Final Submission 3.5 hr = 6 lab hours total)
- Capstone Rubric & Self-Check Guide (5 criteria × 3 performance levels, shared across 3 format options)
- "Companion practice" panel on every Week 1–5 Overview, "Practice before the demonstration" block on Week 6
- WTP design system applied uniformly (Inter + Playfair Display, navy + teal palette)

### Gradebook
- **Course total = 100 points:** 50 Final Exam + 50 Capstone Final Submission
- All other activities (Knowledge Checks, Self-Reflections, Capstone Plan & Draft, Clinical Verification Form, HIPAA, Radiation Safety) set to weight = 0 — engagement gates only, do not move the score
- Was: 30% module quizzes / 30% final / 40% clinical rubric

### Sequencing & gating
- **Final Exam (cmid 205) restriction:** 18 prerequisites — HIPAA, Radiation Safety, 5 Books, Week 6 Overview, 5 KCs, 5 Self-Reflections (Weeks 1–5)
- **Certification page (cmid 207) restriction:** Clinical Verification Form (206) + Week 6 Capstone Reflection (236)
- **Capstone Final not gating Certification** by default — flag noted in snapshot for future decision

### Section structure
- 9 sections in current course (was 16 topics): General · Getting Started · Week 1–6 · Archive — legacy Module 01 (hidden)
- Legacy Module 01 lessons (cmids 162, 177, 163, 178, 165, 176, 186) moved to Archive section, hidden from students

### Tooling
- TinyMCE caveat documented (see `03-moodle-build/REFERENCE-wtp-design-system.md`): setting `textarea[name="page[text]"].value` directly does not work; must use `tinymce.get('id_page').setContent(html)` then `.save()` then submit
- Section reordering uses `core_courseformat_update_course` AJAX with `action: cm_move` and `targetcmid`

---

## 2026-04-21 — Initial design phase
Original blueprint, module specs, and 6-week pacing calendar produced. See files in `00-overview/` dated before 2026-05-02.
