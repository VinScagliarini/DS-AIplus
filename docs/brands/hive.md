# HIVE

> Network di intelligenze, organizzato.

**Slug:** `hive` · **Hue:** amber

![Badge](../../assets/badges/hive.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#FDB84B` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#FAD08E` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#EA9003` | Per emphasis su sfondo light |
| `--brand-ink` | `#3A2E1B` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#181818` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #FAD08E 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #FAD08E 55%, #FDB84B 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #3A2E1B 0%, #181818 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="hive">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Network di intelligenze, organizzato.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Network di intelligenze, organizzato.
  </h1>
</header>
```

## Asset

- `assets/badges/hive.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/hive.png` — glass logo 3D
- `tokens/brands/hive.json` — tutti i token in formato design-tokens
- `styles/brands/hive.css` — custom property pronte all'uso

## Quando usare HIVE

`Network di intelligenze, organizzato.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
