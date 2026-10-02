# Design theory with numbers

Principles condensed from working designers' published canon. Paraphrased, attributed; use as
rules of thumb, break them only on purpose.

## Typography (Butterick, *Practical Typography*; Bringhurst, *The Elements of Typographic Style*)
- Body text decides the page. Set it first: **16–20 px** on screen (Butterick: 15–25 px), line
  height **1.3–1.5** (120–145% of size), measure **45–90 characters** (aim ~60–75).
- Line height shrinks as size grows: display 1.0–1.15, headings 1.15–1.3, body 1.4–1.6.
- Use a **modular scale** (Bringhurst): pick one ratio — 1.125 (dense UI), 1.2, 1.25, 1.333
  (editorial), 1.5/1.618 (posters). Every size on the page comes from it.
- One or two families. If two, they must differ clearly in structure (e.g. serif text + grotesk
  UI), never two similar sans. Weights: 2–3 per family.
- All caps only for short labels (< 1 line), with **+5–12% letter-spacing**; never for body.
- Bold *or* italic, never both. No underline except links. Real quotes “ ” and apostrophes ’,
  real dashes – —, real ellipsis …, non-breaking spaces where words must stay together
  (in Russian: «ёлочки», неразрывный пробел after one-letter prepositions and before «—»).
- Centered text only for short display lines; long text is left-aligned (ragged right).
- Kerning on (`font-kerning: normal`), `text-rendering: optimizeLegibility` for display,
  `font-variant-numeric: tabular-nums` in tables, `hanging-punctuation` where supported.
- Paragraphs: first-line indent **or** space between paragraphs, not both.

## Hierarchy (Wathan & Schoger, *Refactoring UI*)
- Emphasise by **de-emphasising** the rest: secondary text in a lighter colour/weight before
  making primary text bigger.
- Hierarchy tools in order of subtlety: colour/contrast → weight → size → space → position.
- Labels are a last resort: `Email: a@b.c` → just `a@b.c` where context is obvious.
- Separate with space or background shifts before borders; avoid boxes inside boxes.
- Primary action looks primary; secondary actions are quieter (outline/text), destructive actions
  are not loud unless they are the main action.
- Grey text on coloured backgrounds looks dead — use a tint/shade of the background hue instead.

## Space and grid (Müller-Brockmann, *Grid Systems*; Vignelli, *The Vignelli Canon*)
- Choose a **base unit** (4 or 8 px) and a spacing scale (e.g. 4, 8, 12, 16, 24, 32, 48, 64, 96,
  128). Gaps grow faster than linearly: start with too much white space, then remove.
- Grid: 4, 6 or 12 columns for screens; outer margins larger than gutters; content snaps to
  column lines and a **baseline** (multiple of the base unit).
- Asymmetry is allowed and often stronger (Tschichold): a narrow column of captions beside a wide
  text column reads as designed, a centred stack reads as template.
- Break the grid deliberately and rarely — one bleed image, one oversized number — so the break
  carries meaning.
- Vignelli: semantics (is it saying the right thing?), syntactics (do the parts form a consistent
  whole?), pragmatics (is it understood?). Few typefaces, strict grid, consistency over novelty.

## Gestalt
- Proximity groups; related items closer to each other than to unrelated ones (inner spacing <
  outer spacing).
- Similarity: same function → same style; different function → visibly different.
- Alignment: every element aligns to something; count your alignment lines and reduce them.
- Figure/ground: one clear focal point per view.

## Colour (Albers, *Interaction of Color*; modern OKLCH practice)
- Colour is relative: the same value looks different on different grounds — judge colours in
  place, in the screenshot, not in the swatch.
- Build neutrals with a slight hue (warm or cool from the brand), not pure grey/black.
  Avoid #000 on #fff for large text areas; near-black on off-white reads calmer.
- Define the palette in **OKLCH**: keep lightness steps perceptually even (e.g. L 98/95/90/80/
  65/50/35/20/12), vary chroma carefully; accents at similar lightness feel related.
- Proportion: dominant neutral (most of the area), secondary (structure), accent (≤ 5–10%,
  reserved for the one thing that must be seen). An accent used everywhere stops being one.
- Contrast: WCAG AA 4.5:1 for body, 3:1 for large text and UI boundaries.
- Colour can come from the subject (safety orange of a site helmet, cyan of a blueprint, the green
  of a circuit board) — that is more distinctive than any trendy palette.

## Restraint (Dieter Rams, ten principles)
- Good design is useful, understandable, unobtrusive, honest, long-lasting, thorough down to the
  last detail, and **as little design as possible** — "less, but better".
- Each element must earn its place: if removing it loses nothing, remove it.

## Images and graphic devices
- Prefer real photography/documents of the subject over illustration packs and abstract blobs.
- Graphic devices should come from the domain: technical drawing lines, tables, maps, specimen
  sheets, timetables, labels, stamps — used as structure, not wallpaper.
- Crop with intent (tight crops, edge bleeds); consistent treatment across all images.

## UX writing
- Headlines say what it is and for whom, concretely; no slogans that would fit any product.
- Buttons are verbs that match the result ("Download report" → toast "Report downloaded").
- Numbers and specifics beat adjectives.
