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

1. `<html data-brand="<slug>">` (oppure `.brand-<slug>` su wrapper).
2. **Topbar** con `.ds-topbar` (dark navy fissa in alto):
   - `.ds-topbar__brand` con `<NOME>` + `<sup>AI+</sup>` + tag minore
   - `.ds-topbar__nav` con `.ds-topbar__cta` (pill cyan brand-soft con bordo nero) + `.ds-topbar__powered` ("powered by logotel")
3. **Eco rail** sotto la topbar (link a tutti i 9 brand, attivo con `data-active="1"`).
4. **Hero card** con `.ds-hero-card`:
   - `.ds-hero-card__eyebrow` (caps tracking-wide)
   - `.ds-hero-card__title` (MuseoModerno SemiBold uppercase, max 16ch)
   - `.ds-hero-card__sub` (Roboto)
   - `.ds-hero-card__pills` con 2-3 `.ds-pill` di status (`--cyan`, `--cream`, `--coral`, `--lime`, `--neutral`, `--brand`)
5. **Status row** sotto la hero: pill `.ds-pill--coral` "ON AIR" + label uppercase descrittivo.
6. **Big card** focus modulo principale con `.ds-big-card`:
   - thumbnail quadrata cyan a sinistra (`.ds-big-card__thumb`)
   - body con eyebrow code/status, titolo, descrizione
   - `.ds-button` "Apri prototipo →" sulla destra
7. **Section header** con `.ds-section-header` (titolo grande + descrizione + count moduli).
8. **Module grid** con `.ds-module-grid` di `.ds-module-card` (5-9 moduli, code "X1..X9", titolo uppercase, mini-desc, footer "approfondisci").
9. Eventuali `.ds-stat` per i numeri.

**Pattern fondamentale**: il sistema NON è "hero pieno colorato a tutto schermo".
È "card cyan rounded grandi su sfondo cream", **edge-to-edge ma con padding**, in
una composizione editoriale **a strati** (topbar / eco-rail / hero-card / big-card /
section-header / grid). Imitare il sito reference `willsell-gilt.vercel.app`.

Quando ti chiedono "una pagina umbrella" / "ecosystem map":

- Usa una topbar con `AI+ ECOSYSTEM<sup>9</sup>` e tag "Umbrella brand"
- Hero card con gradient diverso (mix di 2-3 brand soft) e H1 grande
- Section header "I 9 brand verticali" + count
- Grid 9-up di `.ds-badge` brand-specifici, ciascuno dentro `.brand-<slug>`
- CTA row in basso per linkare il prototipo navigazione

## Sistema di navigazione 2D (capitoli + insight)

C'è un prototipo in `examples/navigation-prototype.html`:

- **Verticale (snap)**: ogni capitolo = una `<section class="chapter">` di `100vh` dentro `.chapters` con `scroll-snap-type: y mandatory`.
- **Orizzontale (snap)**: dentro ogni capitolo, una `.insights__track` con `scroll-snap-type: x mandatory` per gli insight.
- **Cover ↔ Insights**: la chapter ha `data-expanded="0|1"`; con `1` la grid passa da `1fr 0fr` a `minmax(28rem, 33vw) 1fr` con curva spring `var(--ds-ease-spring)` e durata `var(--ds-dur-slow)` (720ms).
- **Rail anteprima**: `.rail` è un floating panel con i titoli degli insight, sempre visibile sul bordo destro della cover (collapsed) e diventa un indice statico quando il chapter è expanded.
- **Tastiera**: `↑/↓` cambia capitolo, `→` apre / next insight, `←` previous insight / chiude.
- **WebGL shader**: il `<canvas data-shader="<slug>">` dentro `.cover` ha un fragment shader plasma (FBM noise) che usa `--brand-soft` e `--brand` (in vec3 RGB 0..1, lookup in `SHADER_BRANDS`). Si disabilita con `prefers-reduced-motion: reduce`.

Per produzione, la stessa logica andrebbe portata in **GSAP + ScrollTrigger** (per
controllare timeline, parallax e linked animations) e **Three.js / react-three-fiber**
per shader piu' avanzati (bloom, distortion, glass, mesh).

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

## V2 / brand expansion (glass + 3D shape)

Da maggio 2026 il sistema ha una **seconda voce v2** che convive con la v1
(non la sostituisce). Sorgenti: `Brand direction/brand espanso/CREATIVE_STUDIO_BrandBoard.ai`
+ `Brand direction/assets/glass-logos/*.png` (entrambi nella cartella OneDrive
di lavoro — la cartella `Brand direction/` NON è nel repo).

**Tre ingredienti v2:**

1. **Glass badge** — `.ds-glass-badge`, pill rounded translucida con highlight
   superiore, brand-soft di fondo, soft shadow.
2. **3D shape brand-specific** — `.ds-glass-shape` con `<svg><use href="assets/shapes/sprite.svg#shape-<slug>"/></svg>`.
   Mapping fisso: creative-studio=square, jump=chair/J, hive=hexagon,
   willsell=T, dojo=ring, maindset=M-wave, leadai=E, changelab=Q,
   liveai-plus=plus. **Non scambiare le shape.**
3. **Glassmorphic surfaces** — `.ds-glass-card`, `.ds-glass-module`,
   `.ds-glass-button`, `.ds-glass-pill` con `backdrop-filter: blur()`,
   inset ring, drop shadow brand-aware.

**Setup pagina v2:**

```html
<html data-brand="creative-studio">
<link rel="stylesheet" href="styles/index.css" />
<link rel="stylesheet" href="styles/v2.css" />
<script src="scripts/glass-shape.js" defer></script>
```

`scripts/glass-shape.js` inietta lo sprite SVG inline (necessario perché
`<use href="external.svg#id"/>` non eredita CSS variables su tutti i browser).

**Quando usare v2 vs v1:**

- v2 = touchpoint marca/storia (cover, hero, landing, ecosystem map).
- v1 = pagine dense di testo / documentazione / dashboard moduli.
- v2 è additiva: la topbar dark, l'eco-rail, le pill di status, il
  section-header restano i pattern v1.

**Don't (v2-specifici):**

- Niente `.ds-glass-*` su body text lungo (blur degrada la leggibilità).
- Niente shape mischiate tra brand.
- Niente `--ds-glass-blur` sotto 12px.

File chiave: `tokens/glass.json`, `styles/v2.css`, `assets/shapes/`,
`scripts/glass-shape.js`, `examples/v2-*.html`, `docs/usage-v2.md`.

## Tono di voce per le copy generate

Italiano, diretto, evita gergo americano in copertina. Frasi corte.
Verbi all'imperativo per i titoli (`Trasforma`, `Allena`, `Produci`).
Non usare emoji nei titoli ufficiali. Powered-by Logotel è sempre
in lowercase.
