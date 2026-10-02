"""Screenshot a page at desktop and mobile sizes (viewport + full page) for design review.

Usage:
  ~/.claude/skills/distinct-web-design/.venv/bin/python3 \
      ~/.claude/skills/distinct-web-design/scripts/shoot.py <url-or-html-file> <out-dir> [--dark]

Writes desktop.png, desktop-full.png, mobile.png, mobile-full.png and prints the paths plus
basic layout facts (page height, horizontal overflow, fonts actually rendered).
Needs Playwright and a Chromium build in the skill venv (see README). On a machine where other
projects share the Playwright browser cache, pin the Playwright version whose build is already
cached instead of running `playwright install`, which can remove other versions' builds.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

VIEWPORTS = {"desktop": (1440, 900), "mobile": (390, 844)}

FACTS_JS = """() => {
  const fonts = new Set();
  for (const el of document.querySelectorAll('body *')) {
    const s = getComputedStyle(el);
    if (el.childNodes.length && [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
      fonts.add(s.fontFamily.split(',')[0].trim().replace(/["']/g, ''));
  }
  return {
    height: document.documentElement.scrollHeight,
    overflowX: document.documentElement.scrollWidth > window.innerWidth,
    fonts: [...fonts].slice(0, 8),
  };
}"""


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    target, out = sys.argv[1], Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    url = target if "://" in target else Path(target).resolve().as_uri()
    scheme = "dark" if "--dark" in sys.argv else "light"
    report = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, (w, h) in VIEWPORTS.items():
            page = browser.new_page(viewport={"width": w, "height": h}, color_scheme=scheme,
                                    device_scale_factor=1)
            page.goto(url, wait_until="networkidle", timeout=45_000)
            page.wait_for_timeout(600)  # web fonts, first animation frame
            page.screenshot(path=str(out / f"{name}.png"))
            page.screenshot(path=str(out / f"{name}-full.png"), full_page=True)
            report[name] = page.evaluate(FACTS_JS)
            page.close()
        browser.close()
    for name in VIEWPORTS:
        print(out / f"{name}.png")
        print(out / f"{name}-full.png")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
