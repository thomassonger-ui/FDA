# TEMPLATE — Dummy Student QA Run

End-to-end test executed in Phase 4. Simulates a real student from enrollment to certificate.

**Run by:** __________________  **Date:** __________________
**Environment:** ☐ Sandbox  ☐ Review  ☐ Production
**Cohort:** __________________

---

## Setup

- [ ] Create dummy student profile (test email, non-FIDA domain)
- [ ] Add to cohort
- [ ] Verify enrollment emails send correctly

## Course flow

- [ ] Login → course homepage shows progress block
- [ ] Topic 0 Welcome Label renders correctly
- [ ] Acknowledgment form submits and saves
- [ ] Topic 0 quiz → 80% → unlocks Topic 1

Repeat for each topic:

- [ ] Topic 1 — all activities complete, quiz ≥ 80%, next topic unlocks
- [ ] Topic 2 — same
- [ ] Topic 3 — same
- [ ] Topic 4 — same
- [ ] Topic 5 — same
- [ ] Topic 6 — H5P holder simulator works; quiz ≥ 80%
- [ ] Topic 7 — same
- [ ] Topic 8 — same
- [ ] Topic 9 — same
- [ ] Topic 10 — same
- [ ] Topic 11 — same
- [ ] Topic 12 — same

## Final exam (Topic 13)

- [ ] SEB launches correctly on test machine
- [ ] 100 items drawn (count + composition)
- [ ] Timer runs; auto-submit on expiry
- [ ] Score ≥ 80% → pass recorded
- [ ] Feedback shown per policy (overall only, after close)

## Clinical Day (Topic 14)

- [ ] Attendance marked Present
- [ ] Rubric: 7 competencies all scored ≥ 3
- [ ] No remediation triggered

## Completion & certificate

- [ ] Course completion fires (all 6 conditions met)
- [ ] Certificate auto-issues
- [ ] Certificate PDF: correct name, course title, FAC citation, hours, date, unique ID, QR code scans to verification URL
- [ ] Post-course survey submitted

## Admin verification

- [ ] `report_trainingrecord` CSV export retrieved
- [ ] Gradebook CSV export matches expected structure
- [ ] Audit log shows clean session

## Failure cases (run separately on a second dummy student)

- [ ] Fail a module quiz twice → module re-locks; reset request path works
- [ ] Fail final exam → 7-day cooling period enforced + review assignment appears
- [ ] Score a clinical competency < 3 → Remediation Log appears; 30-day re-test path works

## Sign-off

QA runner: __________________
Date: __________________
Issues logged: __________________
Acceptance: ☐ Pass  ☐ Pass with notes  ☐ Fail — remediate and re-run
