# REFERENCE — Moodle Plugins

Required plugins for the FIDA Moodle build. Install order matters where noted.

## Core-Required

| Plugin | Purpose | Notes |
|---|---|---|
| Certificate (mod_customcert) | Issue FAC 64B5-9.011 completion certificates | Required for radiography; supports custom PDF templates with logo |
| Quiz (core) | Assessment engine | Use for module quizzes + final exam |
| Assignment (core) | Skill demonstration uploads | Externship sign-offs |
| SCORM (core) | If any existing SCORM content is imported | Confirm with client before enabling |
| Completion (core) | Activity + course completion tracking | Required to trigger certificate |

## Compliance / Audit

| Plugin | Purpose | Notes |
|---|---|---|
| Report: Course completion | Cohort-level completion export | FDOE audit requirement |
| Report: Logs | Login/access logs | Retention period TBD |
| Attendance (mod_attendance) | Document student session attendance | Confirm if required for online CE |

## UX / Quality of Life

| Plugin | Purpose | Notes |
|---|---|---|
| BigBlueButton OR Zoom | Synchronous sessions if offered | Optional for self-paced radiography |
| Checklist (mod_checklist) | Student-facing progress list | Good for radiography 16-topic visibility |
| H5P | Interactive practice (drag-drop anatomy, image ID) | Recommended for radiography modules 11–12 |

## Theming

| Plugin | Purpose | Notes |
|---|---|---|
| Boost Union (custom child) | FIDA brand theme | Load Oswald/Inter via Google Fonts |

## Open Questions

- [ ] Will FIDA host Moodle themselves or use Atticus/WorldTeachPathways infrastructure?
- [ ] Is H5P licensing covered?
- [ ] Does FDOE audit require any specific reporting plugin?
