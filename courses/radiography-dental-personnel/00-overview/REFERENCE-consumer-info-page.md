# REFERENCE — Consumer Information & Transparency Statement (cmid 184)

Canonical text of the Consumer Information page that satisfies CIE transparency requirements. Last updated 2026-05-16.

URL: https://fldentalassisting.moodlecloud.com/mod/page/view.php?id=184

---

## Sections (in order)

1. **Hero** — "Policies · Consumer Information · Consumer Information & Transparency Statement · What FIDA discloses to every prospective and enrolled student — outcomes, costs, refund terms, and how to file a complaint."
2. **Who we are** — FIDA = Jacksonville, FL CE provider; alignment with FAC 64B5-9.011, FDOE Standard 17, §466.024(6) F.S.
3. **Tuition & fees** — disclosed at enrollment in writing; no undisclosed fees; tuition reviewed annually; increases do not affect students already enrolled in an active cohort.
4. **Refund & cancellation policy** — see below
5. **Outcomes (updated annually)** — see below
6. **Florida licensure note** — present but not edited in this round
7. **Complaint resolution** — present but not edited in this round

---

## Refund & cancellation policy (official 8-point text)

> Should a student's enrollment be terminated or cancelled for any reason, all refunds will be made according to the following schedule.
>
> 1. Cancellation can be made in person, by electronic mail, by Certified Mail, or by termination.
> 2. All monies will be refunded if the school does not accept the applicant, or if the student cancels within three (3) business days after signing the enrollment agreement and making initial payment.
> 3. Cancellation after the third (3rd) business day but before the first class results in a refund of all monies paid, with the exception of the registration fee (not to exceed $150.00).
> 4. Cancellation after attendance has begun, through 40% completion of the program, will result in a pro-rated refund computed on the number of hours completed relative to total program hours.
> 5. Cancellation after completing more than 40% of the program will result in no refund.
> 6. **Termination date.** In calculating the refund due to a student, the last date of actual attendance is used unless earlier written notice is received.
> 7. Refunds will be made within 30 days of termination of the student's enrollment or receipt of the Cancellation Notice from the student.
> 8. Textbooks are to be returned upon signing the withdrawal form.
>
> *Florida Institute of Dental Assisting · CIE institution #6501 · Last updated 2026-05-16.*

---

## Outcomes (updated annually) — current figures

| Metric | Value | Cohort scope |
|---|---|---|
| Completion Rate | **100%** | current cohort |
| First-Attempt Pass Rate | **95%** | current cohort |
| Average Satisfaction | **100%** | current cohort |

Footer line: "Outcomes data will be updated within 60 days of each cohort's end and published here."

Previous state (pre-2026-05-16): all three metrics showed "TBD · first cohort still in progress".

---

## Visual / structural pattern

Each section is a white card:
```
<div style="background: white; border: 1px solid #e6e8ee; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: 22px; ...">Section title</h2>
  <p ...>...</p>
  ... section body ...
</div>
```

Hero uses the standard FIDA navy→teal gradient panel (see `03-moodle-build/REFERENCE-wtp-design-system.md` for the canonical hero CSS).

---

## When to edit

- **Annually** (typically January or after each cohort closes): refresh the Outcomes table with the latest figures.
- **As needed**: update the refund policy footer date when the policy text changes. If the underlying policy changes, route through compliance and update this REFERENCE doc + the live page in sync.
- **As regulator guidance changes**: confirm the Who we are / Florida licensure note / Complaint resolution sections still cite current statute and rule references.

---

## Linked decisions

- 2026-05-16 — Refund policy text adopted from FIDA's official CIE-aligned wording (8 items).
- 2026-05-16 — Outcomes figures populated for the first cohort (100% / 95% / 100%); subtext updated from "first cohort still in progress" to "current cohort".
