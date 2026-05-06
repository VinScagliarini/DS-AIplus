/**
 * AI+ Ecosystem · Tailwind preset
 *
 *   tailwind.config.js
 *   ----------------------------------------
 *   import preset from "ai-plus-ecosystem-ds/tailwind/preset.js";
 *   export default {
 *     presets: [preset],
 *     content: ["./app/** /*.{ts,tsx}"],
 *   };
 *
 * I colori brand (`--brand`, `--brand-soft`, `--brand-ink`, ...)
 * sono variabili CSS popolate dai file in `styles/brands/*.css`.
 * Tailwind li espone come utility "brand" / "brand-soft" / ecc.
 */

const brands = require("../tokens/index.json").brands;

/** @type {import('tailwindcss').Config} */
const preset = {
  theme: {
    extend: {
      colors: {
        cream:    "#F7F6F3",
        ink:      "#0F0418",
        "ink-soft":  "#1A0E2A",
        "ink-muted": "#6B5B7A",

        // Token brand-aware: uguale per tutti i brand, cambia il valore
        // della custom property a runtime.
        brand:           "var(--brand)",
        "brand-soft":    "var(--brand-soft)",
        "brand-deep":    "var(--brand-deep)",
        "brand-ink":     "var(--brand-ink)",
        "brand-ink-deep":"var(--brand-ink-deep)",

        // Esposizione esplicita di ogni brand (per casi cross-brand)
        ...Object.fromEntries(
          brands.map((b) => [
            b.slug,
            {
              soft:    b.soft,
              DEFAULT: b.primary,
            },
          ])
        ),
      },
      fontFamily: {
        display: ["MuseoModerno", "system-ui", "sans-serif"],
        body:    ["Roboto", "Myriad Pro", "system-ui", "sans-serif"],
        mono:    ["JetBrains Mono", "ui-monospace", "monospace"],
      },
      fontSize: {
        display: ["clamp(3rem, 6vw + 1rem, 6.5rem)",   { lineHeight: "1.0",  letterSpacing: "-0.02em" }],
        h1:      ["clamp(2.25rem, 3.5vw + 1rem, 4rem)", { lineHeight: "1.15", letterSpacing: "-0.02em" }],
        h2:      ["clamp(1.75rem, 2vw + 1rem, 2.75rem)",{ lineHeight: "1.15" }],
        h3:      ["clamp(1.25rem, 1vw + 1rem, 1.75rem)",{ lineHeight: "1.15" }],
      },
      borderRadius: {
        card:   "1.75rem",
        swatch: "1.25rem",
        pill:   "9999px",
      },
      boxShadow: {
        "card-soft": "0 6px 24px -8px rgba(15,4,24,0.12), 0 2px 6px -2px rgba(15,4,24,0.06)",
        "card-glow": "0 24px 60px -12px var(--brand-glow)",
      },
      backgroundImage: {
        "brand-badge":  "var(--brand-gradient-badge)",
        "brand-hero":   "var(--brand-gradient-hero)",
        "brand-ink-card":"var(--brand-gradient-ink-card)",
      },
    },
  },
};

module.exports = preset;
module.exports.default = preset;
