# Typefaces

Verified against the Google Fonts metadata on 2026-10-02 (`Cyr` = has a Cyrillic subset,
`rank` = Google Fonts popularity rank, lower = more common). Popularity matters: the most common
faces read as "default". Ranks drift by a few places month to month. Always check the license and Cyrillic needs of the project; re-verify
availability if in doubt (`https://fonts.google.com/metadata/fonts`).

## Avoid as the brand/display face (AI defaults or overexposed)
Inter (rank 4), Roboto (2), Poppins (8, no Cyr), Montserrat (7), Raleway (21), Oswald (16),
Nunito Sans (22), Rubik (25), DM Sans (19), Manrope (27), Figtree (36), Space Grotesk (48 —
strong AI tell), Playfair Display (18), Fraunces / Instrument Serif (the "tasteful AI" serifs),
Bricolage Grotesque (34, trendy AI pick), JetBrains Mono as a mood face ("terminal chic"),
and from Fontshare: Satoshi, General Sans, Cabinet Grotesk, Clash Display (overused by
AI-built landing pages). They remain fine for invisible UI text inside an existing system.

## Choose by character (prefer less common, verified)

### Neutral / Swiss-leaning grotesk (directions 1, 2, 3, 9, 11)
- IBM Plex Sans — Cyr, rank 44. Engineered, slightly quirky; good for technical/industrial.
- Golos Text — Cyr, rank 225. Russian grotesk (Paratype); excellent for RU interfaces/body.
- Onest — Cyr, rank 144. Calm geometric-grotesk hybrid, good RU/EN body.
- Commissioner — Cyr, rank 236. Variable, flared options; humane grotesk.
- Libre Franklin — Cyr, rank 67. American Gothic flavour, strong headlines.
- Schibsted Grotesk — no Cyr, rank 82. Newspaper-born grotesk with character.
- Hanken Grotesk — no Cyr, rank 116. Clean, friendly.
- Familjen Grotesk — no Cyr, rank 402. Scandinavian, slightly condensed character.
- Public Sans — no Cyr, rank 68. Government-neutral (USWDS), honest.

### Technical / DIN-like / condensed (direction 4, 11)
- Barlow / Barlow Condensed — no Cyr, rank 43/66. Highway-sign heritage, tables and specs.
- Overpass — Cyr, rank 96. Highway Gothic-inspired; good for signage-like UI.
- Exo 2 — Cyr, rank 99. Technical display (use sparingly).
- Geologica — Cyr, rank 157. Variable with sharpness axis; good for RU technical brands.
- IBM Plex Mono — Cyr, rank 63; PT Mono — Cyr, rank 260; Martian Mono — Cyr, rank 561:
  for codes, part numbers, data — not as decoration.

### Text serifs (directions 5, 12, 14)
- Source Serif 4 — Cyr, rank 36 (common). Sturdy, optical sizes; great long-form.
- Literata — Cyr, rank 179. Designed for reading on screens; RU-friendly.
- Spectral — Cyr, rank 143. Elegant, screen-first serif.
- PT Serif — Cyr, rank 57. Russian classic; pairs with PT Sans.
- EB Garamond — Cyr, rank 70. Classical book face (needs size ≥ 18 px on screen).
- Vollkorn — Cyr, rank 71. Dark, robust text face.
- Alegreya — Cyr, rank 199. Calligraphic rhythm, literary character.
- Newsreader — no Cyr, rank 102. Editorial text with optical sizes.
- Libre Caslon Text — no Cyr, rank 210. Classic, warm.
- Crimson Pro — no Cyr, rank 164. Old-style book face.
- Gentium Book Plus — Cyr, rank 906. Scholarly, multilingual (direction 14).

### Display with personality (use for headings only)
- Unbounded — Cyr, rank 167. Wide, bold geometric display; strong RU headlines.
- Yeseva One — Cyr, rank 313. High-contrast Cyrillic-first display serif.
- Prata — Cyr, rank 180. Didone-like display (direction 12).
- Bodoni Moda — no Cyr, rank 126. Didone (direction 12).
- Old Standard TT — Cyr, rank 208. 19th-c. Modern style; academic/editorial.
- Gloock — no Cyr, rank 406; Young Serif — no Cyr, rank 451: characterful serifs.
- Syne — no Cyr, rank 142; Anybody — no Cyr, rank 559: experimental/creative (direction 8).
- Forum — Cyr, rank 270. Roman inscriptional capitals (headings).

## Pairing rules
- Pair by **contrast of structure** (serif text + grotesk UI, or grotesk + condensed for data),
  never two similar sans.
- One family with good weights is often better than a pair.
- Check both scripts in the same face if the site is bilingual: a Cyrillic fallback in another
  face breaks the texture.
- Load only the weights used; `font-display: swap`; subset to needed scripts.

## Other sources (check license per family)
ParaType (Russian classics: PT family is free), Velvetyne and Collletttivo (libre, experimental),
Use & Modify (curated open-source), Fontshare (free commercial use, but its most popular faces
are now overexposed).
