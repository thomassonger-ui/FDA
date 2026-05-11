# Expanded Functions Dental Assisting (EFDA) — Course Planning Blueprint

**Provider:** Florida Institute of Dental Assisting (FIDA), Jacksonville, FL
**Moodle build target:** course id=**16** (empty shell — fresh build)
**Salvage source:** course id=9 (existing course — H5P assets and quizzes will be ported)
**Reference model:** Radiography for Dental Personnel — Florida CE Certification (course id=14)
**Document status:** ✅ APPROVED 2026-05-10 — moving from planning to scaffolding phase
**Author:** WorldTeachPathways™ · prepared 2026-05-10

---

## Source documents reviewed

| # | Document | Authority |
|---|---|---|
| 1 | Florida Department of Health Board of Dentistry Approval Letter (June 11, 2021) | Regulatory — confirms approval for Expanded Functions/Radiology Programs, Florida only |
| 2 | FIDA EFDA Program Outline (filed with FDOE — DOE Form 504, ID#6501) | Governing curriculum & cost structure |
| 3 | EFDA Employment Verification Form | Pre-enrollment gating document |
| 4 | Bird & Robinson, *Essentials of Dental Assisting* 7th ed. — 18 chapter lesson plans (Chapters 15, 18–24, 36, 44, 46, 49–51, 55–56, 58–59) | Required textbook + canonical content depth |
| 5 | RDP-CE Architecture Snapshot 2026-05-02 | Reference instructional architecture |
| 6 | FDA Moodle README-MERGED + design system reference | Naming conventions, design system, project standards |

---

## 1. Executive Course Analysis

### Course purpose
A 20-hour competency validation program preparing experienced dental assistants to legally perform thirteen designated Expanded Functions ("Remediable Tasks") under a supervising Florida-licensed dentist, in compliance with the Florida Board of Dentistry.

### Regulatory / compliance alignment
- **Authority:** Florida Board of Dentistry (Chapter 466, F.S. and Rule 64B5, F.A.C.)
- **Approval status:** Active — affirmed June 11, 2021 by Paulette Schofill, Program Administrator, Florida Department of Health, Division of Medical Quality Assurance
- **Approved geography:** Florida only. The current live Moodle course summary stating "approved in Florida and Georgia" is unsupported by the documentation provided and must be corrected before publication.
- **Filed program ID:** 6501 · Credential: Expanded Functions Dental Assistant Certificate
- **FDOE Program Outline:** Filed and on record; this blueprint maps every module to its filed EFDA1xx course code.

### Intended learner audience
Working dental assistants who have:
- Completed at least three (3) months of continuous on-the-job chairside training (volunteer/shadowing does not count)
- Reached 18 years of age
- Obtained a signed acknowledgment from a supervising Florida-licensed dentist confirming the above
- Demonstrate adequate English reading, writing, and speaking competency

The audience is post-foundational. Learners arrive with general dental-assisting fluency. Content should not re-teach basics; it should add procedural specifics, legal scope, and competency demonstration.

### Delivery model
- **Total contact:** 20 hours (Theory 13 · Lab 7 · Externship 0)
- **Format:** Online + Other (hybrid). Theory delivered through Moodle LMS; lab competency performed at the student's workplace under their supervising dentist.
- **Cohort length:** 5 weeks per the filed outline (compresses to ~4 hours/week of student commitment)
- **Tuition:** $1,049 (per filed outline)
- **No campus externship.** All clinical performance occurs in the student's existing employment setting.

### Theory vs. Lab breakdown (per filed outline)

| Hours | Allocation |
|---|---|
| 13 | Theory (LMS instruction, scenario-based knowledge checks, reading) |
| 7 | Lab (workplace clinical performance, dentist-verified) |
| 0 | Externship |
| **20** | **Total** |

### Operational risks (high level)
1. **Three-month chairside attestation** is self-reported and dentist-attested. Any audit will trace back to the verification form. The form must be collected and retained before LMS access is granted.
2. **Workplace lab supervision** is the sole quality assurance for hands-on competency. The instructor of record does NOT supervise procedures (mirrors RDP-CE compliance posture).
3. **Geographic-scope misstatement** ("approved in Florida and Georgia") in current Moodle summary is a regulatory exposure if shown to applicants.
4. **No formal externship hours** means the entire lab competency rests on dentist sign-off — make the verification form rigorous.
5. **Module-3 ambiguity** in the existing live course (Liners/Bases/Matrices/Temporary Restorations bundled without EFDA-code labels) creates a 1-to-1 traceability gap with the filed FDOE outline.

### Suggested instructional sequencing (rationale)
Re-order the modules to build cognitive load gradually rather than follow the EFDA101→113 outline numerically. Pedagogical sequencing places infection control first (it underlies every clinical procedure that follows), then field-setup procedures, then restorative materials, then preventive treatments, then impressions/perio/surgery, then final competency. Sequencing rationale detailed in §4.

---

## 2. Recommended Moodle Course Architecture

Mirroring RDP-CE structure (course id=14), adapted for a 20-hour, 5-week, EFDA-specific program.

### High-level section layout

| # | Section | Purpose |
|---|---|---|
| 0 | **General** | Site-wide policies, announcements, statements (always-visible footer of the course) |
| 1 | **Getting Started** | Pre-course gating: enrollment requirements, instructor intro, course orientation, syllabus, technology check, two acknowledgments |
| 2 | **Week 1 — Foundations & Infection Control** | EFDA scope/law preface + EFDA113 |
| 3 | **Week 2 — Patient & Field Preparation** | EFDA111 Dental Dam · EFDA109 Retraction Cord · EFDA106 Matrices |
| 4 | **Week 3 — Restorative Materials & Provisional Care** | EFDA104 Liners/Bases/Bonding · EFDA105 Temporary Restorations · EFDA108 Temporary Crowns |
| 5 | **Week 4 — Preventive Procedures** | EFDA101 Dental Sealants · EFDA102 Fluoride Placement · EFDA103 Coronal Polishing |
| 6 | **Week 5 — Impressions, Periodontal Care & Surgery** | EFDA107 Alginate Impressions & Study Models · EFDA110 Periodontal Dressing · EFDA112 Suture Removal |
| 7 | **Week 6 — Final Competency, Workplace Verification & Certification** | Final exam · Clinical Verification Form · Certificate |
| 8 | **Clinical/Lab Validation Resource Hub** | Workplace forms, photo submission rules, dentist sign-off protocol — referenced from every module |
| 9 | **Student Resources** | Textbook reference, glossary, EFDA scope reference card, downloadable forms, FAQ |

### Section-by-section detail

**General (section 0)** — single source of truth for compliance content. Mirrors RDP-CE General section.
- Announcements Forum
- Academic Integrity Statement
- Accessibility & ADA Statement (full canonical version)
- Privacy & FERPA Notice
- Student Support
- AI Use Policy
- Academic Integrity Policy
- Credit Hour and Weekly Statement
- Consumer Information & Transparency Statement

**Getting Started (section 1)** — gates Week 1.
- Welcome (Page) with embedded WorldTeachPathways-style hero + welcome video
- Meet Your Instructor (Page) with instructor video and credentials
- Course Orientation (Page) with course-walkthrough video
- Student Checklist (Page) — what to have ready before Week 1
- Course Syllabus (Page) — derived from the filed Program Outline
- Technology & Privacy Settings (Page)
- HIPAA Acknowledgment (Assignment, instructor-graded e-signature)
- Supervising Dentist Acknowledgment (Assignment, file upload of completed Employment Verification Form — the regulatory pre-enrollment gate)
- Required Textbook reminder block (Bird & Robinson, *Essentials of Dental Assisting* 7th ed., ISBN 9780323764025)

**Weekly Module Sections (sections 2–6)** — every weekly section follows the same internal pattern:
1. **Overview** (Page) — hero card + learning objectives + week pacing + EFDA code badges
2. **Lesson Material** (Page or Book) — textbook chapter mapping + scenario walk-through
3. **Companion practice** (H5P or Lesson) — interactive scenarios for each procedure
4. **Knowledge Check** (Quiz, ≥75%, 2 attempts, time-limited)
5. **Workplace Activity Log entry** (Assignment) — dentist-attested per-procedure log with photo evidence

**Week 6 — Final Competency & Verification (section 7)** — gated by AND-restriction across every Week 1–5 Knowledge Check (mirrors RDP-CE Final Exam gating).
- Week 6 Overview
- Final Exam (25 scenario MCQs, ≥75%, 2 attempts, 30 min)
- Clinical Verification Form (Assignment, file upload of dentist-signed competency for all 13 procedures)
- Course Completion Certificate (customcert plugin, auto-issued upon Final Exam ≥75% AND Clinical Verification approved)

**Clinical/Lab Validation Resource Hub (section 8)** — always visible. Holds the workplace-side documents that students reference repeatedly:
- Employment Verification Form (PDF download, completed pre-enrollment)
- Procedure Activity Log Template (per-procedure dentist sign-off sheet)
- Photo Evidence Submission Standards (anti-PHI, anonymization rules)
- Dentist Sign-Off Protocol (one-page how-to for the supervising dentist)
- Florida Board Scope of Practice quick-reference card

**Student Resources (section 9)** — always visible.
- Textbook chapter map (which textbook chapter pairs with which EFDA module)
- EFDA Glossary
- Florida Board of Dentistry — official EFDA scope link
- Mobile-learning tips
- Common questions / FAQ

---

## 3. Full Module-by-Module Outline

### Week 1 · Module 1 — Foundations & Infection Control
**Filed mapping:** Instructor preface (not on outline) + EFDA113 (2.0 clock hrs)
**Total seat time:** ~4 hrs (theory-heavy week)

| Element | Detail |
|---|---|
| **Title** | Foundations: EFDA Scope, Florida Law & Infection Control |
| **Learning objectives** | 1) State the legal scope of an EFDA in Florida 2) Identify the chain of infection and how to break it at each link 3) Demonstrate proper PPE selection, sequencing, and removal 4) Distinguish cleaning, disinfection, and sterilization 5) Apply CDC and OSHA standards in the dental operatory 6) Recognize regulatory authorities (FL Board, OSHA, CDC, EPA) and their roles |
| **Competencies covered** | EFDA scope literacy · infection prevention competence (foundational to every later module) |
| **Theory topics (textbook anchor)** | Bird & Robinson Ch 18 Microbiology · Ch 19 Disease Transmission & Infection Prevention · Ch 20 Disinfection · Ch 21 Sterilization · Ch 22 Regulatory Agencies · Ch 23 Chemical & Waste Management · Ch 24 Dental Unit Waterlines · Ch 15 Dental Caries (foundational context) |
| **Clinical concepts** | Hand hygiene timing · PPE donning/doffing sequence · surface barrier vs. wipe-down · instrument processing workflow · biological monitoring · waterline maintenance |
| **Suggested assessments** | Knowledge Check (10 scenario MCQs, time-limited) · Discussion: "Which step in *your* office's sterilization workflow is the weakest link, and why?" |
| **Suggested activities** | H5P interactive: chain-of-infection click-through · H5P branching scenario: a contaminated instrument is found mid-procedure — what next? |
| **Suggested videos / demos** | Welcome-to-the-week video (instructor) · 3-min PPE donning demo · Sterilization cycle walk-through · Florida Board scope of practice explainer |
| **Suggested reflection prompt** | "Describe one infection-control habit your office could improve and the standard that supports your recommendation." |
| **Workplace activity log** | Document one full instrument processing cycle in your office and obtain dentist initials |

---

### Week 2 · Module 2 — Patient & Field Preparation
**Filed mapping:** EFDA111 Dental Dam (1.5) · EFDA109 Retraction Cord (1.5) · EFDA106 Matrices (1.5)
**Total seat time:** ~4.5 hrs

| Element | Detail |
|---|---|
| **Title** | Patient & Field Preparation: Dental Dam · Retraction Cord · Matrix Systems |
| **Learning objectives** | 1) Explain the role of moisture control in restorative success 2) Correctly select clamp, frame, and dental dam material for an isolated quadrant 3) Place and remove a dental dam without trauma to soft tissue 4) Select cord size and chemistry for retraction in a Class V or full-coverage prep 5) Place and remove retraction cord using both single- and double-cord techniques 6) Select an appropriate matrix system for a Class II or Class III restoration 7) Place and remove sectional and Tofflemire matrices |
| **Competencies covered** | EFDA111 · EFDA109 · EFDA106 |
| **Theory topics (textbook anchor)** | Ch 36 Moisture Control · Ch 49 Matrix Systems · Ch 50 Fixed Prosthodontics (retraction sections) |
| **Clinical concepts** | Atraumatic tissue management · isolation as quality assurance · matrix adaptation and contour · gingival hemostasis · post-procedure re-evaluation |
| **Suggested assessments** | Knowledge Check (15 MCQs across all three procedures) · Clinical Competency Assignment: typodont-based dental dam application with photo |
| **Suggested activities** | H5P drag-and-match: retraction cord size to clinical scenario · H5P branching: cord placement complications |
| **Suggested videos / demos** | Dental dam application demo (instructor or vetted YouTube) · Cord placement demo · Tofflemire vs. sectional matrix comparison |
| **Suggested discussion prompt** | "When does dental dam isolation actively change patient outcomes? Cite a procedure type from your own experience." |
| **Workplace activity log** | One observed dental dam placement (dentist-attested) · One observed cord placement |

---

### Week 3 · Module 3 — Restorative Materials & Provisional Care
**Filed mapping:** EFDA104 Liners, Bases & Bonding (1.5) · EFDA105 Temporary Restorations (1.5) · EFDA108 Temporary Crowns (1.5)
**Total seat time:** ~4.5 hrs

| Element | Detail |
|---|---|
| **Title** | Restorative Materials: Liners, Bases, Bonding Systems · Temporary Restorations · Temporary Crowns |
| **Learning objectives** | 1) Differentiate liners, bases, and bonding agents by function and chemistry 2) Apply pulp-protection material in proper sequence 3) Place a Class V temporary restoration using IRM or zinc oxide eugenol 4) Fabricate a single-tooth provisional crown using preformed and direct-method techniques 5) Cement and finish a provisional restoration · 6) Provide post-operative instructions to a patient with a temporary restoration |
| **Competencies covered** | EFDA104 · EFDA105 · EFDA108 |
| **Theory topics (textbook anchor)** | Ch 44 Liners, Bases & Bonding Systems · Ch 50 Fixed Prosthodontics · Ch 51 Provisional Coverage |
| **Clinical concepts** | Pulp biology under restorative materials · biocompatibility · temp-cement selection · occlusal adjustment of provisionals · marginal seal evaluation |
| **Suggested assessments** | Knowledge Check (15 MCQs) · Clinical Competency: typodont-based provisional crown fabrication with submission photo |
| **Suggested activities** | H5P scenario: which material is right for this restoration? · H5P sequencer: layered base/liner application |
| **Suggested videos / demos** | Material-by-material walkthrough · Provisional fabrication demo · Patient-instruction script template |
| **Suggested discussion prompt** | "Describe a case in your office where the provisional restoration's quality directly affected the final outcome." |
| **Workplace activity log** | One observed provisional fabrication (dentist-attested, with photo of finished prov in place) |

---

### Week 4 · Module 4 — Preventive Procedures
**Filed mapping:** EFDA101 Dental Sealants (1.5) · EFDA102 Fluoride Placement (1.5) · EFDA103 Coronal Polishing (1.5)
**Total seat time:** ~4.5 hrs

| Element | Detail |
|---|---|
| **Title** | Preventive Procedures: Sealants · Fluoride · Coronal Polishing |
| **Learning objectives** | 1) Identify caries risk indicators that justify preventive intervention 2) Select tooth surfaces appropriate for sealant placement 3) Place pit-and-fissure sealants using the four-step etch-rinse-place-cure protocol 4) Choose between gel, foam, and varnish fluoride delivery systems 5) Apply topical fluoride safely with appropriate isolation 6) Perform coronal polishing using selective polishing principles |
| **Competencies covered** | EFDA101 · EFDA102 · EFDA103 |
| **Theory topics (textbook anchor)** | Ch 15 Dental Caries (caries risk) · Ch 58 Coronal Polishing · Ch 59 Dental Sealants |
| **Clinical concepts** | Caries risk assessment · tooth surface evaluation · etching chemistry · fluoride uptake · selective vs. full-mouth polishing · prophy paste grit selection |
| **Suggested assessments** | Knowledge Check (15 MCQs) · Clinical Competency Assignment: photo-documented sealant placement on a typodont molar |
| **Suggested activities** | H5P "The Science of Sealant Bonding" interactive (already exists in live course) · H5P "Coronal Polishing & Fluoride Application Interactive Video" (already exists) · H5P clinical documentation challenge (already exists) |
| **Suggested videos / demos** | Sealant placement demo · Fluoride application demo · Selective polishing comparison |
| **Suggested discussion prompt** | "Selective polishing is now considered standard of care. How does that change what you actually polish on a routine prophylaxis?" |
| **Workplace activity log** | One observed sealant placement · one fluoride application · one coronal polishing |

---

### Week 5 · Module 5 — Impressions, Periodontal Care & Surgery
**Filed mapping:** EFDA107 Alginate Impressions & Study Models (1.5) · EFDA110 Periodontal Dressing (1.5) · EFDA112 Suture Removal (1.5)
**Total seat time:** ~4.5 hrs

| Element | Detail |
|---|---|
| **Title** | Impressions, Periodontal Care & Surgical Follow-Up |
| **Learning objectives** | 1) Mix alginate at competency · 2) Take maxillary and mandibular preliminary impressions · 3) Pour and trim study models · 4) Place and remove periodontal dressing per surgeon instructions · 5) Identify suture types and removal indications · 6) Remove sutures atraumatically and document healing status |
| **Competencies covered** | EFDA107 · EFDA110 · EFDA112 |
| **Theory topics (textbook anchor)** | Ch 46 Impression Materials and Techniques · Ch 55 Periodontics (dressing sections) · Ch 56 Oral & Maxillofacial Surgery (suture sections) |
| **Clinical concepts** | Tray selection · alginate mixing ratios · model trimming standards · periodontal pack chemistry · atraumatic suture removal · suture-removal timing per type |
| **Suggested assessments** | Knowledge Check (15 MCQs) · Clinical Competency: full-arch alginate impression with model pour, photo-documented |
| **Suggested activities** | H5P "The Perfect Impression: Virtual Lab" (already exists) · H5P "Suture Removal: Clinical Decision-Making" (already a Lesson activity in live course) · H5P "Periodontal Dressing Mastery" (already exists as Lesson) |
| **Suggested videos / demos** | Alginate technique walkthrough · Model trimming demo · Periodontal dressing application · Suture removal types compilation |
| **Suggested discussion prompt** | "What single step most often produces a non-diagnostic alginate impression in your experience? How would you fix it?" |
| **Workplace activity log** | One observed alginate impression · one suture removal · one periodontal dressing placement OR removal |

---

### Week 6 · Final Competency, Workplace Verification & Certification
**Filed mapping:** Cumulative — covers all 13 EFDA competencies
**Total seat time:** ~2 hrs (assessment-only)

| Element | Detail |
|---|---|
| **Title** | Final Competency, Workplace Verification & Certification |
| **Activities** | 1) Week 6 Overview page (recap + what unlocks next) 2) Final Exam — 25 scenario MCQs, 2 pts each (50 marks), 30-min time limit, 2 attempts, ≥75% to pass, randomized question bank 3) Clinical Verification Form (Assignment, file upload, dentist-signed for all 13 EFDA procedures) 4) End-of-Course Feedback Survey (Feedback module, ungraded but required) 5) Certificate of Completion (customcert, auto-issued when Final Exam ≥75% AND Clinical Verification approved) |
| **Sequential gating** | Final Exam unlocked only when ALL Week 1–5 Knowledge Checks completed (engagement gate, mirrors RDP-CE) · Clinical Verification submission visible only after Final Exam pass · Certificate visible only after Verification instructor-approved |

---

## 4. Suggested Module Sequence — Rationale

The official outline lists EFDA101→113 in clinical-domain order (preventive → operative → prosthetic → periodontal → infection control). For learner experience, I recommend re-sequencing to follow **cognitive scaffolding**, not document order:

| Week | Module | Why this position |
|---|---|---|
| 1 | Foundations & Infection Control | Infection control underlies every later procedure — must be mastered before any clinical activity log entry. Also the largest single time block (2 hrs in outline). |
| 2 | Patient & Field Preparation | Field setup precedes every restorative procedure students will perform later. Front-loads the "before-you-treat" skills. |
| 3 | Restorative Materials & Provisional Care | Builds on field preparation — once isolation and matrix placement are taught, students can correctly contextualize material selection. |
| 4 | Preventive Procedures | Lower clinical complexity; refresher for procedures students likely already perform. Provides a pacing breather mid-course. |
| 5 | Impressions, Periodontal Care & Surgery | Highest single-procedure complexity (alginate technique + post-surgical care). Placed late so students have built up procedural confidence first. |
| 6 | Final Competency & Verification | Cumulative assessment + workplace sign-off submission. |

**Alternative — if FDOE auditor prefers strict outline order:** Group modules by EFDA code numerically. The trade-off is that infection control would land at the end (EFDA113) which contradicts pedagogical best practice. Recommend rejecting this alternative unless an auditor explicitly requires it.

---

## 5. Compliance & Risk Review

### Florida Board of Dentistry considerations
- Course must remain on the Board's approved list of Expanded Functions/Radiology Programs (currently confirmed via June 11, 2021 affirmation letter)
- Renewal verification with the Board on a recurring schedule — recommend an annual reverification task on Tom's calendar
- Course materials should reference the Board approval date and ID# in the syllabus and certificate

### Infection control considerations
- All H5P scenarios and demonstration videos must reflect current CDC and OSHA guidance, not the textbook publication date (Bird & Robinson 7th ed. is © 2017; verify against current CDC infection-control guidelines for dental settings)
- Recommend a "last reviewed" date stamp on the infection control module

### Student documentation requirements (must be collected and retained)
1. Signed Employment Verification Form (pre-enrollment, supervising dentist attests 3 months chairside)
2. Government-issued ID confirming applicant is 18+
3. HIPAA Acknowledgment (e-signed inside Moodle, Getting Started)
4. Supervising Dentist Acknowledgment uploaded to Moodle (Getting Started)
5. Clinical Verification Form (Week 6 — supervising dentist signs all 13 EFDA competency boxes)
6. Final Exam attempt records (Moodle quiz log)
7. Certificate of Completion archive (customcert audit trail)

**Records retention:** Recommend matching RDP-CE policy — 4 years minimum.

### Lab supervision considerations
The course does NOT supervise clinical performance. The supervising Florida-licensed dentist is the sole authority for lab competency validation. This must be stated explicitly in:
- Welcome page
- Course Syllabus
- Each module's Workplace Activity Log instructions
- Clinical Verification Form

This boundary mirrors RDP-CE's compliance posture and is critical for regulatory defensibility.

### Clinical validation concerns
- Photo submissions risk PHI exposure → enforce anti-PHI rule (no patient identifiers in any image, typodont-only for clinical competency assignments where possible)
- Dentist signatures require authentication — recommend uploading scan + dentist license number for audit trail

### Potential audit / compliance risks
| Risk | Severity | Mitigation |
|---|---|---|
| "Florida + Georgia" misstatement in current course summary | High | Correct to Florida-only before publication |
| Module 3 in current live course contains unlabeled EFDA104/105/106 content | Medium | Restructure into three labeled modules or one explicitly multi-code module |
| No EFDA106 Matrices module exists | Medium | Add as a sub-component of Week 2 (this blueprint) |
| End-of-Course Feedback Survey unconfigured | Low | Configure before launch |
| Bird & Robinson 7th ed. (2017) currency vs. current CDC/Board guidance | Low-Medium | Cross-check infection control content against current CDC Dental Settings guidance |
| No dentist license # verification on Clinical Verification Form | Medium | Add license # field to the form template |

---

## 6. Student Experience Strategy

### Best learner navigation flow
1. Land on course → see Welcome hero → watch welcome video
2. Forced sequential read-through of Getting Started (each page sets the next as restriction)
3. Submit HIPAA + Supervising Dentist acknowledgments → Week 1 unlocks
4. Each Week opens to Overview page → reading → companion practice → Knowledge Check → Activity Log
5. Once all 5 Knowledge Checks complete → Final Exam unlocks
6. Once Final Exam passed → Verification form unlocks
7. Once Verification approved → Certificate visible

### Engagement methods
- **Cohort-paced** rather than self-paced. Five-week cohorts with weekly cadence emails.
- **Welcome video + per-week intro video** from the instructor (mirror what was just added to RDP-CE).
- **H5P interactive scenarios** in every module, not just text + quiz. Live course already has 7 H5P assets to reuse.
- **Discussion forum per week** for cohort interaction (kept light — one prompt per week).
- **Workplace activity logs** create a personal-stakes connection to the student's own office and supervising dentist.

### Moodle activity recommendations per module
| Activity type | Per module |
|---|---|
| Page (Overview) | 1 |
| Page or Book (Lesson Material) | 1 |
| H5P (Companion Practice) | 1–2 |
| Quiz (Knowledge Check) | 1 |
| Assignment (Workplace Activity Log) | 1 |
| Forum (Discussion) | 1 (could be cohort-wide for the week, not per-module) |

### Mobile-first considerations
- All hero cards and pillar grids must collapse cleanly to single-column on phones (RDP-CE design system already handles this — reuse it)
- H5P content must be tested on iOS Safari and Android Chrome before launch
- Video embeds must be 16:9 responsive with `nocookie` host
- Workplace Activity Log uploads must accept phone-camera HEIC and JPG
- Avoid PDF-only content for mobile readers

### Completion tracking recommendations
Mirror RDP-CE engagement-gate pattern (`e=1`):
- **Pages:** marked complete on view
- **H5P:** marked complete on attempt (any score)
- **Knowledge Checks:** marked complete on attempt (any score) — score gate is separate
- **Workplace Activity Logs:** marked complete on submission
- **Final Exam:** must achieve ≥75%
- **Clinical Verification Form:** must be instructor-approved (manual)

### Instructor communication touchpoints
1. Welcome email at enrollment (auto)
2. Week-opening announcement each Monday (manual or scheduled)
3. Mid-cohort progress check (Week 3)
4. Final Exam reminder (Week 5)
5. Verification form approval / clarification messages (Week 6, per student)
6. Certificate issuance email (auto via customcert)

---

## 7. Assessment Planning

### Quiz strategy
- **Knowledge Checks (per week, Weeks 1–5):** 10–15 scenario MCQs, time-limited (15 min), 2 attempts, ≥75% to "pass" but engagement gate (any attempt unlocks Final Exam, mirroring RDP-CE)
- **Final Exam:** 25 scenario MCQs, randomized from a question bank of 75+ items, 30-min time limit, 2 attempts, ≥75% to pass
- **Question authoring standard:** Scenario-based, not recall. Each question should describe a clinical situation and ask the learner to choose the correct action.
- **Anti-cheat:** Time limits + randomization + scenario format + short-answer prompts where appropriate (mirror RDP-CE anti-cheat doctrine)

### Skills validation strategy
- **Workplace Activity Logs (per module):** dentist-initialed log of one observed performance per procedure, photo evidence where the typodont can be used (no PHI for live patients)
- **Clinical Competency Assignments (Weeks 2–5):** one typodont-based photo submission per week showing competency on the week's marquee procedure (dental dam, provisional crown, sealant, alginate impression)

### Practical evaluation checkpoints
| Checkpoint | When | Who validates |
|---|---|---|
| Week 1 reflection | End of Week 1 | Instructor reviews |
| Week 2–5 Workplace Activity Logs | End of each week | Supervising dentist signs · instructor reviews |
| Week 2–5 Clinical Competency typodont photos | End of each week | Instructor grades |
| Final Exam | Week 6 | Auto-graded by Moodle |
| Clinical Verification Form (all 13 procedures) | Week 6 | Supervising dentist signs · instructor approves |

### Final assessment structure
- **Final Exam** (25 questions × 2 pts = 50 marks · ≥75% pass · Moodle quiz · 2 attempts)
- **Clinical Verification Form** (13 procedures × dentist sign-off · instructor approval gates certificate)
- **End-of-Course Feedback Survey** (ungraded but required to unlock certificate)

### Competency verification methods
1. Cognitive: Knowledge Checks (engagement) + Final Exam (≥75%)
2. Applied: H5P scenarios + Clinical Competency typodont assignments
3. Hands-on: Workplace Activity Logs + Clinical Verification Form (dentist-attested)

This three-layer model is the same defensible posture used in RDP-CE.

---

## 8. Content Production Recommendations

### Types of videos needed (priority-ordered)
| Priority | Video | Length | Notes |
|---|---|---|---|
| P0 | Course Welcome (instructor) | ~2 min | Like the RDP-CE Welcome video — sets cohort expectations |
| P0 | Meet Your Instructor (Debbie) | ~2 min | Mirrors RDP-CE instructor video |
| P0 | Course Orientation walkthrough | ~3 min | "Here's how this course works, here's what you'll do each week" |
| P1 | Week-1 Infection Control overview | ~5 min | Sets the tone for the entire course |
| P1 | Per-week opener (Weeks 2–5) | ~2 min each | Brief weekly pacing video |
| P2 | PPE donning/doffing demo | ~3 min | Can be sourced from CDC public-domain content |
| P2 | Dental dam application demo | ~5 min | In-office filming opportunity |
| P2 | Provisional crown fabrication demo | ~6 min | In-office filming |
| P2 | Sealant placement demo | ~4 min | In-office filming |
| P2 | Alginate impression demo | ~5 min | In-office filming |
| P2 | Suture removal types | ~4 min | In-office or sourced |
| P3 | Final Exam pre-check (study tips) | ~2 min | Optional engagement booster |

### Demonstration priorities
- **Highest priority:** procedures students perform but rarely see on video at this depth — provisional crown fabrication, retraction cord placement, periodontal dressing placement.
- **Medium priority:** procedures students likely already do but may have bad habits — sealants, fluoride, polishing.
- **Sourced acceptable:** infection control basics, PPE — CDC and OSHA both publish reusable content.

### Visual learning opportunities
- Diagrams: chain of infection · sterilization workflow · matrix system anatomy · dental dam frame setup
- Photo galleries: cord-size selection chart · matrix system selector · suture types reference
- Comparison tables: alginate setting times · fluoride delivery vehicle pros/cons · provisional cement options

### Downloadable resources
- Bird & Robinson chapter map (PDF, one page, "which chapter goes with which module")
- Florida Board EFDA scope quick-reference card (PDF, one page, laminate-able)
- Procedure Activity Log template (PDF, fillable, dentist sign-off rows for all 13 procedures)
- Photo Evidence Submission Standards (PDF, one page — anti-PHI rules)
- Glossary (PDF, alphabetical)

### Forms / checklists needed during development
- Employment Verification Form (PDF — already exists, may want to convert to fillable PDF for online submission convenience)
- Clinical Verification Form — long form for Week 6 (PDF, needs to be designed; should include dentist license # field per §5 mitigation)
- Per-module Workplace Activity Log (PDF, fillable)
- Photo Submission release confirmation (PDF, anti-PHI attestation)
- Course Completion Certificate template (customcert in-Moodle)

---

## Decisions resolved at approval (2026-05-10)

| # | Decision | Resolution |
|---|---|---|
| 1 | Florida-only vs. "Florida + Georgia" approval scope | ✅ Florida only — confirmed by FL Department of Health letter dated June 11, 2021 |
| 2 | 5-week cohort cadence vs. self-paced | ✅ 5-week cohort cadence per filed outline |
| 3 | Pedagogical re-sequencing (infection control first) vs. strict EFDA101→113 | ✅ Pedagogical re-sequencing approved |
| 4 | Restructure id=9 in place vs. parallel new course shell | ✅ Build fresh in **id=16** (empty shell). Salvage H5P + quizzes from id=9 (do not destroy id=9) |
| 5 | Build new EFDA Pressbook vs. hybrid sourcing | ✅ Hybrid: Bird & Robinson + Tier 1 OER Pressbooks (link out, mirror RDP-CE pattern) + in-house H5P for gaps |
| 6 | Add a "Foundations" preface module (EFDA Scope, Florida Law) not on filed outline | ✅ Approved — included in Week 1 |
| 7 | Record-retention policy | ✅ 4 years minimum (matches RDP-CE) |

---

## Confirmed content sourcing strategy — Hybrid

Three layers, mirroring the RDP-CE pattern (textbook anchor + external Pressbook chapter linked OUT + embedded interactive activity):

1. **Primary textbook:** Bird & Robinson, *Essentials of Dental Assisting*, 7th ed. (Elsevier, ISBN 9780323764025) — students must purchase. Same textbook as RDP-CE, so most students will already own it.
2. **External Pressbook activities:** Link OUT from each lesson page (do NOT embed or copy — respects CC license terms, preserves attribution, mirrors how RDP-CE handles DE 115).
3. **In-house H5P:** Reuse 7 existing H5P assets from id=9 + author 3 new pieces for the gaps (retraction cord, provisional crown, refreshed dental dam interactive).

### Pressbook chapter mapping per module

| Week | Module | Bird & Robinson chapter anchors | External Pressbook link-out |
|---|---|---|---|
| 1 | Foundations & Infection Control | Ch 18 Microbiology · Ch 19 Disease Transmission · Ch 20 Disinfection · Ch 21 Sterilization · Ch 22 Regulatory Agencies · Ch 23 Chemical & Waste · Ch 24 Waterlines · Ch 15 Dental Caries (foundation) | [Introduction to Infection Prevention and Control Practices](https://ecampusontario.pressbooks.pub/introductiontoipcp/) (eCO, CC BY-NC) — full IPC framework · [Dentistry Environment Essentials](https://uq.pressbooks.pub/dentistryenvironment/) (UQ, CC BY-NC) — surgery layout, sterilization area, instruments, consumables |
| 2 | Patient & Field Preparation (Dam · Cord · Matrices) | Ch 36 Moisture Control · Ch 49 Matrix Systems · Ch 50 Fixed Prosthodontics (retraction sections) | [Restorative Mastery for the Dental Hygienist](https://mhcc.pressbooks.pub/restorativedentistry/) (MHCC, CC BY 4.0) — Tofflemire band/wedge prep · Rubber Dam Setup PDF |
| 3 | Restorative Materials & Provisional Care | Ch 44 Liners/Bases/Bonding · Ch 50 Fixed Prosthodontics · Ch 51 Provisional Coverage | [Restorative Mastery for the Dental Hygienist](https://mhcc.pressbooks.pub/restorativedentistry/) (MHCC, CC BY 4.0) — Placing Composite/Amalgam Restorations + Common Problems and Solutions |
| 4 | Preventive (Sealants · Fluoride · Polishing) | Ch 15 Dental Caries (caries risk) · Ch 58 Coronal Polishing · Ch 59 Dental Sealants | [Histology and Embryology for Dental Hygiene](https://openoregon.pressbooks.pub/histologyandembryology/) (Open Oregon, CC BY) — tooth/periodontal histology for caries-risk reasoning |
| 5 | Impressions · Periodontal · Surgery | Ch 46 Impression Materials · Ch 55 Periodontics (dressing) · Ch 56 OMS (sutures) | [Oral & Maxillofacial Surgery — A Handbook for Certified Dental Assistants](https://pressbooks.pub/oralsurgery4cdas/) (CC BY 4.0) — perioperative care + sterile technique + suture context · [Clinical Procedures for Safer Patient Care, Ch 4.4 Suture Removal](https://ecampusontario.pressbooks.pub/clinicalskills/chapter/4-3-suture-care-and-removal/) (eCO) — supplemental suture removal procedure |
| 6 | Final Competency & Verification | Cumulative — references all chapters above | n/a (assessment week) |

### In-house H5P — port + author

**Port from id=9 (7 assets, all already EFDA-built):**
1. Interactive Video: EFDA Scope & Restoration Safety
2. Dental Restorative Instruments Challenge
3. The "Perfect" Impression: Virtual Lab
4. The Science of Sealant Bonding
5. Coronal Polishing & Fluoride Application Interactive Video
6. Clinical Documentation Challenge
7. Plus Lesson-format: Suture Removal Clinical Decision-Making + Periodontal Dressing Mastery (technically Lesson activities, also port)

**Author new (3 pieces to fill gaps):**
1. Retraction Cord Placement — interactive scenario (size/chemistry selection + placement steps)
2. Provisional Crown Fabrication — interactive walk-through (preformed vs. direct method)
3. Dental Dam Application — refreshed interactive (clamp/frame/material selection + placement)

### License compliance posture

All Pressbook content is **linked OUT, never embedded or copied.** This:
- Respects CC license terms across all six selected resources (BY-NC, BY-NC-ND, BY 4.0)
- Preserves author attribution automatically (link points to source)
- Matches the RDP-CE precedent established with DE 115 Dental Radiography
- Eliminates derivative-work questions for the BY-NC-ND DE 115 chapter

### Citation list (8 OER sources approved for use)

1. [Restorative Mastery for the Dental Hygienist (Mt. Hood Community College)](https://mhcc.pressbooks.pub/restorativedentistry/) — CC BY 4.0
2. [Oral & Maxillofacial Surgery — A Handbook for Certified Dental Assistants](https://pressbooks.pub/oralsurgery4cdas/) — CC BY 4.0
3. [Dentistry Environment Essentials (University of Queensland)](https://uq.pressbooks.pub/dentistryenvironment/) — CC BY-NC 4.0
4. [Introduction to Infection Prevention and Control Practices (eCampusOntario)](https://ecampusontario.pressbooks.pub/introductiontoipcp/) — CC BY-NC 4.0
5. [Histology and Embryology for Dental Hygiene (Open Oregon)](https://openoregon.pressbooks.pub/histologyandembryology/) — CC BY 4.0
6. [Clinical Procedures for Safer Patient Care, Ch 4.4 Suture Removal (eCampusOntario)](https://ecampusontario.pressbooks.pub/clinicalskills/chapter/4-3-suture-care-and-removal/) — CC BY-SA 4.0
7. [DE 115 Dental Radiography, Ch 16.1 Infection Control (eCampusOntario)](https://ecampusontario.pressbooks.pub/de115radiography/) — CC BY-NC-ND 4.0 (already linked from RDP-CE)
8. [eCampusOntario Pressbooks catalog (parent index)](https://ecampusontario.pressbooks.pub/catalog/)

---

## Next phase — scaffold and build (in order)

1. ✅ **Scaffold sections in id=16** — rename empty placeholders to: General · Getting Started · Week 1–5 · Week 6 Final Competency
2. Confirm Module 3 content from id=9 (read summary HTML to assess what's salvageable for EFDA104/105/106 in Week 3)
3. Port the 7 H5P assets from id=9 → id=16
4. Build Getting Started pages with WorldTeachPathways design system (Welcome, Meet Instructor, Course Orientation, Student Checklist, Syllabus, Tech & Privacy, HIPAA Acknowledgment, Supervising Dentist Acknowledgment)
5. Build per-week Overview pages with hero + objectives + Pressbook link-out + companion practice
6. Wire completion rules and section restrictions (mirror RDP-CE engagement-gate pattern)
7. Author 3 new H5P pieces (retraction cord, provisional crown, dental dam)
8. Build Final Exam in Moodle Quiz with question bank (≥75 items)
9. Configure customcert for Certificate of Completion
10. End-to-end student walkthrough QA before publication

---

*Designed by WorldTeachPathways™ (dba WorldTeachESL LLC). Planning blueprint — not for student distribution.*
