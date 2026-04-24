# TEMPLATE — Moodle Course Shell

Starter structure to copy when creating a new FIDA Moodle course.

## Course Metadata

- **Full name:** {{Course Full Name}}
- **Short name:** {{COURSE-CODE}} (e.g., RAD-64B5, EFDA-2026)
- **Category:** Continuing Education / Core Program / etc.
- **Format:** Topics format (one section per module) — OR — Single activity format (for short CE)
- **Course summary:** 2–3 sentences matching brand voice. Include FAC reference if applicable.

## Section Structure

```
Section 0 (General/Intro)
├── Welcome announcement (Label)
├── Syllabus (PDF resource)
├── Instructor intro (Page)
├── How this course works (Page)
└── Academic integrity (Page)

Section 1: Module 01 — {{Module Title}}
├── Module overview (Label)
├── Lesson pages (Book or Lesson activity)
├── Optional practice (H5P)
├── Module quiz (Quiz, 80% pass)
└── Module reflection (optional Forum)

... repeat Section 1 pattern for Modules 02–N ...

Section N+1: Final Competency
├── Final assessment guide (Page)
├── Final competency exam (Quiz, 80% pass, 3 attempts)
└── Certificate download (Custom certificate)
```

## Required Settings Checklist

- [ ] Enrollment method: cohort sync (not manual)
- [ ] Course start date set
- [ ] Course image uploaded (on-brand, see `/marketing`)
- [ ] Completion tracking enabled
- [ ] Gradebook configured with assessment weights
- [ ] Certificate configured and tested
- [ ] Mobile preview checked
- [ ] Accessibility: alt text on all images, captions on videos

## Content Authoring Guidelines

- Module titles: Oswald uppercase in Moodle theme — keep them short
- Each lesson should include: learning objective, reading, at least one visual, practice check
- Assessment questions mapped to learning objectives
- Use the radiography course as the reference pattern once built

## Handoff Checklist (before launch)

- [ ] All modules reviewed by subject-matter expert
- [ ] Compliance section reviewed against FDOE + Florida Board of Dentistry requirements
- [ ] Test cohort enrollment end-to-end
- [ ] Certificate generates correctly with real student name
- [ ] Backup of fully-populated course taken
