# Demo Prototype — 5-Page Radiography Shell

A presentation-ready demonstration shell for FIDA ownership review, showing what a professionally architected Radiography course could look like inside Moodle.

**Purpose:** leadership pitch + scalable template, not a full course build.

## Files in this folder

| File | Purpose |
|---|---|
| `demo-prototype.html` | Standalone browser-viewable prototype. Open in Chrome/Safari/Edge — no login, no Moodle required. Tabs at top switch between the 5 pages. Use this for the leadership pitch. |
| `moodle-page1-landing.html` | Moodle-ready HTML: **Section Landing** (paste into Moodle Page) |
| `moodle-page2-module.html` | Moodle-ready HTML: **Lesson / Module Template** |
| `moodle-page3-knowledge-check.html` | Moodle-ready HTML: **Interactive Practice / Knowledge Check** |
| `moodle-page4-clinical.html` | Moodle-ready HTML: **Clinical Competency** |
| `moodle-page5-resources.html` | Moodle-ready HTML: **Resources / Wrap** |
| `BUILD-INSTRUCTIONS.md` | Step-by-step: how to add the 5 Pages to the Sandbox course in Moodle |

## Design system

Professional allied-health aesthetic — premium, accreditation-ready, not default Moodle.

**Palette:**
- Primary Navy `#1B365D`
- Teal Accent `#2D6F73` (primary button + accents)
- Soft Gray background `#F5F7FA`
- Compliance Red `#B33A3A` (regulatory alerts only)
- Secondary warning Amber `#B87A00` (clinical tips)
- White content cards

**Typography:**
- Headlines: Playfair Display (serif, weight 700) — gives boutique-institute feel
- Body + UI: Inter (sans-serif, weights 400–700)
- Fonts served via Google Fonts

**Reusable instructional components demonstrated:**
- Branded hero banner with meta row
- Learning outcomes panel (numbered)
- Progress path visual (completion-aware)
- Instructor intro card (navy block)
- Overview panel with meta grid
- Video placeholder (swap for embed)
- Key concept / clinical tip / compliance alert / reflection callouts
- Content cards (border-top accent)
- Scenario-based quiz preview with feedback
- Skills checkpoint banner
- Skills checklist with pass/pending scoring
- Numbered procedure steps
- Instructor sign-off block with signature lines
- Resource repository cards (PDF, MP4, H5P, DOC, LINK)
- Next-module progression checkpoint
- Branded footer

These components are intentionally reusable — the same pattern can populate every module across the Radiography course (and future Expanded Functions, Dental Assisting programs).

## Relationship to the rest of the course reference material

This prototype is the **visual design system applied**. The underlying instructional architecture lives one level up in [`../`](../):

- Topics, modules, and hours: `/01-curriculum/REFERENCE-topics.md`, `REFERENCE-module-specs.md`
- Gradebook + rubric: `/02-assessments/`
- Plugins, completion rules, layout: `/03-moodle-build/`
- Pacing, Clinical Day, welcome copy: `/04-delivery/`

The brand spec at `/marketing/REFERENCE-brand-spec.md` uses the FIDA public-site palette (navy + bright teal gradient). The prototype here uses a slightly more reserved allied-health palette (navy + darker teal + compliance red). **Open decision:** which palette ownership prefers for the Moodle-facing experience — can align to either.
