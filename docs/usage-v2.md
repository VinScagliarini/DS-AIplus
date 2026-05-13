# AI+ Ecosystem · V2 / Logotel AI+ Solutions — guida d'uso

La **v2** è un'estensione del design system, non una sostituzione.
La v1 (badge a gradient diagonale 135° su sfondo cream, hero card piatte,
module grid editoriale) resta valida. La v2 aggiunge un linguaggio
**glassmorphic + 3D shape** che fa emergere ciascun brand con una
forma distintiva.

> Sorgenti: `Brand direction/brand espanso/CREATIVE_STUDIO_BrandBoard.ai`
> + `Brand direction/assets/glass-logos/*.png` (vivono nella cartella
> OneDrive di lavoro, non nel repo).

## TL;DR

```html
<html data-brand="creative-studio">
<link rel="stylesheet" href="styles/index.css" />   <!-- v1 -->
<link rel="stylesheet" href="styles/v2.css" />       <!-- v2 -->
<script src="scripts/glass-shape.js" defer></script> <!-- inietta sprite -->
```

Per ogni brand: usa la stessa `data-brand="<slug>"` di v1. Sotto il cofano
v2 cambia solo i componenti `.ds-glass-*`. I componenti v1 continuano a
funzionare.

## I tre ingredienti

1. **Glass badge** (`.ds-glass-badge`) — versione "vetro liquido" del badge v1.
   Pill rounded bianca translucida con highlight superiore, brand-soft di
   fondo e drop shadow morbida.
2. **3D shape** (`.ds-glass-shape`) — una forma geometrica brand-specific,
   stilizzata in SVG (square, T, hexagon, ring, plus...). Si renderizza
   in `currentColor` = `var(--brand)`, con highlight bianco per evocare il
   vetro. Per logotel AI+ Solutions fotorealistiche, usa i PNG in
   `assets/glass-logos/<slug>.png`.
3. **Glassmorphic surface** (`.ds-glass-card`, `.ds-glass-module`,
   `.ds-glass-button`, `.ds-glass-pill`) — superfici translucide con
   `backdrop-filter: blur()`, `inset ring`, drop shadow brand-aware.

## Mappa shape → brand

| Slug              | Shape       | Hue         |
|-------------------|-------------|-------------|
| `creative-studio` | square      | magenta     |
| `jump`            | chair / J   | mint        |
| `hive`            | hexagon     | gold        |
| `willsell`        | T           | cyan        |
| `dojo`            | ring        | yellow      |
| `maindset`        | M-wave      | violet      |
| `leadai`          | E           | coral       |
| `reframing-lab`       | Q           | blue        |
| `liveai-plus`     | plus        | green       |

Definita in `tokens/glass.json#shape-of-brand` e nel sprite
`assets/shapes/sprite.svg` (symbol per ciascuno).

## Pattern componibili

### Lockup (badge + shape uno accanto all'altro)

```html
<div class="ds-glass-lockup">
  <div class="ds-glass-shape">
    <svg viewBox="0 0 240 240">
      <use href="assets/shapes/sprite.svg#shape-creative-studio"/>
    </svg>
  </div>
  <div class="ds-glass-badge">
    <div class="ds-glass-badge__wordmark">CREATIVE<br/>STUDIO</div>
    <div class="ds-glass-badge__footer">
      <span class="ds-glass-badge__aiplus">AI+</span>
      <span class="ds-glass-badge__powered">
        <span>powered by</span><span>logotel</span>
      </span>
    </div>
  </div>
</div>
```

> Lo script `scripts/glass-shape.js` (incluso con `defer`) inietta il
> sprite inline all'inizio del `<body>` così che `<use href="...#id"/>`
> erediti correttamente le CSS variables (necessario per il fill
> brand-aware).

### Hero v2 con lockup laterale

```html
<article class="ds-glass-hero">
  <div class="ds-glass-hero__body">
    <span class="ds-glass-hero__eyebrow">CREATIVE PRODUCTION · v2</span>
    <h1 class="ds-glass-hero__title">Creatività alla velocità degli algoritmi.</h1>
    <p class="ds-glass-hero__sub">…</p>
    <div class="ds-glass-hero__actions">
      <a class="ds-glass-button ds-glass-button--brand" href="#">CTA primaria →</a>
      <a class="ds-glass-button" href="#">CTA secondaria</a>
    </div>
  </div>
  <div class="ds-glass-hero__media">
    <div class="ds-glass-lockup">…</div>
  </div>
</article>
```

### Module grid glass

```html
<section class="ds-glass-module-grid">
  <a class="ds-glass-module" href="#">
    <div class="ds-glass-module__head">
      <span>CS · 02</span>
      <span class="ds-glass-module__icon">▭</span>
    </div>
    <h4 class="ds-glass-module__title">Static asset factory</h4>
    <p class="ds-glass-module__desc">…</p>
  </a>
</section>
```

## Token v2 (estratti da `tokens/glass.json`)

```css
--ds-glass-tint:        rgba(255, 255, 255, 0.58);
--ds-glass-tint-strong: rgba(255, 255, 255, 0.72);
--ds-glass-tint-soft:   rgba(255, 255, 255, 0.32);
--ds-glass-blur:        24px;
--ds-glass-ring:        inset 0 0 0 1px rgba(255, 255, 255, 0.65);
--ds-glass-shadow:      0 24px 60px -20px rgba(15, 4, 24, 0.30),
                        0 8px 18px -8px  rgba(15, 4, 24, 0.18);
--ds-glass-highlight:   linear-gradient(180deg, rgba(255,255,255,0.6) 0%, rgba(255,255,255,0) 55%);
--ds-radius-glass-card:  1.5rem;
--ds-radius-glass-badge: 1.1rem;
```

I token brand v1 (`--brand`, `--brand-soft`, `--brand-deep`, `--brand-glow`)
sono riutilizzati 1:1 — non rifaccio la palette.

## Do / Don't

✅ **Do**

- Usa la v2 per touchpoint "marca / storia": cover, hero, landing,
  pagina brand. Aggiunge dimensionalità senza distrarre.
- Mantieni la mappa shape → brand fissa. Lo square è di Creative Studio,
  l'esagono è di Hive — non scambiarli.
- Combina con i pattern v1: topbar dark, eco-rail, status pill,
  section-header. La v2 è additiva.
- Su sfondi pieni brand (`background: var(--brand)`), usa `.ds-glass-card`
  per garantire leggibilità del testo.

❌ **Don't**

- Non usare `.ds-glass-*` su pagine dense di testo. Il blur degrada
  la leggibilità del body lungo: in quel caso resta su v1.
- Non sovrapporre due shape diverse nello stesso lockup (es. badge
  Hive con shape Willsell).
- Non ridurre la `--ds-glass-blur` sotto 12px o il vetro diventa "sporco"
  senza leggersi come glass.
- Non sostituire MuseoModerno (display) né Roboto (body).

## Palette estesa Creative Studio (v2)

Estratta dal brandboard `CREATIVE_STUDIO_BrandBoard.ai`. Sovrascrive la
palette v1 SOLO quando l'`<html>` ha `data-ds-version="2"`.

| Step | Hex | Ruolo |
|---|---|---|
| `--brand-bg-start` | `#FDF6FB` | Off-white tinto magenta — base pagina |
| `--brand-soft`     | `#F6D4F3` | Lavender chiaro — card light, hover |
| `--brand`          | `#E76BF0` | Magenta primary — CTA, accenti, fill |
| `--brand-ink`      | `#2D1035` | Plum-black — headline su light |
| `--brand-ink-deep` | `#0D050F` | Quasi-nero — body text, surfaces dark |

Activazione:

```html
<html data-brand="creative-studio" data-ds-version="2">
```

> Le altre 8 palette espanse arriveranno quando saranno disponibili i
> brandboard dei rispettivi brand.

## Componenti dal brandboard

Tutti definiti in `styles/v2.css`, copy esatta dal `.ai`.

| Classe | Brandboard | Note |
|---|---|---|
| `.ds-glass-heading-card` | "Scegli cosa creare. Lui fa il resto." | Wordmark gigante sx + headline body dx, gradient brand-soft |
| `.ds-glass-carousel-card` | "PRODUCI CREATIVITÀ ALLA VELOCITÀ DEGLI ALGORITMI" | Portrait, headline con `.ds-glass-highlight`, dots, wordmark |
| `.ds-glass-stat-card` | "75% dei Designer e Videomaker..." | Numero + highlight, label, fonte, SVG area chart |
| `.ds-glass-image-card` | "UN SOLO PROMPT. UN WORKFLOW GUIDATO..." | Foto bg + overlay brand + headline con highlight + CTA pill |
| `.ds-glass-split-card` | "L'AI IMPARA IL TUO BRAND" | Foto landscape + caption + pill "Create something" overlap |
| `.ds-glass-hero-ink` | "Un editor AI che capisce il linguaggio naturale" | Hero dark con UI mockup laterale + lockup + CTA "Start creating" |
| `.ds-glass-nav` | Sidebar Overview/Features/Clients/Pricing/Help/About | Badge in cima + link list, active = pill gradient |
| Buttons v2 | 6 stati visivi | `--soft-light`, default, `--brand-fill`, `--brand-gradient`, `--outline`, `--ink`, `--icon` |
| Utility | text highlight inline | `.ds-glass-highlight` — span con bg `--ds-highlight-cream` (`#FBE0DE`) |

Vedi `examples/v2-creative-studio.html` per il render completo.

## Accessibility

- Tutti i componenti rispettano `prefers-reduced-motion: reduce`:
  niente transform su hover, niente rotation sulla shape.
- Il contrasto del testo nei glass card è verificato con
  `--brand-ink-deep` su background con `--ds-glass-tint-strong`
  (rapporto > 7:1 WCAG AAA).
- Le SVG hanno `role="img"` + `aria-label` sul wrapper di pagina.

## Browser support

- `backdrop-filter` è supportato in Chromium, Safari, Firefox
  (≥ FF103). Su browser legacy il fallback è un solid white tint
  ≈ 58% — il layout regge.
- `color-mix(in srgb, ...)` è supportato da Chromium 111, Safari 16.2,
  Firefox 113. Usato negli stage radial gradients. Su browser più
  vecchi, la sfumatura cade su `var(--ds-cream)`.

## File chiave

- `tokens/glass.json` — token v2 (estende `ecosystem.json`)
- `styles/v2.css` — componenti glassmorphic
- `assets/shapes/<slug>.svg` — 9 forme standalone
- `assets/shapes/sprite.svg` — sprite con tutti i `<symbol>`
- `assets/glass-logos/<slug>.png` — render fotorealistici (3D)
- `scripts/glass-shape.js` — injector dello sprite (deferred)
- `examples/v2-index.html` — vetrina umbrella v2
- `examples/v2-creative-studio.html` — vetrina full pilot

## Roadmap

- Declinare 8 vetrine brand v2 (sul modello di Creative Studio).
- Generare 9 SVG "premium" (mesh gradient + chromatic dispersion) da
  affiancare ai render PNG.
- Pattern dark-mode per glass surfaces (richiede ricalibrare ring + highlight).
- Tailwind preset esteso (`bg-glass`, `glass-card`, ecc.).
