# REFERENCE — WTP Design System (Moodle pages)

The WorldTeachPathways design system applied to every Moodle page in this course. Use this for any new page so the look stays consistent.

---

## Tokens

### Typography
- **Body:** `Inter, -apple-system, BlinkMacSystemFont, sans-serif`
- **Headings:** `'Playfair Display', Georgia, serif`

### Color palette
| Token | Hex | Usage |
|---|---|---|
| Navy | `#1B365D` | Primary heading color, hero gradient start |
| Teal | `#2D6F73` | Accent color, hero gradient end, panel accents |
| Light teal | `#7EC9CD` | Hero eyebrow color, accent on dark backgrounds |
| Cool gray border | `#E0E4EA` | Card borders |
| Panel | `#F5F7FA` | Light panel background |
| Body text | `#1a1f2c` | Default body text |
| Muted text | `#5A6B7C` | Secondary text, footers, labels |

### Hero gradient
`linear-gradient(135deg, #1B365D 0%, #2D6F73 100%)` — used on every page hero, navy → teal diagonal.

---

## Component patterns

### 1. Hero (every page)
```html
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 14px; padding: 36px 40px; margin-bottom: 28px; color: white;">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #7EC9CD; font-weight: 600; margin-bottom: 12px;">{{Section}} · {{Page Type}}</div>
  <h1 style="font-family: Playfair Display, Georgia, serif; font-size: 32px; font-weight: 700; margin: 0 0 12px; color: white; line-height: 1.2;">{{Page Title}}</h1>
  <p style="font-size: 16px; color: rgba(255,255,255,0.9); margin: 0; line-height: 1.5;">{{One-sentence subtitle}}</p>
</div>
```

### 2. Content card (white, neutral)
```html
<div style="background: white; border: 1px solid #E0E4EA; border-radius: 12px; padding: 28px 32px; margin-bottom: 20px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <h2 style="color: #1B365D; font-size: 20px; font-weight: bold; font-family: Playfair Display, Georgia, serif; margin: 0 0 12px;">{{Heading}}</h2>
  <p style="margin: 0; color: #1a1f2c; font-size: 15px; line-height: 1.65;">{{Body text}}</p>
</div>
```

### 3. Expectations panel (5px navy left rail)
```html
<div style="background: #F5F7FA; border-left: 5px solid #1B365D; border-radius: 8px; padding: 24px 28px; margin-bottom: 20px;">
  <h2 style="color: #1B365D; font-size: 18px; font-weight: bold; font-family: Playfair Display, Georgia, serif; margin: 0 0 10px;">{{Heading}}</h2>
  <p style="margin: 0; color: #1a1f2c; font-size: 15px; line-height: 1.65;">{{Body text}}</p>
</div>
```

### 4. Companion practice / Lesson list panel (5px teal left rail)
```html
<div style="background: white; border: 1px solid #E0E4EA; border-left: 5px solid #2D6F73; border-radius: 12px; padding: 28px 32px; margin-bottom: 18px; box-shadow: 0 1px 2px rgba(20,30,55,0.04);">
  <div style="font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: #2D6F73; font-weight: 600; margin-bottom: 8px;">Companion practice</div>
  <h2 style="color: #1B365D; font-size: 22px; font-weight: bold; font-family: Playfair Display, Georgia, serif; margin: 0 0 12px;">{{Heading}}</h2>
  <p style="margin: 0 0 16px; color: #1a1f2c; font-size: 15px; line-height: 1.65;">{{Intro text}}</p>
  <!-- repeating lesson card -->
  <a href="{{lesson URL}}" style="display: block; background: #F5F7FA; border: 1px solid #E0E4EA; border-radius: 10px; padding: 16px 20px; text-decoration: none; color: #1a1f2c;">
    <div style="font-size: 11px; letter-spacing: 1px; text-transform: uppercase; color: #2D6F73; font-weight: 600; margin-bottom: 4px;">{{Lesson 1 · Type}}</div>
    <div style="font-size: 16px; color: #1B365D; font-weight: 600; margin-bottom: 4px;">{{Lesson Title}}</div>
    <div style="font-size: 13px; color: #5A6B7C;">{{One-line description}}</div>
  </a>
</div>
```

### 5. Path-forward / CTA panel (gradient navy→teal)
```html
<div style="background: linear-gradient(135deg, #1B365D 0%, #2D6F73 100%); border-radius: 12px; padding: 32px; margin-bottom: 20px; color: white; text-align: center;">
  <p style="margin: 0 0 16px; font-size: 16px; color: rgba(255,255,255,0.95); line-height: 1.5;">{{Setup line}}</p>
  <a href="{{URL}}" style="display: inline-block; background: white; color: #1B365D; padding: 14px 32px; border-radius: 8px; font-weight: 600; text-decoration: none; font-size: 14px; letter-spacing: 0.3px;">{{Button label}} →</a>
</div>
```

### 6. Attribution panel (dashed border)
```html
<div style="background: white; border: 1px dashed #B8C0CC; border-radius: 10px; padding: 20px 24px; margin-bottom: 20px;">
  <div style="font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: #5A6B7C; font-weight: 600; margin-bottom: 6px;">Attribution & license</div>
  <p style="margin: 0; color: #1a1f2c; font-size: 13px; line-height: 1.6;">{{Attribution text}}</p>
</div>
```

### 7. Nav buttons (prev / next)
```html
<div style="display: flex; justify-content: space-between; align-items: stretch; gap: 16px; margin: 32px 0 16px;">
  <a href="{{prev URL}}" style="flex: 1; background: white; border: 1px solid #E0E4EA; border-radius: 10px; padding: 18px 22px; text-decoration: none; color: #1a1f2c;">
    <div style="font-size: 11px; color: #5A6B7C; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; margin-bottom: 4px;">← Previous</div>
    <div style="font-size: 15px; color: #1B365D; font-weight: 600;">{{prev label}}</div>
  </a>
  <a href="{{next URL}}" style="flex: 1; background: white; border: 1px solid #E0E4EA; border-radius: 10px; padding: 18px 22px; text-decoration: none; color: #1a1f2c; text-align: right;">
    <div style="font-size: 11px; color: #5A6B7C; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; margin-bottom: 4px;">Next up →</div>
    <div style="font-size: 15px; color: #1B365D; font-weight: 600;">{{next label}}</div>
  </a>
</div>
```

### 8. Footer attribution (every page)
```html
<p style="text-align: center; color: #5A6B7C; font-size: 12px; margin: 32px 0 8px; font-style: italic;">Designed by WorldTeachPathways™ (dba WorldTeachESL LLC).</p>
```

---

## Critical caveat — TinyMCE editing in Moodle 5.x

When editing Page activity HTML via Chrome JS (or any external automation), setting `textarea[name="page[text]"].value` **directly is NOT sufficient**. The TinyMCE iframe editor (`id_page_ifr`) pushes its content back over the textarea on submit, reverting the change.

**Correct flow:**
```js
const ed = window.tinymce.get('id_page');
ed.setContent(newHtml);
ed.save();                                 // sync iframe → textarea
document.querySelector('button[name="submitbutton2"]').click();
```

**Other gotchas:**
- The dollar-sign character (`$`) in JS-evaluated strings can trigger Chrome MCP's "cookie/query string" content blocker on inspection — encode/strip via `charCodeAt` when reading suspect content
- Section reordering: use `core_courseformat_update_course` AJAX with `action: 'cm_move'` and `targetcmid` (places target BEFORE the targetcmid). Cross-section moves use `targetsectionid` instead. The action requires at least one cmid already in the destination section, so move one cmid first if the destination is empty
