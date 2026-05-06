# LIVE AI+

> Eventi e live experience aumentati dall'AI.

**Slug:** `liveai-plus` · **Hue:** lime

![Badge](../../assets/badges/liveai-plus.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#95EC80` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#BBF0AD` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#52E030` | Per emphasis su sfondo light |
| `--brand-ink` | `#1B331B` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#0E1B0E` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #BBF0AD 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #BBF0AD 55%, #95EC80 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #1B331B 0%, #0E1B0E 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="liveai-plus">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Eventi e live experience aumentati dall'AI.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Eventi e live experience aumentati dall'AI.
  </h1>
</header>
```

## Asset

- `assets/badges/liveai-plus.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/liveai-plus.png` — glass logo 3D
- `tokens/brands/liveai-plus.json` — tutti i token in formato design-tokens
- `styles/brands/liveai-plus.css` — custom property pronte all'uso

## Quando usare LIVE AI+

`Eventi e live experience aumentati dall'AI.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
