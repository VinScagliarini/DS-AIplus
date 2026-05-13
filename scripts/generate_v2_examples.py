#!/usr/bin/env python3
"""
Genera examples/v2-<slug>.html per i 9 brand: stessi moduli, palette
differenziata. Copy per brand definita in CONTENT (sotto). Palette
letta da tokens/brands/<slug>.json.

Run:
    python3 scripts/generate_v2_examples.py
"""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INDEX = json.loads((REPO / "tokens" / "index.json").read_text(encoding="utf-8"))
BRANDS_INFO = {b["slug"]: b for b in INDEX["brands"]}

# Foto brand-aware (originali da Pexels.com, CC0). Path relativi a
# examples/v2-<slug>.html. Tematiche scelte dai prodotti AI+:
# jump=team brainstorming, hive=network, willsell=sales,
# dojo=mobile learning, creative-studio=design tablet,
# maindset=sticky notes, leadai=executive, reframing-lab=lab,
# liveai-plus=conference stage. Credits in assets/photos/README.md.
def _photos(slug):
    return {
        "image_card":   f"../assets/photos/{slug}/image-card.jpg",
        "stack_top":    f"../assets/photos/{slug}/stack-top.jpg",
        "stack_bottom": f"../assets/photos/{slug}/stack-top.jpg",   # legacy alias
        "hero_ink":     f"../assets/photos/{slug}/hero-ink.jpg",
    }

# Copy per brand. Heading/carousel/image/split/hero hanno volutamente
# struttura simile a Creative Studio (brandboard 2026) per consistenza.
CONTENT = {
    "jump": {
        "wordmark":  "JUMP",
        "tag":       "Activity → Knowledge",
        "heading_h": "Trasforma il fare.<br/>Genera conoscenza.",
        "carousel_title": "ATTIVA IL<br/>SAPERE DEL<br/>TEAM. IN UN<br/>CLICK.",
        "carousel_body":  "JUMP raccoglie ciò che il team sa, lo organizza, lo porta nel flusso di lavoro. Senza interrompere nessuno.",
        "stat_n":    "87%",
        "stat_lbl":  "delle aziende ammette che la propria knowledge non è azionabile.",
        "stat_src":  "McKinsey 2024",
        "image_t":   "UNA SOLA RICERCA.<br/>TUTTO IL KNOW-HOW.<br/>ZERO ATTRITO.",
        "image_cta": "Vedi il tour",
        "split_eb":  "L'AI ASCOLTA<br/>IL TUO TEAM",
        "split_txt": "Riunioni,<br/>documenti,<br/>thread.<br/>Tutto strutturato<br/>in un setup.",
        "split_cta": "Try it now",
        "hero_t":    "L'enablement che impara dal flusso.",
        "hero_sub":  "Nessun corso, nessuna piattaforma esterna. Solo un copilot che impara come lavorate e attiva i nodi giusti al momento giusto.",
        "hero_cta":  "Start activating",
    },
    "hive": {
        "wordmark":  "HIVE",
        "tag":       "Network OS",
        "heading_h": "Tanti nodi.<br/>Una sola intelligenza.",
        "carousel_title": "CONNETTI<br/>L'ECOSISTEMA.<br/>INTERROGA<br/>LA RETE.",
        "carousel_body":  "HIVE connette i nodi del tuo ecosistema in un'unica memoria collettiva, interrogabile via AI. Multi-tenant by design.",
        "stat_n":    "64%",
        "stat_lbl":  "del valore aziendale è bloccato in silos non connessi.",
        "stat_src":  "Forrester 2025",
        "image_t":   "OGNI NODO PARLA.<br/>OGNI NODO RICORDA.<br/>OGNI NODO IMPARA.",
        "image_cta": "Esplora la rete",
        "split_eb":  "MEMORIA<br/>CONDIVISA",
        "split_txt": "Documenti,<br/>persone,<br/>processi.<br/>In una mappa<br/>interrogabile.",
        "split_cta": "Map your network",
        "hero_t":    "Un command deck per il tuo ecosistema.",
        "hero_sub":  "Vista unica sulle attività di tutti i nodi. Quello che succede in rete, succede qui. Niente più silos, niente più dispersione.",
        "hero_cta":  "Open command deck",
    },
    "willsell": {
        "wordmark":  "WILL<br/>SELL",
        "tag":       "Sales coach",
        "heading_h": "Allenati a vendere.<br/>Vendi mentre ti alleni.",
        "carousel_title": "ROLE PLAY<br/>INFINITI.<br/>FEEDBACK<br/>IMMEDIATO.",
        "carousel_body":  "WILLSELL è il coach AI 1-to-1 che simula trattative, dà feedback, misura il progresso. Per ogni venditore. Sempre.",
        "stat_n":    "82%",
        "stat_lbl":  "dei venditori dimentica il training dopo 30 giorni.",
        "stat_src":  "Sales Mastery 2024",
        "image_t":   "OBIEZIONI VERE.<br/>RISPOSTE PROVATE.<br/>SCORE IN CHIARO.",
        "image_cta": "Prova una sessione",
        "split_eb":  "L'AI CAPISCE<br/>IL TUO PITCH",
        "split_txt": "Tono di voce,<br/>obiezioni tipiche,<br/>buyer persona.<br/>Tutto inferito<br/>dal tuo CRM.",
        "split_cta": "Train me",
        "hero_t":    "Un coach AI dietro ogni venditore.",
        "hero_sub":  "Sessioni 1-to-1 illimitate, feedback granulare, KPI di adozione. Il sales enablement che non finisce mai.",
        "hero_cta":  "Start coaching",
    },
    "dojo": {
        "wordmark":  "DOJO",
        "tag":       "Training continuo",
        "heading_h": "Apprendimento continuo.<br/>Senza corsi.",
        "carousel_title": "MICRO<br/>SESSIONI.<br/>OGNI GIORNO.<br/>NEL FLUSSO.",
        "carousel_body":  "DOJO inserisce micro-allenamenti nel ritmo di lavoro. Niente piattaforma da aprire: arrivano dove già lavori.",
        "stat_n":    "70%",
        "stat_lbl":  "dei dipendenti non completa i percorsi formativi obbligatori.",
        "stat_src":  "LinkedIn Learning 2024",
        "image_t":   "5 MINUTI AL GIORNO.<br/>UN NUOVO SKILL<br/>OGNI SETTIMANA.",
        "image_cta": "Inizia oggi",
        "split_eb":  "ADATTIVO,<br/>PER PERSONA",
        "split_txt": "L'AI conosce<br/>il tuo ruolo,<br/>i tuoi gap,<br/>il tuo pace.<br/>E si adatta.",
        "split_cta": "Open my dojo",
        "hero_t":    "Allenamento continuo guidato dall'AI.",
        "hero_sub":  "Una piattaforma di micro-learning che si adatta al tuo ruolo, al tuo livello, al tuo tempo. Cinque minuti al giorno bastano.",
        "hero_cta":  "Start training",
    },
    "creative-studio": {
        # copy esatta dal CREATIVE_STUDIO_BrandBoard.ai
        "wordmark":  "CREATIVE<br/>STUDIO",
        "tag":       "Creative production",
        "heading_h": "Scegli cosa creare.<br/>Lui fa il resto.",
        "carousel_title": "PRODUCI<br/>CREATIVITÀ ALLA<br/>VELOCITÀ DEGLI<br/>ALGORITMI",
        "carousel_body":  "Il sistema AI che genera Ads in un click che convertono. Creative Studio genera statiche, UGC e video cinematografici on-brand. Per ogni piattaforma. In secondi.",
        "stat_n":    "75%",
        "stat_lbl":  "dei Designer e Videomaker non scalano linearmente.",
        "stat_src":  "Highspot 2025",
        "image_t":   "UN SOLO PROMPT.<br/>UN WORKFLOW GUIDATO.<br/>ZERO SETUP TECNICO.",
        "image_cta": "Request a demo",
        "split_eb":  "L'AI IMPARA<br/>IL TUO BRAND",
        "split_txt": "Tone of voice,<br/>visual identity,<br/>messaging.<br/>Tutto assorbito<br/>in un setup.",
        "split_cta": "Create something",
        "hero_t":    "Un editor AI che capisce il linguaggio naturale.",
        "hero_sub":  "Solo una riga di testo e la creatività che cambia sotto i tuoi occhi. È come avere un designer che lavora alla velocità del pensiero.",
        "hero_cta":  "Start creating",
        # palette estesa V2 dal CREATIVE_STUDIO_BrandBoard.ai (override
        # rispetto a tokens/brands/creative-studio.json che è ancora V1).
        # Coerente con [data-ds-version="2"] in styles/v2.css.
        "palette_override": {
            "bg_start": "#FDF6FB",
            "soft":     "#F6D4F3",
            "primary":  "#E76BF0",
            "ink":      "#2D1035",
            "ink_deep": "#0D050F",
        },
    },
    "maindset": {
        "wordmark":  "MAIND<br/>SET",
        "tag":       "Mindset coach",
        "heading_h": "Cambia il modo.<br/>Cambia il risultato.",
        "carousel_title": "NUOVI<br/>MODELLI<br/>MENTALI.<br/>OGNI MESE.",
        "carousel_body":  "MAINDSET è il coach AI che lavora sui pattern mentali del team. Trasformazione culturale guidata, misurata, scalabile.",
        "stat_n":    "68%",
        "stat_lbl":  "delle trasformazioni aziendali fallisce per resistenze culturali.",
        "stat_src":  "BCG 2024",
        "image_t":   "PATTERN VECCHI?<br/>L'AI LI VEDE.<br/>E LI RIPROGRAMMA.",
        "image_cta": "Scopri come",
        "split_eb":  "IL MINDSET<br/>SI MISURA",
        "split_txt": "Reazioni,<br/>parole chiave,<br/>indicatori<br/>di apertura<br/>al cambiamento.",
        "split_cta": "Shift now",
        "hero_t":    "Un coach AI per la trasformazione culturale.",
        "hero_sub":  "Workshop, pillole, conversazioni 1-to-1. Tutto orchestrato da un'AI che capisce dove sta resistendo il team.",
        "hero_cta":  "Start shifting",
    },
    "leadai": {
        "wordmark":  "LEAD<br/>AI",
        "tag":       "Leadership amplified",
        "heading_h": "Guida con AI.<br/>Decide con dati.",
        "carousel_title": "DECISIONI<br/>VELOCI.<br/>CONTESTO<br/>RICCO.",
        "carousel_body":  "LEADAI è il copilot per chi guida: briefing, scenari, recap. Ogni decisione importante con dati e contesto a portata di mano.",
        "stat_n":    "77%",
        "stat_lbl":  "dei leader non ha tempo per leggere tutto prima di decidere.",
        "stat_src":  "Harvard Business Review 2024",
        "image_t":   "BRIEF IN 60 SECONDI.<br/>SCENARI IN UN CLICK.<br/>DECISIONE CONSAPEVOLE.",
        "image_cta": "Prova un briefing",
        "split_eb":  "IL TUO COPILOT<br/>DI LEADERSHIP",
        "split_txt": "Riunioni,<br/>mail, report.<br/>Sintetizzati<br/>nel format<br/>che preferisci.",
        "split_cta": "Lead with AI",
        "hero_t":    "Leadership amplificata dall'AI.",
        "hero_sub":  "Briefing su misura, scenari pre-calcolati, recap delle riunioni. Il tempo del leader torna a essere su persone e visione.",
        "hero_cta":  "Start leading",
    },
    "reframing-lab": {
        "wordmark":  "REFRAMING<br/>LAB",
        "tag":       "Change ops",
        "heading_h": "Il cambiamento, come un laboratorio.",
        "carousel_title": "ESPERIMENTI<br/>CONTINUI.<br/>RISULTATI<br/>MISURABILI.",
        "carousel_body":  "REFRAMING LAB orchestra le iniziative di trasformazione come un laboratorio: ipotesi, esperimenti, evidenze, scale-up.",
        "stat_n":    "73%",
        "stat_lbl":  "delle iniziative di trasformazione non ha un metodo di verifica strutturato.",
        "stat_src":  "MIT Sloan 2024",
        "image_t":   "OGNI INIZIATIVA<br/>È UN ESPERIMENTO.<br/>OGNI DATO È IPOTESI.",
        "image_cta": "Open the lab",
        "split_eb":  "DA HUNCH<br/>A EVIDENZA",
        "split_txt": "Idee,<br/>test,<br/>misure,<br/>scale-up.<br/>In un solo flow.",
        "split_cta": "Launch experiment",
        "hero_t":    "Trasformazione come laboratorio continuo.",
        "hero_sub":  "Un sistema operativo per change manager: orchestra iniziative, misura impatto, decide cosa scalare. Senza Excel.",
        "hero_cta":  "Start the lab",
    },
    "liveai-plus": {
        "wordmark":  "LIVE<br/>AI+",
        "tag":       "Eventi live",
        "heading_h": "Eventi che parlano.<br/>Dati che restano.",
        "carousel_title": "OGNI EVENTO<br/>UN ARCHIVIO<br/>VIVO. CHE<br/>SI INTERROGA.",
        "carousel_body":  "LIVE AI+ trasforma keynote, workshop e dibattiti in un patrimonio interrogabile: trascrizioni, insight, follow-up. Dal vivo, in tempo reale.",
        "stat_n":    "80%",
        "stat_lbl":  "del valore di un evento aziendale si perde nelle 48 ore successive.",
        "stat_src":  "Cvent 2024",
        "image_t":   "UN EVENTO LIVE.<br/>UN KNOWLEDGE BASE<br/>ATTIVO PER ANNI.",
        "image_cta": "Vedi un evento",
        "split_eb":  "DAL VIVO<br/>ALL'ARCHIVIO",
        "split_txt": "Speaker,<br/>domande,<br/>chat,<br/>poll.<br/>Tutto indicizzato.",
        "split_cta": "Go live",
        "hero_t":    "Eventi live, conoscenza per sempre.",
        "hero_sub":  "Trascrive, struttura, distribuisce. Il valore del tuo evento non scade alle 18 dell'ultimo giorno.",
        "hero_cta":  "Stream now",
    },
}


TEMPLATE = """<!doctype html>
<html lang="it" data-brand="{slug}" data-ds-version="2">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{name} · v2 — AI+ Ecosystem · Logotel</title>
<meta name="description" content="Vetrina v2 / brand expansion del brand {name}: heading, nav, stat, carousel, image card, split, hero ink, buttons, palette, stili." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@300..700&family=Roboto:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles/index.css" />
<link rel="stylesheet" href="../styles/v2.css" />
<script src="../scripts/glass-shape.js" defer></script>
<style>
  body {{
    margin: 0;
    background: var(--brand-bg-start, var(--ds-cream));
    color: var(--ds-ink);
    font-family: var(--ds-font-body);
  }}
  .ds-eco-rail {{
    display: flex; gap: 0.5rem; flex-wrap: wrap;
    padding: 0.6rem clamp(1rem, 2vw, 1.5rem);
    background: var(--ds-paper);
    border-bottom: 1px solid var(--ds-line);
    font-size: 0.78rem;
  }}
  .ds-eco-link {{
    text-decoration: none; color: var(--ds-ink-muted);
    padding: 0.25rem 0.65rem; border-radius: 999px;
    letter-spacing: 0.06em; text-transform: uppercase; font-weight: 600;
    transition: background 120ms, color 120ms;
  }}
  .ds-eco-link:hover {{ color: var(--ds-ink-deep); background: var(--brand-soft); }}
  .ds-eco-link[data-active="1"] {{ background: var(--brand-soft); color: var(--ds-ink-deep); }}

  .v2-shell {{
    max-width: 92rem; margin: 0 auto;
    padding: clamp(1rem, 2vw, 1.5rem);
    display: grid; gap: clamp(1.25rem, 2vw, 1.75rem);
  }}
  .v2-section-title {{
    display: flex; justify-content: space-between; align-items: end; gap: 1rem;
    padding-bottom: 0.5rem; border-bottom: 1px solid var(--ds-line);
    margin-top: 1rem;
  }}
  .v2-section-title h2 {{
    font-family: var(--ds-font-display);
    font-size: clamp(1.25rem, 2vw, 1.85rem);
    font-weight: 600; letter-spacing: -0.005em; text-transform: uppercase;
    margin: 0; color: var(--ds-ink-deep);
  }}
  .v2-section-title small {{
    font-family: var(--ds-font-body); font-size: var(--ds-fs-small);
    color: var(--ds-ink-muted); text-transform: uppercase; letter-spacing: 0.06em;
  }}
  .v2-deck {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr));
    gap: clamp(1rem, 2vw, 1.5rem); align-items: start;
  }}
  .v2-row {{
    display: grid;
    grid-template-columns: minmax(14rem, 16rem) minmax(0, 1fr);
    gap: clamp(1.25rem, 3vw, 2.5rem); align-items: start;
  }}
  @media (max-width: 820px) {{ .v2-row {{ grid-template-columns: 1fr; }} }}

  .v2-style-list {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
    gap: 1rem;
  }}
  .v2-style-list dt {{
    font-family: var(--ds-font-body); font-size: 0.7rem; font-weight: 700;
    letter-spacing: 0.1em; text-transform: uppercase; color: var(--ds-ink-muted);
    margin-bottom: 0.35rem;
  }}
  .v2-style-list dd {{
    margin: 0 0 0.85rem; font-family: var(--ds-font-body); font-size: 0.92rem;
    color: var(--ds-ink-deep);
  }}
  .v2-style-list code {{
    font-family: var(--ds-font-mono); font-size: 0.85rem;
    background: rgba(15,4,24,0.05); padding: 0.05rem 0.35rem; border-radius: 0.25rem;
  }}
  .v2-style-list ul {{ margin: 0; padding-left: 1.1rem; }}
  .v2-style-list li {{ font-size: 0.86rem; line-height: 1.5; }}

  .v2-swatch {{
    padding: 2rem 1rem; border-radius: var(--ds-radius-glass-card);
    font-family: var(--ds-font-body); font-weight: 600;
    box-shadow: var(--ds-glass-ring-dark);
  }}
  .v2-swatch[data-tone="light"]  {{ color: var(--ds-ink-deep); }}
  .v2-swatch[data-tone="dark"]   {{ color: var(--ds-cream); }}

  /* Style guide blocks */
  .v2-grad {{
    height: 96px; border-radius: 1rem;
    padding: 0.75rem 1rem;
    color: var(--ds-ink-deep);
    font-family: var(--ds-font-mono); font-size: 0.7rem;
    box-shadow: var(--ds-shadow-card-soft);
  }}
  .v2-grad b {{
    font-family: var(--ds-font-display);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-size: 0.78rem;
    display: block;
  }}
  .v2-grad small {{ display: block; opacity: 0.65; margin-top: 2px; }}
  .v2-grad--dark {{ color: var(--ds-cream); }}

  .v2-radii {{
    display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;
  }}
  .v2-radius {{
    width: 5rem; height: 5rem;
    border: 1.5px solid var(--ds-ink-deep);
    background: var(--ds-white);
    display: grid; place-items: center;
    font-family: var(--ds-font-mono); font-size: 0.65rem;
    color: var(--ds-ink-deep);
    text-align: center; line-height: 1.2;
  }}
  .v2-radius--pill {{
    width: 8rem; height: 2.5rem;
    border-radius: 9999px;
  }}

  .v2-shadows {{
    display: flex; gap: 1rem; flex-wrap: wrap;
  }}
  .v2-shadow {{
    width: 6.5rem; height: 4.5rem;
    background: var(--ds-white);
    border-radius: 1rem;
    display: grid; place-items: center;
    font-family: var(--ds-font-mono); font-size: 0.7rem; color: var(--ds-ink-deep);
  }}
  .v2-shadow--soft {{
    box-shadow: 0 6px 24px -8px rgba(15,4,24,0.12), 0 2px 6px -2px rgba(15,4,24,0.06);
  }}
  .v2-shadow--glow {{
    box-shadow: 0 24px 60px -12px var(--brand-glow);
  }}

  .v2-spacing-scale {{
    display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.4rem; align-items: end;
  }}
  .v2-spacing-scale > div {{ text-align: center; }}
  .v2-spacing-scale span {{
    display: block; background: var(--brand-ink-deep);
    border-radius: 4px; width: 100%;
  }}
  .v2-spacing-scale small {{
    display: block; margin-top: 4px;
    font-family: var(--ds-font-mono); font-size: 0.62rem; color: var(--ds-ink-muted);
  }}

  .v2-stat {{ display: grid; gap: 0.4rem; min-width: 14rem; }}
  .v2-stat__num {{
    font-family: var(--ds-font-display); font-weight: 600;
    font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1;
    color: var(--ds-ink-deep);
  }}
  .v2-stat__num--accent {{ color: var(--brand); }}
  .v2-stat__lbl {{
    font-family: var(--ds-font-body); font-size: 0.85rem;
    color: var(--ds-ink-muted); max-width: 26ch; line-height: 1.45;
  }}

  .v2-voice {{ display: grid; gap: 0.5rem; margin: 0; }}
  .v2-voice > div {{
    display: grid; grid-template-columns: 7rem 1fr; gap: 0.75rem;
    padding: 0.6rem 0.85rem; background: rgba(255,255,255,0.45);
    border-radius: 0.75rem;
    align-items: center;
  }}
  .v2-voice dt {{
    font-family: var(--ds-font-mono); font-size: 0.7rem;
    color: var(--ds-ink-muted); text-transform: uppercase;
    margin: 0;
  }}
  .v2-voice dd {{
    margin: 0; font-family: var(--ds-font-body); font-size: 0.85rem;
    color: var(--ds-ink-deep);
  }}
  .v2-voice__headline {{
    font-family: var(--ds-font-display) !important; font-weight: 600;
    text-transform: uppercase; letter-spacing: -0.005em;
    font-size: 0.95rem !important;
  }}
  .v2-voice__eyebrow {{
    text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--ds-ink-muted) !important; font-size: 0.75rem !important;
  }}
  .v2-voice__tone {{ color: var(--ds-ink-muted) !important; font-size: 0.78rem !important; }}
</style>
</head>
<body>

  <header class="ds-topbar">
    <div class="ds-topbar__brand">
      {name}<sup>AI+</sup>
      <span class="ds-topbar__tag">v2 · brand expansion</span>
    </div>
    <nav class="ds-topbar__nav">
      <a href="./v2-index.html" class="ds-topbar__cta">↩ V2 ECOSYSTEM</a>
      <a href="./{slug}.html" class="ds-topbar__cta" style="background:transparent;color:var(--ds-cream);border-color:rgba(247,246,243,0.4)">Vai a v1</a>
      <span class="ds-topbar__powered">powered by logotel</span>
    </nav>
  </header>

  <nav class="ds-eco-rail">
    <a href="./v2-index.html" class="ds-eco-link" style="color: var(--ds-ink-deep);">↩ Ecosystem v2</a>
{eco_links}
  </nav>

  <main class="v2-shell">

    <!-- HEADING CARD -->
    <section class="ds-glass-heading-card">
      <h1 class="ds-glass-heading-card__wordmark">{wordmark}</h1>
      <p class="ds-glass-heading-card__headline">{heading_h}</p>
    </section>

    <div class="v2-row">

      <!-- NAV -->
      <aside>
        <nav class="ds-glass-nav">
          <div class="ds-glass-nav__brand">
            <div class="ds-glass-badge ds-glass-badge--lg" style="width:100%; aspect-ratio:1/1;">
              <div class="ds-glass-badge__wordmark">{wordmark}</div>
              <div class="ds-glass-badge__footer">
                <span class="ds-glass-badge__aiplus">AI+</span>
                <span class="ds-glass-badge__powered"><span>powered by</span><span>logotel</span></span>
              </div>
            </div>
          </div>
          <ul class="ds-glass-nav__list">
            <li><a class="ds-glass-nav__link" href="#">Overview</a></li>
            <li><a class="ds-glass-nav__link" href="#">Features</a></li>
            <li><a class="ds-glass-nav__link" href="#">Clients</a></li>
            <li><a class="ds-glass-nav__link" href="#" data-active="1">Pricing</a></li>
            <li><a class="ds-glass-nav__link" href="#">Help</a></li>
            <li><a class="ds-glass-nav__link" href="#">About</a></li>
          </ul>
        </nav>
      </aside>

      <div class="v2-deck">

        <!-- STAT CARD -->
        <article class="ds-glass-stat-card">
          <h2 class="ds-glass-stat-card__number">{stat_n}</h2>
          <p class="ds-glass-stat-card__label">{stat_lbl}</p>
          <p class="ds-glass-stat-card__source">{stat_src}</p>
          <svg class="ds-glass-stat-card__chart" viewBox="0 0 240 110" preserveAspectRatio="none" aria-hidden="true">
            <path d="M0,110 L0,80 L30,75 L55,90 L85,60 L115,72 L150,40 L185,55 L210,25 L240,15 L240,110 Z"/>
          </svg>
        </article>

        <!-- CAROUSEL CARD -->
        <article class="ds-glass-carousel-card">
          <h2 class="ds-glass-carousel-card__title">{carousel_title}</h2>
          <p class="ds-glass-carousel-card__body">{carousel_body}</p>
          <div class="ds-glass-carousel-card__dots" aria-label="carousel">
            <i></i><i></i><i></i><i></i><i></i><i data-active="1"></i>
          </div>
          <div class="ds-glass-carousel-card__wordmark">{wordmark}</div>
        </article>

        <!-- IMAGE CARD -->
        <article class="ds-glass-image-card">
          <div class="ds-glass-image-card__bg">
            <img src="{img_url}" alt="" loading="lazy" />
          </div>
          <h3 class="ds-glass-image-card__title">{image_t}</h3>
          <div class="ds-glass-image-card__footer">
            <span class="ds-glass-image-card__wordmark">{wordmark}</span>
            <a class="ds-glass-image-card__cta" href="#">{image_cta}</a>
          </div>
        </article>

      </div>
    </div>

    <!-- STACK CARD — top-only (versione semplificata) -->
    <section class="ds-glass-stack-card">
      <div class="ds-glass-stack-card__top">
        <img src="{stack_top_url}" alt="" loading="lazy" />
        <div class="ds-glass-stack-card__caption">
          <span class="ds-glass-stack-card__caption-eyebrow">{split_eb}</span>
          <p class="ds-glass-stack-card__caption-text">{split_txt}</p>
        </div>
      </div>
    </section>

    <!-- HERO INK -->
    <section class="ds-glass-hero-ink">
      <div>
        <div class="ds-glass-hero-ink__lockup">
          <div class="ds-glass-hero-ink__symbol" aria-hidden="true">{monogram}</div>
          <span class="ds-glass-hero-ink__wordmark">{name_compact}</span>
        </div>
        <h2 class="ds-glass-hero-ink__title">{hero_t}</h2>
        <p class="ds-glass-hero-ink__sub">{hero_sub}</p>
        <a class="ds-glass-button ds-glass-button--brand-gradient" href="#">{hero_cta}</a>
      </div>
      <div class="ds-glass-hero-ink__media">
        <img src="{hero_url}" alt="" loading="lazy" />
      </div>
    </section>

    <!-- BUTTON SYSTEM -->
    <div class="v2-section-title">
      <h2>Button system</h2>
      <small>brand expansion · 6 stati + icone</small>
    </div>
    <section class="ds-glass-card" style="padding:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
      <button class="ds-glass-button ds-glass-button--soft-light">Light soft</button>
      <button class="ds-glass-button">Light</button>
      <button class="ds-glass-button ds-glass-button--brand-fill">Brand fill</button>
      <button class="ds-glass-button ds-glass-button--brand-gradient">Brand gradient</button>
      <button class="ds-glass-button ds-glass-button--outline">Outline</button>
      <button class="ds-glass-button ds-glass-button--ink">Ink</button>
      <span style="display:inline-flex;gap:0.5rem;margin-left:1rem;align-items:center;">
        <button class="ds-glass-button ds-glass-button--icon" aria-label="menu">≡</button>
        <button class="ds-glass-button ds-glass-button--icon" aria-label="close">×</button>
        <button class="ds-glass-button ds-glass-button--icon" aria-label="next">→</button>
      </span>
    </section>

    <!-- PALETTE -->
    <div class="v2-section-title">
      <h2>Palette {name}</h2>
      <small>5 step</small>
    </div>
    <section style="display:grid;grid-template-columns: repeat(5, 1fr); gap:0.75rem;">
      <div class="v2-swatch" data-tone="light" style="background:{hex_bg_start};">{hex_bg_start_label}</div>
      <div class="v2-swatch" data-tone="light" style="background:{hex_soft};">{hex_soft_label}</div>
      <div class="v2-swatch" data-tone="dark"  style="background:{hex_primary};">{hex_primary_label}</div>
      <div class="v2-swatch" data-tone="dark"  style="background:{hex_ink};">{hex_ink_label}</div>
      <div class="v2-swatch" data-tone="dark"  style="background:{hex_ink_deep};">{hex_ink_deep_label}</div>
    </section>

    <!-- GRADIENTS -->
    <div class="v2-section-title">
      <h2>Gradients</h2>
      <small>3 valori canonici · brand-aware</small>
    </div>
    <section class="v2-deck">
      <div class="v2-grad" style="background: linear-gradient(135deg, {hex_bg_start} 0%, {hex_soft} 100%);">
        <b>Badge · 135°</b>
        <small>cream → brand-soft · ratio 1:1</small>
      </div>
      <div class="v2-grad" style="background: linear-gradient(160deg, {hex_bg_start} 0%, {hex_soft} 55%, {hex_primary} 100%);">
        <b>Hero · 160°</b>
        <small>cream → soft (55%) → primary</small>
      </div>
      <div class="v2-grad v2-grad--dark" style="background: linear-gradient(180deg, {hex_ink} 0%, {hex_ink_deep} 100%);">
        <b>Ink card · 180°</b>
        <small>brand-ink → brand-ink-deep</small>
      </div>
    </section>

    <!-- RADII · SHADOWS · SPACING -->
    <div class="v2-section-title">
      <h2>Radii · Shadows · Spacing</h2>
      <small>token geometrici condivisi</small>
    </div>
    <section class="v2-deck">
      <article class="ds-glass-card">
        <p class="ds-glass-card__eyebrow">Radii</p>
        <div class="v2-radii">
          <div class="v2-radius" style="border-radius: 1.25rem;">swatch · 1.25rem</div>
          <div class="v2-radius" style="border-radius: 1.75rem;">card · 1.75rem</div>
          <div class="v2-radius v2-radius--pill">pill · 9999px</div>
        </div>
      </article>
      <article class="ds-glass-card">
        <p class="ds-glass-card__eyebrow">Shadows</p>
        <div class="v2-shadows">
          <div class="v2-shadow v2-shadow--soft">card-soft</div>
          <div class="v2-shadow v2-shadow--glow">card-glow</div>
        </div>
        <small style="display:block;margin-top:0.6rem;font-size:0.7rem;color:var(--ds-ink-muted);">due shadow totali · glow usa --brand-glow</small>
      </article>
      <article class="ds-glass-card">
        <p class="ds-glass-card__eyebrow">Spacing scale</p>
        <div class="v2-spacing-scale">
          <div><span style="height:4px"></span><small>xs · 4</small></div>
          <div><span style="height:8px"></span><small>sm · 8</small></div>
          <div><span style="height:16px"></span><small>md · 16</small></div>
          <div><span style="height:24px"></span><small>lg · 24</small></div>
          <div><span style="height:40px"></span><small>xl · 40</small></div>
          <div><span style="height:64px"></span><small>2xl · 64</small></div>
          <div><span style="height:96px"></span><small>3xl · 96</small></div>
        </div>
      </article>
    </section>

    <!-- STATS SPECIMEN -->
    <div class="v2-section-title">
      <h2>Stats</h2>
      <small>numero gigante · MuseoModerno · brand-ink-deep</small>
    </div>
    <section class="ds-glass-card" style="display:flex;gap:2.5rem;flex-wrap:wrap;align-items:end;">
      <div class="v2-stat">
        <div class="v2-stat__num">+50</div>
        <div class="v2-stat__lbl">varianti creative on-brand in un pomeriggio, pronte per il launch</div>
      </div>
      <div class="v2-stat">
        <div class="v2-stat__num v2-stat__num--accent">3×</div>
        <div class="v2-stat__lbl">più velocità di produzione vs. il flusso tradizionale</div>
      </div>
      <div class="v2-stat">
        <div class="v2-stat__num">{stat_n}</div>
        <div class="v2-stat__lbl">{stat_lbl}</div>
      </div>
    </section>

    <!-- COPY & VOICE -->
    <div class="v2-section-title">
      <h2>Copy & Voice</h2>
      <small>Italiano · imperativo · tu · zero gergo · zero emoji</small>
    </div>
    <section class="ds-glass-card">
      <dl class="v2-voice">
        <div><dt>Headline</dt><dd class="v2-voice__headline">{heading_h_text}</dd></div>
        <div><dt>Eyebrow</dt><dd class="v2-voice__eyebrow">{tag} · powered by Logotel</dd></div>
        <div><dt>CTA</dt><dd>{hero_cta} · {image_cta} · {split_cta}</dd></div>
        <div><dt>Sub</dt><dd>{hero_sub}</dd></div>
        <div><dt>Tone</dt><dd class="v2-voice__tone">Italiano · imperativo · tu · zero gergo · zero emoji</dd></div>
      </dl>
    </section>

    <!-- STILI ATTIVI -->
    <div class="v2-section-title">
      <h2>Stili attivi · {name}</h2>
      <small>tutto ciò che è applicato in questa pagina</small>
    </div>
    <section class="ds-glass-card">
      <dl class="v2-style-list">
        <div>
          <dt>Brand slug</dt>
          <dd><code>data-brand="{slug}"</code></dd>
          <dt>Versione DS</dt>
          <dd><code>data-ds-version="2"</code></dd>
        </div>
        <div>
          <dt>Palette</dt>
          <dd>
            <code>--brand-bg-start</code> {hex_bg_start_label}<br/>
            <code>--brand-soft</code> {hex_soft_label}<br/>
            <code>--brand</code> {hex_primary_label}<br/>
            <code>--brand-ink</code> {hex_ink_label}<br/>
            <code>--brand-ink-deep</code> {hex_ink_deep_label}
          </dd>
        </div>
        <div>
          <dt>Tipografia</dt>
          <dd>
            Display <code>MuseoModerno</code><br/>
            Body <code>Roboto</code><br/>
            Mono <code>JetBrains Mono</code>
          </dd>
          <dt>Forma 3D</dt>
          <dd><code>#shape-{slug}</code> ({shape_kind})</dd>
        </div>
        <div>
          <dt>Moduli mostrati</dt>
          <dd>
            <ul>
              <li><code>.ds-glass-heading-card</code></li>
              <li><code>.ds-glass-nav</code></li>
              <li><code>.ds-glass-stat-card</code></li>
              <li><code>.ds-glass-carousel-card</code></li>
              <li><code>.ds-glass-image-card</code></li>
              <li><code>.ds-glass-stack-card</code></li>
              <li><code>.ds-glass-hero-ink</code></li>
              <li>Buttons <code>--soft-light / default / --brand-fill / --brand-gradient / --outline / --ink / --icon</code></li>
              <li>Style guide: gradients, radii, shadows, spacing, stats, copy &amp; voice</li>
            </ul>
          </dd>
        </div>
      </dl>
    </section>

    <footer style="margin-top:2rem;padding:1.5rem 0;color:var(--ds-ink-muted);font-size:0.78rem;border-top:1px solid var(--ds-line);">
      AI+ Ecosystem · v2 / brand expansion · brand {name} · powered by logotel
    </footer>

  </main>

</body>
</html>
"""


SHAPE_KIND = {
    "creative-studio": "square frame",
    "jump":            "J / chair",
    "hive":            "hexagon ring",
    "willsell":        "T",
    "dojo":            "torus / ring",
    "maindset":        "M wave",
    "leadai":          "E",
    "reframing-lab":       "Q",
    "liveai-plus":     "plus / cross",
}

# Monogram 2-char visualizzato come emblem nel hero-ink (image #27)
MONOGRAM = {
    "creative-studio": "TI",   # come da brandboard image #27
    "jump":            "JM",
    "hive":            "HI",
    "willsell":        "WS",
    "dojo":            "DJ",
    "maindset":        "MS",
    "leadai":          "LA",
    "reframing-lab":       "RL",
    "liveai-plus":     "L+",
}

# Map brand → relative tone (light = dark text on it, dark = light text)
SWATCH_TONE = {
    # given indices [bg_start, soft, primary, ink, ink_deep]
    # default: first 2 light, last 3 dark — works for most brands
}


def highlight_lines(s: str) -> str:
    """Wrappa ogni riga (separata da <br/>) in <span class="ds-glass-highlight">.
    Brandboard image #15: il titolo dell'image-card ha un marker cream-pink
    per ciascuna delle 3 righe."""
    parts = s.split("<br/>")
    return "<br/>".join(f'<span class="ds-glass-highlight">{p}</span>' for p in parts)


def load_palette(slug: str) -> dict:
    tk = json.loads((REPO / "tokens" / "brands" / f"{slug}.json").read_text(encoding="utf-8"))
    return {
        "bg_start":  tk["color"]["bg"]["start"]["value"],
        "soft":      tk["color"]["soft"]["value"],
        "primary":   tk["color"]["primary"]["value"],
        "ink":       tk["color"]["ink"]["value"],
        "ink_deep":  tk["color"]["ink-deep"]["value"],
    }


def build_eco_links(active_slug: str) -> str:
    out = []
    for b in INDEX["brands"]:
        marker = ' data-active="1"' if b["slug"] == active_slug else ""
        out.append(f'    <a href="./v2-{b["slug"]}.html" class="ds-eco-link"{marker}>{b["name"]}</a>')
    return "\n".join(out)


def render(slug: str) -> str:
    info = BRANDS_INFO[slug]
    c = CONTENT[slug]
    pal = load_palette(slug)
    # Allow per-brand palette override (es. Creative Studio V2 espansa
    # dal brandboard 2026, non ancora persistita in tokens/brands/<slug>.json).
    if "palette_override" in c:
        pal.update(c["palette_override"])
    name = info["name"]
    name_compact = name.replace(" ", "").upper()
    return TEMPLATE.format(
        slug=slug,
        name=name,
        name_compact=name_compact,
        wordmark=c["wordmark"],
        heading_h=c["heading_h"],
        heading_h_text=c["heading_h"].replace("<br/>", " ").replace("<br />", " "),
        tag=c["tag"],
        carousel_title=c["carousel_title"],
        carousel_body=c["carousel_body"],
        stat_n=c["stat_n"],
        stat_lbl=c["stat_lbl"],
        stat_src=c["stat_src"],
        image_t=c["image_t"],
        image_cta=c["image_cta"],
        split_eb=c["split_eb"],
        split_txt=c["split_txt"],
        split_cta=c["split_cta"],
        hero_t=c["hero_t"],
        hero_sub=c["hero_sub"],
        hero_cta=c["hero_cta"],
        img_url=_photos(slug)["image_card"],
        stack_top_url=_photos(slug)["stack_top"],
        stack_bottom_url=_photos(slug)["stack_bottom"],
        hero_url=_photos(slug)["hero_ink"],
        hex_bg_start=pal["bg_start"],   hex_bg_start_label=pal["bg_start"].upper().lstrip("#"),
        hex_soft=pal["soft"],           hex_soft_label=pal["soft"].upper().lstrip("#"),
        hex_primary=pal["primary"],     hex_primary_label=pal["primary"].upper().lstrip("#"),
        hex_ink=pal["ink"],             hex_ink_label=pal["ink"].upper().lstrip("#"),
        hex_ink_deep=pal["ink_deep"],   hex_ink_deep_label=pal["ink_deep"].upper().lstrip("#"),
        shape_kind=SHAPE_KIND[slug],
        monogram=MONOGRAM[slug],
        eco_links=build_eco_links(slug),
    )


def main():
    out_dir = REPO / "examples"
    for slug in BRANDS_INFO:
        html = render(slug)
        path = out_dir / f"v2-{slug}.html"
        path.write_text(html, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")


if __name__ == "__main__":
    main()
