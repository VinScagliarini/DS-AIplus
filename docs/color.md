# Color system

## Modello a 3 livelli

1. **Neutrali condivisi** (`--ds-cream`, `--ds-ink`, `--ds-ink-muted`, ...) — uguali per tutti i brand.
2. **Token brand-aware** (`--brand`, `--brand-soft`, `--brand-deep`, `--brand-ink`, `--brand-ink-deep`) — assumono valori diversi a seconda del brand attivo (`data-brand="..."`).
3. **Gradient costruiti** (`--brand-gradient-badge`, `--brand-gradient-hero`, `--brand-gradient-ink-card`) — derivati dai token sopra, garantiscono coerenza tra slide hero, badge e card scure.

## Neutrali

| Token | Hex | Uso |
|---|---|---|
| `--ds-cream` | `#F7F6F3` | Sfondo pagina, top-left di ogni gradient badge |
| `--ds-ink` | `#0F0418` | Testo body massima leggibilità |
| `--ds-ink-soft` | `#1A0E2A` | Plum-black per surface dark |
| `--ds-ink-muted` | `#6B5B7A` | Testo secondario, eyebrow |
| `--ds-white` | `#FFFFFF` | Testo su superfici dark |

## Brand colors (per ciascuno dei 9 brand)

| Token | Tipo | Esempio per Creative Studio |
|---|---|---|
| `--brand-soft` | tint chiaro | `#F0BEF7` |
| `--brand` | saturated | `#D464F0` |
| `--brand-deep` | shade | `#B331E0` |
| `--brand-ink` | charcoal con undertone | `#1A0E2A` |
| `--brand-ink-deep` | quasi-nero | `#0F0418` |
| `--brand-glow` | rgba per shadow | `rgba(212,100,240,0.35)` |

Tutti i 9 valori sono in [`docs/brands.md`](./brands.md) e nei file
[`tokens/brands/*.json`](../tokens/brands).

## Gradient

Il gradient diagonale 135° è la **firma visiva** dell'ecosistema. Tutti i
badge partono da `#F7F6F3` (cream) e arrivano al colore brand soft.

```css
.badge {
  background: linear-gradient(135deg, #F7F6F3 0%, var(--brand-soft) 100%);
}
```

Per gli hero, l'angolo è 160° e la rampa attraversa cream → soft → primary:

```css
.hero {
  background: linear-gradient(160deg,
    #F7F6F3 0%,
    var(--brand-soft) 55%,
    var(--brand) 100%);
}
```

## Contrasto

- Su sfondi `--brand-soft` e `--brand`: usa `--brand-ink-deep` o `--ds-ink`.
- Su sfondi `--brand-ink` o `--brand-ink-deep`: usa `--ds-white`.
- Eyebrow e label secondarie: `--ds-ink-muted` su sfondi light.

## Glow / shadow

```css
.brand-card:hover {
  box-shadow: 0 24px 60px -12px var(--brand-glow);
}
```
