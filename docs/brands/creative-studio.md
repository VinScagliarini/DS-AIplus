# CREATIVE STUDIO

> Creatività alla velocità degli algoritmi.

**Slug:** `creative-studio` · **Hue:** magenta

![Badge](../../assets/badges/creative-studio.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#D464F0` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#F0BEF7` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#B916E2` | Per emphasis su sfondo light |
| `--brand-ink` | `#1A0E2A` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#0F0418` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #F0BEF7 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #F0BEF7 55%, #D464F0 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #1A0E2A 0%, #0F0418 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="creative-studio">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Creatività alla velocità degli algoritmi.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Creatività alla velocità degli algoritmi.
  </h1>
</header>
```

## Asset

- `assets/badges/creative-studio.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/creative-studio.png` — glass logo 3D
- `tokens/brands/creative-studio.json` — tutti i token in formato design-tokens
- `styles/brands/creative-studio.css` — custom property pronte all'uso

## Quando usare CREATIVE STUDIO

`Creatività alla velocità degli algoritmi.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
