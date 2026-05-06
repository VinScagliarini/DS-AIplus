#!/usr/bin/env python3
"""Genera docs/brands/<slug>.md con la spec sintetica di ciascun brand."""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BRANDS = json.loads((REPO / "tokens" / "index.json").read_text(encoding="utf-8"))["brands"]
DOCS = REPO / "docs" / "brands"
DOCS.mkdir(parents=True, exist_ok=True)


def render(brand: dict) -> str:
    slug = brand["slug"]
    full = json.loads((REPO / "tokens" / "brands" / f"{slug}.json").read_text(encoding="utf-8"))
    color = full["color"]
    grad = full["gradient"]

    return f"""# {brand['name']}

> {brand['tagline']}

**Slug:** `{slug}` · **Hue:** {full['hue']}

![Badge](../../assets/badges/{slug}.png)

## Token chiave

| Token | Valore | Uso |
|---|---|---|
| `--brand` | `{color['primary']['value']}` | Colore brand saturato. Fill principale, accenti, link attivi |
| `--brand-soft` | `{color['soft']['value']}` | Versione tenue. Sfondi card, hover, badge |
| `--brand-deep` | `{color['deep']['value']}` | Per emphasis su sfondo light |
| `--brand-ink` | `{color['ink']['value']}` | Charcoal con undertone brand. Testo headline su light |
| `--brand-ink-deep` | `{color['ink-deep']['value']}` | Quasi-nero per body |

## Gradient

```css
/* Badge (135°) */
background: {grad['badge']['value']};

/* Hero (160°) */
background: {grad['hero']['value']};

/* Ink card (verticale) */
background: {grad['ink-card']['value']};
```

## Uso rapido

```html
<!-- Imposta il brand sull'<html> o su qualsiasi wrapper -->
<html data-brand="{slug}">
  <link rel="stylesheet" href="styles/index.css" />
  ...
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">eyebrow · powered by Logotel</div>
    <h1 class="ds-hero__title">{brand['tagline']}</h1>
  </header>
  ...
</html>
```

```jsx
// Tailwind preset esposto in tailwind/preset.js
<header className="bg-brand-hero text-brand-ink-deep p-16 rounded-card">
  <h1 className="font-display text-display uppercase tracking-tight">
    {brand['tagline']}
  </h1>
</header>
```

## Asset

- `assets/badges/{slug}.png` — badge AI+ (1:1, 616x616)
- `assets/glass-logos/{slug}.png` — glass logo 3D
- `tokens/brands/{slug}.json` — tutti i token in formato design-tokens
- `styles/brands/{slug}.css` — custom property pronte all'uso

## Quando usare {brand['name']}

`{brand['tagline']}` — questo brand serve i casi d'uso che richiedono questo
posizionamento specifico. Per tutto il resto dell'ecosistema, vedi [`../brands.md`](../brands.md).
"""


def main():
    for b in BRANDS:
        out = DOCS / f"{b['slug']}.md"
        out.write_text(render(b), encoding="utf-8")
        print("wrote", out.relative_to(REPO))


if __name__ == "__main__":
    main()
