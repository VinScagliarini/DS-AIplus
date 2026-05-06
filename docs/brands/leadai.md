# LEADAI

> Lead generation potenziata dall'AI.

**Slug:** `leadai` · **Hue:** coral

![Badge](../../assets/badges/leadai.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#F2746F` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#F4ABA6` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#EA231B` | Per emphasis su sfondo light |
| `--brand-ink` | `#3A1A1A` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#181818` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #F4ABA6 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #F4ABA6 55%, #F2746F 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #3A1A1A 0%, #181818 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="leadai">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Lead generation potenziata dall'AI.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Lead generation potenziata dall'AI.
  </h1>
</header>
```

## Asset

- `assets/badges/leadai.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/leadai.png` — glass logo 3D
- `tokens/brands/leadai.json` — tutti i token in formato design-tokens
- `styles/brands/leadai.css` — custom property pronte all'uso

## Quando usare LEADAI

`Lead generation potenziata dall'AI.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
