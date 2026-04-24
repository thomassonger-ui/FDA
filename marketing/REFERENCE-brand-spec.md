# FIDA Moodle — Brand & Theme Spec

**Source of truth:** fldentalassisting.com (April 2026 audit)
**Applies to:** Moodle LMS theming for Florida Institute of Dental Assisting — Radiography for Dental Personnel, Expanded Functions, and future CE courses.

---

## 1. Color Tokens

| Role | Token | Value | Where to use |
|---|---|---|---|
| Primary navy | `--fida-navy` | `#012D50` | Site header, top nav bar, H1/H2, footer background |
| Navy dark | `--fida-navy-dark` | `#023C6A` | Hover states for navy surfaces |
| Teal primary (CTA) | `--fida-teal` | `#40CDD0` | Primary buttons, active nav, progress bar fill |
| Teal light | `--fida-teal-light` | `#9EFCFF` | Top of CTA gradient, focus ring |
| Teal hover | `--fida-teal-hover` | `#48C3C6` | Button hover |
| Teal accent | `--fida-teal-accent` | `#72E6E9` | Sub-menu hover, badge backgrounds |
| Aqua wash | `--fida-aqua-wash` | `#F4FBFB` | Alternating section bands, card backgrounds |
| Body text | `--fida-text` | `#4F4F4F` | Paragraph body, secondary headings |
| Ink | `--fida-ink` | `#111111` | H3 and below, form labels |
| White | `--fida-white` | `#FFFFFF` | Secondary button background, card surface |

**Signature CTA gradient** (use only on primary buttons):
```css
background: linear-gradient(0deg, #40CDD0 0%, #9EFCFF 100%);
```

---

## 2. Typography

Load via Google Fonts in Moodle theme `<head>`:
```html
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Inter:wght@400;500;700&family=Roboto:wght@500&display=swap" rel="stylesheet">
```

| Element | Font | Weight | Treatment |
|---|---|---|---|
| H1 (course title, hero) | Oswald | 600 | Uppercase, letter-spacing -1px to -2px, 60–95px |
| H2 (section headers) | Oswald | 500 | Uppercase, navy |
| H3 (lesson titles) | Oswald | 500 | Sentence case acceptable |
| Body, paragraphs | Inter | 400 | Line-height 1.6 |
| Lead/subhead | Inter | 700 | Slightly larger than body |
| Sub-nav, breadcrumbs | Roboto | 500 | — |
| Buttons | Inter | 700 | Uppercase, letter-spacing 1px |

---

## 3. Logo Usage

- Source SVG: `https://fldentalassisting.com/wp-content/themes/fida/library/images/logo.svg`
- Alt text: "Florida Institute of Dental Assisting" (**not** "fida" as currently on the public site — fix this for a11y/SEO in Moodle).
- Minimum clear space: equal to the x-height of the logotype on all sides.
- On navy backgrounds: use the SVG as-is (it already reads on navy).
- On white/aqua-wash: use as-is.
- Never stretch, recolor, or place on busy photography without a 50% black overlay.

---

## 4. Button System

**Primary (Apply / Enroll / Start Course):**
```css
background: linear-gradient(0deg, #40CDD0 0%, #9EFCFF 100%);
color: #012D50;
font: 700 14px/1 Inter, sans-serif;
text-transform: uppercase;
letter-spacing: 1px;
padding: 16px 32px;
border-radius: 4px;
border: none;
```
Hover: flatten gradient to solid `#48C3C6`.

**Secondary (Schedule Tour / Download Syllabus):**
```css
background: #FFFFFF;
color: #012D50;
border: 2px solid #012D50;
```
Hover: background `#012D50`, color `#FFFFFF`.

**Tertiary/link:** navy text, teal underline on hover.

---

## 5. Moodle-Specific Theme Mapping

Assuming the Boost theme as the base (Moodle 4.x):

| Moodle region | Apply |
|---|---|
| `#page-header` / navbar | Navy `#012D50`, Oswald nav items white, teal underline on active |
| Course card title | Oswald 500, navy |
| Course card CTA | Primary teal gradient button |
| Progress bar fill | `#40CDD0` on `#F4FBFB` track |
| Completion checkmark | Teal `#40CDD0` |
| Activity icons | Navy on aqua-wash circle |
| Block headers (right rail) | Oswald 500 navy on white |
| Footer | Navy `#012D50`, Inter white text |
| Alerts — info | Aqua-wash bg, navy text |
| Alerts — success | Teal `#40CDD0` bg, navy text |
| Alerts — warning | Keep Moodle default amber (brand lacks a warning color) |

---

## 6. Voice & Tone (for course copy)

Match public-site voice: second-person, career-change friendly, aspirational-practical.

**Do:**
- "Start your new career today."
- "Become a valuable member of a dental healthcare team."
- "Discover a rewarding career."
- Short sentences. Active verbs. Florida/Jacksonville when relevant.

**Don't:**
- "Students will be able to…" (academic voice)
- Jargon without definition on first use
- Long compound sentences

---

## 7. Trust-Signal Upgrades (gap-fill)

The public homepage omits accreditation/regulatory badges. Inside Moodle, lean in:

- Radiography course header should cite **FAC 64B5-9.011** and **Florida Board of Dentistry** compliance.
- Module footer: *"This course satisfies Florida Administrative Code 64B5-9.011 requirements for dental personnel radiography training."*
- Certificate of completion: include FIDA logo, course name, FAC reference, clock hours, date.

---

## 8. Don'ts

- Don't introduce new brand colors outside this palette.
- Don't use any font other than Oswald / Inter / Roboto.
- Don't apply the teal gradient to non-CTA elements (dilutes the primary action).
- Don't use stock imagery of generic "students at computers" — prefer real FIDA classroom/team photos when available (request from Dr. Hall / Debbie).

---

**Questions to confirm before finalizing the Moodle theme:**
1. Confirm FIDA has a high-res logo.svg or ai file — the web SVG may rasterize poorly in certificate PDFs.
2. Confirm whether branded photography exists beyond the Dr. Hall team photo.
3. Confirm accreditation language for the course footer (FAC 64B5-9.011 verbatim vs. summarized).
