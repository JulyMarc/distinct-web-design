"""Scan front-end source for code-certain AI-design tells (stdlib only).

Usage: python3 tells_scan.py <file-or-dir> [...] [--json]
Exit code 2 if any P0/P1 finding, else 0. Silence an intentional choice on a line with
`design-ok: <reason>` in a comment.

P0 = a layperson notices "AI made this"; P1 = a designer/developer notices; P2 = polish.
Covers only what is certain from code; visual tells need the screenshot review (qa.md).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".astro",
        ".md", ".mdx"}
SKIP_FILES = {"DESIGN.md", "README.md", "CHANGELOG.md"}  # docs describe tells, they are not UI
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".venv", "vendor", "coverage"}

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


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 1
    findings = [f for p in iter_files(paths) for f in scan(p)]
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
