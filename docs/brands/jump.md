# JUMP

> Trasforma l'attività in conoscenza azionabile.

**Slug:** `jump` · **Hue:** mint

![Badge](../../assets/badges/jump.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `#56E3B0` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `#BEF6D3` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `#1FBE84` | Per emphasis su sfondo light |
| `--brand-ink` | `#31352E` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `#181818` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: linear-gradient(135deg, #F7F6F3 0%, #BEF6D3 100%);

/* Hero (160°) */
background: linear-gradient(160deg, #F7F6F3 0%, #BEF6D3 55%, #56E3B0 100%);

/* Ink card (verticale) */
background: linear-gradient(180deg, #31352E 0%, #181818 100%);
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="jump">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">Trasforma l'attività in conoscenza azionabile.</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    Trasforma l'attività in conoscenza azionabile.
  </h1>
</header>
```

## Asset

- `assets/badges/jump.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/jump.png` — glass logo 3D
- `tokens/brands/jump.json` — tutti i token in formato design-tokens
- `styles/brands/jump.css` — custom property pronte all'uso

## Quando usare JUMP

`Trasforma l'attività in conoscenza azionabile.` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
