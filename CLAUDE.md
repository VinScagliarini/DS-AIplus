# Istruzioni per AI tools

Questo file dà a un LLM (Claude Code, Cursor, Claude.ai con repo loader,
ecc.) il contesto sufficiente a generare nuovo materiale visivo coerente
con il design system **AI+ Ecosystem** di Logotel.

## Identità del sistema

- Umbrella brand: **AI+ Ecosystem** (powered by Logotel).
- 9 brand verticali, slug:
  `jump`, `hive`, `willsell`, `dojo`, `creative-studio`, `maindset`,
  `leadai`, `changelab`, `liveai-plus`.
- Tutti condividono: badge a gradient diagonale 135°, tipografia
  MuseoModerno (display) + Roboto (body), lockup `AI+` e `powered by
  logotel`, palette a 5 step con cream condiviso `#F7F6F3` come
  punto di partenza.

## Come selezionare un brand

Imposta l'attributo `data-brand="<slug>"` sull'elemento radice (o su un
wrapper). Le custom property `--brand-*` si aggiornano di conseguenza:

```html
<html data-brand="creative-studio">
```

In React/Tailwind: usa la classe `.brand-<slug>` come wrapper.

## Token canonici da rispettare

```css
/* Neutrali (tutti i brand) */
--ds-cream:     #F7F6F3;
--ds-ink:       #0F0418;
--ds-ink-soft:  #1A0E2A;
--ds-ink-muted: #6B5B7A;

/* Brand-aware (cambiano per ciascuno) */
--brand;          /* saturated */
--brand-soft;     /* tint chiaro - usato come endpoint del gradient badge */
--brand-deep;     /* shade per emphasis */
--brand-ink;      /* charcoal con undertone brand */
--brand-ink-deep; /* quasi-nero */
--brand-glow;     /* rgba per shadow */
```

Tabella valori per brand: `tokens/index.json` e `tokens/brands/<slug>.json`.

## Cosa NON fare

- Non mescolare hue di brand diversi nella stessa vista (es. badge HIVE
  con palette WILLSELL).
- Non sostituire MuseoModerno / Roboto con altri font.
- Non cambiare l'angolo del gradient badge: deve restare **135°** (top-left
  → bottom-right).
- Non usare `--brand` su testo body lungo: usa `--brand-ink-deep` per
  garantire leggibilità. `--brand` va su accenti, link, fill, CTA.
- Non rimuovere il lockup `AI+` né `powered by logotel` dai badge.

## Cosa GENERARE bene

Quando ti chiedono "una pagina per <brand>", produci:

1. `<html data-brand="<slug>">` o `<div className="brand-<slug>">` come wrapper.
2. Hero con `.ds-hero` (gradient brand 160°), `.ds-hero__eyebrow`,
   `.ds-hero__title` (MuseoModerno uppercase), `.ds-hero__sub`.
3. Una `.ds-badge` o un asset da `assets/badges/<slug>.png`.
4. CTA con `.ds-button` (oppure `.ds-button--ghost` per secondaria).
5. Eventuali `.ds-stat` per mostrare numeri grandi.
6. Sezioni `.ds-ink-card` quando serve contrasto su fondo light.

Quando ti chiedono "una pagina umbrella" / "ecosystem map":

- Usa `.ds-ecosystem-grid` con 9 `.ds-badge` brand-specifici, ciascuno
  dentro `.brand-<slug>`. Fondo `--ds-cream`. Titolo MuseoModerno uppercase.

## File chiave

- `tokens/ecosystem.json` — schema condiviso
- `tokens/brands/*.json` — token per brand
- `styles/index.css` — entry CSS unico (basta linkare questo)
- `tailwind/preset.js` — preset Tailwind (con `bg-brand-hero`, `text-brand-ink-deep`, ecc.)
- `examples/index.html` — pagina umbrella di esempio
- `examples/<slug>.html` — pagina esempio per brand
- `docs/usage.md` — pattern d'uso completi

## Quando estendi il sistema

Per aggiungere un brand: vedi sezione "Aggiungere un brand" in
`docs/usage.md`. Lo script `scripts/generate_brand_tokens.py` è
l'unico punto in cui si dichiarano i 5 colori brand; tutti i CSS
e i JSON sono derivati da lì.

## Quando ti chiedono varianti dark mode

Per ora il sistema è "light first" (il pacchetto originale è quasi
interamente su sfondo cream). Per dark, sovrascrivi a livello pagina:

```css
html[data-theme="dark"] {
  --ds-cream: var(--brand-ink-deep);
  --ds-ink:   #FFFFFF;
  --ds-ink-soft: var(--brand-ink);
}
```

Mantieni i gradient hero così come sono (sono già pensati per terminare
sul brand color saturato e leggono bene su entrambe le superfici).

## Tono di voce per le copy generate

Italiano, diretto, evita gergo americano in copertina. Frasi corte.
Verbi all'imperativo per i titoli (`Trasforma`, `Allena`, `Produci`).
Non usare emoji nei titoli ufficiali. Powered-by Logotel è sempre
in lowercase.
