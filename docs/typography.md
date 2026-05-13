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

## Body — Roboto

- Sub heads, paragrafi, UI minute, micro-copy.
- Pesi: `300`, `400`, `500`, `700`.
- Vale per v1 e v2 (il brandboard 2026 propone Open Sans ma la
  convenzione del DS resta Roboto).
- CDN: `https://fonts.googleapis.com/css2?family=Roboto:wght@300..700&display=swap`

```css
body { font-family: "Roboto", system-ui, sans-serif; line-height: 1.65; }
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
