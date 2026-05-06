#!/usr/bin/env python3
"""
Genera un esempio HTML per ogni brand (examples/<slug>.html) + una
pagina umbrella examples/index.html con la griglia di tutti i 9 brand.

Ogni pagina brand mostra:
 - Hero con gradient brand
 - Badge replicato in HTML/CSS
 - Type specimen (display + body)
 - Palette a 5 swatch
 - Stat block reference
 - Ink card con CTA pill
 - Footer "powered by logotel"
"""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = json.loads((REPO / "tokens" / "index.json").read_text(encoding="utf-8"))
BRANDS_INFO = {b["slug"]: b for b in INDEX["brands"]}

# Sample copy per brand (placeholder pitch in linea con ciascun nome)
COPY = {
    "jump": {
        "eyebrow": "Activation enablement",
        "title": "Trasforma la tua attività in conoscenza azionabile.",
        "sub":   "JUMP raccoglie ciò che il tuo team sa, lo organizza, lo porta nel flusso di lavoro. Senza interrompere nessuno.",
        "stat":  ("87%", "delle aziende ammette che la propria conoscenza non è azionabile"),
        "cta":   "Scopri JUMP",
    },
    "hive": {
        "eyebrow": "Network intelligence",
        "title": "Network di intelligenze, organizzato.",
        "sub":   "HIVE connette i nodi del tuo ecosistema (persone, partner, fornitori) in un'unica memoria collettiva interrogabile via AI.",
        "stat":  ("3x", "più velocità nel localizzare l'expertise giusta"),
        "cta":   "Esplora HIVE",
    },
    "willsell": {
        "eyebrow": "AI sales coach",
        "title": "Allena i tuoi venditori. Migliora i risultati. Ogni giorno.",
        "sub":   "WILLSELL è il coach AI per la rete vendita: scenari reali, feedback istantaneo, metrica della crescita.",
        "stat":  ("75%", "dei sales leader accede ai tool di enablement meno di 5 volte a trimestre"),
        "cta":   "Avvia WILLSELL",
    },
    "dojo": {
        "eyebrow": "Continuous training",
        "title": "Allenamento continuo, guidato dall'AI.",
        "sub":   "DOJO mantiene viva la pratica: micro-sessioni, simulazioni, review. Il sapere non si cristallizza, si esercita.",
        "stat":  ("4x", "retention della formazione rispetto al one-shot training"),
        "cta":   "Entra nel DOJO",
    },
    "creative-studio": {
        "eyebrow": "Creative production",
        "title": "Produci creatività alla velocità degli algoritmi.",
        "sub":   "CREATIVE STUDIO genera statiche, UGC e video cinematografici on-brand. Per ogni piattaforma. In secondi.",
        "stat":  ("+50", "varianti creative on-brand in un pomeriggio, pronte per il launch"),
        "cta":   "Apri il CREATIVE STUDIO",
    },
    "maindset": {
        "eyebrow": "AI culture",
        "title": "Il mindset operativo di chi adotta l'AI.",
        "sub":   "MAINDSET allinea cultura, capability e linguaggio comune perché l'AI diventi un modo di lavorare, non un tool tra altri.",
        "stat":  ("68%", "delle iniziative AI fallisce per mancanza di mindset, non di tecnologia"),
        "cta":   "Avvia MAINDSET",
    },
    "leadai": {
        "eyebrow": "AI lead generation",
        "title": "Lead generation potenziata dall'AI.",
        "sub":   "LEADAI individua, qualifica e ingaggia il tuo prossimo cliente. Continuamente. In multilingua.",
        "stat":  ("2.3x", "conversion rate sui lead inbound qualificati con LEADAI"),
        "cta":   "Genera con LEADAI",
    },
    "changelab": {
        "eyebrow": "Change as experiment",
        "title": "Cambiamento progettato come un esperimento.",
        "sub":   "CHANGELAB porta nel cambiamento organizzativo il rigore della sperimentazione: ipotesi, prototipi, evidenza.",
        "stat":  ("12 sett.", "il ciclo medio per validare una nuova capability con CHANGELAB"),
        "cta":   "Avvia un lab",
    },
    "liveai-plus": {
        "eyebrow": "Live experience",
        "title": "Eventi e live experience aumentati dall'AI.",
        "sub":   "LIVE AI+ trasforma ogni evento in un sistema vivo: orchestrazione, contenuti dinamici, follow-up personalizzato.",
        "stat":  ("+40%", "engagement medio sugli eventi orchestrati con LIVE AI+"),
        "cta":   "Prova LIVE AI+",
    },
}


def render_brand_page(slug: str, brand_meta: dict) -> str:
    info = COPY[slug]
    name = brand_meta["name"]
    primary = brand_meta["primary"]
    soft = brand_meta["soft"]
    nav = "\n      ".join(
        f'<a href="./{s}.html" class="ds-eco-nav__link" data-active="{"1" if s == slug else "0"}">{BRANDS_INFO[s]["name"]}</a>'
        for s in BRANDS_INFO
    )

    return f"""<!doctype html>
<html lang="it" data-brand="{slug}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>AI+ {name} · Logotel</title>
<meta name="description" content="{info['sub']}" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles/index.css" />
<style>
  body {{
    font-family: var(--ds-font-body);
    margin: 0;
    background: var(--ds-cream);
    color: var(--brand-ink-deep);
  }}
  .ds-shell {{
    max-width: 1200px;
    margin: 0 auto;
    padding: clamp(1rem, 3vw, 2.5rem);
    display: grid;
    gap: clamp(1.5rem, 3vw, 2.5rem);
  }}
  .ds-eco-nav {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    padding: 0.75rem;
    background: var(--ds-cream);
    border-radius: var(--ds-radius-pill);
    box-shadow: var(--ds-shadow-card-soft);
    align-items: center;
    justify-content: center;
  }}
  .ds-eco-nav__home {{
    font-family: var(--ds-font-display);
    font-weight: 600;
    color: var(--ds-ink);
    text-decoration: none;
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
  }}
  .ds-eco-nav__link {{
    font-family: var(--ds-font-body);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--ds-ink-muted);
    text-decoration: none;
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    transition: background 120ms ease, color 120ms ease;
  }}
  .ds-eco-nav__link:hover {{ color: var(--brand-ink-deep); }}
  .ds-eco-nav__link[data-active="1"] {{
    background: var(--brand);
    color: var(--brand-ink-deep);
  }}
  .ds-grid-2 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
    gap: clamp(1rem, 2vw, 2rem);
    align-items: stretch;
  }}
  .ds-section-title {{
    font-family: var(--ds-font-display);
    font-size: var(--ds-fs-h3);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--ds-ink-muted);
    margin: 0 0 0.75rem;
  }}
  .ds-card-light {{
    background: var(--ds-white);
    border-radius: var(--ds-radius-card);
    padding: clamp(1.25rem, 2.5vw, 2rem);
    box-shadow: var(--ds-shadow-card-soft);
  }}
  .ds-typespec h2 {{ margin: 0; font-family: var(--ds-font-display); font-size: 4rem; line-height: 1; color: var(--brand-ink-deep); }}
  .ds-typespec p  {{ margin: 1rem 0 0; max-width: 60ch; line-height: 1.6; color: var(--ds-ink); }}
  .ds-footer {{
    text-align: center;
    color: var(--ds-ink-muted);
    font-size: 0.8rem;
    padding: 2rem 0 3rem;
  }}
</style>
</head>
<body>
<div class="ds-shell">

  <nav class="ds-eco-nav" aria-label="AI+ Ecosystem">
    <a class="ds-eco-nav__home" href="./index.html">AI+ Ecosystem</a>
    {nav}
  </nav>

  <!-- HERO -->
  <header class="ds-hero">
    <div class="ds-hero__eyebrow">{info['eyebrow']} · powered by Logotel</div>
    <h1 class="ds-hero__title">{info['title']}</h1>
    <p class="ds-hero__sub">{info['sub']}</p>
    <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
      <a href="#" class="ds-button">{info['cta']}</a>
      <a href="#" class="ds-button ds-button--ghost">Scopri il metodo</a>
    </div>
  </header>

  <!-- BADGE + STAT -->
  <section class="ds-grid-2">
    <div class="ds-card-light" style="display:grid; place-items:center;">
      <div class="ds-section-title">Brand badge</div>
      <div class="ds-badge">
        <div class="ds-badge__wordmark">{name}</div>
        <div class="ds-badge__footer">
          <div class="ds-badge__ai-mark">AI<sup>+</sup></div>
          <div class="ds-badge__powered">
            <span>powered by</span>
            <span>logotel</span>
          </div>
        </div>
      </div>
    </div>

    <div class="ds-card-light">
      <div class="ds-section-title">Stat hero</div>
      <div class="ds-stat">
        <div class="ds-stat__number">{info['stat'][0]}</div>
        <div class="ds-stat__label">{info['stat'][1]}</div>
      </div>
      <hr style="margin: 1.5rem 0; border: none; height: 1px; background: rgba(15,4,24,0.08);" />
      <div class="ds-section-title">Ink card</div>
      <div class="ds-ink-card">
        <div style="font-family: var(--ds-font-display); font-size: 1.6rem; line-height: 1.1; text-transform: uppercase; letter-spacing: -0.01em;">
          {name}
        </div>
        <p style="margin: 1rem 0 1.5rem; opacity: 0.8;">{info['sub']}</p>
        <a href="#" class="ds-button ds-button--soft">{info['cta']}</a>
      </div>
    </div>
  </section>

  <!-- TYPESPEC + PALETTE -->
  <section class="ds-grid-2">
    <div class="ds-card-light ds-typespec">
      <div class="ds-section-title">Type specimen</div>
      <h2>aAkK <span style="color: var(--brand)">aAkK</span></h2>
      <p style="font-family: var(--ds-font-display); font-size: 1.25rem; line-height: 1.4;">
        ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789
      </p>
      <p>
        <strong style="font-family: var(--ds-font-display);">MuseoModerno</strong> per headlines.
        <strong>Roboto</strong> per sub heads e paragrafi. Il display imposta la voce
        del brand, il body porta il carico di lettura.
      </p>
    </div>

    <div class="ds-card-light">
      <div class="ds-section-title">Palette</div>
      <div class="ds-swatches">
        <div class="ds-swatch" style="background: var(--ds-cream); color: var(--ds-ink);">{brand_meta['soft'].replace('#','#').upper()}</div>
        <div class="ds-swatch" style="background: var(--brand-soft); color: var(--ds-ink);">{soft.upper()}</div>
        <div class="ds-swatch" style="background: var(--brand); color: var(--ds-ink);">{primary.upper()}</div>
        <div class="ds-swatch" style="background: var(--brand-ink); color: var(--ds-white);">brand-ink</div>
        <div class="ds-swatch" style="background: var(--brand-ink-deep); color: var(--ds-white);">brand-ink-deep</div>
      </div>
    </div>
  </section>

  <footer class="ds-footer">
    AI+ Ecosystem · {name} — design system di Logotel S.p.A.<br>
    powered by logotel · MuseoModerno + Roboto
  </footer>

</div>
</body>
</html>
"""


def render_index(brands: list[dict]) -> str:
    cards = []
    for b in brands:
        slug = b["slug"]
        cards.append(f"""
        <a href="./{slug}.html" class="brand-{slug}" style="text-decoration:none;">
          <div class="ds-badge">
            <div class="ds-badge__wordmark">{b['name']}</div>
            <div class="ds-badge__footer">
              <div class="ds-badge__ai-mark">AI<sup>+</sup></div>
              <div class="ds-badge__powered">
                <span>powered by</span>
                <span>logotel</span>
              </div>
            </div>
          </div>
          <div style="margin-top: 0.75rem; text-align: center; font-family: var(--ds-font-body); font-size: 0.8rem; color: var(--ds-ink-muted);">{COPY[slug]['eyebrow']}</div>
        </a>""")

    grid = "".join(cards)
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>AI+ Ecosystem · Logotel</title>
<meta name="description" content="L'umbrella brand AI+ Ecosystem di Logotel: 9 brand verticali, un metodo, una grammatica." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles/index.css" />
<style>
  body {{
    font-family: var(--ds-font-body);
    margin: 0;
    background: var(--ds-cream);
    color: var(--ds-ink);
  }}
  .umbrella {{
    max-width: 1240px;
    margin: 0 auto;
    padding: clamp(2rem, 5vw, 5rem);
  }}
  .umbrella__header {{
    text-align: center;
    margin-bottom: clamp(2rem, 4vw, 4rem);
  }}
  .umbrella__eyebrow {{
    font-family: var(--ds-font-body);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--ds-ink-muted);
  }}
  .umbrella__title {{
    font-family: var(--ds-font-display);
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    line-height: 1.0;
    text-transform: uppercase;
    letter-spacing: -0.02em;
    margin: 0.5rem 0 1rem;
    color: var(--ds-ink);
  }}
  .umbrella__sub {{
    font-family: var(--ds-font-body);
    font-size: 1.05rem;
    line-height: 1.6;
    max-width: 60ch;
    margin: 0 auto;
    color: var(--ds-ink);
    opacity: 0.8;
  }}
  .umbrella__grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
    gap: clamp(1rem, 2vw, 2rem);
  }}
  .umbrella__grid .ds-badge {{
    width: 100%;
    aspect-ratio: 1 / 1;
    transition: transform 200ms ease, box-shadow 200ms ease;
  }}
  .umbrella__grid a:hover .ds-badge {{
    transform: translateY(-4px);
    box-shadow: 0 24px 60px -12px var(--brand-glow);
  }}
  .umbrella__footer {{
    margin-top: clamp(2rem, 4vw, 4rem);
    text-align: center;
    color: var(--ds-ink-muted);
    font-size: 0.85rem;
    line-height: 1.6;
  }}
  .umbrella__footer code {{
    font-family: var(--ds-font-mono);
    background: rgba(15,4,24,0.05);
    padding: 0.15rem 0.4rem;
    border-radius: 6px;
    color: var(--ds-ink);
  }}
</style>
</head>
<body>
<main class="umbrella">

  <header class="umbrella__header">
    <div class="umbrella__eyebrow">Umbrella brand · powered by Logotel</div>
    <h1 class="umbrella__title">AI+ Ecosystem</h1>
    <p class="umbrella__sub">
      Nove brand verticali costruiti sulla stessa grammatica: badge a gradient diagonale,
      tipografia MuseoModerno + Roboto, palette a 5 step, lockup AI+.
      Una coerenza visibile, una specializzazione per ogni dominio.
    </p>
  </header>

  <div class="umbrella__grid">
    {grid}
  </div>

  <footer class="umbrella__footer">
    Clicca un badge per la pagina dedicata · ogni brand espone le sue
    custom property in <code>styles/brands/&lt;slug&gt;.css</code>.<br>
    Token JSON: <code>tokens/brands/&lt;slug&gt;.json</code> · Tailwind preset: <code>tailwind/preset.js</code>.
  </footer>

</main>
</body>
</html>
"""


def main():
    examples = REPO / "examples"
    examples.mkdir(exist_ok=True)
    for slug, b in BRANDS_INFO.items():
        out = examples / f"{slug}.html"
        out.write_text(render_brand_page(slug, b), encoding="utf-8")
        print("wrote", out.relative_to(REPO))

    (examples / "index.html").write_text(render_index(list(BRANDS_INFO.values())), encoding="utf-8")
    print("wrote examples/index.html (umbrella)")


if __name__ == "__main__":
    main()
