# TEMPLATE — External Practice Lesson Page

Used for the 18 lesson pages that link out to Confederation College Pressbook H5P activities (CC BY-NC-ND 4.0). Each lesson is a Page activity, not an Assignment.

## Required structure

1. **Hero** — eyebrow `Week N · Lesson · External Practice` + activity title + 1-sentence subtitle
2. **"Why this matters"** content card — single paragraph framing the relevance
3. **"What you'll do"** panel (5px teal left rail) — 4-step numbered list
4. **CTA panel** (gradient navy→teal) — single button "Open activity in Pressbook →"
5. **Attribution panel** (dashed border) — full CC BY-NC-ND 4.0 citation with chapter number
6. **Nav buttons** — prev (Book or previous lesson) + next (next lesson or KC)
7. **Footer attribution**

## Skeleton

```html
<div class="wtp-page" style="font-family: Inter, ...; max-width: 860px; margin: 0 auto; line-height: 1.6; color: #1a1f2c;">

<!-- Hero -->
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 14px; padding: 36px 40px; margin-bottom: 28px; color: white;">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #7EC9CD; font-weight: 600; margin-bottom: 12px;">Week {{N}} · Lesson · External Practice</div>
  <h1 style="font-family: Playfair Display, Georgia, serif; font-size: 30px; font-weight: 700; margin: 0 0 12px; color: white; line-height: 1.2;">{{Lesson Title}}</h1>
  <p style="font-size: 16px; color: rgba(255,255,255,0.9); margin: 0; line-height: 1.5;">{{H5P type, e.g. "An Image Hotspots activity that..."}} {{One-sentence learning outcome}}</p>
</div>

<!-- Why this matters -->
<div style="background: white; border: 1px solid #E0E4EA; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <h2 style="color: #1B365D; font-size: 20px; ...">{{Why-this-matters heading}}</h2>
  <p>{{Single paragraph connecting concept to clinical reality}}</p>
</div>

<!-- What you'll do -->
<div style="background: #F5F7FA; border-left: 5px solid #2D6F73; border-radius: 8px; padding: 24px 28px; margin-bottom: 20px;">
  <h2>What you'll do</h2>
  <ol>
    <li>Click the <strong>Open activity</strong> button to launch Chapter {{X.Y}} on Confederation College's Pressbook.</li>
    <li>Scroll to the <em>{{Activity name}}</em> activity ({{H5P type}}).</li>
    <li>{{Specific instruction for this H5P}}</li>
    <li>Return here and mark the lesson complete.</li>
  </ol>
</div>

<!-- CTA -->
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 12px; padding: 32px; margin-bottom: 20px; color: white; text-align: center;">
  <p style="margin: 0 0 16px;">Ready? Open the activity in a new tab.</p>
  <a href="{{Pressbook chapter URL}}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: white; color: #1B365D; padding: 14px 32px; border-radius: 8px; font-weight: 600; text-decoration: none;">Open activity in Pressbook →</a>
  <p style="margin: 14px 0 0; color: rgba(255,255,255,0.7); font-size: 12px;">Activity opens in a new tab. Approximately {{N}} minutes.</p>
</div>

<!-- Attribution -->
<div style="background: white; border: 1px dashed #B8C0CC; border-radius: 10px; padding: 20px 24px; margin-bottom: 20px;">
  <div style="font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: #5A6B7C; font-weight: 600; margin-bottom: 6px;">Attribution & license</div>
  <p style="margin: 0; color: #1a1f2c; font-size: 13px; line-height: 1.6;">Activity from <em>Radiography</em>, Confederation College, published on eCampus Ontario Pressbooks (2024). Chapter {{X.Y}} — {{Chapter title}}. Licensed <strong>CC BY-NC-ND 4.0</strong> (Attribution · NonCommercial · NoDerivatives). Used here under educational, non-commercial CE-program use; the source activity is not modified.</p>
</div>

<!-- Nav buttons + Footer -->
```

## Required activity settings

- **Activity type:** Page
- **Completion:** "Show activity as complete when conditions are met" — view required (`completionview`)
- **Visible:** Yes

## Pressbook chapter URL pattern
`https://ecampusontario.pressbooks.pub/de115radiography/chapter/{{slug}}/`

Slugs are stable across the Pressbook (verified during 2026-05-02 build). If a chapter is removed, only the linked-out lesson breaks — the rest of the course stays whole.
