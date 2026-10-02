---
name: distinct-web-design
description: Design and build websites and web pages that do not look AI-generated. Use for any landing page, marketing site, product/app UI, portfolio, docs site or HTML page where visual quality matters, and when asked to redesign or "make less AI-looking". Grounds the design in the subject and a real design tradition, applies typography/grid/color theory from leading designers, bans first- and second-order AI-design tells (including the "tasteful" anti-slop defaults), and requires a screenshot critique loop before delivery.
---

# Distinct web design

AI-made sites are recognisable because every model reaches for the same defaults — and the popular
"anti-slop" skills have created a second set of defaults (cream + terracotta, black + acid green,
broadsheet layouts, mono caps labels). This skill avoids both by deciding from the **subject**, a
**real design tradition** and **theory**, then **looking at the result** before shipping.

Read the references when you reach the step that needs them:
- `references/theory.md` — typography, hierarchy, grid, colour, spacing rules with numbers.
- `references/tells.md` — AI tells (obvious and "tasteful"), each with what to do instead.
- `references/directions.md` — art-direction deck grounded in real traditions.
- `references/fonts.md` — non-default typefaces by character, with Cyrillic coverage.
- `references/qa.md` — screenshot loop, critique rubric, scripts.

## Workflow

### 1. Brief (no pixels yet)
Write down, in 5–8 lines: what the thing is, who uses it, the one job of the page, what the
reader must believe/do, and the **materials of the subject** — real objects, documents, places,
tools, vocabulary of that field (e.g. commissioning: P&IDs, punch lists, loop checks, site
permits, hard-hat stickers). Distinct design comes from these materials, not from style words.
Use real content: real names, numbers, product facts. If content is missing, ask or mark it
clearly — never lorem ipsum, never invented testimonials/logos/metrics.

### 2. Art direction
Pick ONE direction from `references/directions.md` (or a real-world reference the user names)
that fits the brief, and state why it fits this subject. Then write `DESIGN.md` (or a block at the
top of the page source) with:
- direction + 1–3 real references (designers, publications, objects) it borrows from;
- type: families, roles, sizes (a modular scale), measure, line-height;
- grid: columns, margins, gutters, baseline unit, where the grid is broken on purpose;
- colour: 1 dominant neutral system + at most 1–2 accents, with their *meaning*; values in OKLCH;
- imagery/graphic devices derived from the subject materials;
- motion: at most one deliberate moment, or none;
- **5 "template vs us" decisions**: what an AI template would do at 5 key places, and what this
  design does instead and why.

### 3. Critique the plan before coding
Check the plan against `references/tells.md`. If any first- or second-order tell appears without
a brief-driven reason, change the plan. Ask: "Would a reader guess the subject from a screenshot
with the text blurred?" If not, the direction is too generic.

### 4. Build
- Start from the grid and type scale, then content, then decoration (if any).
- Hierarchy through weight, colour and space before size (theory.md §Hierarchy).
- Spacing from one scale; no ad-hoc values. Tokens as CSS custom properties.
- Accessibility is part of quality: contrast ≥ 4.5:1 body / 3:1 large, focus states, semantic
  HTML, `prefers-reduced-motion`, real alt text, touch targets ≥ 44px.
- Respect an existing design system when one exists; in product UI, consistency beats novelty.

### 5. Look at it (mandatory)
Render screenshots at 1440×900 and 390×844 (full page too) with `scripts/shoot.py`, run
`scripts/tells_scan.py` on the site directory, then
critique with the rubric in `references/qa.md`.
Fix and re-shoot. **At least two rounds.** Do not claim the design is done without having looked.

### 6. Deliver
Report the direction, the 5 "template vs us" decisions, remaining compromises, and the final
screenshots (or paths). If the user can see artifacts, show them.

## Hard rules
- No default stack look: not Inter/Roboto/Arial/system as the brand face, not untouched
  shadcn/Tailwind palettes, not purple/indigo/blue-violet gradients, not centred-hero + three icon
  cards, not `rounded-2xl shadow-lg` everywhere, not glassmorphism by reflex, not emoji as icons.
- Not the "tasteful" defaults either unless the brief demands them: cream + terracotta serif,
  near-black + acid green mono, broadsheet/newspaper pastiche, uppercase mono micro-labels,
  decorative 01/02/03 numbering, one italic accent word in the headline, fake window dots.
- Two typefaces maximum (one is often enough). Every colour has a job.
- Copy: specific, plain, active voice. Ban "elevate", "seamless", "unlock", "supercharge",
  "revolutionize", "in today's fast-paced world", sparkle icons.
- Decoration must encode meaning (structure, data, sequence, the subject's materials) or go.
- Variety across projects: never reuse the previous project's direction, font pair or accent
  colour without a reason from the brief.
