# Build Instructions — 5-Page Demo in Moodle Sandbox

Target: Radiography Foundations section inside the Sandbox course
URL: https://fldentalassisting.moodlecloud.com/course/view.php?id=14

Total time: ~25 minutes if images are pre-uploaded.

## Before you start

1. Log into Moodle as an editing teacher or admin.
2. Turn on **Edit mode** (toggle top-right of course page).
3. Decide which Section/Topic inside the Sandbox course this demo lives in — create a fresh one named "Radiography Foundations — Demo" so it doesn't collide with real content.

## For each of the 5 Pages

Repeat this flow, using the 5 HTML files in this folder in order:

1. In the target section click **Add an activity or resource**.
2. Choose **Page**.
3. **Name** the page per the table below.
4. **Description:** 1 sentence matching the page (shown on the course homepage under the Page link).
5. Scroll to **Page content**. Click the **`<>` (HTML source)** button — this is critical. Pasting into the visual editor will mangle the styles.
6. Paste the full contents of the corresponding `moodle-pageN-*.html` file.
7. Click `<>` again to return to visual mode and preview.
8. **Display options** → set "Display page name" on; "Display page description" off.
9. Save and display.

| # | Moodle Page name | Paste file |
|---|---|---|
| 1 | `01 · Section Landing` | `moodle-page1-landing.html` |
| 2 | `02 · Lesson — X-Ray Tube Anatomy` | `moodle-page2-module.html` |
| 3 | `03 · Knowledge Check (Practice)` | `moodle-page3-knowledge-check.html` |
| 4 | `04 · Clinical Competency` | `moodle-page4-clinical.html` |
| 5 | `05 · Resources & Wrap` | `moodle-page5-resources.html` |

## After all 5 are created — wire up the navigation

The snippets use placeholder URLs like `[[MOODLE_URL_LESSON_PAGE]]`. Replace them with the real Page URLs:

1. Open each created Page in a new tab and copy its URL.
2. Edit each Page's HTML and find-replace the placeholders:
   - Page 1 → `[[MOODLE_URL_LESSON_PAGE]]` = URL of Page 2
   - Page 2 → `[[MOODLE_URL_LANDING]]` = URL of Page 1 · `[[MOODLE_URL_KNOWLEDGE_CHECK]]` = URL of Page 3
   - Page 3 → `[[MOODLE_URL_LESSON]]` = URL of Page 2 · `[[MOODLE_URL_CLINICAL]]` = URL of Page 4 · `[[MOODLE_URL_GRADED_QUIZ]]` = URL of your Moodle Quiz activity (once created)
   - Page 4 → `[[MOODLE_URL_KNOWLEDGE_CHECK]]` = URL of Page 3 · `[[MOODLE_URL_RESOURCES]]` = URL of Page 5
   - Page 5 → `[[MOODLE_URL_LANDING]]` = URL of Page 1 · `[[MOODLE_URL_MODULE_02]]` = URL of next module (or a placeholder anchor) · plus the resource `[[MOODLE_URL_*]]` placeholders (point to uploaded PDFs, videos, H5P activities once those exist)
3. For resource placeholders (PDFs, videos): either upload the files to Moodle as File/URL resources and link them, or leave the placeholder text `[[...]]` visible for the demo — ownership will understand these represent actual content once the course is fully populated.

## Common issues

**Styles didn't apply.** You pasted into the visual editor instead of the HTML source. Switch to `<>` and re-paste.

**Fonts look wrong (default serif).** MoodleCloud may strip the Google Fonts `<link>` tag. If so, fonts will degrade gracefully to system sans-serif, which still looks professional. If ownership wants the exact fonts, add the `<link>` to the theme's custom CSS at site level.

**Inline styles don't render.** MoodleCloud's default ATTO editor sometimes strips inline `style=` attributes on save. If you see this, switch the course's default text editor to TinyMCE or the newer Moodle 4 editor via Site admin → Plugins → Text editors. Alternatively, keep the HTML clean by saving and re-editing in HTML source mode only.

**Image placeholders.** The video block in Page 2 is a placeholder — replace with a real `<video>` embed or Moodle media filter link once video content is filmed.

## For the leadership pitch

You don't actually need to build all 5 in Moodle to pitch ownership. Open `demo-prototype.html` directly in Chrome on a laptop and walk them through the 5 pages using the tab nav at the top. That's faster, looks the same, and doesn't require any Moodle login.

Use the Moodle build when you're ready to stand up the shell as a template for the real course.
