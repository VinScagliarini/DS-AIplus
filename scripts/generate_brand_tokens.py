#!/usr/bin/env python3
"""
Genera i token JSON e CSS per ciascun brand dell'AI+ Ecosystem.

Dati sorgente:
- Gradient endpoint (BR del badge) campionato dal pacchetto AI+_ECOSYSTEM.ai
- Per JUMP e WILLSELL: palette completa a 5 step letta dalla brand-sheet
- Per gli altri brand: palette estrapolata via HSL dal soft color
"""
from __future__ import annotations

import colorsys
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TOKENS_DIR = REPO / "tokens" / "brands"
CSS_DIR = REPO / "styles" / "brands"
TOKENS_DIR.mkdir(parents=True, exist_ok=True)
CSS_DIR.mkdir(parents=True, exist_ok=True)

CREAM = "#F7F6F3"

# brand: (name, tagline, hue label, soft (badge BR), measured 5-step palette or None)
BRANDS = {
    "jump": {
        "name": "JUMP",
        "tagline": "Trasforma l'attività in conoscenza azionabile.",
        "hue_name": "mint",
        "soft":   "#BEF6D3",  # measured swatch 2
        "primary":"#56E3B0",  # measured swatch 3
        "ink":    "#31352E",  # measured swatch 4
        "ink_deep":"#181818",
    },
    "hive": {
        "name": "HIVE",
        "tagline": "Network di intelligenze, organizzato.",
        "hue_name": "amber",
        "soft":   "#FAD08E",
        "primary":"#FDB84B",
        "ink":    "#3A2E1B",
        "ink_deep":"#181818",
    },
    "willsell": {
        "name": "WILLSELL",
        "tagline": "Coach AI per venditori.",
        "hue_name": "cyan",
        "soft":   "#A6F1F3",
        "primary":"#06CBD2",
        "ink":    "#152831",
        "ink_deep":"#181818",
    },
    "dojo": {
        "name": "DOJO",
        "tagline": "Allenamento continuo guidato dall'AI.",  # ASCII 'AI' OK, no accents
        "hue_name": "yellow",
        "soft":   "#F9E590",
        "primary":"#FBD947",
        "ink":    "#33301A",
        "ink_deep":"#181818",
    },
    "creative-studio": {
        "name": "CREATIVE STUDIO",
        "tagline": "Creatività alla velocità degli algoritmi.",
        "hue_name": "magenta",
        "soft":   "#F0BEF7",
        "primary":"#D464F0",
        "ink":    "#1A0E2A",
        "ink_deep":"#0F0418",
    },
    "maindset": {
        "name": "MAINDSET",
        "tagline": "Il mindset operativo di chi adotta l'AI.",
        "hue_name": "violet",
        "soft":   "#BFB8FA",
        "primary":"#968CFF",
        "ink":    "#1B1740",
        "ink_deep":"#0E0B2C",
    },
    "leadai": {
        "name": "LEADAI",
        "tagline": "Lead generation potenziata dall'AI.",
        "hue_name": "coral",
        "soft":   "#F4ABA6",
        "primary":"#F2746F",
        "ink":    "#3A1A1A",
        "ink_deep":"#181818",
    },
    "changelab": {
        "name": "CHANGELAB",
        "tagline": "Cambiamento progettato come un esperimento.",
        "hue_name": "blue",
        "soft":   "#95B5FA",
        "primary":"#568BFF",
        "ink":    "#0F1B3A",
        "ink_deep":"#080F22",
    },
    "liveai-plus": {
        "name": "LIVE AI+",
        "tagline": "Eventi e live experience aumentati dall'AI.",
        "hue_name": "lime",
        "soft":   "#BBF0AD",
        "primary":"#95EC80",
        "ink":    "#1B331B",
        "ink_deep":"#0E1B0E",
    },
}


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    r, g, b = (max(0, min(255, round(c))) for c in rgb)
    return f"#{r:02X}{g:02X}{b:02X}"


def shift_lightness(hex_color: str, dl: float) -> str:
    r, g, b = (c / 255 for c in hex_to_rgb(hex_color))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0, min(1, l + dl))
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return rgb_to_hex((r2 * 255, g2 * 255, b2 * 255))


def glow_rgba(hex_color: str, alpha: float = 0.35) -> str:
    r, g, b = hex_to_rgb(hex_color)
    return f"rgba({r}, {g}, {b}, {alpha})"


def build_brand(slug: str, info: dict) -> dict:
    soft = info["soft"]
    primary = info["primary"]
    deep = shift_lightness(primary, -0.18)
    return {
        "name": info["name"],
        "slug": slug,
        "tagline": info["tagline"],
        "hue": info["hue_name"],
        "color": {
            "bg": {
                "start": {"value": CREAM, "type": "color"},
                "end":   {"value": soft,  "type": "color", "description": "Endpoint del gradient diagonale del badge"},
            },
            "soft":      {"value": soft,        "type": "color"},
            "primary":   {"value": primary,     "type": "color", "description": "Colore brand saturato, per accenti e fill"},
            "deep":      {"value": deep,        "type": "color", "description": "Versione piu' scura del primary, per emphasis"},
            "ink":       {"value": info["ink"],      "type": "color", "description": "Charcoal con undertone brand, per testo headline su sfondo light"},
            "ink-deep":  {"value": info["ink_deep"], "type": "color", "description": "Quasi-nero, per testo body massima leggibilita'"},
        },
        "gradient": {
            "badge": {
                "value": f"linear-gradient(135deg, {CREAM} 0%, {soft} 100%)",
                "type": "gradient",
            },
            "hero": {
                "value": f"linear-gradient(160deg, {CREAM} 0%, {soft} 55%, {primary} 100%)",
                "type": "gradient",
            },
            "ink-card": {
                "value": f"linear-gradient(180deg, {info['ink']} 0%, {info['ink_deep']} 100%)",
                "type": "gradient",
            },
        },
        "shadow": {
            "glow": {
                "value": f"0 24px 60px -12px {glow_rgba(primary, 0.35)}",
                "type": "shadow",
            }
        },
    }


def to_css(slug: str, brand: dict) -> str:
    c = brand["color"]
    return f""":root[data-brand="{slug}"], .brand-{slug} {{
  /* AI+ Ecosystem brand: {brand['name']} */
  --brand-name: "{brand['name']}";
  --brand-bg-start: {c['bg']['start']['value']};
  --brand-bg-end:   {c['bg']['end']['value']};
  --brand-soft:     {c['soft']['value']};
  --brand:          {c['primary']['value']};
  --brand-deep:     {c['deep']['value']};
  --brand-ink:      {c['ink']['value']};
  --brand-ink-deep: {c['ink-deep']['value']};
  --brand-glow:     {glow_rgba(c['primary']['value'], 0.35)};
  --brand-gradient-badge: {brand['gradient']['badge']['value']};
  --brand-gradient-hero:  {brand['gradient']['hero']['value']};
  --brand-gradient-ink-card: {brand['gradient']['ink-card']['value']};
}}
"""


def main() -> None:
    index = []
    for slug, info in BRANDS.items():
        brand = build_brand(slug, info)
        (TOKENS_DIR / f"{slug}.json").write_text(
            json.dumps(brand, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (CSS_DIR / f"{slug}.css").write_text(to_css(slug, brand), encoding="utf-8")
        index.append({
            "slug": slug,
            "name": brand["name"],
            "tagline": brand["tagline"],
            "primary": brand["color"]["primary"]["value"],
            "soft": brand["color"]["soft"]["value"],
            "tokens": f"tokens/brands/{slug}.json",
            "css": f"styles/brands/{slug}.css",
            "badge": f"assets/badges/{slug}.png",
            "glass": f"assets/glass-logos/{slug}.png",
        })
    (REPO / "tokens" / "index.json").write_text(
        json.dumps({"brands": index}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Generated {len(index)} brand token files in {TOKENS_DIR}")
    print(f"Generated {len(index)} brand CSS files in {CSS_DIR}")


if __name__ == "__main__":
    main()
