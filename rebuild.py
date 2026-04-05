"""
QuillPhen — Complete M3 site rebuild.
Generates: styles.css, index.html, all 32 project pages, sitemap.xml
"""
import os, json

BASE = r"d:\mc packs\sites\revmap\quillphen"

# ──────────────────────────────────────────────────────── CSS ──
CSS = r"""/* =======================================================
   QuillPhen · Material Design 3
   Roboto · Proper M3 tonal palette · Spec-correct
   ======================================================= */

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');

/* ── M3 System Tokens (seed #006E1C) ─────────────────── */
:root {
  /* Primary */
  --md-pri:     #006E1C;
  --md-pri-on:  #FFFFFF;
  --md-pri-c:   #96F990;
  --md-pri-c-on:#002105;

  /* Secondary */
  --md-sec:     #52634F;
  --md-sec-on:  #FFFFFF;
  --md-sec-c:   #D5E8CF;
  --md-sec-c-on:#111F0F;

  /* Tertiary */
  --md-ter:     #38656A;
  --md-ter-on:  #FFFFFF;
  --md-ter-c:   #BCEBF0;
  --md-ter-c-on:#002023;

  /* Error */
  --md-err:     #BA1A1A;
  --md-err-on:  #FFFFFF;
  --md-err-c:   #FFDAD6;
  --md-err-c-on:#410002;

  /* Background + Surface */
  --md-bg:      #F6FAF3;
  --md-bg-on:   #191C18;
  --md-surf:    #F6FAF3;
  --md-surf-on: #191C18;
  --md-surv:    #DDE5D8;   /* surface-variant */
  --md-surv-on: #414940;

  /* Surface Containers (lowest → highest) */
  --md-sc0: #FFFFFF;
  --md-sc1: #F0F5EC;
  --md-sc2: #EAF0E6;
  --md-sc3: #E4EAE0;
  --md-sc4: #DFE5DA;

  /* Outline */
  --md-out:   #727970;
  --md-outv:  #C1C9BE;   /* outline-variant */

  /* Inverse */
  --md-inv-s:    #2E312E;
  --md-inv-s-on: #EFF2EA;
  --md-inv-pri:  #7ADA7A;

  /* ── Shape ── */
  --r-xs:   4px;
  --r-sm:   8px;
  --r-md:   12px;
  --r-lg:   16px;
  --r-xl:   20px;
  --r-2xl:  28px;
  --r-full: 9999px;

  /* ── Elevation (light = shadows) ── */
  --e0: none;
  --e1: 0 1px 2px rgba(0,0,0,.15), 0 1px 3px rgba(0,0,0,.10);
  --e2: 0 1px 2px rgba(0,0,0,.15), 0 2px 8px rgba(0,0,0,.12);
  --e3: 0 2px 4px rgba(0,0,0,.15), 0 6px 16px rgba(0,0,0,.12);
  --e4: 0 4px 8px rgba(0,0,0,.15), 0 12px 28px rgba(0,0,0,.14);

  /* ── Motion ── */
  --dur1: 100ms;
  --dur2: 200ms;
  --dur3: 300ms;
  --dur4: 400ms;
  --ease:     cubic-bezier(0.2, 0.0, 0.0, 1.0);
  --ease-out: cubic-bezier(0.05, 0.7, 0.1, 1.0);
  --ease-in:  cubic-bezier(0.3, 0.0, 1.0, 1.0);

  /* ── Accent swatches (icon containers, chips) ── */
  --ice-amber-bg:  #FFEFC4; --ice-amber:  #5E3B00;
  --ice-pink-bg:   #FFDAEB; --ice-pink:   #680031;
  --ice-purple-bg: #ECDDFF; --ice-purple: #21005D;
  --ice-blue-bg:   #D4E4FF; --ice-blue:   #001849;

  /* ── Layout ── */
  --max-w:    1280px;
  --pad:      24px;
  --hh:       64px;   /* header height */
}

/* ── Dark palette ────────────────────────────────────── */
@media (prefers-color-scheme: dark) {
  :root {
    --md-pri:     #7ADA7A;
    --md-pri-on:  #003909;
    --md-pri-c:   #005315;
    --md-pri-c-on:#96F990;

    --md-sec:     #B9CCBA;
    --md-sec-on:  #243523;
    --md-sec-c:   #3B4B38;
    --md-sec-c-on:#D5E8CF;

    --md-ter:     #A0CED4;
    --md-ter-on:  #003739;
    --md-ter-c:   #1F4D52;
    --md-ter-c-on:#BCEBF0;

    --md-bg:      #111411;
    --md-bg-on:   #E1E4DF;
    --md-surf:    #111411;
    --md-surf-on: #E1E4DF;
    --md-surv:    #414940;
    --md-surv-on: #C1C9BE;

    --md-sc0: #0C0F0C;
    --md-sc1: #191C18;
    --md-sc2: #1D211C;
    --md-sc3: #272B26;
    --md-sc4: #323631;

    --md-out:  #8B9389;
    --md-outv: #414940;

    --md-inv-s:    #E1E4DF;
    --md-inv-s-on: #2E312E;
    --md-inv-pri:  #006E1C;

    --e1: 0 1px 2px rgba(0,0,0,.45), 0 1px 3px rgba(0,0,0,.35);
    --e2: 0 1px 2px rgba(0,0,0,.45), 0 2px 8px rgba(0,0,0,.40);
    --e3: 0 2px 4px rgba(0,0,0,.45), 0 6px 16px rgba(0,0,0,.45);
    --e4: 0 4px 8px rgba(0,0,0,.45), 0 12px 28px rgba(0,0,0,.50);

    --ice-amber-bg:  #3E2400; --ice-amber:  #FFDDB5;
    --ice-pink-bg:   #3F001D; --ice-pink:   #FFB1C5;
    --ice-purple-bg: #17004B; --ice-purple: #CEBBFF;
    --ice-blue-bg:   #002A6E; --ice-blue:   #A9C7FF;
  }
}

/* ── Reset ───────────────────────────────────────────── */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0; padding: 0;
}
html {
  scroll-behavior: smooth;
  color-scheme: light dark;
}
body {
  font-family: 'Roboto', 'Google Sans', system-ui, sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  background: var(--md-bg);
  color: var(--md-bg-on);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}
a { color: var(--md-pri); text-decoration: none; }
img { display: block; max-width: 100%; }
ul, ol { list-style: none; }

/* ── Material Symbols ────────────────────────────────── */
.mi {
  font-family: 'Material Symbols Rounded', sans-serif;
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  direction: ltr;
  -webkit-font-smoothing: antialiased;
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  user-select: none;
  pointer-events: none;
}

/* ── State layer pattern (M3 spec) ───────────────────── */
/* Applied to all interactive surfaces via ::after pseudo */

/* ── Layout ──────────────────────────────────────────── */
.wrap {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--pad);
  width: 100%;
}

/* ── Top App Bar ─────────────────────────────────────── */
.top-bar {
  position: sticky;
  top: 0;
  z-index: 200;
  height: var(--hh);
  background: color-mix(in srgb, var(--md-sc1) 84%, transparent);
  border-bottom: 1px solid transparent;
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  transition:
    box-shadow var(--dur2) var(--ease),
    border-color var(--dur2) var(--ease);
}
.top-bar.raised {
  box-shadow: var(--e1);
  border-color: var(--md-outv);
}
.top-bar__row {
  height: 100%;
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--pad);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}
.top-bar__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--md-surf-on);
}
.top-bar__avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 1.5px solid var(--md-outv);
}
.top-bar__avatar img { width: 100%; height: 100%; object-fit: cover; }
.top-bar__wordmark {
  font-size: 1.375rem;
  font-weight: 400;
  letter-spacing: 0;
  color: var(--md-surf-on);
}
.top-bar__nav {
  display: flex;
  align-items: center;
  gap: 2px;
}

/* Text button (nav links) */
.btn-text {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 40px;
  padding: 0 12px;
  border-radius: var(--r-full);
  border: none;
  background: transparent;
  color: var(--md-surv-on);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: color var(--dur1) var(--ease);
}
.btn-text::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: currentColor;
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.btn-text:hover { color: var(--md-surf-on); }
.btn-text:hover::after { opacity: .08; }
.btn-text:active::after { opacity: .12; }

/* ── Hero ────────────────────────────────────────────── */
.hero {
  padding: 80px 0 64px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  pointer-events: none;
  background:
    radial-gradient(
      ellipse 80% 65% at 50% -15%,
      color-mix(in srgb, var(--md-pri-c) 55%, transparent),
      transparent 65%
    );
}
.hero__inner { position: relative; z-index: 1; }

.hero__avatar {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 88px; height: 88px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 20px;
  box-shadow:
    0 0 0 3px var(--md-bg),
    0 0 0 6px var(--md-outv),
    var(--e3);
  animation: zoomIn var(--dur4) var(--ease-out) both;
}
.hero__avatar img { width: 100%; height: 100%; object-fit: cover; }

.hero__title {
  /* Display Large */
  font-size: clamp(2.25rem, 5.5vw, 3.5625rem);
  font-weight: 400;
  letter-spacing: -.015em;
  line-height: 1.1;
  color: var(--md-surf-on);
  margin-bottom: 12px;
  animation: slideUp var(--dur4) var(--ease-out) 80ms both;
}
.hero__sub {
  /* Body Large */
  font-size: clamp(.9375rem, 2vw, 1.125rem);
  font-weight: 400;
  letter-spacing: .03125rem;
  line-height: 1.65;
  color: var(--md-surv-on);
  max-width: 500px;
  margin: 0 auto 28px;
  animation: slideUp var(--dur4) var(--ease-out) 160ms both;
}
.hero__badges {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 32px;
  animation: slideUp var(--dur4) var(--ease-out) 240ms both;
}
.badge {
  display: inline-flex;
  align-items: center;
  height: 28px;
  padding: 0 12px;
  border-radius: var(--r-sm);
  background: var(--md-sc2);
  color: var(--md-surv-on);
  border: 1px solid var(--md-outv);
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .03125rem;
}
.hero__ctas {
  display: flex;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
  animation: slideUp var(--dur4) var(--ease-out) 320ms both;
}

/* Filled button */
.btn-filled {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 40px;
  padding: 0 24px;
  border-radius: var(--r-full);
  border: none;
  background: var(--md-pri);
  color: var(--md-pri-on);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  box-shadow: var(--e1);
  transition: box-shadow var(--dur2) var(--ease);
}
.btn-filled::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: var(--md-pri-on);
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.btn-filled:hover { box-shadow: var(--e2); }
.btn-filled:hover::after { opacity: .08; }
.btn-filled:active::after { opacity: .12; }
.btn-filled > * { position: relative; }

/* Tonal button */
.btn-tonal {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 40px;
  padding: 0 24px;
  border-radius: var(--r-full);
  border: none;
  background: var(--md-sec-c);
  color: var(--md-sec-c-on);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  box-shadow: var(--e1);
  transition: box-shadow var(--dur2) var(--ease);
}
.btn-tonal::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: var(--md-sec-c-on);
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.btn-tonal:hover { box-shadow: var(--e2); }
.btn-tonal:hover::after { opacity: .08; }
.btn-tonal:active::after { opacity: .12; }
.btn-tonal > * { position: relative; }

/* Outlined button */
.btn-outlined {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 40px;
  padding: 0 24px;
  border-radius: var(--r-full);
  border: 1px solid var(--md-out);
  background: transparent;
  color: var(--md-pri);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: border-color var(--dur1) var(--ease);
}
.btn-outlined::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: var(--md-pri);
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.btn-outlined:hover::after { opacity: .08; }
.btn-outlined:active::after { opacity: .12; }
.btn-outlined > * { position: relative; }

/* ── Filter Bar ──────────────────────────────────────── */
.filter-bar {
  position: sticky;
  top: var(--hh);
  z-index: 100;
  padding: 12px 0 0;
  background: color-mix(in srgb, var(--md-bg) 88%, transparent);
  border-bottom: 1px solid transparent;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition:
    border-color var(--dur2) var(--ease),
    box-shadow var(--dur2) var(--ease);
}
.filter-bar.stuck {
  border-color: var(--md-outv);
  box-shadow: var(--e1);
}
.filter-bar__row {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--pad) 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}

/* M3 Filter Chip */
.fchip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  height: 32px;
  padding: 0 16px;
  border-radius: var(--r-sm);
  border: 1px solid var(--md-out);
  background: transparent;
  color: var(--md-surv-on);
  font-family: inherit;
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition:
    background var(--dur2) var(--ease),
    border-color var(--dur2) var(--ease),
    color var(--dur2) var(--ease),
    padding-left var(--dur2) var(--ease);
  user-select: none;
  white-space: nowrap;
}
.fchip::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: currentColor;
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.fchip:hover::after { opacity: .08; }
.fchip:active::after { opacity: .12; }
.fchip.on {
  background: var(--md-sec-c);
  border-color: transparent;
  color: var(--md-sec-c-on);
  padding-left: 8px;
}
.fchip__ck {
  display: none;
  font-size: 16px;
  width: 16px;
  line-height: 1;
  font-variation-settings: 'FILL' 1, 'wght' 600, 'GRAD' 0, 'opsz' 20;
}
.fchip.on .fchip__ck { display: inline-block; }
.fchip__label { position: relative; }
.fchip__ck    { position: relative; }

/* Search field */
.search-fld {
  display: flex;
  align-items: center;
  gap: 4px;
  height: 32px;
  padding: 0 14px;
  border-radius: var(--r-sm);
  border: 1px solid var(--md-out);
  background: var(--md-sc0);
  color: var(--md-surf-on);
  transition:
    border-color var(--dur1) var(--ease),
    border-width var(--dur1) var(--ease);
}
.search-fld:focus-within {
  border-color: var(--md-pri);
  border-width: 2px;
}
.search-fld .mi { font-size: 18px; color: var(--md-surv-on); }
.search-fld input {
  border: none;
  background: none;
  font-family: inherit;
  font-size: .875rem;
  font-weight: 400;
  letter-spacing: .015625rem;
  color: var(--md-surf-on);
  width: 180px;
  outline: none;
}
.search-fld input::placeholder { color: var(--md-surv-on); }

/* ── Projects section ────────────────────────────────── */
.projects-sec {
  padding: 20px 0 80px;
}
.sec-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}
.sec-title {
  /* Title Large */
  font-size: 1.375rem;
  font-weight: 400;
  letter-spacing: 0;
  color: var(--md-surf-on);
}
.cnt-badge {
  display: inline-flex;
  align-items: center;
  height: 24px;
  padding: 0 10px;
  border-radius: var(--r-full);
  background: var(--md-sec-c);
  color: var(--md-sec-c-on);
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .03125rem;
}

/* ── M3 Elevated Card ────────────────────────────────── */
.pgrid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(296px, 1fr));
  gap: 12px;
}
.pcard {
  background: var(--md-sc1);   /* surface-container-low */
  border-radius: var(--r-md);  /* 12dp Medium shape */
  box-shadow: var(--e1);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transition:
    box-shadow var(--dur2) var(--ease),
    transform var(--dur2) var(--ease);
  animation: cardIn var(--dur4) var(--ease-out) both;
}
.pcard::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: inherit;
  background: var(--md-surf-on);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--dur1) var(--ease);
}
.pcard:hover {
  box-shadow: var(--e2);
  transform: translateY(-2px);
}
.pcard:hover::before { opacity: .05; }

.pcard__body    { padding: 16px 16px 0;  flex: 1; display: flex; flex-direction: column; }
.pcard__head    { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; }

/* Icon container — M3 medium shape, tonal */
.ic {
  width: 48px; height: 48px;
  border-radius: var(--r-md);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  font-size: 24px;
  background: var(--md-pri-c);
  color: var(--md-pri-c-on);
}
.ic.teal   { background: var(--md-ter-c);     color: var(--md-ter-c-on);  }
.ic.sc     { background: var(--md-sec-c);     color: var(--md-sec-c-on);  }
.ic.amber  { background: var(--ice-amber-bg); color: var(--ice-amber);    }
.ic.pink   { background: var(--ice-pink-bg);  color: var(--ice-pink);     }
.ic.purple { background: var(--ice-purple-bg);color: var(--ice-purple);   }
.ic.blue   { background: var(--ice-blue-bg);  color: var(--ice-blue);     }

.pcard__meta  { flex: 1; min-width: 0; }
.pcard__title {
  /* Title Medium */
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: .009375rem;
  line-height: 1.4;
  color: var(--md-surf-on);
  margin-bottom: 6px;
}
.pcard__chips { display: flex; gap: 4px; flex-wrap: wrap; }

/* Assist chips (edition + type) */
.achip {
  display: inline-flex;
  align-items: center;
  height: 24px;
  padding: 0 8px;
  border-radius: var(--r-xs);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .03125rem;
  text-transform: uppercase;
}
.achip-java     { background: color-mix(in srgb, #2E7D32 14%, transparent); color: #1B5E20;  }
.achip-bedrock  { background: color-mix(in srgb, #E65100 14%, transparent); color: #BF360C;  }
.achip-datapack { background: color-mix(in srgb, var(--md-pri-c) 70%, transparent); color: var(--md-pri-c-on); }
.achip-mod      { background: color-mix(in srgb, #7B1FA2 14%, transparent); color: #4A148C;  }
.achip-resourcepack { background: color-mix(in srgb, #C2185B 14%, transparent); color: #880E4F; }
.achip-shader   { background: color-mix(in srgb, #E65100 14%, transparent); color: #7A4500;  }
.achip-addon    { background: color-mix(in srgb, var(--md-ter-c) 70%, transparent); color: var(--md-ter-c-on); }

@media (prefers-color-scheme: dark) {
  .achip-java        { background: #1B5E20; color: #81C784; }
  .achip-bedrock     { background: #3E1A00; color: #FFAB76; }
  .achip-datapack    { background: var(--md-pri-c); color: var(--md-pri-c-on); }
  .achip-mod         { background: #1D003A; color: #CEBBFF; }
  .achip-resourcepack{ background: #3F0018; color: #FFB1C8; }
  .achip-shader      { background: #3E1F00; color: #FFDDB5; }
  .achip-addon       { background: var(--md-ter-c); color: var(--md-ter-c-on); }
}

.pcard__desc {
  font-size: .875rem;
  font-weight: 400;
  letter-spacing: .015625rem;
  line-height: 1.65;
  color: var(--md-surv-on);
  flex: 1;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.pcard__actions {
  padding: 8px 8px 10px;
  display: flex;
  gap: 8px;
}

/* Card action buttons — compact */
.cbtn {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  height: 36px;
  padding: 0 12px;
  border-radius: var(--r-sm);
  border: none;
  font-family: inherit;
  font-size: .8125rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  transition: box-shadow var(--dur1) var(--ease);
}
.cbtn::after {
  content: '';
  position: absolute; inset: 0;
  background: currentColor;
  opacity: 0;
  border-radius: inherit;
  transition: opacity var(--dur1) var(--ease);
}
.cbtn:hover::after  { opacity: .08; }
.cbtn:active::after { opacity: .12; }
.cbtn > * { position: relative; }
.cbtn .mi { font-size: 15px; }

.cbtn-sec {
  background: var(--md-sc2);
  color: var(--md-surf-on);
}
.cbtn-pri {
  background: var(--md-pri);
  color: var(--md-pri-on);
  box-shadow: var(--e1);
}
.cbtn-pri:hover { box-shadow: var(--e2); }

/* ── Empty state ─────────────────────────────────────── */
.empty {
  grid-column: 1/-1;
  padding: 64px 16px;
  text-align: center;
  color: var(--md-surv-on);
}
.empty .mi { font-size: 56px; display: block; margin: 0 auto 12px; opacity: .4; }
.empty h3  { font-size: 1.125rem; font-weight: 500; color: var(--md-surf-on); margin-bottom: 4px; }
.empty p   { font-size: .9375rem; }

/* ── Footer ──────────────────────────────────────────── */
.site-footer {
  background: var(--md-sc2);
  border-top: 1px solid var(--md-outv);
  padding: 48px 0 0;
}
.footer__grid {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--pad);
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 40px;
  padding-bottom: 40px;
}
.footer__brand-link {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--md-surf-on);
  text-decoration: none;
  margin-bottom: 10px;
}
.footer__brand-link img {
  width: 32px; height: 32px;
  border-radius: 50%;
  border: 1.5px solid var(--md-outv);
}
.footer__brand-name {
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: .009375rem;
}
.footer__brand-desc {
  font-size: .875rem;
  color: var(--md-surv-on);
  line-height: 1.65;
}
.footer__col-head {
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--md-surv-on);
  margin-bottom: 12px;
}
.footer__links { display: flex; flex-direction: column; gap: 8px; }
.footer__links a {
  font-size: .875rem;
  color: var(--md-surv-on);
  transition: color var(--dur1) var(--ease);
}
.footer__links a:hover { color: var(--md-pri); }
.footer__bottom {
  border-top: 1px solid var(--md-outv);
  padding: 16px var(--pad);
  max-width: var(--max-w);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}
.footer__copy {
  font-size: .75rem;
  color: var(--md-surv-on);
  letter-spacing: .025rem;
}
.footer__legal { display: flex; gap: 20px; }
.footer__legal a {
  font-size: .75rem;
  color: var(--md-surv-on);
  transition: color var(--dur1) var(--ease);
}
.footer__legal a:hover { color: var(--md-pri); }

/* ── Project Page ────────────────────────────────────── */
.page-wrap {
  max-width: 840px;
  margin: 0 auto;
  padding: 24px var(--pad) 80px;
}
.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 36px;
  padding: 0 20px 0 12px;
  border-radius: var(--r-full);
  background: var(--md-sc1);
  color: var(--md-surv-on);
  border: 1px solid var(--md-outv);
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .00625rem;
  text-decoration: none;
  margin-bottom: 24px;
  position: relative;
  overflow: hidden;
  transition: background var(--dur1) var(--ease);
}
.back-btn::after {
  content: '';
  position: absolute; inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity var(--dur1) var(--ease);
}
.back-btn:hover::after { opacity: .08; }
.back-btn .mi { font-size: 18px; position: relative; }
.back-btn span:not(.mi) { position: relative; }

/* Project banner card */
.proj-banner {
  background: var(--md-sc1);
  border: 1px solid var(--md-outv);
  border-radius: var(--r-2xl);
  padding: 40px 32px 32px;
  text-align: center;
  margin-bottom: 12px;
  position: relative;
  overflow: hidden;
}
.proj-banner::before {
  content: '';
  position: absolute; inset: 0;
  pointer-events: none;
  background: radial-gradient(
    ellipse 65% 55% at 50% -10%,
    color-mix(in srgb, var(--md-pri-c) 60%, transparent),
    transparent 65%
  );
}
.proj-banner > * { position: relative; z-index: 1; }

.proj-banner__icon {
  width: 64px; height: 64px;
  border-radius: var(--r-lg);
  display: flex; align-items: center; justify-content: center;
  font-size: 32px;
  margin: 0 auto 20px;
  box-shadow: var(--e2);
  background: var(--md-pri-c);
  color: var(--md-pri-c-on);
}
.proj-banner__icon.teal   { background: var(--md-ter-c);      color: var(--md-ter-c-on);  }
.proj-banner__icon.sc     { background: var(--md-sec-c);      color: var(--md-sec-c-on);  }
.proj-banner__icon.amber  { background: var(--ice-amber-bg);  color: var(--ice-amber);    }
.proj-banner__icon.pink   { background: var(--ice-pink-bg);   color: var(--ice-pink);     }
.proj-banner__icon.purple { background: var(--ice-purple-bg); color: var(--ice-purple);   }
.proj-banner__icon.blue   { background: var(--ice-blue-bg);   color: var(--ice-blue);     }

.proj-banner__title {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
  font-weight: 400;
  letter-spacing: -.01em;
  line-height: 1.15;
  color: var(--md-surf-on);
  margin-bottom: 8px;
}
.proj-banner__sub {
  font-size: 1rem;
  font-weight: 400;
  letter-spacing: .03125rem;
  line-height: 1.6;
  color: var(--md-surv-on);
  margin-bottom: 20px;
}
.proj-banner__chips {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
}

/* Content cards */
.ccard {
  background: var(--md-sc1);
  border: 1px solid var(--md-outv);
  border-radius: var(--r-lg);
  padding: 24px;
  margin-bottom: 12px;
}
.ccard__title {
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: .009375rem;
  color: var(--md-surf-on);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.ccard__title .mi { font-size: 20px; color: var(--md-pri); }
.ccard p {
  font-size: .9375rem;
  line-height: 1.75;
  color: var(--md-surv-on);
  margin-bottom: 12px;
}
.ccard p:last-child { margin-bottom: 0; }
.ccard a { color: var(--md-pri); }

/* Feature list */
.feat-list { display: flex; flex-direction: column; gap: 8px; }
.feat-list li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: .9375rem;
  line-height: 1.55;
  color: var(--md-surv-on);
}
.feat-list li::before {
  content: 'check_circle';
  font-family: 'Material Symbols Rounded', sans-serif;
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 20;
  font-size: 18px;
  color: var(--md-pri);
  flex-shrink: 0;
  margin-top: 2px;
}

/* Download card (primary-container bg) */
.dl-card {
  background: var(--md-pri-c);
  border: 1px solid color-mix(in srgb, var(--md-pri) 25%, transparent);
  border-radius: var(--r-lg);
  padding: 28px 24px;
  text-align: center;
  margin-bottom: 12px;
}
.dl-card__title {
  font-size: 1.375rem;
  font-weight: 400;
  color: var(--md-pri-c-on);
  margin-bottom: 4px;
  letter-spacing: 0;
}
.dl-card__sub {
  font-size: .875rem;
  color: color-mix(in srgb, var(--md-pri-c-on) 70%, transparent);
  margin-bottom: 20px;
  letter-spacing: .015625rem;
}
.dl-card__btns { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }

/* Specs table */
.specs {
  width: 100%;
  border-collapse: collapse;
}
.specs th, .specs td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid var(--md-outv);
  font-size: .875rem;
  line-height: 1.55;
}
.specs th {
  font-weight: 500;
  color: var(--md-surv-on);
  width: 38%;
  letter-spacing: .015625rem;
}
.specs td { color: var(--md-surf-on); }
.specs tr:last-child th, .specs tr:last-child td { border-bottom: none; }

/* ── Animations ──────────────────────────────────────── */
@keyframes zoomIn {
  from { opacity: 0; transform: scale(.6); }
  to   { opacity: 1; transform: scale(1);  }
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0);    }
}
@keyframes cardIn {
  from { opacity: 0; transform: translateY(14px) scale(.98); }
  to   { opacity: 1; transform: translateY(0)    scale(1);   }
}

.pcard:nth-child(1)  { animation-delay: .03s; }
.pcard:nth-child(2)  { animation-delay: .06s; }
.pcard:nth-child(3)  { animation-delay: .09s; }
.pcard:nth-child(4)  { animation-delay: .12s; }
.pcard:nth-child(5)  { animation-delay: .15s; }
.pcard:nth-child(6)  { animation-delay: .18s; }
.pcard:nth-child(7)  { animation-delay: .21s; }
.pcard:nth-child(8)  { animation-delay: .24s; }
.pcard:nth-child(9)  { animation-delay: .27s; }
.pcard:nth-child(10) { animation-delay: .30s; }
.pcard:nth-child(11) { animation-delay: .33s; }
.pcard:nth-child(12) { animation-delay: .36s; }

/* ── Reduced motion ──────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 1ms !important;
    animation-delay: 0ms !important;
    transition-duration: 1ms !important;
  }
}

/* ── Responsive ──────────────────────────────────────── */
@media (max-width: 1024px) {
  .footer__grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 768px) {
  :root { --pad: 16px; }
  .hero { padding: 56px 0 48px; }
  .pgrid { grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }
  .footer__grid { grid-template-columns: 1fr; gap: 32px; }
  .proj-banner { padding: 28px 20px; }
  .ccard { padding: 20px 16px; }
  .top-bar__wordmark { font-size: 1.125rem; }
}
@media (max-width: 480px) {
  .pgrid { grid-template-columns: 1fr; }
  .filter-bar__row { gap: 6px; }
  .search-fld input { width: 128px; }
  .proj-banner__title { font-size: 1.5rem; }
}
"""

# ──────────────────────────────────────────────── Shared HTML ──

GA = """  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K3W2T4M8K8"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-K3W2T4M8K8');</script>
  <!-- Ads -->
  <script src="https://quge5.com/88/tag.min.js" data-zone="226719" async data-cfasync="false"></script>"""

FONTS = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>"""

NAV = """<header class="top-bar" id="top-bar">
  <div class="top-bar__row">
    <a href="index.html" class="top-bar__brand">
      <div class="top-bar__avatar">
        <img src="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp" alt="QuillPhen" width="32" height="32" loading="eager">
      </div>
      <span class="top-bar__wordmark">QuillPhen</span>
    </a>
    <nav class="top-bar__nav">
      <a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener" class="btn-text">
        <svg viewBox="0 0 512 514" aria-hidden="true" width="16" height="16" style="fill:currentColor;flex-shrink:0"><path d="M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"/></svg>
        <span>Modrinth</span>
      </a>
      <a href="https://www.curseforge.com/members/quillphen/projects" target="_blank" rel="noopener" class="btn-text">CurseForge</a>
    </nav>
  </div>
</header>"""

FOOTER = """<footer class="site-footer">
  <div class="footer__grid">
    <div>
      <a href="index.html" class="footer__brand-link">
        <img src="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp" alt="QuillPhen" width="32" height="32" loading="lazy">
        <span class="footer__brand-name">QuillPhen</span>
      </a>
      <p class="footer__brand-desc">Quality-of-life Minecraft mods, data packs, resource packs and shaders for Java &amp; Bedrock Edition.</p>
    </div>
    <div>
      <p class="footer__col-head">Links</p>
      <ul class="footer__links">
        <li><a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener">Modrinth Profile</a></li>
        <li><a href="https://www.curseforge.com/members/quillphen/projects" target="_blank" rel="noopener">CurseForge Profile</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
        <li><a href="rss.xml">RSS Feed</a></li>
      </ul>
    </div>
    <div>
      <p class="footer__col-head">Categories</p>
      <ul class="footer__links">
        <li><a href="index.html#projects">Data Packs</a></li>
        <li><a href="index.html#projects">Mods</a></li>
        <li><a href="index.html#projects">Resource Packs</a></li>
        <li><a href="index.html#projects">Shaders</a></li>
        <li><a href="index.html#projects">Bedrock Addons</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <p class="footer__copy">&copy; 2026 QuillPhen &mdash; Not affiliated with Mojang or Microsoft</p>
    <div class="footer__legal">
      <a href="robots.txt">Robots</a>
      <a href="sitemap.xml">Sitemap</a>
    </div>
  </div>
</footer>"""

MDR_SVG = '<svg viewBox="0 0 512 514" aria-hidden="true" width="14" height="14" style="fill:currentColor;flex-shrink:0"><path d="M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"/></svg>'

PAGE_JS = """<script>
const tb=document.getElementById('top-bar');
window.addEventListener('scroll',()=>tb.classList.toggle('raised',scrollY>8),{passive:true});
</script>"""

# ──────────────────────────────────────────────── Projects ──────

PROJECTS = [
  {'id':'tree-vein-miner','title':'Tree Vein Miner','type':'datapack','edition':'java','icon':'forest','ic':'','mr':'https://modrinth.com/datapack/tree-vein-miner','pg':'tree-vein-miner.html','desc':'Removes entire trees — logs and leaves — when you crouch and break a log. Smart and efficient.','tagline':'Fell entire trees with a single crouched break','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Breaks all connected logs of the same type instantly','Leaves clean up automatically — no floating orphans','Activate by crouching while breaking any log','Respects Fortune and Silk Touch enchantments','Works on all vanilla and modded wood types','Zero performance overhead — pure command-based']},
  {'id':'ore-vein-miner','title':'Ore Vein Miner','type':'datapack','edition':'java','icon':'diamond','ic':'teal','mr':'https://modrinth.com/datapack/ore-vein-miner','pg':'ore-vein-miner.html','desc':'Automatically mines all connected ore blocks of the same type when you break one while crouching.','tagline':'Mine entire ore veins in a single swing','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Mines the full connected vein from one break','Proper Fortune and Silk Touch support','Triggered by crouching while mining','Handles all vanilla ores including deepslate variants','No mod loader required','SMP compatible — works for all players']},
  {'id':'vein-miner','title':'VeinMiner','type':'datapack','edition':'java','icon':'hardware','ic':'','mr':'https://modrinth.com/datapack/vein_miner','pg':'vein-miner.html','desc':'Mine entire ore veins and fell whole trees efficiently. A lightweight chain-mining data pack.','tagline':'Combined ore and tree chain-mining in one pack','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Chain-mines entire ore veins from one break','Fells complete trees — logs and leaves','Respects tool enchantments (Fortune, Silk Touch)','Crouch-to-activate for full player control','Compatible with all vanilla wood and ore types','Minimal overhead']},
  {'id':'cave-vision','title':'Night Vision','type':'datapack','edition':'java','icon':'remove_red_eye','ic':'','mr':'https://modrinth.com/datapack/cave-vision','pg':'cave-vision.html','desc':'Grants all players permanent Night Vision — caves and dark areas are effortlessly bright without potions.','tagline':'Permanent Night Vision for every player','versions':'1.14 – 1.21+','loader':'Vanilla Data Pack','features':['Grants perpetual Night Vision to all online players','No potions or brewing stands required','Works in caves, the Nether, and the End','Automatically re-applies if the effect expires','Zero performance cost — lightweight tick loop','Compatible with every SMP and singleplayer world']},
  {'id':'enchantment-descriptions','title':'Enchantment Descriptions','type':'resourcepack','edition':'java','icon':'auto_stories','ic':'pink','mr':'https://modrinth.com/datapack/enchantment-descriptions-java','pg':'enchantment-descriptions.html','desc':'Adds detailed descriptions for every vanilla enchantment directly in the tooltip.','tagline':'Know exactly what every enchantment does','versions':'1.20 – 1.21+','loader':'Resource Pack (no mods needed)','features':['Tooltip descriptions for all 40+ vanilla enchantments','Clear, concise language — no wiki required','Shows compatibility, max level, and effect details','Works with any mod loader or vanilla clients','Drag-and-drop installation — no config needed','Updated for the latest Minecraft versions']},
  {'id':'vein-miner-preview','title':'Vein Miner & Preview','type':'datapack','edition':'java','icon':'preview','ic':'teal','mr':'https://modrinth.com/datapack/the-vein-miner','pg':'vein-miner-preview.html','desc':'Universal vein miner supporting Silk Touch, durability handling, and visual previews on 1.14–1.21+.','tagline':'Vein mining with a real-time visual preview','versions':'1.14 – 1.21+','loader':'Vanilla Data Pack','features':['Mines full ore veins in a single break','Visual preview shows which blocks will be mined','Fortune and Silk Touch enchantment support','Tool durability consumed correctly per block','Crouch to activate — per-player','Broad version support from 1.14 through 1.21+']},
  {'id':'glowing-ore','title':'Glowing Ores','type':'resourcepack','edition':'java','icon':'flare','ic':'amber','mr':'https://modrinth.com/resourcepack/glowing-ores-java','pg':'glowing-ore.html','desc':'Transforms all 18 ore blocks into brilliant glowing treasures with a 5-tier intensity system.','tagline':'Every ore block glows with emissive light','versions':'1.17 – 1.21+','loader':'Resource Pack (OptiFine / Iris recommended)','features':['Emissive glow textures for all 18 ore variants','Normal and deepslate ore variants covered','Five hand-tuned intensity tiers by ore rarity','Pulsing animation on diamond and netherite ores','Compatible with OptiFine and Iris shaders','Clean design — not oversaturated']},
  {'id':'dynamic-lighting','title':'Dynamic Lighting','type':'datapack','edition':'java','icon':'flashlight_on','ic':'amber','mr':'https://modrinth.com/datapack/dynamic-lighting','pg':'dynamic-lighting.html','desc':'Emits real-time light from held light-emitting items and glowing entities — no mods required.','tagline':'Held torches and lanterns actually light your way','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Light sources held in hand illuminate nearby blocks','Supports torches, lanterns, glowstone, sea lanterns','Glowing entities emit light dynamically','No OptiFine or Sodium/Iris required','Smooth interpolation as you move','Compatible with all game modes and dimensions']},
  {'id':'tree-veinminer-enchant','title':'Tree Veinminer Enchantment','type':'datapack','edition':'java','icon':'auto_fix_high','ic':'amber','mr':'https://modrinth.com/datapack/tree-veinminer-enchant','pg':'tree-veinminer-enchant.html','desc':'Adds a Tree Veinminer enchantment for axes — instantly fell entire trees with a single chop.','tagline':'Enchant your axe to fell whole trees at once','versions':'1.20 – 1.21+','loader':'Vanilla Data Pack','features':['New Tree Veinminer enchantment available for axes','Fells the entire connected tree instantly on break','Obtainable via enchanting table and loot tables','Balances power with durability cost per log','Leaves clean up automatically','Works with all vanilla and modded wood types']},
  {'id':'explosive-arrow','title':'TNT Arrow','type':'datapack','edition':'java','icon':'rocket_launch','ic':'pink','mr':'https://modrinth.com/datapack/tnt-arrow','pg':'explosive-arrow.html','desc':'Adds explosive TNT arrows that detonate on impact. Great for combat and rapid terrain clearing.','tagline':'Explosive arrows that detonate on impact','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['TNT arrows explode on impact with any surface or entity','Configurable explosion radius and power','Craft TNT arrows with a simple recipe','Deals AoE damage — effective in PvP and mob farms','Explosion particles and sound effects included','Toggle mob griefing to control terrain damage']},
  {'id':'potions-description','title':'Potions Description','type':'resourcepack','edition':'java','icon':'science','ic':'purple','mr':'https://modrinth.com/datapack/potions-description','pg':'potions-description.html','desc':'Provides clear, detailed tooltip descriptions for every potion in the game. Brew smarter.','tagline':'Every potion explained in plain language','versions':'1.20 – 1.21+','loader':'Resource Pack (no mods needed)','features':['Tooltip text for every brewed and splash potion','Shows duration, potency, and effect description','Covers all vanilla potion types including extended/enhanced','Lingering and splash variants included','Works without any mod loader','Drag-and-drop installation']},
  {'id':'dynamic-light-shader','title':'Dynamic Light Shader','type':'shader','edition':'java','icon':'auto_awesome','ic':'amber','mr':'https://modrinth.com/shader/dynamic-light-shader','pg':'dynamic-light-shader.html','desc':'Lightweight Iris/OptiFine shader that makes held items emit visible light with a glow bloom.','tagline':'Shader-quality glow bloom for held light sources','versions':'1.17 – 1.21+','loader':'OptiFine / Iris (Sodium)','features':['Realistic bloom glow from held torches and lanterns','Minimal performance cost — highly optimised GLSL','Compatible with Iris (Sodium) and OptiFine','Configurable bloom radius and intensity','Stacks nicely with other shader packs','Works in all dimensions']},
  {'id':'auto-builder','title':'Auto Builder','type':'datapack','edition':'java','icon':'construction','ic':'teal','mr':'https://modrinth.com/datapack/auto-bridge','pg':'auto-builder.html','desc':'Automatically places blocks beneath you as you walk forward — perfect for bridges and paths.','tagline':'Auto-bridge as you walk over any gap','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Automatically places held block under your feet','Walk forward over any gap to instantly bridge','Works with any solid buildable block','Activate by crouching while walking','No mod loader required','Great for sky bridges and SMP builds']},
  {'id':'outlined-ores','title':'Outlined Ores','type':'resourcepack','edition':'java','icon':'border_outer','ic':'teal','mr':'https://modrinth.com/resourcepack/outlined-ores-java','pg':'outlined-ores.html','desc':'Highlights ore blocks with glowing outlines for better visibility without X-ray cheating.','tagline':'Glowing outlines on all ore blocks for easy spotting','versions':'1.17 – 1.21+','loader':'Resource Pack (OptiFine / Iris recommended)','features':['High-contrast outlines on all 18 ore variants','Visible against stone, deepslate, and netherrack','Unique colour per ore type for fast recognition','Works with emissive-compatible shaders','Only visible on exposed faces — no X-ray','Compatible with most other texture packs']},
  {'id':'mob-capture-orb','title':'Mob Capture ORB','type':'mod','edition':'java','icon':'cruelty_free','ic':'amber','mr':'https://modrinth.com/mod/mob-capture-orb','pg':'mob-capture-orb.html','desc':'Capture any mob in a magical orb, carry it in your inventory, and release it wherever you want.','tagline':'Capture, carry, and release any mob with an orb','versions':'1.20 – 1.21+','loader':'Fabric / Forge / NeoForge','features':['Capture any mob — passive, neutral, and hostile','Captured mobs stored as inventory items','Mob health, equipment, and NBT data preserved','Craftable orbs with a simple recipe','Release by right-clicking any surface','Compatible with all major mod loaders']},
  {'id':'auto-replant-crops','title':'Auto Replant Crops','type':'datapack','edition':'java','icon':'grass','ic':'','mr':'https://modrinth.com/datapack/auto-replant-crops','pg':'auto-replant-crops.html','desc':'Automatically replants fully grown crops after harvesting. Lightweight QoL for survival and SMP.','tagline':'Harvest without replanting — crops regrow automatically','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Harvesting a mature crop auto-replants it','Works for wheat, carrots, potatoes, beetroot','Seeds consumed from inventory on replant','If no seeds available, crop drops normally','Zero performance cost on large farms','SMP-friendly per-player seed check']},
  {'id':'ore-veinminer-enchant','title':'Ore Veinminer Enchantment','type':'datapack','edition':'java','icon':'auto_fix_high','ic':'teal','mr':'https://modrinth.com/datapack/ore-veinminer-enchant','pg':'ore-veinminer-enchant.html','desc':'Adds an Ore Veinminer enchantment for pickaxes — instantly mine entire ore veins with one swing.','tagline':'Enchant your pickaxe to clear full ore veins','versions':'1.20 – 1.21+','loader':'Vanilla Data Pack','features':['New Ore Veinminer enchantment for pickaxes','Mines the entire connected vein on a single break','Obtainable at the enchanting table','Fortune and Silk Touch work on the full vein','Durability cost scales with blocks mined','Works for all vanilla and deepslate ore variants']},
  {'id':'coordinates-hud','title':'Coordinates HUD','type':'mod','edition':'java','icon':'gps_fixed','ic':'blue','mr':'https://modrinth.com/mod/coordinateshud','pg':'coordinates-hud.html','desc':'Advanced coordinate display mod with fully customizable HUD showing coordinates, biome, compass direction, and more.','tagline':'Clean, configurable coordinates and biome HUD','versions':'1.20 – 1.21+','loader':'Fabric / Forge / NeoForge','features':['Real-time X, Y, Z coordinate display','Current biome name and dimension shown','Compass direction and facing angle','Fully configurable position, size, and colour','Toggle HUD visibility with a keybind','Minimal performance impact']},
  {'id':'ai-crafter','title':'Minecraft AI Assistant','type':'mod','edition':'java','icon':'smart_toy','ic':'purple','mr':'https://modrinth.com/mod/minecraft-ai-assistant','pg':'ai-crafter.html','desc':'Brings Google Gemini AI into Minecraft — ask questions, get help, and execute commands via natural language.','tagline':'Google Gemini AI as your Minecraft companion','versions':'1.21.5+','loader':'Fabric / Forge / NeoForge / Quilt','features':['Ask any Minecraft question in natural language via /ai','Execute commands by describing them via /aic','Powered by Google Gemini 2.5 Flash and Pro','API key stored locally — no data collected','Survival-mode protection blocks cheat commands','Configure via in-game menu (K key)'],'extra':'<p>Requires a free Google Gemini API key from <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener">Google AI Studio</a>. Press <strong>K</strong> in-game to open config and paste your key.</p>'},
  {'id':'mob-vision','title':'Mob Vision','type':'datapack','edition':'java','icon':'person_search','ic':'amber','mr':'https://modrinth.com/datapack/mobvision','pg':'mob-vision.html','desc':'Applies a glowing effect to mobs near you so you can spot enemies through walls within a configurable radius.','tagline':'See nearby mobs through walls with a glow effect','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Applies Glowing status to all mobs within range','Configurable detection radius (default 20 blocks)','Works on all hostile, neutral, and passive mobs','Effect removed when mob moves out of range','No mod loader required','Useful for caving, raiding, and PvP']},
  {'id':'waypoints','title':'Waypoints & Teleport','type':'datapack','edition':'java','icon':'place','ic':'pink','mr':'https://modrinth.com/datapack/waypoints-teleport','pg':'waypoints.html','desc':'Lightweight survival-friendly waypoint system with fast travel and teleports for singleplayer and SMP.','tagline':'Save locations and teleport between them in survival','versions':'1.21.6+','loader':'Vanilla Data Pack','features':['Set named waypoints anywhere in the world','Teleport to any saved waypoint instantly','Per-player storage — private to each player','Works in all dimensions — Overworld, Nether, End','List and delete waypoints via simple commands','No mods required — pure vanilla commands']},
  {'id':'insight-hud','title':'Insight HUD','type':'mod','edition':'java','icon':'dashboard','ic':'teal','mr':'https://modrinth.com/mod/insight-hud','pg':'insight-hud.html','desc':'Two essential HUD overlays showing detailed entity information and equipment stats — clean and vanilla-friendly.','tagline':'Entity info and gear stats in a clean overlay','versions':'1.20 – 1.21+','loader':'Fabric / Forge / NeoForge','features':['Gear & Item Insight: live durability and stats for held/worn items','Combat HUD: target health and loot table while in battle','Minimalist design — no screen clutter','Toggle each module independently (H key)','Fully configurable position and appearance','Lightweight — minimal performance cost']},
  {'id':'smithing-templates-descriptions','title':'Smithing Templates Descriptions','type':'mod','edition':'java','icon':'description','ic':'blue','mr':'https://modrinth.com/mod/smithing-templates-descriptions','pg':'smithing-templates-descriptions.html','desc':'Replaces smithing template names with detailed multi-line descriptions including usage, duplication, and lore.','tagline':'Full descriptions on every smithing template','versions':'1.20 – 1.21+','loader':'Fabric / Forge / NeoForge','features':['Every smithing template gets a multi-line tooltip','Shows the armor/weapon upgrade effect it applies','Duplication recipe shown inline in the tooltip','Where to find it — biome and structure hint','Lore text for Netherite Upgrade and trims','Works out of the box with no configuration']},
  {'id':'stackable-item','title':'Stackable Item','type':'datapack','edition':'java','icon':'inventory_2','ic':'blue','mr':'https://modrinth.com/datapack/stackable-item','pg':'stackable-item.html','desc':'Makes potions, boats, saddles, totems, and more stackable — keep your inventory clean and organised.','tagline':'Stack potions, saddles, totems, and more','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Potions stack up to 16 per slot','Saddles, boats, minecarts, and name tags stack','Totems of Undying and shields stack','Ender pearls and snowballs stack to 64','No mod loader required','Reduces inventory clutter dramatically']},
  {'id':'smart-arrows','title':'Smart Arrows','type':'mod','edition':'java','icon':'arrow_forward','ic':'teal','mr':'https://modrinth.com/mod/smart-arrows','pg':'smart-arrows.html','desc':'Arrow mechanics overhaul — arrows can ricochet off surfaces and teleport the shooter on contact.','tagline':'Ricocheting and teleporting arrow mechanics','versions':'1.20 – 1.21+','loader':'Fabric / Forge / NeoForge','features':['Arrows ricochet off hard surfaces at realistic angles','Special arrow type: Teleport (blink to impact point)','Configurable ricochet count and friction','Compatible with existing enchantments','New crafting recipes for special arrow variants','Works on multiplayer servers']},
  {'id':'automatic-smelt','title':'Automatic Smelt','type':'datapack','edition':'java','icon':'local_fire_department','ic':'amber','mr':'https://modrinth.com/datapack/automatic-smelt','pg':'automatic-smelt.html','desc':'Every block you mine that can be smelted automatically drops its smelted form — no furnace needed.','tagline':'Mine blocks and get their smelted drops instantly','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Auto-smelts ore blocks (raw iron, gold, copper) on break','Sand drops glass, cobblestone drops stone','Works with Fortune for bonus drops','Activates when you have the correct tool held','No furnaces needed for common smelting tasks','Toggle via simple in-game command']},
  {'id':'custom-vein-miner','title':'Custom Vein Miner','type':'datapack','edition':'java','icon':'tune','ic':'','mr':'https://modrinth.com/datapack/custom-vm','pg':'custom-vein-miner.html','desc':'Mine entire ore veins and fell whole trees with full Fortune and Silk Touch support. Highly customizable.','tagline':'Fully configurable vein mining data pack','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Configurable max vein size (default 64 blocks)','Separate toggle for ore veins vs tree felling','Full Fortune and Silk Touch enchantment support','Custom block whitelist/blacklist via config file','Per-player toggle with persistent settings','Balanced durability consumption per block']},
  {'id':'automatic-smelt-tools','title':'Automatic Smelt Tools','type':'datapack','edition':'java','icon':'construction','ic':'amber','mr':'https://modrinth.com/datapack/automatic-smelt-tools','pg':'automatic-smelt-tools.html','desc':'Tool-based Auto Smelt — equip smelting tools and let blocks drop their smelted forms automatically.','tagline':'Craft Auto Smelt tools to smelt blocks on break','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Craftable "smelting" variants of pickaxe, axe, shovel','Equipped smelting tool auto-smelts mined blocks','Works with all smeltable blocks and ores','Fortune equivalent bonus on smelted drops','Tools have standard durability','Per-tool control — mix and match as needed']},
  {'id':'better-mob-heads','title':'Better Mob Heads','type':'datapack','edition':'java','icon':'face','ic':'','mr':'https://modrinth.com/datapack/better-mob-heads','pg':'better-mob-heads.html','desc':'Gives vanilla mobs unique decorative head drops when slain, perfect for building and collecting.','tagline':'Unique decorative heads from every vanilla mob','versions':'1.17 – 1.21+','loader':'Vanilla Data Pack','features':['Unique head item for every vanilla mob on death','Heads are decorative blocks — place them anywhere','Drop rate configurable (default ~10%)','Looting enchantment increases drop chance','Does not interfere with existing mob drops','Hundreds of unique player head textures used']},
  {'id':'cave-vision-bedrock','title':'Cave Vision Bedrock','type':'addon','edition':'bedrock','icon':'remove_red_eye','ic':'teal','mr':'https://modrinth.com/user/quillphen','cf':'https://www.curseforge.com/minecraft-bedrock/addons/cave-vision-bedrock','pg':'cave-vision-bedrock.html','desc':'Lightweight Bedrock addon granting infinite Night Vision — explore any cave without torches or shaders.','tagline':'Permanent Night Vision for Bedrock Edition','versions':'1.20+','loader':'Bedrock Addon (.mcaddon)','features':['Permanent Night Vision on all players','Works in caves, the Nether, and the End','Import with a single .mcaddon file','No shaders or resource packs required','Compatible with Marketplace content','Works on Bedrock, Education Edition, and Realms']},
  {'id':'x-ray-java','title':'X-RAY Java Edition','type':'resourcepack','edition':'java','icon':'visibility','ic':'pink','mr':'https://modrinth.com/user/quillphen','cf':'https://www.curseforge.com/minecraft/mc-mods/x-ray-java-edition','pg':'x-ray-java.html','desc':'Makes stone blocks semi-transparent and highlights all ore types for easy mining in Java Edition.','tagline':'See through stone to find ores instantly','versions':'1.17 – 1.21+','loader':'Resource Pack (OptiFine required)','features':['Stone, dirt, and filler blocks rendered transparent','All ore types highlighted with bright colours','Unique colour per ore for instant identification','Configurable transparency level','Works with OptiFine custom textures','For singleplayer or approved servers only']},
  {'id':'dynamic-lighting-mcpe','title':'Dynamic Lighting MCPE','type':'addon','edition':'bedrock','icon':'lightbulb','ic':'amber','mr':'https://modrinth.com/user/quillphen','cf':'https://www.curseforge.com/minecraft/mc-mods/dynamic-lightings','pg':'dynamic-lighting-mcpe.html','desc':'Real-time dynamic lighting for Bedrock — torches, lanterns, and glowstone light up when held.','tagline':'Held light sources illuminate Bedrock worlds','versions':'1.20+','loader':'Bedrock Addon (.mcaddon)','features':['Dynamic light emitted from held torches and lanterns','Glowstone, sea lanterns, and glow berries supported','Works without Render Dragon shaders','Compatible with Realm and local worlds','No RTX required','Lightweight behavior pack']},
]

TYPE_LABELS = {'datapack':'Data Pack','mod':'Mod','resourcepack':'Resource Pack','shader':'Shader','addon':'Bedrock Addon'}
EDITION_LABELS = {'java':'Java Edition','bedrock':'Bedrock Edition'}

# ──────────────────────────────────────────── Write CSS ──

def write_css():
    with open(os.path.join(BASE, 'styles.css'), 'w', encoding='utf-8') as f:
        f.write(CSS)
    print(f'  styles.css ({len(CSS):,} chars)')

# ──────────────────────────────────────────── Index HTML ──

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
__GA__
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QuillPhen &ndash; Minecraft Mods, Data Packs &amp; Resource Packs</title>
  <meta name="description" content="Quality-of-life Minecraft mods, data packs, resource packs, and shaders for Java and Bedrock Edition. 32 projects by QuillPhen on Modrinth.">
  <meta name="keywords" content="minecraft mods, minecraft data packs, minecraft resource packs, quillphen, vein miner, tree vein miner, enchantment descriptions, glowing ores, cave vision, dynamic lighting, insight hud, coordinates hud">
  <meta name="author" content="QuillPhen">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://quillphen.netlify.app/">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://quillphen.netlify.app/">
  <meta property="og:title" content="QuillPhen &ndash; Minecraft Mods &amp; Data Packs">
  <meta property="og:description" content="Quality-of-life Minecraft mods, data packs, resource packs, and shaders. 32 projects for Java and Bedrock Edition.">
  <meta property="og:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">
  <meta property="og:site_name" content="QuillPhen">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">
  <meta name="theme-color" content="#006E1C">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="manifest" href="manifest.json">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">
  <link rel="alternate" type="application/rss+xml" title="QuillPhen Updates" href="/rss.xml">
__FONTS__
  <link rel="preload" href="styles.css" as="style">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"QuillPhen","description":"Quality-of-life Minecraft mods, data packs, resource packs, and shaders","url":"https://quillphen.netlify.app/","author":{"@type":"Person","name":"QuillPhen","url":"https://modrinth.com/user/quillphen"},"sameAs":["https://modrinth.com/user/quillphen"]}</script>
</head>
<body>
__NAV__

<section class="hero" aria-label="QuillPhen">
  <div class="wrap hero__inner">
    <div class="hero__avatar">
      <img src="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp" alt="QuillPhen" width="88" height="88" fetchpriority="high">
    </div>
    <h1 class="hero__title">QuillPhen</h1>
    <p class="hero__sub">Quality-of-life mods, data packs, resource packs &amp; shaders<br>for Minecraft Java and Bedrock Edition</p>
    <div class="hero__badges">
      <span class="badge">32 Projects on Modrinth</span>
      <span class="badge">Java &amp; Bedrock</span>
      <span class="badge">Mods &middot; Data Packs &middot; Shaders</span>
    </div>
    <div class="hero__ctas">
      <a href="https://modrinth.com/user/quillphen" target="_blank" rel="noopener" class="btn-filled">
        <svg viewBox="0 0 512 514" width="16" height="16" style="fill:currentColor;flex-shrink:0"><path d="M503.16 323.56C461.56 400.02 379.27 452 285.32 452c-130.06 0-235.86-103.77-237.44-233.48L29.7 207.04c1.39 64.97 28.67 123.12 72.03 165.71a229.89 229.89 0 0 1-15.99-72.47l32.45 11.27c4.82 75.4 57.32 137.94 127.83 159.15a232.6 232.6 0 0 1-38.61-6.8c40.55 23.63 87.55 37.21 137.79 37.21 85.73 0 162.17-39.65 212.04-101.75l-54.08-75.8zm-230.77 93.4-.2-.12zm223.2-155.06C484.3 180.93 427.08 121.69 353.24 95.24c-72.61-26-160.21-13.28-219.15 40.64l-55.67-73.08C133.33 14.08 251.95-12.71 360.7 27.21c76.38 27.32 140.07 81.73 178.9 151.68l-44.01-7.8a232.24 232.24 0 0 1 4.49 78.73l-4.69-37.92zM27.41 288.33C19.76 251.07 20.31 211.29 31.92 174l36.17 50.41c-2.53 17.86-3.36 37.14-2.02 56.37L27.41 288.33z"/></svg>
        View on Modrinth
      </a>
      <a href="#projects" class="btn-tonal">Browse Projects</a>
    </div>
  </div>
</section>

<div class="filter-bar" id="filter-bar">
  <div class="filter-bar__row" role="group" aria-label="Filter projects">
    <button class="fchip on"      data-f="all"         aria-pressed="true">
      <span class="mi fchip__ck">check</span><span class="fchip__label">All</span>
    </button>
    <button class="fchip" data-f="datapack"    aria-pressed="false">
      <span class="mi fchip__ck">check</span><span class="fchip__label">Data Packs</span>
    </button>
    <button class="fchip" data-f="mod"         aria-pressed="false">
      <span class="mi fchip__ck">check</span><span class="fchip__label">Mods</span>
    </button>
    <button class="fchip" data-f="resourcepack" aria-pressed="false">
      <span class="mi fchip__ck">check</span><span class="fchip__label">Resource Packs</span>
    </button>
    <button class="fchip" data-f="shader"      aria-pressed="false">
      <span class="mi fchip__ck">check</span><span class="fchip__label">Shaders</span>
    </button>
    <button class="fchip" data-f="addon"       aria-pressed="false">
      <span class="mi fchip__ck">check</span><span class="fchip__label">Bedrock</span>
    </button>
    <label class="search-fld" for="search">
      <span class="mi">search</span>
      <input type="search" id="search" placeholder="Search projects&hellip;" autocomplete="off">
    </label>
  </div>
</div>

<main class="wrap projects-sec" id="projects">
  <div class="sec-head">
    <h2 class="sec-title">Projects</h2>
    <span class="cnt-badge" id="cnt">32</span>
  </div>
  <div class="pgrid" id="pgrid"></div>
</main>

__FOOTER__

<script>
const MDR=`__MDR__`;
const TL={datapack:'Data Pack',mod:'Mod',resourcepack:'Resource Pack',shader:'Shader',addon:'Bedrock Addon'};
const PROJECTS=__PROJECTS_JSON__;
let AF='all',AS='';
function render(){
  const q=AS.toLowerCase();
  const list=PROJECTS.filter(p=>(AF==='all'||p.type===AF)&&(!q||p.title.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q)));
  document.getElementById('cnt').textContent=list.length;
  const g=document.getElementById('pgrid');
  if(!list.length){
    g.innerHTML='<div class="empty"><span class="mi">search_off</span><h3>No projects found</h3><p>Try a different filter or keyword.</p></div>';
    return;
  }
  g.innerHTML=list.map((p,i)=>`<article class="pcard" data-type="${p.type}" data-edition="${p.edition}" style="animation-delay:${Math.min(i,11)*.03+.03}s">
<div class="pcard__body">
<div class="pcard__head">
<div class="ic ${p.ic}" aria-hidden="true"><span class="mi">${p.icon}</span></div>
<div class="pcard__meta">
<h3 class="pcard__title">${p.title}</h3>
<div class="pcard__chips">
<span class="achip achip-${p.edition}">${p.edition==='java'?'Java':'Bedrock'}</span>
<span class="achip achip-${p.type}">${TL[p.type]||p.type}</span>
</div>
</div></div>
<p class="pcard__desc">${p.desc}</p>
</div>
<div class="pcard__actions">
<a href="${p.pg}" class="cbtn cbtn-sec"><span class="mi">info</span>Details</a>
<a href="${p.mr}" target="_blank" rel="noopener" class="cbtn cbtn-pri">${MDR}Modrinth</a>
</div></article>`).join('');
}
document.querySelectorAll('.fchip').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.fchip').forEach(c=>{c.classList.remove('on');c.setAttribute('aria-pressed','false');});
  b.classList.add('on');b.setAttribute('aria-pressed','true');
  AF=b.dataset.f;render();
  document.getElementById('projects').scrollIntoView({behavior:'smooth',block:'start'});
}));
document.getElementById('search').addEventListener('input',e=>{AS=e.target.value.trim();render();});
const tb=document.getElementById('top-bar');
const fb=document.getElementById('filter-bar');
window.addEventListener('scroll',()=>{
  tb.classList.toggle('raised',scrollY>8);
  fb.classList.toggle('stuck',fb.getBoundingClientRect().top<=64);
},{passive:true});
render();
</script>
</body>
</html>"""

def write_index():
    projects_json = json.dumps(
        [{'id':p['id'],'title':p['title'],'type':p['type'],'edition':p['edition'],'icon':p['icon'],'ic':p['ic'],'mr':p['mr'],'pg':p['pg'],'desc':p['desc']} for p in PROJECTS],
        separators=(',',':')
    )
    html = INDEX_HTML
    html = html.replace('__GA__',     GA)
    html = html.replace('__FONTS__',  FONTS)
    html = html.replace('__NAV__',    NAV)
    html = html.replace('__FOOTER__', FOOTER)
    html = html.replace('__MDR__',    MDR_SVG.replace('`', r'\`'))
    html = html.replace('__PROJECTS_JSON__', projects_json)
    with open(os.path.join(BASE, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  index.html ({len(html):,} chars)')

# ──────────────────────────────────────────────── Project pages ──

def build_page(p):
    ed   = EDITION_LABELS.get(p['edition'], p['edition'])
    ty   = TYPE_LABELS.get(p['type'], p['type'])
    url  = f"https://quillphen.netlify.app/{p['pg']}"
    feat = '\n'.join(f'<li>{f}</li>' for f in p.get('features', []))
    extra = p.get('extra', '')
    cf_btn1 = (f'        <a href="{p["cf"]}" target="_blank" rel="noopener" class="btn-tonal"><span class="mi" style="font-size:16px">download</span>CurseForge</a>\n') if p.get('cf') else ''
    cf_btn2 = cf_btn1
    ld = json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":p['title'],"description":p['desc'],"url":url,"applicationCategory":"GameApplication","operatingSystem":f"Minecraft {ed}","author":{"@type":"Person","name":"QuillPhen","url":"https://modrinth.com/user/quillphen"},"downloadUrl":p['mr'],"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}, separators=(',',':'))

    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        + GA + '\n'
        + f'  <meta charset="UTF-8">\n'
        f'  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{p["title"]} &ndash; {p["tagline"]} | QuillPhen</title>\n'
        f'  <meta name="description" content="{p["desc"]} By QuillPhen on Modrinth.">\n'
        f'  <meta name="author" content="QuillPhen">\n'
        f'  <meta name="robots" content="index, follow">\n'
        f'  <link rel="canonical" href="{url}">\n'
        f'  <meta property="og:type" content="article">\n'
        f'  <meta property="og:url" content="{url}">\n'
        f'  <meta property="og:title" content="{p["title"]} &mdash; {p["tagline"]} | QuillPhen">\n'
        f'  <meta property="og:description" content="{p["desc"]}">\n'
        f'  <meta property="og:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">\n'
        f'  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:image" content="https://cdn.modrinth.com/data/MGf2bGd9/2719043ab9e48b7b4913986c96b2d5edbcffce7f_96.webp">\n'
        f'  <meta name="theme-color" content="#006E1C">\n'
        f'  <link rel="icon" type="image/x-icon" href="favicon.ico">\n'
        f'  <link rel="manifest" href="manifest.json">\n'
        + FONTS + '\n'
        f'  <link rel="preload" href="styles.css" as="style">\n'
        f'  <link rel="stylesheet" href="styles.css">\n'
        f'  <script type="application/ld+json">{ld}</script>\n'
        '</head>\n'
        '<body>\n'
        + NAV + '\n'
        '<main>\n'
        '  <div class="page-wrap">\n'
        f'    <a href="index.html" class="back-btn">\n'
        f'      <span class="mi">arrow_back</span>All Projects\n'
        f'    </a>\n\n'
        f'    <div class="proj-banner">\n'
        f'      <div class="proj-banner__icon {p["ic"]}">\n'
        f'        <span class="mi">{p["icon"]}</span>\n'
        f'      </div>\n'
        f'      <h1 class="proj-banner__title">{p["title"]}</h1>\n'
        f'      <p class="proj-banner__sub">{p["tagline"]}</p>\n'
        f'      <div class="proj-banner__chips">\n'
        f'        <span class="achip achip-{p["edition"]}">{ed}</span>\n'
        f'        <span class="achip achip-{p["type"]}">{ty}</span>\n'
        f'      </div>\n'
        f'    </div>\n\n'
        f'    <div class="dl-card">\n'
        f'      <p class="dl-card__title">Download</p>\n'
        f'      <p class="dl-card__sub">Free to download &mdash; open-source and community supported</p>\n'
        f'      <div class="dl-card__btns">\n'
        f'        <a href="{p["mr"]}" target="_blank" rel="noopener" class="btn-filled">{MDR_SVG}&thinsp;Get on Modrinth</a>\n'
        + cf_btn1
        + f'        <a href="index.html" class="btn-outlined">Browse All</a>\n'
        '      </div>\n'
        '    </div>\n\n'
        f'    <div class="ccard">\n'
        f'      <h2 class="ccard__title"><span class="mi">info</span>About</h2>\n'
        f'      <p>{p["desc"]}</p>\n'
        + (f'      {extra}\n' if extra else '')
        + f'    </div>\n\n'
        f'    <div class="ccard">\n'
        f'      <h2 class="ccard__title"><span class="mi">star</span>Key Features</h2>\n'
        f'      <ul class="feat-list">\n'
        f'        {feat}\n'
        f'      </ul>\n'
        f'    </div>\n\n'
        f'    <div class="ccard">\n'
        f'      <h2 class="ccard__title"><span class="mi">tune</span>Compatibility</h2>\n'
        f'      <table class="specs">\n'
        f'        <tr><th>Edition</th><td>{ed}</td></tr>\n'
        f'        <tr><th>Type</th><td>{ty}</td></tr>\n'
        f'        <tr><th>Game Versions</th><td>{p["versions"]}</td></tr>\n'
        f'        <tr><th>Loader</th><td>{p["loader"]}</td></tr>\n'
        f'        <tr><th>License</th><td>MIT</td></tr>\n'
        f'        <tr><th>Author</th><td>QuillPhen</td></tr>\n'
        f'      </table>\n'
        f'    </div>\n\n'
        f'    <div class="dl-card">\n'
        f'      <p class="dl-card__title">Ready to install?</p>\n'
        f'      <p class="dl-card__sub">Download for free and drop it into your Minecraft world</p>\n'
        f'      <div class="dl-card__btns">\n'
        f'        <a href="{p["mr"]}" target="_blank" rel="noopener" class="btn-filled">{MDR_SVG}&thinsp;Download from Modrinth</a>\n'
        + cf_btn2
        + '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '</main>\n'
        + FOOTER + '\n'
        + PAGE_JS + '\n'
        '</body>\n'
        '</html>'
    )

def write_pages():
    for p in PROJECTS:
        path = os.path.join(BASE, p['pg'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(build_page(p))
        print(f'  {p["pg"]}')

# ──────────────────────────────────────────────── Sitemap ──

def write_sitemap():
    pages  = [('index.html','1.0','weekly')]
    pages += [(p['pg'],'0.8','monthly') for p in PROJECTS]
    lines  = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pg, pri, freq in pages:
        lines.append(f'  <url>\n    <loc>https://quillphen.netlify.app/{pg}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>')
    lines.append('</urlset>')
    with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  sitemap.xml ({len(pages)} URLs)')

# ──────────────────────────────────────────────── Run ──

print('QuillPhen – M3 Rebuild')
print('=' * 44)
print('Writing CSS...');       write_css()
print('Writing index.html...'); write_index()
print('Writing project pages...'); write_pages()
print('Writing sitemap...');   write_sitemap()
print('=' * 44)
print('Done.')
