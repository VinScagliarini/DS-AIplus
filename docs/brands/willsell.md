# WILLSELL

> Coach AI per venditori.

**Slug:** `willsell` · **Hue:** cyan

![Badge](../../assets/badges/willsell.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#06CBD2` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#A6F1F3` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#037579` | Per emphasis su sfondo light |
| `--brand-ink` | `#152831` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#181818` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #A6F1F3 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #A6F1F3 55%, #06CBD2 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #152831 0%, #181818 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="willsell">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Coach AI per venditori.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Coach AI per venditori.
  </h1>
</header>
```

## Asset

- `assets/badges/willsell.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/willsell.png` — glass logo 3D
- `tokens/brands/willsell.json` — tutti i token in formato design-tokens
- `styles/brands/willsell.css` — custom property pronte all'uso

## Quando usare WILLSELL

`Coach AI per venditori.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
