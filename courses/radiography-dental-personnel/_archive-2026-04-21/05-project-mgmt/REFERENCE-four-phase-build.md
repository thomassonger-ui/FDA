# REFERENCE — Four-Phase Build Plan

**Contractor:** WorldTeachPathways dba WorldTeachESL / Atticus™
**Client:** Florida Institute of Dental Assisting
**Red-dot items = go / no-go gates.** A phase does not close until all red-dot items in that phase are complete and signed off.

---

## Phase 1 — Preliminary

**Goal:** Every input needed to build is confirmed, sourced, and approved.

### 1A Curriculum documents
- [ ] Master syllabus signed, states "64 contact hours"
- [ ] 13 lesson plans (M1–M12 + Final Exam)
- [ ] FDOE Standard 17 crosswalk signed
- [ ] FAC 64B5-9.011 alignment attested

### 1B State & regulatory approvals
- [ ] Florida Board of Dentistry submission filed (if required for this cohort model)
- [ ] 4-year record retention SOP documented

### 1C Books & instructional materials
- [ ] Textbook chosen (Iannucci vs. DALE) — see open decision #1
- [ ] Textbook licensing confirmed
- [ ] ≥ 100 intra-oral + ≥ 50 panoramic de-identified training images curated
- [ ] Video scripts / storyboards approved

### 1D Faculty & instructor
- [ ] Instructor of Record selected — open decision #5
- [ ] Florida dental license verified
- [ ] Supervising dentist for Clinical Day booked
- [ ] CV on file for audit

### 1E Infrastructure & technology
- [ ] Moodle hosting decision — open decision #2
- [ ] Moodle version confirmed 4.3+
- [ ] Sandbox environment provisioned
- [ ] PayPal (or chosen payment) business account ready
- [ ] Atticus CE API decision — open decision #3

### 1F Policies & student-facing documents
- [ ] Student handbook / policies draft
- [ ] Student acknowledgment form finalized
- [ ] Refund / withdrawal policy
- [ ] Accommodation policy

### 1G Clinical Day logistics
- [ ] Clinical site selected + booked (date scheduled)
- [ ] Cohort size confirmed — open decision #4
- [ ] Clinical Day schedule drafted (0800–1700)
- [ ] Equipment checklist (operatories, PPE, panoramic unit, imaging sensors, phantoms)

**Gate to Phase 2:** all 1A–1G critical items checked; open decisions resolved OR explicitly deferred with owner + date.

---

## Phase 2 — Assessments Configured

**Weeks 1–2 of build.** Goal: Moodle stands up end-to-end with all assessments live in sandbox.

### 2A Moodle setup
- [ ] Install plugins: customcert, H5P, attendance, SEB, competency, training record, completion progress
- [ ] Short name `RAD-DENT-PERS`
- [ ] 16 topics created
- [ ] Restrict Access gating configured across all topics

### 2B Module quizzes
- [ ] 13 module quizzes configured (M0–M12)
- [ ] Each draws from its module's item bank; 2 attempts, 80% pass
- [ ] Completion rules tie quiz pass → next topic unlock

### 2C Final exam
- [ ] 100-item quiz configured
- [ ] Random draw per composition table ([`/02-assessments/REFERENCE-final-exam-spec.md`](../02-assessments/REFERENCE-final-exam-spec.md))
- [ ] 120-min timer, SEB config uploaded
- [ ] 7-day cooling period + review assignment for retake

### 2D Clinical rubric
- [ ] 7-competency 4-point rubric set up (Assignment + `local_competency`)
- [ ] Remediation Log conditional activity configured

### 2E Commerce & enrollment
- [ ] Cohort `RAD-2026-05` created
- [ ] Cohort sync enrollment configured
- [ ] Self-enrollment disabled
- [ ] $1 sandbox PayPal test transaction passes
- [ ] Course pass threshold ≥ 80% set in course completion

**Gate to Phase 3:** sandbox PayPal test passes + all critical items checked.

---

## Phase 3 — Editing & Revising

**Weeks 3–4 of build.** Goal: content populated; client review; accessibility pass.

### 3A Content populated
- [ ] All 12 content modules fully populated (labels, readings, videos, H5P, quizzes, resources)
- [ ] Videos have captions + transcripts
- [ ] H5P interactives finalized

### 3B Question bank
- [ ] Each module: 25–30 items authored and SME-reviewed
- [ ] Categories + sub-categories tagged for random draw
- [ ] Final exam random-draw verified with 5+ trial runs

### 3C Accessibility
- [ ] WCAG 2.1 AA pass across course
- [ ] Alt text on every image
- [ ] Mobile: iOS Safari + Android Chrome tested
- [ ] Desktop: Chrome, Safari, Edge, Firefox tested
- [ ] Safe Exam Browser launch tested end-to-end on at least 3 student-grade machines

### 3D Client review
- [ ] Review URL provided to Client
- [ ] Client feedback captured in tracked issue log
- [ ] Each issue either resolved or accepted-as-is with sign-off

### 3E Certificate & survey
- [ ] Custom certificate PDF template populated with FIDA logo + QR
- [ ] Certificate verification URL — open decision #6
- [ ] Post-course survey (Topic 15) live

**Gate to Phase 4:** client review feedback incorporated + accessibility pass complete.

---

## Phase 4 — Sign-Off & Handoff

**Week 5 of build.** Goal: production-ready, client-owned, documented.

### 4A Dummy-student run
- [ ] Dummy student completes M0 → M12 (all quizzes ≥ 80%)
- [ ] Dummy student passes final via SEB
- [ ] Dummy student attendance marked Present on Clinical Day
- [ ] Dummy student rubric passes all 7 competencies
- [ ] Certificate auto-issues with valid verification code
- [ ] CSV gradebook export retrieved

### 4B Handoff documentation
- [ ] Instructor admin guide delivered
- [ ] 30-min recorded walkthrough delivered
- [ ] Student welcome email template delivered
- [ ] Board-audit export procedure delivered
- [ ] Retention & backup SOP delivered

### 4C Admin close
- [ ] QA report signed
- [ ] Sign-off form executed (all 4 phases)
- [ ] Contractor W-9 on file
- [ ] Final invoice + payment reconciled

### 4D Warranty
- **30-day warranty** from handoff.
- Contractor response time: **3 business days** on any defect during warranty.
- Out-of-scope changes tracked as new engagement.

**Gate to Production:** end-to-end dummy-student pass + QA report accepted.

---

## Phase Sign-Off Sheet

Use the template at [`TEMPLATE-phase-signoff.md`](./TEMPLATE-phase-signoff.md). One signature per phase per side (Contractor + Client).
