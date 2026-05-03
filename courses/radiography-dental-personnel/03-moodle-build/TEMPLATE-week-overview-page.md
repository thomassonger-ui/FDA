# TEMPLATE — Week Overview Page

Use this template when creating any Week N Overview page (cmids 193–198 use this pattern). All Week Overviews follow the same structural skeleton.

## Required sections (in order)

1. **Hero** (gradient navy→teal, eyebrow + heading + subtitle)
2. **Time on task panel** (border-left teal, shows hours + activity breakdown)
3. **"Why this week matters"** content card
4. **"What you'll learn"** content card with 4 numbered Topic blocks
5. **Companion practice panel** (5px teal left rail) — links to 3 external-practice lessons
6. **Activity panel** (5px navy left rail) — describes the Knowledge Check
7. **Submission requirements** content card
8. **Compliance / AI policy** content card
9. **"Before you finish this week"** gradient panel — links to the Self-Reflection assignment
10. **Nav buttons** — prev (varies) + next (the week's first activity, e.g. Chapter Book)
11. **Footer attribution**

## Skeleton

```html
<div class="wtp-page" style="font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif; max-width: 860px; margin: 0 auto; line-height: 1.6; color: #1a1f2c;">

<!-- 1. Hero -->
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 14px; padding: 36px 40px; margin-bottom: 28px; color: white;">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #7EC9CD; font-weight: 600; margin-bottom: 12px;">{{Theory phase / Lab phase}} · Week {{N}}</div>
  <h1 style="font-family: Playfair Display, Georgia, serif; font-size: 32px; font-weight: 700; margin: 0 0 12px; color: white; line-height: 1.2;">{{Week title}}</h1>
  <p style="font-size: 16px; color: rgba(255,255,255,0.9); margin: 0; line-height: 1.5;">{{One-sentence subtitle on the week's focus}}</p>
</div>

<!-- 2. Time on task -->
<div style="background: #F5F7FA; border: 1px solid #E0E4EA; border-left: 5px solid #2D6F73; border-radius: 12px; padding: 20px 24px; margin-bottom: 22px; ...">
  <!-- Time breakdown -->
</div>

<!-- 3. Why this week matters -->
<div style="background: white; border: 1px solid #E0E4EA; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <h2 style="color: #1B365D; ...">Why this week matters</h2>
  <p>...</p>
</div>

<!-- 4. What you'll learn (4 Topics) -->
<div style="background: white; border: 1px solid #E0E4EA; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px;">
  <h2 style="color: #1B365D; ...">What you'll learn</h2>
  <!-- Topic 01-04 cards -->
</div>

<!-- 5. Companion practice panel (TEAL left rail) -->
<div style="background: white; border: 1px solid #E0E4EA; border-left: 5px solid #2D6F73; border-radius: 12px; padding: 28px 32px; margin-bottom: 18px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <div style="...">Companion practice</div>
  <h2>Three short interactive lessons before the Knowledge Check</h2>
  <p>...</p>
  <!-- 3 lesson cards each linking to a lesson page -->
</div>

<!-- 6. Activity panel (NAVY left rail) -->
<div style="background: #F5F7FA; border: 1px solid #E0E4EA; border-left: 5px solid #1B365D; border-radius: 12px; padding: 24px 28px; margin-bottom: 18px;">
  <h2 style="color: #1B365D; ...">Activity — Scenario-based knowledge check</h2>
  <!-- KC details -->
</div>

<!-- 7-8. Submission + Compliance + Theory note -->

<!-- 9. Before you finish this week (gradient panel, links to reflection) -->
<div style="background: linear-gradient(135deg, #2D6F73 0%, #1B365D 100%); border-radius: 14px; padding: 28px 32px; margin: 24px 0 20px; color: white;">
  <div style="...">Before you finish this week</div>
  <h2 style="...">Submit your Week {{N}} Self-Reflection</h2>
  <p>A 200-word individual reflection ...</p>
  <a href="https://fldentalassisting.moodlecloud.com/mod/assign/view.php?id={{REFLECTION_CMID}}" style="...">Open the reflection →</a>
  <p><em>Required for Final Exam unlock.</em></p>
</div>

<!-- 10. Nav buttons -->
<div style="display: flex; justify-content: space-between; ...">
  <a href="{{prev URL}}">← Previous {{label}}</a>
  <a href="{{next URL}}">Next up → {{label}}</a>
</div>

<!-- 11. Footer -->
<p style="text-align: center; color: #5A6B7C; font-size: 12px; ...">Designed by WorldTeachPathways™ (dba WorldTeachESL LLC).</p>

</div>
```

## Conventions

- **Topic count per week:** 4 (always — even if a Pressbook chapter has fewer headings, restructure the content to fit 4 topics so all weeks look uniform)
- **Companion practice cards:** 3 (the same 3 external lessons referenced in `02-assessments/REFERENCE-self-reflection-prompts.md`)
- **Nav buttons:** Overview's "Next up" must point to the first content activity of the same week (Book or first Lesson) — NOT to the next week's Overview. This was a course-wide bug that was fixed during the 2026-05-02 audit
