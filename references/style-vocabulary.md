# Style vocabulary and how to vary the result

Same tool, different brief, different result. Generic output comes from a generic brief. This file
is a method plus a vocabulary of named traditions for when `directions.md` has no good fit or two
projects would otherwise land on the same look. Method and style list are adapted from John
Hartnup's article on AI event posters (john.hartnup.uk/2026/06/07/ai-event-posters.html) and his
catalogue of 100 poster styles (john.hartnup.uk/poster-prompts/). His prompts are written for
image generation; here they are translated into web decisions.

## Method

1. **Brief plus bans.** State the subject, the audience and explicit exclusions (for example no
   pastel, no stock people, no gradients). Without bans the first result is the default template.
2. **Use the generic draft as a negative reference.** If a first draft or plan looks like the
   template, keep it only as "what not to do" and ask for something that differs from it.
3. **Name what you got.** Ask what style the current draft is (Bauhaus, Swiss, modernist,
   geometric minimalism...). The names become vocabulary you can steer with.
4. **Ask for a menu.** List 10–15 candidate styles grouped by mood (clean, graphic, bold,
   understated, playful), each with one line of visual description. Pick by subject, not taste.
5. **Anchor in era, movement, medium or process.** "1980 punk fanzine, photocopy, a little colour
   added" says more than "edgy". A material cue (riso, letterpress, cut paper, halftone) gives
   concrete rules for colour count, texture and edges.
6. **Combine two incompatible sources only on purpose**, for example professional typography over
   a child's poster-paint drawing. Needs a reason from the brief and a clear hierarchy.
7. **Set structure up front**: grid, white space, number of colours, type character. Models
   invent filler text and it carries into later revisions, so write all real copy in the brief.
8. **Aim for distinctive, not just different.** Swapping one style for another is not the goal;
   the result should still belong to the subject.

## Translating a print style to the web

- Take the **rules**, not the surface: grid, type contrast, colour count and meaning, how images
  are cropped, how edges look.
- Texture (grain, misregistration, halftone) only where it is cheap and honest: SVG or CSS on a
  few large elements, never a full-page noise overlay or filter stack that hurts text contrast.
- Write the result into the `DESIGN.md` fields from the workflow: type, grid, colour (OKLCH),
  devices, motion. A style name alone does not count as a decision.
- Check licensing of any named typeface and never imitate a living designer's or a brand's
  identity too closely.

## Named styles by family

Names only; look them up in the catalogue for example images. Entries marked (d) are already
covered in `directions.md`.

- **Graphic design movements:** Arts and Crafts, Art Nouveau, Art Deco, Streamline Moderne,
  Bauhaus (d), Swiss / International (d), Constructivist, De Stijl, Mid-century modern, Memphis (d),
  Brutalist (d), Contemporary editorial (d), Wayfinding / signage, Vienna Secession, Glasgow Style,
  Push Pin Studios, New Wave typography (d), Grunge typography.
- **Fine-art movements:** Japonisme, Victorian broadside, Belle Époque lithograph, Futurist, Dada
  collage, Cubist, Surrealist, Expressionist woodcut, Pop Art, Op Art, Psychedelic sixties,
  Suprematism, Vorticism, Neue Sachlichkeit, Concrete art, CoBrA, Pre-Raphaelite illustration.
- **Print techniques:** Risograph, Letterpress, Screenprint, Botanical scientific illustration,
  Cut paper (Matisse), Monochrome plus one accent, Cyanotype / blueprint, Halftone / newsprint,
  Etching / engraving, Mimeograph, Penny dreadful cover.
- **Handmade and vernacular:** Child poster paint with pro typography, School cut-out collage,
  Crayon folk, Punk photocopied fanzine, Zine cut-and-paste, Calavera / Posada, Fraktur
  (Pennsylvania Dutch), Madhubani, Scandinavian folk (rosemaling).
- **National and era styles:** Polish poster school, Golden-age travel poster, Japanese minimal (d),
  Diner Americana neon, East German DEFA, Taisho modern, Shanghai calendar poster, Festival of
  Britain, Tropicália, Italian Futurist typography, Zagreb school, German Expressionist film,
  Hong Kong cinema, Ukiyo-e.
- **Political and activist traditions:** WPA, Soviet propaganda and space programme, Cuban OSPAAAL,
  Atelier Populaire (Paris 1968), ACT UP. Use as a study of structure and slogan typography, not
  as costume; check the context before borrowing any of them for a commercial subject.
- **Music and subcultures:** 90s rave / acid graphics, drum and bass flyer, Factory Records, 4AD,
  heavy metal poster, reggae sound-system flyer, 80s NYC hip-hop flyer, skateboard graphics.
- **Digital and screen:** Designers Republic, NASA worm modernist, Y2K chrome, flat illustration,
  Vaporwave, Synthwave, Glitch, Pixel art, Low poly.

## Use

When `directions.md` yields two equal options or none, run steps 3–5 above to produce 3 candidates
from different families, drop the one closest to a template, and carry the winner into step 2 of
the workflow with its era or medium written down.
