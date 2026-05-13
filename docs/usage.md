# Usage

## Tre modi di consumare il design system

### 1. Vanilla HTML/CSS (più semplice, zero build)

```html
<!doctype html>
<html lang="it" data-brand="creative-studio">
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="path/to/ai-plus-ecosystem-ds/styles/index.css">
</head>
<body>
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">creative production · powered by Logotel</div>
    <h1 class="ds-hero__title">Produci creatività alla velocità degli algoritmi.</h1>
    <p class="ds-hero__sub">CREATIVE STUDIO genera statiche, UGC e video on-brand.</p>
  </header>
</body>
</html>
```

Per cambiare brand basta modificare l'attributo `data-brand` (`jump`,
`hive`, `willsell`, `dojo`, `creative-studio`, `maindset`, `leadai`,
`reframing-lab`, `liveai-plus`).

### 2. Tailwind preset

`tailwind.config.{js,ts}`:

```js
import preset from "ai-plus-ecosystem-ds/tailwind/preset.js";

export default {
  presets: [preset],
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
};
```

Componente:

```tsx
export function CreativeStudioHero() {
  return (
    <div data-brand="creative-studio">
      <header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
        <p className="font-body text-sm uppercase tracking-widest opacity-70">
          creative production · powered by Logotel
        </p>
        <h1 className="font-display text-display uppercase tracking-tight">
          Produci creatività alla velocità degli algoritmi.
        </h1>
      </header>
    </div>
  );
}
```

### 3. Solo design tokens (JSON)

Importali in qualunque toolchain di design (Figma Variables, Style
Dictionary, Theo, ecc.):

```js
import ecosystem from "ai-plus-ecosystem-ds/tokens/ecosystem.json";
import creativeStudio from "ai-plus-ecosystem-ds/tokens/brands/creative-studio.json";
```

Schema: vedi [`docs/color.md`](./color.md) e [`docs/typography.md`](./typography.md).

## Scaffolding di una nuova pagina brand

```bash
# Copia un esempio esistente come base
cp examples/creative-studio.html examples/<nuova-pagina>.html

# Cambia data-brand sul tag <html>
# Modifica i contenuti
```

Oppure rigenera tutto da `scripts/generate_examples.py` aggiungendo una
voce in `COPY` e in `BRANDS_INFO`.

## Aggiungere un brand

1. Aggiungi la voce in `scripts/generate_brand_tokens.py` (slug, nome, soft, primary, ink, ink_deep, tagline)
2. Esegui: `python3 scripts/generate_brand_tokens.py`
3. Aggiungi la voce in `scripts/generate_examples.py:COPY`
4. Esegui: `python3 scripts/generate_examples.py && python3 scripts/generate_brand_docs.py`
5. Includi il nuovo CSS in `styles/index.css`

## Componenti disponibili

| Classe | Cosa fa |
|---|---|
| `.ds-hero` | Hero pieno con gradient brand 160° |
| `.ds-badge` | Card 1:1 con gradient 135°, wordmark, lockup AI+ |
| `.ds-ink-card` | Card scura con gradient verticale brand-ink |
| `.ds-button` / `.ds-button--soft` / `.ds-button--ghost` | Pill button |
| `.ds-stat` | Numero gigante + label |
| `.ds-swatches` / `.ds-swatch` | Palette display verticale |
| `.ds-ecosystem-grid` | Griglia 9-up dei badge brand |
| `.ds-display` / `.ds-h1`...`.ds-h3` / `.ds-body` / `.ds-eyebrow` / `.ds-label` | Tipografia semantica |
