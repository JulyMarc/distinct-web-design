"""Scan front-end source for code-certain AI-design tells (stdlib only).

Usage: python3 tells_scan.py <file-or-dir> [...] [--json]
Exit code 2 if any P0/P1 finding, else 0. Silence an intentional choice on a line with
`design-ok: <reason>` in a comment (`design-ok: project` anywhere disables project-level checks).
Pass the whole site directory: project-level checks (focus styles, reduced motion, fonts actually
loaded, muted-text contrast, accent hue) read HTML and linked stylesheets together.

P0 = a layperson notices "AI made this"; P1 = a designer/developer notices; P2 = polish.
Covers only what is certain from code; visual tells need the screenshot review (qa.md).
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".astro",
        ".md", ".mdx"}
SKIP_FILES = {"DESIGN.md", "README.md", "CHANGELOG.md"}  # docs describe tells, they are not UI
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".venv", "vendor", "coverage"}
GENERIC_FACES = {"serif", "sans-serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif",
                 "ui-monospace", "cursive", "fantasy", "inherit", "initial", "unset", "-apple-system",
                 "blinkmacsystemfont", "segoe ui", "helvetica", "helvetica neue", "arial", "georgia",
                 "times new roman", "menlo", "consolas", "courier new", "var"}

RULES: list[tuple[str, str, str, str]] = [
    # (id, severity, regex, message)
    ("font-default", "P1",
     r"font-family\s*:[^;]*\b(Inter|Roboto|Poppins|Montserrat|Arial|Helvetica Neue)\b|"
     r"family=(Inter|Roboto|Poppins|Montserrat)[:&\"']|\bfont-(inter|roboto|poppins)\b",
     "default/overused brand face — choose by subject (fonts.md)"),
    ("font-tasteful", "P1",
     r"\b(Space Grotesk|Fraunces|Instrument Serif|Bricolage Grotesque|Clash Display|"
     r"Cabinet Grotesk|Satoshi|General Sans)\b",
     "second-order 'tasteful AI' face"),
    ("gradient-purple", "P0",
     r"(from|via|to)-(purple|violet|indigo|fuchsia)-\d{2,3}|"
     r"linear-gradient\([^)]*(#(?:6366f1|8b5cf6|7c3aed|a855f7|9333ea|4f46e5|6d28d9)|"
     r"purple|violet|indigo)",
     "purple/indigo gradient"),
    ("gradient-text", "P0", r"bg-clip-text|background-clip\s*:\s*text",
     "gradient headline text"),
    ("glass", "P1", r"backdrop-blur|backdrop-filter\s*:\s*blur", "reflexive glassmorphism"),
    ("radius-shadow", "P1", r"rounded-(2xl|3xl)[^\"'`]*shadow-(lg|xl|2xl)|shadow-(lg|xl|2xl)[^\"'`]*rounded-(2xl|3xl)",
     "rounded-2xl + big shadow card"),
    ("blob", "P1", r"blur-3xl|blur-\[\d{2,}px\]|filter\s*:\s*blur\(\s*\d{2,}px", "blurred blob decoration"),
    ("emoji-icon", "P0", r"[✨\U0001F680\U0001F4A1\U0001F525⚡\U0001F3AF\U0001F4C8✅\U0001F31F\U0001F4AA]",
     "emoji used as icon/decoration"),
    ("copy-cliche", "P0",
     r"\b(elevate|seamless(ly)?|supercharge|unlock(s|ing)? (the|your)|revolutioni[sz]e|"
     r"empower(s|ing)?|game[- ]chang(er|ing)|cutting[- ]edge|next[- ]gen(eration)?|"
     r"in today's fast[- ]paced)\b",
     "generic marketing copy"),
    ("badge-pill", "P1", r"rounded-full[^\"'`]*(px-3|px-4)[^\"'`]*(text-xs|text-sm)[^\"'`]*(uppercase|tracking)|"
     r"✨\s*New", "pill badge above headline"),
    ("mono-caps-label", "P1",
     r"(font-mono[^\"'`]*uppercase[^\"'`]*tracking-|uppercase[^\"'`]*tracking-(widest|wider)[^\"'`]*font-mono)",
     "uppercase mono micro-label (second-order tell)"),
    ("window-dots", "P1", r"(rounded-full[^\"'`]*bg-(red|yellow|green)-[345]00[\s\S]{0,200}){3}",
     "fake window chrome dots"),
    ("fade-up-everywhere", "P2", r"(fade-?in-?up|animate-fade|data-aos=)", "stock reveal animation"),
    ("bounce-ease", "P1", r"cubic-bezier\([^)]*1\.[2-9]|ease-bounce|animate-bounce|spring\(",
     "bounce/elastic easing"),
    ("count-up", "P2", r"countUp|count-up|CountUp", "count-up stats"),
    ("pure-black", "P2", r"(?<![\w-])(#000000|#000\b|rgb\(0,\s*0,\s*0\))", "pure black — use a tinted near-black"),
    ("lorem", "P0", r"lorem ipsum", "placeholder text"),
    ("middot-chrome", "P2", r">[^<>\n]{1,60} (·|&middot;) [^<>\n]{1,60}<", "metadata joined with middle dots"),
    ("cream-terracotta", "P1",
     r"#(f5f0e8|faf7f2|f4efe6|fbf8f3|f7f3ec)[\s\S]{0,400}#(c2410c|b45309|c4622d|cc5a2b|b85c38|d97757)|"
     r"#(c2410c|c4622d|cc5a2b|b85c38|d97757)[\s\S]{0,400}#(f5f0e8|faf7f2|f4efe6|fbf8f3|f7f3ec)",
     "cream + terracotta palette (the 'Claude look')"),
    ("italic-accent-word", "P1", r"<h1[^>]*>[^<]{0,80}<(em|i)\b",
     "one italic accent word in the headline (second-order tell)"),
    ("number-markers", "P2", r"<(span|div|p|small)[^>]*>\s*0[1-9]\.?\s*</(span|div|p|small)>",
     "decorative 01/02/03 markers — keep only for a real sequence"),
    ("arrow-cta", "P2", r"(→|&rarr;|->)\s*</(a|button)>|<(a|button)\b[^>]*>\s*(→|&rarr;)",
     "arrow glyph welded to a link/button label"),
    ("shadcn-base", "P0", r"222\.2\s+84%\s+4\.9%|222\.2\s+47\.4%\s+11\.2%",
     "untouched shadcn/ui base theme tokens"),
    ("generator-signature", "P1",
     r"<meta[^>]+name=[\"']generator[\"'][^>]+(v0|lovable|bolt|framer|webflow)|"
     r"(made|built) with (v0|lovable|bolt\.new)",
     "site-generator signature left in"),
    ("acid-on-black", "P1",
     r"#(0a0a0a|0b0b0b|0d0d0d|111111|09090b)[\s\S]{0,400}#(a3e635|bef264|84cc16|c6ff00|d4ff3a|39ff14)",
     "near-black + acid green"),
]
COMPILED = [(rid, sev, re.compile(rx, re.I), msg) for rid, sev, rx, msg in RULES]


def iter_files(paths: list[str]):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in p.rglob("*"):
                if (f.is_file() and f.suffix.lower() in EXTS and not SKIP_DIRS & set(f.parts)
                        and f.name not in SKIP_FILES):
                    yield f


def scan(path: Path) -> list[dict]:
    try:
        text = path.read_text(errors="ignore")
    except OSError:
        return []
    lines = text.splitlines()
    out = []
    for rid, sev, rx, msg in COMPILED:
        for m in rx.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            line = lines[line_no - 1] if line_no <= len(lines) else ""
            if "design-ok:" in line:
                continue
            out.append({"file": str(path), "line": line_no, "rule": rid, "severity": sev,
                        "message": msg, "match": m.group(0)[:60]})
    return out


# --- Project-level checks: need all files at once (a stylesheet linked from the HTML counts) ---

def _lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _oklch_to_linear_rgb(L: float, C: float, h: float) -> tuple[float, float, float]:
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    return tuple(min(1.0, max(0.0, v)) for v in rgb)


def _linear_rgb_to_oklch(r: float, g: float, b: float) -> tuple[float, float, float]:
    l = (0.4122214708 * r + 0.5363295215 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360


def parse_color(value: str):
    """Return (linear sRGB, oklch) for hex, rgb() or oklch() values; None otherwise."""
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", v)
    if m:
        h = m.group(1)
        h = "".join(c * 2 for c in h) if len(h) == 3 else h
        rgb = tuple(_lin(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
        return rgb, _linear_rgb_to_oklch(*rgb)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+).*\)", v)
    if m:
        rgb = tuple(_lin(int(x) / 255) for x in m.groups())
        return rgb, _linear_rgb_to_oklch(*rgb)
    m = re.fullmatch(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)(?:deg)?\s*(?:/[^)]*)?\)", v)
    if m:
        L = float(m.group(1)) / (100 if m.group(2) else 1)
        lch = (L, float(m.group(3)), float(m.group(4)))
        return _oklch_to_linear_rgb(*lch), lch
    return None


def contrast(a, b) -> float:
    ya, yb = (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2] for c in (a, b))
    return (max(ya, yb) + 0.05) / (min(ya, yb) + 0.05)


BG_TOKEN = re.compile(r"^--(bg|background|paper|surface|ground|page|canvas)(-?\d*)$", re.I)
MUTED_TOKEN = re.compile(r"^--.*(muted|subtle|secondary|ink-2|text-2|fg-2|meta|caption|dim).*$", re.I)
PRIMARY_TOKEN = re.compile(r"^--(primary|brand)(-\d+)?$", re.I)
ACCENT_TOKEN = re.compile(r"^--(accent|highlight|cta)(-\d+)?$", re.I)


def project_checks(files: list[Path]) -> list[dict]:
    texts = {f: f.read_text(errors="ignore") for f in files}
    html = {f: t for f, t in texts.items() if f.suffix.lower() in {".html", ".htm"}}
    styles = "\n".join(t for f, t in texts.items() if f.suffix.lower() != ".md")
    out = []

    def add(f, rid, sev, msg, match="", line=1):
        out.append({"file": str(f), "line": line, "rule": rid, "severity": sev, "message": msg,
                    "match": match[:60]})

    first = next(iter(texts), None)
    if first is None or "design-ok: project" in styles:
        return out
    if html and re.search(r"<(a|button|input|select|textarea)\b", "\n".join(html.values()), re.I) \
            and not re.search(r":focus(-visible|-within)?\b", styles):
        add(next(iter(html)), "no-focus-style", "P1",
            "interactive elements but no :focus/:focus-visible style anywhere")
    if re.search(r"@keyframes|animation\s*:|transition\s*:\s*(?!none)", styles, re.I) \
            and "prefers-reduced-motion" not in styles:
        add(first, "no-reduced-motion", "P1", "motion without a prefers-reduced-motion rule")

    if html:  # declared faces must be loaded (Google Fonts link/@import or @font-face)
        loaded = {n.replace("+", " ").lower()
                  for n in re.findall(r"family=([A-Za-z0-9+]+)", styles)}
        loaded |= {n.strip("\"' ").lower()
                   for n in re.findall(r"@font-face\s*{[^}]*font-family\s*:\s*([^;}]+)", styles, re.I)}
        for f, t in texts.items():
            for m in re.finditer(r"(?:font-family\s*:|--[\w-]*(?:font|serif|sans|mono|face)[\w-]*\s*:)"
                                 r"\s*([^;}{]+)", t, re.I):
                face = m.group(1).split(",")[0].strip().strip("\"'").lower()
                if face and not face.startswith("var(") and face not in GENERIC_FACES \
                        and face not in loaded and not face.startswith(("inherit", "-")):
                    add(f, "font-not-loaded", "P1", f"'{face}' declared but never loaded",
                        m.group(0), t.count("\n", 0, m.start()) + 1)

    tokens = {}
    for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;}]+)", styles):
        tokens.setdefault(name, value.strip())  # first definition = light/default theme
    colors = {n: c for n, v in tokens.items() if (c := parse_color(re.sub(r"/\*.*?\*/", "", v)))}
    bgs = [colors[n] for n in colors if BG_TOKEN.match(n)]
    body_bg = re.search(r"body\s*{[^}]*background(?:-color)?\s*:\s*(#[0-9a-f]{3,6}|oklch\([^)]*\)|rgb\([^)]*\))",
                        styles, re.I)
    if body_bg and (c := parse_color(body_bg.group(1))):
        bgs.append(c)
    if bgs:
        bg = bgs[0]
        for n, c in colors.items():
            if MUTED_TOKEN.match(n) and (r := contrast(c[0], bg[0])) < 4.5:
                add(first, "muted-contrast", "P1",
                    f"{n} on the page background is {r:.2f}:1, below WCAG AA 4.5:1", tokens[n])
    prim = [(n, c) for n, c in colors.items() if PRIMARY_TOKEN.match(n)]
    acc = [(n, c) for n, c in colors.items() if ACCENT_TOKEN.match(n)]
    for (pn, pc), (an, ac) in ((p, a) for p in prim[:1] for a in acc[:1]):
        dh = abs(pc[1][2] - ac[1][2]) % 360
        if pc[1][1] > 0.04 and ac[1][1] > 0.04 and min(dh, 360 - dh) < 20:
            add(first, "hue-twins", "P2", f"{pn} and {an} are within 20° of hue: one colour, two names")
    return out


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 1
    files = list(iter_files(paths))
    findings = [f for p in files for f in scan(p)] + project_checks(files)
    findings.sort(key=lambda f: (f["severity"], f["file"], f["line"]))
    if as_json:
        print(json.dumps(findings, ensure_ascii=False, indent=1))
    else:
        for f in findings:
            print(f"{f['severity']} {f['file']}:{f['line']} [{f['rule']}] {f['message']} — {f['match']!r}")
        counts = {s: sum(f["severity"] == s for f in findings) for s in ("P0", "P1", "P2")}
        print(f"summary: P0={counts['P0']} P1={counts['P1']} P2={counts['P2']}")
    return 2 if any(f["severity"] in ("P0", "P1") for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
