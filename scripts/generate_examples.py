#!/usr/bin/env python3
"""
Genera un esempio HTML per ogni brand (examples/<slug>.html) + index.html
umbrella, allineati al look del sito di reference (willsell-gilt.vercel.app):
topbar dark, hero card cyan, pill bordo nero, big-card con thumb,
section-header con count, module-grid.
"""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = json.loads((REPO / "tokens" / "index.json").read_text(encoding="utf-8"))
BRANDS_INFO = {b["slug"]: b for b in INDEX["brands"]}

# Sample copy per brand
COPY = {
    "jump": {
        "tag": "Pannello UX",
        "eyebrow": "ACTIVATION ENABLEMENT · POWERED BY LOGOTEL",
        "title": "Trasforma la tua attività in conoscenza azionabile.",
        "sub":   "JUMP raccoglie ciò che il tuo team sa, lo organizza, lo porta nel flusso di lavoro. Senza interrompere nessuno.",
        "pills": [("cyan", "1 Live"), ("cream", "12 In design"), ("neutral", "9 Da progettare")],
        "big_card": ("A0", "ONBOARDING ATTIVATION", "Setup in 7 step per importare il knowhow del team. Punto di partenza dell'enablement."),
        "modules": [
            ("A1", "Knowledge Capture", "Raccogli i casi d'uso ricorrenti dal team operativo."),
            ("A2", "Tagging & Map", "Indicizza per dominio, persona, deal stage."),
            ("A3", "Activation Feed", "Distribuisci insight nel flow del seller."),
            ("A4", "Replay", "Rivedi cosa ha funzionato, ripeti in scala."),
            ("A5", "Coach Loop", "Loop di feedback con il sales manager."),
        ],
        "stat": ("87%", "delle aziende ammette che la propria conoscenza non è azionabile"),
    },
    "hive": {
        "tag": "Network OS",
        "eyebrow": "NETWORK INTELLIGENCE · POWERED BY LOGOTEL",
        "title": "Network di intelligenze, organizzato.",
        "sub":   "HIVE connette i nodi del tuo ecosistema in un'unica memoria collettiva, interrogabile via AI.",
        "pills": [("cyan", "3 Live"), ("cream", "Beta partner"), ("neutral", "Multi-tenant")],
        "big_card": ("H0", "COMMAND DECK", "Vista unica sulle attività di tutti i nodi della tua rete. Quello che succede, succede qui."),
        "modules": [
            ("H1", "Node Directory", "Profilo capability di ogni nodo."),
            ("H2", "Signal Bus", "Eventi cross-rete in real-time."),
            ("H3", "Brief Composer", "Lancia richieste mirate ai nodi giusti."),
            ("H4", "Activity Map", "Heatmap delle interazioni."),
            ("H5", "Network Score", "Salute relazionale del network."),
        ],
        "stat": ("3x", "più velocità nel localizzare l'expertise giusta"),
    },
    "willsell": {
        "tag": "AI Sales Coach",
        "eyebrow": "AI SALES COACH · POWERED BY LOGOTEL",
        "title": "Allena i tuoi venditori. Migliora i risultati. Ogni giorno.",
        "sub":   "WILLSELL è il coach AI per la rete vendita: scenari reali, feedback istantaneo, metrica della crescita.",
        "pills": [("cyan", "Live"), ("cream", "Bozza HTML"), ("neutral", "30 Da progettare")],
        "big_card": ("W0", "SCENARIO ENGINE", "Genera scenari realistici sui prodotti del cliente. Allena. Misura."),
        "modules": [
            ("W1", "Scenario Library", "Casistiche per industry e ruolo."),
            ("W2", "Coach Loop", "Feedback puntuale per ogni call simulata."),
            ("W3", "Skill Map", "Le competenze chiave, monitorate."),
            ("W4", "Win Patterns", "Cosa fanno i top performer, codificato."),
            ("W5", "Manager Dash", "Cockpit per il sales leader."),
        ],
        "stat": ("75%", "dei sales leader accede ai tool di enablement meno di 5 volte a trimestre"),
    },
    "dojo": {
        "tag": "Continuous Training",
        "eyebrow": "CONTINUOUS TRAINING · POWERED BY LOGOTEL",
        "title": "Allenamento continuo, guidato dall'AI.",
        "sub":   "DOJO mantiene viva la pratica: micro-sessioni, simulazioni, review. Il sapere non si cristallizza, si esercita.",
        "pills": [("cyan", "Live"), ("cream", "Pilota Italgas"), ("lime", "M365 Copilot")],
        "big_card": ("D0", "DAILY DRILL", "10 minuti al giorno per restare allenati. Generati su misura per ogni profilo."),
        "modules": [
            ("D1", "Drill Generator", "Esercizi calibrati sul livello."),
            ("D2", "Streak Tracker", "Costanza misurata, gamification leggera."),
            ("D3", "Topic Map", "Le aree dove investire pratica."),
            ("D4", "Live Spar", "Sparring partner AI per il dialogo."),
            ("D5", "Review Coach", "Sintesi post-drill con plan."),
        ],
        "stat": ("4x", "retention della formazione rispetto al one-shot training"),
    },
    "creative-studio": {
        "tag": "Creative Production",
        "eyebrow": "CREATIVE PRODUCTION · POWERED BY LOGOTEL",
        "title": "Produci creatività alla velocità degli algoritmi.",
        "sub":   "CREATIVE STUDIO genera statiche, UGC e video cinematografici on-brand. Per ogni piattaforma. In secondi.",
        "pills": [("cyan", "Live"), ("cream", "Beta brand kit"), ("lime", "Veo 3 + Sora")],
        "big_card": ("C0", "BRAND KIT ENGINE", "L'AI assorbe il tuo brand. Ogni output è on-brand di default."),
        "modules": [
            ("C1", "Static Generator", "Statics per Meta, TikTok, Display."),
            ("C2", "UGC Studio", "Avatar e creator AI, senza shooting."),
            ("C3", "Cinematic", "Video text-to-video con Veo 3 / Sora."),
            ("C4", "Variant Engine", "+50 varianti in un pomeriggio."),
            ("C5", "Chat Editor", "Modifica ogni asset in linguaggio naturale."),
            ("C6", "Multi-Platform", "Adatta a 7 canali in un click."),
        ],
        "stat": ("+50", "varianti creative on-brand in un pomeriggio, pronte per il launch"),
    },
    "maindset": {
        "tag": "AI Culture OS",
        "eyebrow": "AI CULTURE · POWERED BY LOGOTEL",
        "title": "Il mindset operativo di chi adotta l'AI.",
        "sub":   "MAINDSET allinea cultura, capability e linguaggio comune perché l'AI diventi un modo di lavorare, non un tool tra altri.",
        "pills": [("cyan", "Live"), ("cream", "Pilot Logotel"), ("neutral", "120 fellows")],
        "big_card": ("M0", "COMMON GROUND", "Vocabolario condiviso, principi operativi, pattern d'uso."),
        "modules": [
            ("M1", "Belief Map", "Le convinzioni che bloccano o abilitano."),
            ("M2", "Practice Library", "I rituali AI-friendly da adottare."),
            ("M3", "Champion Track", "Identifica e attiva i primi adopter."),
            ("M4", "Pulse", "Misura culturale ricorrente."),
            ("M5", "Manifesto", "Il documento vivente del team."),
        ],
        "stat": ("68%", "delle iniziative AI fallisce per mancanza di mindset, non di tecnologia"),
    },
    "leadai": {
        "tag": "AI Lead Gen",
        "eyebrow": "AI LEAD GENERATION · POWERED BY LOGOTEL",
        "title": "Lead generation potenziata dall'AI.",
        "sub":   "LEADAI individua, qualifica e ingaggia il tuo prossimo cliente. Continuamente. In multilingua.",
        "pills": [("coral", "1 Live"), ("cream", "B2B SaaS"), ("neutral", "12 lingue")],
        "big_card": ("L0", "PROSPECT RADAR", "Sniffa segnali sui canali che contano e ti dice chi vale ora."),
        "modules": [
            ("L1", "Signal Watch", "Hiring, news, intent, social."),
            ("L2", "ICP Builder", "Profilo cliente ideale, vivente."),
            ("L3", "Qualifier", "Score automatico contestualizzato."),
            ("L4", "Outreach Multi", "Sequenze multicanale generate."),
            ("L5", "Reply Coach", "Aiuta il SDR a rispondere bene."),
        ],
        "stat": ("2.3x", "conversion rate sui lead inbound qualificati con LEADAI"),
    },
    "changelab": {
        "tag": "Change as Experiment",
        "eyebrow": "CHANGE AS EXPERIMENT · POWERED BY LOGOTEL",
        "title": "Cambiamento progettato come un esperimento.",
        "sub":   "CHANGELAB porta nel cambiamento organizzativo il rigore della sperimentazione: ipotesi, prototipi, evidenza.",
        "pills": [("cyan", "Live"), ("cream", "3 lab attivi"), ("lime", "Iteration 12")],
        "big_card": ("CL0", "LAB BOARD", "Da idea a ipotesi a prototipo. Il backlog del cambiamento."),
        "modules": [
            ("CL1", "Hypothesis Card", "Format leggero per dichiarare ipotesi."),
            ("CL2", "Probe Library", "Microsperimenti pronti."),
            ("CL3", "Evidence Log", "Cosa abbiamo imparato, datato."),
            ("CL4", "Decision Doc", "Dalla ipotesi alla decisione."),
            ("CL5", "Cycle Review", "Il rituale del lab."),
        ],
        "stat": ("12 sett.", "il ciclo medio per validare una nuova capability con CHANGELAB"),
    },
    "liveai-plus": {
        "tag": "Live Experience",
        "eyebrow": "LIVE EXPERIENCE · POWERED BY LOGOTEL",
        "title": "Eventi e live experience aumentati dall'AI.",
        "sub":   "LIVE AI+ trasforma ogni evento in un sistema vivo: orchestrazione, contenuti dinamici, follow-up personalizzato.",
        "pills": [("lime", "Live"), ("cream", "WeFest 2026"), ("neutral", "Multi-stage")],
        "big_card": ("LA0", "STAGE OS", "Backend dell'evento: scaletta, regia AI, monitor live."),
        "modules": [
            ("LA1", "Run-of-Show", "Scaletta dinamica, modificabile in tempo reale."),
            ("LA2", "Audience Pulse", "Sentiment vivo della sala."),
            ("LA3", "AI Recap", "Sintesi a fine talk per il sito."),
            ("LA4", "Follow-up", "Email personalizzata per ogni partecipante."),
            ("LA5", "Photo Hub", "Foto + tag automatico."),
        ],
        "stat": ("+40%", "engagement medio sugli eventi orchestrati con LIVE AI+"),
    },
}

ECOSYSTEM_NAV = ["jump", "hive", "willsell", "dojo", "creative-studio",
                 "maindset", "leadai", "changelab", "liveai-plus"]


def render_topbar(active: str) -> str:
    name = BRANDS_INFO[active]["name"]
    tag = COPY[active]["tag"]
    return f"""<header class="ds-topbar">
    <div class="ds-topbar__brand">
      {name}<sup>AI+</sup>
      <span class="ds-topbar__tag">{tag}</span>
    </div>
    <nav class="ds-topbar__nav">
      <a href="#" class="ds-topbar__cta">▭ Knowledge Explorer</a>
      <span class="ds-topbar__powered">powered by logotel</span>
    </nav>
  </header>"""


def render_brand_page(slug: str, brand_meta: dict) -> str:
    info = COPY[slug]
    name = brand_meta["name"]

    pills_html = "\n      ".join(
        f'<span class="ds-pill ds-pill--{kind}"><span class="ds-pill__dot"></span>{label}</span>'
        for kind, label in info["pills"]
    )

    big_eyebrow_code, big_title, big_desc = info["big_card"]

    modules_html = "\n        ".join(
        f"""<a href="#" class="ds-module-card">
          <div class="ds-module-card__head"><span>{code}</span><span class="ds-module-card__icon">●</span></div>
          <h3 class="ds-module-card__title">{title}</h3>
          <p class="ds-module-card__desc">{desc}</p>
          <div class="ds-module-card__footer">Approfondisci →</div>
        </a>"""
        for code, title, desc in info["modules"]
    )

    nav_links = "\n        ".join(
        f'<a href="./{s}.html" class="ds-eco-link" data-active="{1 if s == slug else 0}">{BRANDS_INFO[s]["name"]}</a>'
        for s in ECOSYSTEM_NAV
    )

    return f"""<!doctype html>
<html lang="it" data-brand="{slug}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{name} · {info['tag']} — AI+ Ecosystem · Logotel</title>
<meta name="description" content="{info['sub']}" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles/index.css" />
<style>
  body {{
    margin: 0;
    background: var(--ds-cream);
    color: var(--ds-ink);
    font-family: var(--ds-font-body);
  }}
  .ds-eco-rail {{
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    padding: 0.6rem clamp(1rem, 2vw, 1.5rem);
    background: var(--ds-paper);
    border-bottom: 1px solid var(--ds-line);
    font-size: 0.78rem;
  }}
  .ds-eco-link {{
    text-decoration: none;
    color: var(--ds-ink-muted);
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-weight: 600;
    transition: background 120ms, color 120ms;
  }}
  .ds-eco-link:hover {{ color: var(--ds-ink-deep); background: var(--ds-cream); }}
  .ds-eco-link[data-active="1"] {{ background: var(--brand-soft); color: var(--ds-ink-deep); }}
  .ds-on-air {{
    display: flex;
    align-items: center;
    gap: 0.85rem;
    margin: 1.25rem 0 0.5rem;
  }}
  .ds-on-air__label {{
    font-family: var(--ds-font-body);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: var(--ds-tracking-eyebrow);
    text-transform: uppercase;
    color: var(--ds-ink-muted);
  }}
</style>
</head>
<body>

  {render_topbar(slug)}

  <nav class="ds-eco-rail">
    <a href="./index.html" class="ds-eco-link" style="color: var(--ds-ink-deep);">↩ Ecosystem</a>
    {nav_links}
  </nav>

  <main class="ds-shell" style="display: grid; gap: 1.25rem; padding-top: 1.5rem;">

    <!-- HERO CARD -->
    <section class="ds-hero-card">
      <div class="ds-hero-card__eyebrow">{info['eyebrow']}</div>
      <h1 class="ds-hero-card__title">{info['title']}</h1>
      <p class="ds-hero-card__sub">{info['sub']}</p>
      <div class="ds-hero-card__pills">
        {pills_html}
      </div>
    </section>

    <div class="ds-on-air">
      <span class="ds-pill ds-pill--coral"><span class="ds-pill__dot"></span>ON AIR</span>
      <span class="ds-on-air__label">Moduli prototipati e navigabili</span>
    </div>

    <!-- BIG CARD -->
    <section class="ds-big-card">
      <div class="ds-big-card__thumb">{big_eyebrow_code}</div>
      <div class="ds-big-card__body">
        <div class="ds-big-card__eyebrow"><span>{big_eyebrow_code}</span> · <span>LIVE</span></div>
        <h2 class="ds-big-card__title">{big_title}</h2>
        <p class="ds-big-card__desc">{big_desc}</p>
      </div>
      <a href="#" class="ds-button">Apri prototipo <span class="ds-button__arrow">→</span></a>
    </section>

    <!-- MODULE GRID -->
    <header class="ds-section-header">
      <h2 class="ds-section-header__title">Moduli {name}</h2>
      <p class="ds-section-header__desc">L'area operativa del prodotto. Ogni modulo prototipato e navigabile.</p>
      <span class="ds-section-header__count">{len(info['modules'])} moduli</span>
    </header>

    <section class="ds-module-grid">
        {modules_html}
    </section>

    <!-- STAT -->
    <section style="margin-top: 3rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr)); gap: 2rem; align-items: center;">
      <div class="ds-stat">
        <div class="ds-stat__number">{info['stat'][0]}</div>
        <div class="ds-stat__label">{info['stat'][1]}</div>
      </div>
      <div style="font-family: var(--ds-font-display); font-size: clamp(1.25rem, 1.5vw, 1.6rem); line-height: 1.25; text-transform: uppercase; letter-spacing: -0.005em;">
        {name} è l'ecosistema operativo<br>per chi non aspetta.
      </div>
      <a href="#" class="ds-button ds-button--brand">Apri il prototipo <span class="ds-button__arrow">→</span></a>
    </section>

    <footer style="margin: 4rem 0 2rem; text-align: center; color: var(--ds-ink-muted); font-size: 0.8rem;">
      AI+ Ecosystem · {name} — design system di Logotel S.p.A.<br>
      MuseoModerno + Roboto · powered by logotel
    </footer>

  </main>

</body>
</html>
"""


def render_index() -> str:
    cards = []
    for slug in ECOSYSTEM_NAV:
        b = BRANDS_INFO[slug]
        cards.append(f"""
        <a href="./{slug}.html" class="brand-{slug}" style="text-decoration:none; display: grid; gap: 0.6rem;">
          <div class="ds-badge">
            <div class="ds-badge__wordmark">{b['name']}</div>
            <div class="ds-badge__footer">
              <div style="font-weight:600;">AI<sup>+</sup></div>
              <div class="ds-badge__powered"><span>powered by</span><span>logotel</span></div>
            </div>
          </div>
          <div style="font-family: var(--ds-font-body); font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ds-ink-muted); text-align: center;">{COPY[slug]['tag']}</div>
        </a>""")
    grid = "".join(cards)

    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>AI+ Ecosystem · Logotel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles/index.css" />
<style>
  body {{ margin: 0; background: var(--ds-cream); color: var(--ds-ink); font-family: var(--ds-font-body); }}
  .ds-topbar__brand sup {{ color: #A6F1F3; }}
  .umbrella {{ max-width: 92rem; margin: 0 auto; padding: clamp(1.5rem, 3vw, 3rem); }}
  .umbrella__hero {{
    border-radius: var(--ds-radius-card);
    background: linear-gradient(135deg, #F7F6F3 0%, #ECEEF0 50%, #BFB8FA 100%);
    padding: clamp(2rem, 4vw, 3.5rem);
    margin: 1.5rem 0 2.5rem;
  }}
  .umbrella__eyebrow {{
    font-size: var(--ds-fs-eyebrow); font-weight: 600; letter-spacing: var(--ds-tracking-eyebrow);
    text-transform: uppercase; color: var(--ds-ink-deep);
  }}
  .umbrella__title {{
    font-family: var(--ds-font-display); font-size: clamp(2.5rem, 5vw, 5rem);
    font-weight: 600; line-height: 1.0; letter-spacing: -0.015em;
    text-transform: uppercase; margin: 0.75rem 0 1rem; color: var(--ds-ink-deep);
  }}
  .umbrella__sub {{ font-size: 1.05rem; line-height: 1.6; max-width: 60ch; color: var(--ds-ink); }}
  .umbrella__grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(11rem, 1fr)); gap: 1.5rem; }}
  .umbrella__grid .ds-badge {{ width: 100%; aspect-ratio: 1/1; transition: transform 220ms var(--ds-ease-spring), box-shadow 220ms ease; }}
  .umbrella__grid a:hover .ds-badge {{ transform: translateY(-4px); box-shadow: 0 24px 60px -12px var(--brand-glow); }}
  .umbrella__cta-row {{
    display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; margin: 2.5rem 0;
    padding: 1.25rem clamp(1rem, 2.5vw, 1.75rem); border-radius: var(--ds-radius-card);
    background: var(--ds-paper); border: 1px solid var(--ds-line);
  }}
</style>
</head>
<body>

  <header class="ds-topbar" style="--brand-soft: #A6F1F3;">
    <div class="ds-topbar__brand">
      AI+ Ecosystem<sup>9</sup>
      <span class="ds-topbar__tag">Umbrella brand</span>
    </div>
    <nav class="ds-topbar__nav">
      <a href="./navigation-prototype.html" class="ds-topbar__cta">▭ Navigation prototype</a>
      <span class="ds-topbar__powered">powered by logotel</span>
    </nav>
  </header>

  <main class="umbrella">

    <section class="umbrella__hero">
      <div class="umbrella__eyebrow">UMBRELLA BRAND · POWERED BY LOGOTEL</div>
      <h1 class="umbrella__title">AI+ Ecosystem.<br>Nove brand, una grammatica.</h1>
      <p class="umbrella__sub">
        Tutti partono dallo stesso cream <code>#F7F6F3</code> e arrivano a un loro hue.
        Stessa tipografia (MuseoModerno + Roboto), stesso lockup AI+, stessa logica di gradient.
        Una specializzazione visibile per ogni dominio.
      </p>
    </section>

    <header class="ds-section-header">
      <h2 class="ds-section-header__title">I 9 brand verticali</h2>
      <p class="ds-section-header__desc">Ognuno ha la sua palette, il suo pitch, la sua pagina dedicata.</p>
      <span class="ds-section-header__count">{len(ECOSYSTEM_NAV)} brand</span>
    </header>

    <section class="umbrella__grid">
      {grid}
    </section>

    <div class="umbrella__cta-row">
      <span class="ds-pill ds-pill--cyan"><span class="ds-pill__dot"></span>NUOVO</span>
      <strong style="font-family: var(--ds-font-display); font-size: 1.1rem; text-transform: uppercase; letter-spacing: -0.005em;">Prototipo navigazione 2D</strong>
      <span style="color: var(--ds-ink-muted); font-size: 0.9rem;">scroll giù tra capitoli, scroll dx tra insight, cover che si rimpicciolisce con animazione spring</span>
      <a href="./navigation-prototype.html" class="ds-button" style="margin-left: auto;">Apri prototipo <span class="ds-button__arrow">→</span></a>
    </div>

    <footer style="text-align: center; color: var(--ds-ink-muted); font-size: 0.85rem; padding: 2rem 0 3rem;">
      Token · CSS · Tailwind preset · esempi HTML — repo: <code>VinScagliarini/DS-AIplus</code>
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
    (examples / "index.html").write_text(render_index(), encoding="utf-8")
    print("wrote examples/index.html (umbrella)")


if __name__ == "__main__":
    main()
