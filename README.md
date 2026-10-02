# distinct-web-design

An agent skill (Claude Code / any SKILL.md-compatible harness) for building websites that do not
look AI-generated — including not looking like the output of the popular "anti-slop" skills.

How it differs:
- **Subject before style.** Every design starts from the materials of the product's field and one
  real design tradition (`references/directions.md`: Swiss, Dutch structural, technical manual,
  Japanese restraint, Tufte-style data, …), recorded in a DESIGN.md contract with five explicit
  "what a template would do → what we do instead" decisions.
- **Theory with numbers** from working designers' canon: Butterick, Bringhurst, Refactoring UI,
  Müller-Brockmann, Vignelli, Rams, Albers, Gestalt (`references/theory.md`).
- **Two layers of tells**: classic AI defaults *and* second-order "tasteful" defaults
  (cream + terracotta serif, black + acid green mono, broadsheet pastiche, mono caps labels…).
- **Fonts chosen with data**: non-default faces by character, Google Fonts popularity rank and
  Cyrillic coverage (`references/fonts.md`).
- **Mandatory look-at-it loop**: desktop/mobile screenshots (`scripts/shoot.py`) and a
  deterministic, stdlib-only scanner (`scripts/tells_scan.py`): per-line tells plus project-level
  checks for focus styles, reduced motion, fonts actually loaded, muted-text contrast (WCAG AA,
  OKLCH-aware) and accent hue — before anything is called done.

## Install
Copy or clone into `~/.claude/skills/distinct-web-design/`. For screenshots:
```bash
cd ~/.claude/skills/distinct-web-design
python3 -m venv .venv && .venv/bin/pip install playwright==1.55.0
.venv/bin/python3 -m playwright install chromium --only-shell
```
The browser cache (`~/.cache/ms-playwright`) is shared between projects: if another project
already has a Playwright build, pin that Playwright version instead of installing a new browser.
`tells_scan.py` needs only the Python standard library.

## Credits
Tell lists informed by anthropics/skills `frontend-design`, pbakaus/impeccable (Apache-2.0) and
funboy322/avoid-ai-design (MIT); `tells_scan.py` is an independent implementation, no code is
copied from them.
Theory is paraphrased and attributed; no book text is reproduced.

## License
MIT (see LICENSE).
