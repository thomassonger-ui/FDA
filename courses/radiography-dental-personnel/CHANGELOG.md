# Changelog — Radiography for Dental Personnel

## 2026-05-16 — Automated certification flow + Consumer Info updates

The legacy manual "will be emailed" certification flow on cmid 207 is replaced with an auto-issued, restriction-gated `mod_customcert` activity. The previously flagged issue (Capstone not gating certification) is now resolved.

### Certification — new automated flow
- **NEW activity:** `Download Your Certificate` (cmid 302, `mod_customcert`) added to Week 6 (section 125), positioned after `Certification — Course Complete` (cmid 207).
- **Template:** loaded from the site-level `Radiography Certificate` template (template id 6). Elements: Background image, Student name (dynamic), Date (dynamic). PDF preview verified.
- **Access restrictions (AND, all required):**
  1. Grade: `Final Exam — Radiography for Dental Personnel` (cmid 205, grade item id 66) **≥ 75%**
  2. Grade: `Capstone Project — Final Submission` (cmid 238, grade item id 80) **≥ 0%** (i.e. *graded* — any score entered)
  3. Activity completion: `Clinical Verification Form — Florida-Licensed Dentist Sign-Off` (cmid 206) must be marked complete
- **Instructor override:** standard Moodle gradebook override on any of the three gating items unlocks the cert. No custom override flag — `mod_customcert` re-evaluates restrictions on every page load. Grade history captures the override audit trail.
- **Authority chain:** Atticus (FIDA app) is downstream — it mirrors Moodle's `cert.issued` state for display/audit only. Revocation authority sits with Moodle (per session role-split decision 2026-05-16).

### Page cmid 207 (`Certification — Course Complete`) — rewritten
- Removed: legacy "Step 1 Final review → Step 2 Certificate emailed → Step 3 CE record on file" manual issuance flow.
- Added: teal "Your certificate is ready" callout linking directly to `/mod/customcert/view.php?id=302` (`Download Your Certificate`).
- Added: explanatory line "Your certificate is auto-issued the moment your Final Exam, Capstone, and Clinical Verification are all on file."
- Visual structure unchanged (navy hero, FIDA design system).

### Page cmid 184 (`Consumer Information & Transparency Statement`) — content fills
- **Refund & cancellation policy** section replaced with the official 8-point CIE-aligned policy (cancellation methods · within 3 business days = full refund · before first class = full refund minus ≤$150 registration fee · 0–40% completion = pro-rated · >40% = no refund · termination date methodology · 30-day refund window · textbook return). Footer line: "Florida Institute of Dental Assisting · CIE institution #6501 · Last updated 2026-05-16."
- **Outcomes (updated annually)** figures replaced. Completion Rate = **100%**, First-Attempt Pass Rate = **95%**, Average Satisfaction = **100%** (current cohort). Was: all three TBD with "first cohort still in progress" subtext.

### Reference docs added
- `03-moodle-build/REFERENCE-certification-flow.md` — full spec of the cert gating + override paths
- `00-overview/REFERENCE-consumer-info-page.md` — canonical text of cmid 184 (refund policy, outcomes, licensure note, complaint resolution)

### Supersedes
- The 2026-05-02 architecture snapshot flag "Capstone Final not gating Certification by default" is now resolved by the cmid 302 restriction set. The snapshot text stays as a point-in-time record; this CHANGELOG entry is the canonical current state.

---

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
