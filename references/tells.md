# AI-design tells and what to do instead

Two layers. Layer 1 is what every model produced in 2023–25. Layer 2 is what the popular
"anti-slop" skills now produce — readers have learned to spot it too. A tell is allowed only when
the brief genuinely calls for it; write the reason in DESIGN.md.

Sources: own audits plus public lists in anthropics/skills `frontend-design` (five default
clusters), pbakaus/impeccable (detector rules), funboy322/avoid-ai-design (67 tells, P0–P2).

## Layer 1 — obvious
| Tell | Instead |
|---|---|
| Inter / Roboto / Poppins / Montserrat / system font as brand face | A face chosen for the subject (fonts.md) |
| Purple→blue / indigo gradients, gradient text in headlines | Flat colour from the subject; gradients only if they depict something (light, heat, depth) |
| Centred hero + subheading + two buttons + three icon cards | Asymmetric opening built on the grid; lead with the real product/proof |
| `rounded-2xl` + `shadow-lg` on every block, cards inside cards | Consistent, smaller radius (0–6 px) or none; separate with space/rules/background |
| Glassmorphism, blurred blobs, mesh gradients, noise overlays by reflex | Real imagery or none |
| Emoji or generic line icons in coloured rounded squares | No icons unless they aid scanning; if needed, one consistent set, small, monochrome |
| "Trusted by" logo strip of fake/greyed logos, invented testimonials | Real proof only (numbers, named clients, quotes with permission) or omit |
| Fade-up on every element, bounce/elastic easing, count-up stats | One purposeful motion moment or none; ease-out 150–250 ms for UI |
| Pill badge above the headline ("✨ New: …") | Plain text kicker only if it carries information |
| Copy: elevate, seamless, unlock, supercharge, empower, revolutionize, "in today's…" | Concrete claims with numbers and nouns of the domain |
| Dark mode by default with neon accents | Choose the ground from the subject and reading context |
| Everything the same max-width centred column | Grid with deliberate column spans and asymmetry |
| Pricing table with "Most popular" ribbon by default | Only if pricing is the page's job; design it from the actual offer |

## Layer 2 — "tasteful" defaults
| Tell | Instead |
|---|---|
| Warm cream background + terracotta/rust accent + elegant serif (the "Claude look") | Derive ground and accent from subject materials; if warm, make it specific (e.g. kraft paper + stamp red with a reason) |
| Near-black + acid green / lime + monospace ("terminal chic") | Only for genuinely technical CLI/dev products, and then with a non-default mono and real data |
| Broadsheet/newspaper pastiche: rules, small caps, datelines, columns everywhere | Editorial structure only for editorial content; otherwise a grid that fits the content |
| Uppercase monospace micro-labels with wide tracking above every section | Labels only where needed, in the text face, sentence case |
| Decorative 01 / 02 / 03 numbering on non-sequential content | Numbers only for real sequences (steps, rankings) |
| One italic or coloured accent word in the headline | Let the whole headline carry meaning; emphasis via size/weight of the line |
| Fake browser/window chrome (three dots) around screenshots | Show the product plainly, cropped to the relevant part |
| Bento grid of mixed-size cards as the feature section | Feature structure from the content (table, list, diagram, specimen) |
| Big serif display + tiny mono captions as a universal combo | Pair by function and subject (fonts.md) |
| Grain/paper texture to look "human" | Texture only if it is a real material of the subject |
| SaaS template chrome: sticky blurred nav, CTA in nav, footer with 4 link columns | Navigation sized to the site; footer with what users actually need |
| Metadata strings joined with middle dots ("Company · City · 5 min read") | Punctuation of the language (commas), separate lines, or a table column |

## Quick self-test (before and after building)
1. Blur the text: can you tell the subject? If no — direction too generic.
2. Swap the logo for a competitor's: does the page still work for them? If yes — not specific.
3. Count accents, radii, shadows, font sizes: more than the plan allows? — reduce.
4. Name the tradition the page borrows from. If "modern SaaS" — start again.
5. Would a designer from that tradition sign it? What would they remove first? Remove it.
