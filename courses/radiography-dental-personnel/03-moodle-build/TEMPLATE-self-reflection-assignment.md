# TEMPLATE — Self-Reflection Assignment

Each weekly Self-Reflection (cmids 231–236) is an Assignment activity, not a Page. The instructions live in the assignment's intro/description; students submit via online text.

## Required activity settings

| Setting | Value |
|---|---|
| Activity type | Assignment |
| Submission type | Online text (file upload disabled) |
| Word count enforcement | None (instructor returns submissions under 200 words for revision) |
| Completion | "Show activity as complete when conditions are met" + `completionsubmit` (auto-complete on submission) |
| Grade | None / no grade type — activity is engagement-gate only, not graded toward course total |

## Description structure

1. **Hero** — eyebrow `Week N · Self-Reflection`, heading "Connect this week to your practice", subtitle
2. **3 prompts panel** (5px teal left rail, ordered list)
3. **Submission requirements panel** (light gray)

## Skeleton

```html
<div style="font-family: Inter, ...; max-width: 860px; margin: 0 auto; line-height: 1.6; color: #1a1f2c;">

<!-- Hero -->
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 14px; padding: 28px 32px; margin-bottom: 22px; color: white;">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #7EC9CD; font-weight: 600; margin-bottom: 10px;">Week {{N}} · Self-Reflection</div>
  <h2 style="font-family: Playfair Display, Georgia, serif; font-size: 26px; font-weight: 700; margin: 0 0 10px; color: white;">Connect this week to your practice</h2>
  <p style="font-size: 15px; color: rgba(255,255,255,0.9); margin: 0;">A 200-word minimum reflection on {{week topics}}. Write in your own voice — this is about your clinical practice, not the textbook.</p>
</div>

<!-- 3 Prompts -->
<div style="background: white; border: 1px solid #E0E4EA; border-left: 5px solid #2D6F73; border-radius: 12px; padding: 24px 28px; margin-bottom: 18px;">
  <h3 style="color: #1B365D; ...">Respond to all three prompts</h3>
  <ol>
    <li><strong>{{Prompt 1 — applied/practice}}</strong></li>
    <li><strong>{{Prompt 2 — toughest concept + plan}}</strong></li>
    <li><strong>{{Prompt 3 — specific application}}</strong></li>
  </ol>
</div>

<!-- Submission Requirements -->
<div style="background: #F5F7FA; border: 1px solid #E0E4EA; border-radius: 10px; padding: 18px 22px; margin-bottom: 18px;">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #2D6F73; font-weight: 600; margin-bottom: 8px;">Submission requirements</div>
  <ul>
    <li><strong>Minimum 200 words</strong>, total across all three prompts.</li>
    <li>Write in your own voice. AI-generated reflections will be returned ungraded.</li>
    <li>Submit as <strong>online text</strong> directly in Moodle below.</li>
    <li>Marked complete on submission.</li>
  </ul>
</div>

</div>
```

## Prompt design rules

- All three prompts must be **week-specific** — never reuse a prompt verbatim across weeks
- Prompt 1: applied/personal-practice angle (what changes in your operatory)
- Prompt 2: metacognition (which concept was hardest, plan to master)
- Prompt 3: specific scenario application

See `02-assessments/REFERENCE-self-reflection-prompts.md` for the canonical prompt set actually used in the live course.
