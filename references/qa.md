# Visual QA loop

Models judge their own HTML from the code and miss what a human sees in two seconds. Always
look at rendered pixels.

## Commands
```bash
SK=~/.claude/skills/distinct-web-design
# 1. code-certain tells (exit 2 = P0/P1 present). Pass the whole site directory: project-level
#    checks (focus styles, reduced motion, fonts loaded, muted-text contrast, accent hue) read
#    HTML and linked stylesheets together.
python3 $SK/scripts/tells_scan.py <site-dir>        # add --md for Markdown-content sites
# 2. screenshots: desktop 1440x900 + mobile 390x844, viewport and full page
$SK/.venv/bin/python3 $SK/scripts/shoot.py <url-or-index.html> <out-dir>
```
Then open the PNGs (Read tool shows images) and critique. For a dev server, pass its URL.
`shoot.py` also prints the fonts actually rendered — catches silent fallbacks to system fonts.

## Rubric (score each 1–5, fix anything below 4)
1. **Subject legibility** — with text blurred, the screenshot still suggests the subject/field.
2. **Focal point** — one obvious first read per viewport; eye path is clear.
3. **Type** — body size/measure/leading within theory.md ranges; scale steps from one ratio;
   ≤ 2 families; no orphaned single words in headlines; Cyrillic renders in the chosen face.
4. **Grid** — elements align to a small number of lines; spacing from the scale; intended
   asymmetry looks intended, not accidental.
5. **Colour** — accent used only where it means something; contrast passes; neutrals tinted.
6. **Tells** — none from tells.md without a written reason (both layers).
7. **Content** — real, specific copy; no filler sections; every section answers a reader question.
8. **Mobile** — not a squeezed desktop: hierarchy re-ordered for the narrow column, tap targets
   ≥ 44 px, no horizontal overflow (shoot.py reports `overflowX`).
9. **Tables & data** — tables never sit directly in a CSS grid cell (wrap them); on mobile turn
   rows into stacked blocks instead of squeezing columns.
10. **Detail** — states (hover/focus), images crisp and consistently treated, punctuation and
   typographic quotes correct (RU: «ёлочки», неразрывные пробелы).

## Critique like a designer
- Describe what you see first ("large grey block, small headline top-left, three equal boxes"),
  then judge. Describing prevents seeing what you intended instead of what rendered.
- Name the single biggest problem per round and fix it before polishing details.
- Compare against the chosen tradition's real work: what would that designer remove?
- After two rounds, if the page is still generic, change the direction rather than polishing.

## Optional deeper checks
- funboy322/avoid-ai-design (MIT, Node.js): a larger detector and tell catalogue; worth a run
  when a page "feels AI" but `tells_scan.py` is clean. Install it separately and review it first.
- `pbakaus/impeccable` (Apache-2.0): its detector is a Rust binary fetched by `npx`; not vendored
  (prebuilt binary unreviewed, source build is heavy). Use only with owner approval.
- Vercel `web-design-guidelines` for accessibility/performance review.
