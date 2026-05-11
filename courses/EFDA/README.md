# Expanded Functions Dental Assisting (EFDA) Certification Course

**Florida Institute of Dental Assisting · Florida Board of Dentistry-approved (#6501) · 20 clock hours**

This folder is the canonical source for the EFDA Certification Course delivered on Moodle (`fldentalassisting.moodlecloud.com` · course `id=16`). Trust the live Moodle for runtime state; trust this folder for editable source material that drives future revisions.

## Contents

```
EFDA/
├── README.md                         (this file)
├── blueprint/
│   └── EFDA_COURSE_BLUEPRINT.md      Full 8-deliverable course plan, OER mapping, FBOD alignment
├── lessons/
│   ├── EFDA_Lesson_Material_Week_1.md   Foundations & Infection Control (EFDA113)
│   ├── EFDA_Lesson_Material_Week_2.md   Patient & Field Preparation (EFDA111, 109, 106)
│   ├── EFDA_Lesson_Material_Week_3.md   Restorative Materials & Provisional Care (EFDA104, 105, 108)
│   ├── EFDA_Lesson_Material_Week_4.md   Preventive Procedures (EFDA101, 102, 103)
│   └── EFDA_Lesson_Material_Week_5.md   Impressions, Periodontal Care & Surgery (EFDA107, 110, 112)
├── question-banks/
│   ├── EFDA_QBank_KC_Week_1.gift     10 scenario MCQs · Foundations & Infection Control
│   ├── EFDA_QBank_KC_Week_2.gift     10 scenario MCQs · Patient & Field Prep
│   ├── EFDA_QBank_KC_Week_3.gift     10 scenario MCQs · Restorative Materials
│   ├── EFDA_QBank_KC_Week_4.gift     10 scenario MCQs · Preventive Procedures
│   ├── EFDA_QBank_KC_Week_5.gift     10 scenario MCQs · Impressions, Periodontal & Surgery
│   └── EFDA_QBank_Final_Exam.gift    25 scenario MCQs · 2 pts each (50-pt Final Exam)
├── certificate/
│   ├── build_efda_cert_bg.py         ReportLab script generating the landscape A4 cert background
│   ├── EFDA-Certificate-Background.pdf   Source PDF (vector)
│   ├── EFDA-Certificate-Background.png   200dpi raster uploaded as Moodle Customcert bg
│   └── EFDA-Cert-Preview.png         Visual preview / design lock reference
└── assets/
    └── FIDA-logo-extracted.png       Florida Institute of Dental Assisting wordmark + tooth-shield mark
```

## Course architecture (Moodle id=16)

- 5 content weeks + 1 final-competency week
- Per-week sequence: Overview → Lesson Material → Workplace Activity Log → Knowledge Check (75% pass) → Self-Reflection
- Week 6: Clinical Verification Form (dentist sign-off) + Final Exam (50 pts / 75% pass) + Capstone Project (50 pts) + Feedback Survey → Customcert issued automatically

## Grading model

- **Course total = 100 pts** (Final Exam 50 + Capstone 50)
- Knowledge Checks: pass-to-advance only, 0% gradebook weight
- Self-Reflection: 0–5 light rubric, completion gate via submission
- HIPAA, Supervising Dentist Verification, Clinical Verification, Workplace Activity Logs: instructor sign-offs, no gradebook weight

## Regulatory alignment

- §466.024(6), Florida Statutes
- FAC 64B5-16.002 (Required Training)
- FAC 64B5-16.005 (Remediable Tasks Delegable to Dental Assistants)
- FAC 64B5-16.0051 (Delegation of Remediable Restorative Functions)
- Filed FDOE Program Outline #6501

## How to re-import the question banks

1. Moodle → Course id=16 → More → Question bank
2. For each `.gift` file in `question-banks/`: Import → GIFT format → upload file → Import
3. Each file auto-creates a category named `KC Week N` or `Final Exam` based on its `$CATEGORY:` directive

## How to regenerate the certificate

```bash
cd /path/to/this/folder/certificate/
python3 build_efda_cert_bg.py
# Outputs EFDA-Certificate-Background.pdf in same dir
# Convert to 200dpi PNG and re-upload to Customcert
```

## Course code in source

- Build target: Moodle course `id=16` on `fldentalassisting.moodlecloud.com`
- Reference architecture: Radiography for Dental Personnel CE course (`id=14`, see `courses/radiography-dental-personnel/`)
- Live cert template ID in Moodle: customcert template `tid=9`

## Author

Tom Songer · WorldTeachPathways™ (dba WorldTeachESL LLC), Contractor
Client: Florida Institute of Dental Assisting (Jacksonville)
Instructor of Record: Debbie Sanders, CDA · EFDA · Registered Dental Radiographer (FL)
