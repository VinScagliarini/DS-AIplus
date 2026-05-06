# MAINDSET

> Il mindset operativo di chi adotta l'AI.

**Slug:** `maindset` · **Hue:** violet

![Badge](../../assets/badges/maindset.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#968CFF` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#BFB8FA` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#4230FF` | Per emphasis su sfondo light |
| `--brand-ink` | `#1B1740` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#0E0B2C` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #BFB8FA 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #BFB8FA 55%, #968CFF 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #1B1740 0%, #0E0B2C 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="maindset">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Il mindset operativo di chi adotta l'AI.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Il mindset operativo di chi adotta l'AI.
  </h1>
</header>
```

## Asset

- `assets/badges/maindset.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/maindset.png` — glass logo 3D
- `tokens/brands/maindset.json` — tutti i token in formato design-tokens
- `styles/brands/maindset.css` — custom property pronte all'uso

## Quando usare MAINDSET

`Il mindset operativo di chi adotta l'AI.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
