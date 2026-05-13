# Typography

L'ecosistema AI+ usa **due famiglie**, niente terze.

## Display — MuseoModerno

- Pesi disponibili: `300` (Light) → `700` (Bold). Variabile.
- Uso: tutti gli headline, eyebrow uppercase, label, lockup `AI+`.
- Ottimale: `font-weight: 500` con `letter-spacing: -0.02em`, uppercase.
- File locale: [`fonts/MuseoModerno-VariableFont_wght.ttf`](../fonts/)
- CDN: `https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&display=swap`

```css
.headline {
  font-family: "MuseoModerno", system-ui, sans-serif;
  font-weight: 500;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  line-height: 1.0;
}
```

## Body — Roboto (v1) · Open Sans (v2)

- Sub heads, paragrafi, UI minute, micro-copy.
- **v1**: Roboto — pesi `300`, `400`, `500`, `700`.
- **v2 / brand expansion**: Open Sans (vedi `tokens/glass.json`), come
  da `CREATIVE_STUDIO_BrandBoard.ai`.
- CDN Roboto: `https://fonts.googleapis.com/css2?family=Roboto:wght@300..700&display=swap`
- CDN Open Sans: `https://fonts.googleapis.com/css2?family=Open+Sans:wght@300..800&display=swap`

```css
/* v1 */
body { font-family: "Roboto", system-ui, sans-serif; line-height: 1.65; }

/* v2 (su pagine con styles/v2.css linkato) */
body { font-family: var(--ds-font-body-v2); line-height: 1.65; }
```

## Type scale

I token sono fluidi (`clamp()`) per scalare senza media query.

| Ruolo | Token CSS | Valore |
|---|---|---|
| Display hero | `--ds-fs-display` | `clamp(3rem, 6vw + 1rem, 6.5rem)` |
| H1 | `--ds-fs-h1` | `clamp(2.25rem, 3.5vw + 1rem, 4rem)` |
| H2 | `--ds-fs-h2` | `clamp(1.75rem, 2vw + 1rem, 2.75rem)` |
| H3 | `--ds-fs-h3` | `clamp(1.25rem, 1vw + 1rem, 1.75rem)` |
| Body | `--ds-fs-body` | `1rem` |
| Small | `--ds-fs-small` | `0.875rem` |
| Caption | `--ds-fs-caption` | `0.75rem` |

## Classi semantiche pronte

```html
<h1 class="ds-display">Hero headline</h1>
<h2 class="ds-h1">Section title</h2>
<p class="ds-body">Paragrafo standard</p>
<span class="ds-eyebrow">eyebrow · powered by Logotel</span>
```

Vedi [`styles/typography.css`](../styles/typography.css) per la
definizione completa.
