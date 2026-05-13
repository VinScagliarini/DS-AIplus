/**
 * AI+ DS v2 · glass-shape inline injector
 * ----------------------------------------
 * Inietta il file ../assets/shapes/sprite.svg inline all'inizio del <body>
 * così che <use href="#shape-<slug>"/> dentro .ds-glass-shape funzioni con
 * CSS variables (--brand, --brand-soft, ...) brand-aware.
 *
 * Caricabile con:
 *   <script src="../scripts/glass-shape.js" defer></script>
 *
 * Configurabile via attributo `data-sprite-url`:
 *   <script src="..." data-sprite-url="/path/to/sprite.svg"></script>
 */
(function () {
  function findSpriteUrl() {
    const tag = document.querySelector('script[src*="glass-shape.js"]');
    if (tag && tag.dataset.spriteUrl) return tag.dataset.spriteUrl;
    // default: alongside the script in /scripts/, sprite lives in ../assets/shapes/sprite.svg
    if (tag && tag.src) {
      const u = new URL(tag.src, document.baseURI);
      return new URL("../assets/shapes/sprite.svg", u).toString();
    }
    return "../assets/shapes/sprite.svg";
  }

  function inject() {
    if (document.getElementById("ds-glass-sprite")) return;
    const url = findSpriteUrl();
    fetch(url, { credentials: "same-origin" })
      .then((r) => (r.ok ? r.text() : Promise.reject(r.status)))
      .then((svgText) => {
        const wrap = document.createElement("div");
        wrap.id = "ds-glass-sprite";
        wrap.style.cssText = "position:absolute;width:0;height:0;overflow:hidden";
        wrap.setAttribute("aria-hidden", "true");
        wrap.innerHTML = svgText;
        document.body.insertBefore(wrap, document.body.firstChild);
      })
      .catch((err) => console.warn("[ds-glass-shape] sprite load failed:", err));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inject, { once: true });
  } else {
    inject();
  }
})();
