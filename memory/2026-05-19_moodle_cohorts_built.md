# Session Memory — 2026-05-19: Summer 2026 cohorts built; MoodleCloud sync pipeline validated

**Project:** FIDA Moodle build
**Session date:** Tuesday, 2026-05-19 (work spanned into early hours of 2026-05-20 UTC)
**Author:** Tom Songer / Atticus (WorldTeachPathways)
**Status at end of session:** Both Summer 2026 cohort courses live in Moodle, content-complete, hidden masters renamed to "(Master Blueprint v1.0)".

---

## TL;DR

Two big things landed tonight:

1. **MoodleCloud's broken cohort-clone path was diagnosed end-to-end.** The synchronous backup/restore pipeline was validated with a smoke test. Sync backup + restore both work; the 2026-05-17 "stuck" jobs were async-mode artifacts left behind in `mdl_backup_controllers`, not a live failure. MoodleCloud is being asked (via Debbie) to clear those orphan rows for cosmetic reasons.
2. **Both Summer 2026 cohort courses are built.** EFDA-S26 (`course id=21`) and RDP-CE-S26 (`course id=22`) are populated, content-complete clones of their masters, sitting in Professional Development, ready for student enrollment when FIDA is ready.

---

## What was working / not working at start of session

| Thing | State |
|---|---|
| Async backup/restore queueing | **Broken** since 2026-05-17 — submitted course copies hung in "Process pending" indefinitely |
| Site-wide async backup setting | Disabled (MoodleCloud disabled it; sync is the new default) |
| Cron worker | Healthy (verified) |
| Ad-hoc task queue | Empty (verified) |
| Source courses (EFDA id=16, RDP-CE id=14) | Healthy and editable |
| Orphan `mdl_backup_controllers` rows | Still present for courses 14 and 16 from the 2026-05-17 attempts. Cosmetic only — display the "Backup pending for this resource" red banner on `/backup/backup.php?id=14|16` |

---

## The diagnostic walk-through (chronological)

1. **Verified async backup is disabled** at `/admin/settings.php?section=asyncgeneralsettings` (checkbox unchecked).
2. **System Status report:** all green — cron running frequently, 0 failing tasks, ad hoc queue empty, 0 long-running tasks. (`/report/status/index.php`)
3. **Visited copy-progress pages** for the stuck jobs:
   - `/backup/copyprogress.php?id=16` → EFDA → EFDA-S26 still "Process pending" from 2026-05-17 10:48 PM
   - `/backup/copyprogress.php?id=14` → RDP-CE → RDP-CE-S26 still "Process pending" from 2026-05-17 10:50 PM
4. **Concluded** the stuck jobs are inert async-mode artifacts; their ad-hoc task rows were already deleted (IDs 3704, 3705) during 2026-05-17 troubleshooting, but the `mdl_backup_controllers` rows persist. `copyprogress.php` reads from `mdl_backup_controllers`, hence the stale display.
5. **Purged all caches** via `/admin/purgecaches.php`. (Required one retry — first attempt crashed the Chrome renderer mid-render with "Aw, Snap!"; reload + repurge succeeded on the second click.)

---

## Smoke test (Path C — proven good)

Test target: `course id=11` ("Updated EFDA" / shortname `EFDA V2`), the smallest non-trivial course on the site (2 activities, 5 sections).

**Backup leg (sync):**

- Started backup at `/backup/backup.php?id=11`
- All defaults; clicked through Initial → Schema → Confirmation → Perform backup
- Elapsed: **~5 seconds**
- Output: `backup-moodle2-course-11-efda_v2-20260519-2336.mbz`, **486.3 KB**, visible in the course backup area

**Restore leg (sync, restore-as-new-course):**

- Started restore from the `.mbz`
- Destination: Archive category, restore as new course
- Renamed in flight at the Schema step to: `SMOKE TEST — DELETE ME (2026-05-19)` / shortname `smoke-test-20260519` (to avoid shortname collision with source)
- Clicked through Confirm → Destination → Settings → Schema → Review → Perform restore
- Elapsed: **~6 seconds**
- Output: New course id=20 with the full source content
- Cleanup: course id=20 was deleted by Tom from `/course/delete.php?id=20`

**Conclusion:** Sync backup + sync restore work end-to-end on MoodleCloud as of 2026-05-19 23:47 EDT. No site-level failure. The 2026-05-17 issue was async-mode-specific.

---

## The blocking detour (why we switched to Import)

On attempting the real EFDA backup (`/backup/backup.php?id=16`) for the actual cohort build, Moodle blocked us with a red banner:

> "Backup pending for this resource. Asynchronous backups only allow a user to have one pending backup for a resource at a time."

This was the orphan `mdl_backup_controllers` row from 2026-05-17 in action. With that row still present, Moodle refuses to start a new backup for course 16 — and the same would have been true for course 14.

**The pivot:** switched to the **Course Import** workflow instead.

Import doesn't touch `mdl_backup_controllers`. It runs synchronously, doesn't queue, and copies activities/resources/blocks/filters from a source course directly into a target shell.

This is the path memory's "Summer 2026 cohort clone — lesson learned" had already flagged: *"if cron breaks again on future cohort builds, lead with Import, not Course Copy."* Validated in practice tonight.

---

## Cohort builds (Import-based)

### EFDA-S26

| Field | Value |
|---|---|
| Source | EFDA master, `course id=16` |
| Target | New shell created at `/course/edit.php?category=3` |
| Target course id | **21** |
| Full name | Expanded Functions Dental Assistant — Summer 2026 |
| Short name | EFDA-S26 |
| Category | Professional Development |
| Visibility | Show |
| Start date | 2026-05-21 (default) |
| End date | Disabled (open-ended, self-paced per memory) |
| Sections imported | 8 |
| Activities imported | 61 |
| Import elapsed | ~30–40 seconds |
| Direct URL | https://fldentalassisting.moodlecloud.com/course/view.php?id=21 |

### RDP-CE-S26

| Field | Value |
|---|---|
| Source | RDP-CE master, `course id=14` |
| Target course id | **22** |
| Full name | Radiography for Dental Personnel — Summer 2026 |
| Short name | RDP-CE-S26 |
| Category | Professional Development |
| Visibility | Show |
| Start date | 2026-05-21 (default) |
| End date | Disabled |
| Sections imported | 8 |
| Activities imported | 67 |
| Import elapsed | ~15 seconds |
| Direct URL | https://fldentalassisting.moodlecloud.com/course/view.php?id=22 |

---

## Post-build housekeeping done in-session

- Both masters renamed to `… Master Blueprint v1.0` (full name) — done by Tom inside the session.
- Both masters set to **Hide from students** — done by Tom inside the session.
- The "two EFDA" / "two RDP" duplicate-name confusion in Archive resolved by renaming the archived duplicates to `… v1` (also done by Tom).
- Smoke-test course (id=20) deleted by Tom.

---

## Still TODO (carry forward to next session)

Order of suggested attack:

1. **Re-role** Debbie Sanders + Ashley Sanders on the cohorts: from Student (if currently enrolled) → Teacher on both EFDA-S26 and RDP-CE-S26. They should have **no role on the blueprints** so they can't accidentally edit Tom's source-of-truth.
2. **Delete duplicate Announcements forum** in each cohort — Moodle auto-created one in each new shell, then Import brought in the master's Announcements forum, leaving two per course.
3. **Spot-check customcert background image** in both cohorts (the EFDA customcert background fix should have carried via Import, but worth eyeballing).
4. **Unenroll Joe Angley** (`jangley@colemiddleton.com`) from the blueprints — Tom confirmed this is a test enrollment, not a real instructor.
5. **Fix the "Meet Your Instructor" vs "Meet Your Instructors" inconsistency** — RDP-CE master uses singular, EFDA master uses plural. Plural is canonical (Debbie + Ashley = two-instructor team). Worth fixing on the masters and re-importing the affected activity into the cohorts, OR editing the cohorts directly.
6. **Wait for MoodleCloud** to clear the orphan `mdl_backup_controllers` rows for courses 14 and 16. Request was sent to Debbie tonight; she'll relay to MoodleCloud support via the Customer Portal. Until cleared, the red "Backup pending for this resource" banner will continue to display on `/backup/backup.php?id=14|16` — cosmetic only, no functional impact.

---

## Lessons learned (for memory)

### Lesson 1: When sync backup is blocked by an orphan controller row, use Import.

The Backup → Restore-as-new-course path on MoodleCloud reads from `mdl_backup_controllers` to enforce "one pending backup per resource." If a stale row exists for the source course, the path is blocked. **Import does not consult `mdl_backup_controllers`**. It runs synchronously and directly. This is the right escape valve any time the backup path is jammed.

### Lesson 2: For cohort builds where `users=NO`, Import is strictly cleaner than Backup+Restore.

Even if backup were unblocked, Import is the better tool for cohort creation:

- No `.mbz` file artifact to manage / delete afterwards
- No "rename in flight at the Schema step" trick needed — you create the empty shell first with your desired identity, then pour content in
- Doesn't carry user data by definition (no `Include enrolled users` toggle to remember to uncheck)

### Lesson 3: Aw, Snap renderer crashes on long-running sync admin actions are recoverable.

The cache purge attempt crashed Chrome with error code 11. Reload + retry succeeded immediately. Lesson: close other heavy Chrome tabs before initiating any sync Moodle admin action that could take more than a few seconds, to reduce memory pressure. (The smoke test backup at 486 KB and the cohort imports at 30–40 seconds were fine — but the cache purge specifically seems heavier than expected.)

### Lesson 4: MoodleCloud will not auto-clean `mdl_backup_controllers` orphans.

Even after deleting the corresponding ad-hoc task rows in the user-facing admin UI, the `mdl_backup_controllers` rows persist and continue to drive UI state (the red "Backup pending" banner). Only MoodleCloud support can clear them via direct database access. Standing request format: provide course IDs, dates of original submission, and confirmation that the corresponding ad-hoc task rows were already deleted.

---

## State of the site at session end (2026-05-20 ~12:45 AM EDT)

### Professional Development category (live, visible)

- `id=21` Expanded Functions Dental Assistant — Summer 2026 — **NEW COHORT** (shortname EFDA-S26)
- `id=22` Radiography for Dental Personnel — Summer 2026 — **NEW COHORT** (shortname RDP-CE-S26)
- `id=15` Starting with Moodle (default Moodle course)

### Professional Development category (hidden from students)

- `id=16` Expanded Functions Dental Assisting Master Blueprint v1.0 (formerly "Expanded Functions Dental Assisting Certification Course") — MASTER, hidden
- `id=14` Radiography for Dental Personnel Master Blueprint v1.0 (formerly "Radiography for Dental Personnel — Florida CE Certification") — MASTER, hidden

### Archive category

- `id=13` Entry Level DA Program v1
- `id=9`  EFDA v1 (legacy archive snapshot)
- `id=11` Updated EFDA / shortname EFDA V2 (smoke-test source)
- `id=10` RHS v1 (legacy archive snapshot, formerly "Radiology for Dental Personnel Certification Course")

### Site-wide settings

- Async backup: **disabled**
- Caches: purged 2026-05-19 evening
- System Status: green across the board

---

## Emails sent tonight

1. **To Debbie + Ashley re: MoodleCloud orphan rows** — draft saved at `/FDA Moodle/2026-05-19_email_debbie_ashley_moodlecloud_followup.md`. Contains a paste-ready block for Debbie to send to MoodleCloud Customer Portal asking them to clear the orphan `mdl_backup_controllers` rows for courses 14 and 16.
2. **To Debbie + Ashley re: Summer 2026 cohorts built** — draft saved at `/FDA Moodle/2026-05-19_email_debbie_ashley_summer_2026_cohorts.md`. Notifies them the two cohort courses are ready, includes direct URLs, lists non-urgent follow-up items.

---

## Useful URLs (for future sessions)

- Moodle site: https://fldentalassisting.moodlecloud.com/
- EFDA master (hidden): https://fldentalassisting.moodlecloud.com/course/view.php?id=16
- RDP-CE master (hidden): https://fldentalassisting.moodlecloud.com/course/view.php?id=14
- EFDA-S26 cohort: https://fldentalassisting.moodlecloud.com/course/view.php?id=21
- RDP-CE-S26 cohort: https://fldentalassisting.moodlecloud.com/course/view.php?id=22
- Course management: https://fldentalassisting.moodlecloud.com/course/management.php
- Async backup setting: https://fldentalassisting.moodlecloud.com/admin/settings.php?section=asyncgeneralsettings
- System status: https://fldentalassisting.moodlecloud.com/report/status/index.php
- Stuck copy progress (will clear once MoodleCloud removes the orphans):
  - https://fldentalassisting.moodlecloud.com/backup/copyprogress.php?id=16
  - https://fldentalassisting.moodlecloud.com/backup/copyprogress.php?id=14
