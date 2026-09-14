# Production Notes — Korea's Family Transformation

Scope of this pass: assemble the full manuscript (Introduction + Chapters 1–6 + Epilogue + Statistical Appendix) into one publication-structured file with a linked table of contents, standardized image placeholders for every item in `05-visuals.md`, a cover brief, and verified internal cross-references. Per explicit instruction for this task, **binary EPUB/PDF conversion was deferred** rather than attempted, because 19 image slots are still unresolved placeholders — see the standing pipeline rule against finalizing binary output while placeholders remain. Structural/markdown production is complete.

## 1. Files produced in this pass

- `manuscript-assembled.md` — full assembled manuscript: front matter, two prominent Production Notes, linked table of contents, Introduction, Chapters 1–6, Epilogue, and the Statistical Appendix/References, in original chapter order. All original chapter prose is reproduced verbatim from `04-edited/*.md` and `02-chapters/08-appendix-statistical-references.md`; the only additions are anchor tags (`<a id="...">`), markdown link wrapping around existing "Chapter N" / "Figure N" / "Introduction" / "Epilogue" cross-reference text, and the standardized image placeholder blocks replacing the original `[FIGURE N ...]` bracket markers.
- `cover-brief.md` — cover design brief (no cover image exists yet).
- `production-notes.md` — this file.

## 2. Pending images — full list (19 slots, none delivered)

`06-production/images/` was empty at the time of this assembly. Every image below is a `[IMAGE PLACEHOLDER: ...]` in `manuscript-assembled.md`, not a delivered asset. Once a file is dropped into `06-production/images/` matching the ID (any extension, per `05-visuals.md`'s "filename contains the ID" matching rule), replace the corresponding placeholder block manually — this is a controlled step, not automatic, precisely so a human can confirm the delivered image actually matches the brief before it goes to print.

| Image ID | Chapter / location | Official Figure # | AI-generation status per 05-visuals.md |
|---|---|---|---|
| `intro-img01` | Introduction, end of "Compressed Modernization and Cultural Lag" | Figure 1 | AI-suitable (abstract concept diagram) |
| `ch1-img01` | Chapter 1, end of §1.6 | Figure 2 | Table body: not AI; decorative background only |
| `ch1-img02` | Chapter 1, §1.1, after the Hwahoe Mungi table | — (supplementary, not in Figure register) | Chart body: not AI; decorative frame only |
| `ch1-img03` | Chapter 1, §1.3, at the Jokbo comparison bracket | — (supplementary) | Table body: not AI; real archival image needs licensing if used |
| `ch2-img01` | Chapter 2, end of §2.5 | Figure 3 | Not AI (11 precise legal/date markers) |
| `ch2-img02` | Chapter 2, end of §2.6 | Figure 4 | AI-suitable for the wordless version; labels added after |
| `ch2-img03` | Chapter 2, §2.4, near "Severe working conditions" | — (supplementary) | Real archival photo required; AI generation not appropriate; must not depict Jeon Tae-il or the self-immolation |
| `ch3-img01` | Chapter 3, end of §3.5 | Figure 5 | Not AI (legal architecture must be exact) |
| `ch3-img02` | Chapter 3, immediately after ch3-img01 | Figure 6 | Not AI (statute numbers and dates) |
| `ch4-img01` | Chapter 4, §4.2 (relocated — see §3 below) | Figure 7 | Not AI (labor statistics line chart) |
| `ch4-img02` | Chapter 4, §4.3 (relocated — see §3 below) | Figure 8 | Not AI (time-use bar chart) |
| `ch4-img03` | Chapter 4, §4.2, "The Exit Phase" | — (supplementary) | AI-suitable (symbolic staircase concept, no data) |
| `ch4-img04` | Chapter 4, §4.2, "The Re-Entry Phase" | — (supplementary) | Not AI (employment-composition chart) |
| `ch5-img01` | Chapter 5, end of §5.5 | Figure 9 | Not AI (TFR/marriage-age time series) |
| `ch5-img02` | Chapter 5, end of §5.5 | Figure 10 | Not AI (age-band household chart) |
| `ch5-img03` | Chapter 5, end of §5.6 | Figure 11 | AI-suitable (concentric-rings concept diagram) |
| `ch6-img01` | Chapter 6, end of §6.5 | Figure 12 | AI for empty grid template only; cell text added by Production |
| `ch6-img02` | Chapter 6, end of §6.6 | Figure 13 | Not AI; also blocked on a legal-text dependency (see §4 below) |
| `ch6-img03` | Chapter 6, end of §6.7 | Figure 14 | AI for empty 4-panel template only; labels/questions added by Production |

**Full generation prompts, exact data tables, and sourcing guidance for every item above remain in `05-visuals.md` and were not duplicated in full inside the manuscript** — the manuscript placeholders point back to `05-visuals.md` by item ID so nothing has to be re-derived. When images arrive, cross-check them against `05-visuals.md`'s per-item brief before inserting.

Two items (`ch1-img02`, `ch1-img03`) and two more (`ch4-img03`, `ch4-img04`) have **no caption text fixed by the Visual Director** in `05-visuals.md` (no "캡션(원고 지정)" line was given for these four items, unlike every other item). This is flagged explicitly inside each placeholder in the manuscript rather than silently invented. The Editor or author should supply final caption wording for these four before the images are finalized.

## 3. Documented layout decision — Chapter 4 figures relocated

`05-visuals.md` states that the original manuscript placed the `[FIGURE 7]` and `[FIGURE 8]` bracket markers at the very end of Chapter 4 (after §4.5), but explicitly recommends moving them into the body at §4.2 and §4.3 respectively "since that location fits the content better," and leaves the final call to Production. Production adopted that recommendation: `ch4-img01`/Figure 7 now appears in §4.2 immediately after "...plotted in Figure 7..."; `ch4-img02`/Figure 8 appears in §4.3 immediately after the paragraph introducing the Time Use Survey. The original end-of-chapter bracket markers were removed rather than duplicated, and this decision is also flagged inline in the manuscript at the top of Chapter 4. If the author disagrees with this relocation, it is a one-step reversal: move both placeholder blocks in `manuscript-assembled.md` back to the end of §4.5.

## 4. Standing dependency carried over from the source manuscript — do not resolve

Chapter 6, Figure 13 (`ch6-img02`, the Family Rights Bundle table) has an explicit production dependency written into the original manuscript bracket itself: it must not be drafted until the 3 September 2025 Living Together Partnership bill text has been checked clause by clause, because the "registered partnership" column must show only effects the bill itself creates, distinguished from effects that would require separate tax or medical legislation. This dependency is preserved verbatim in the placeholder in `manuscript-assembled.md`. Do not build this figure early to save time — an inaccurate legal-status table is worse than a placeholder.

## 5. Two open author decisions — explicitly not resolved by Production

Per the task instructions, these were **not** resolved and are marked with highly visible markers at both the front of the manuscript and their exact in-text location:

1. **Chapter 1, §1.1 — `[EDITOR QUERY — NOT FOR PRINT]` marker** on whether the 1566 Hwahoe Mungi document directed ritual succession to the eldest son's house (rather than rotating it), which — if confirmed — would move the book's cultural-lag argument back roughly two centuries. Preserved verbatim, wrapped in an additional "AUTHOR DECISION PENDING" banner so it cannot be missed. **This marker must be resolved and removed before the manuscript goes to a reader-facing file.**
2. **"Book 2" self-reference vs. catalog position "Book 1."** The Introduction's "Theoretical Approach, Scope, and Structure" section and its heading both say "Book 2"; the confirmed catalog position per `00-brief.md` is "Korean Culture 본편 제1편" (Book 1). A `[PRODUCTION NOTE]` block is inserted directly under that heading, and the discrepancy is also summarized in the manuscript's front matter and in `cover-brief.md`. Production has not renumbered anything.

## 6. Internal cross-reference verification

Every explicit "Chapter N," "Figure N," "Introduction," and "Epilogue" cross-reference found in the source chapters was checked against the actual location of the thing it refers to (e.g., "see Figure 8, in Chapter 4" in Chapter 1 §1.4 does point to the Unpaid Work and Care Time figure that is in fact in Chapter 4 §4.3). **No incorrect or dangling cross-references were found** — all were converted to working markdown anchor links (`[Chapter 4](#ch-4)`, `[Figure 8](#fig-8)`, etc.) pointing at anchors placed directly above the relevant heading or figure, and the Table of Contents at the top of the manuscript links to every chapter and every `###`-level section heading in the book, plus the Appendix's internal `##` sections. No chapter or section wording was altered to create these links — only markdown link syntax was added around already-existing text.

## 7. Format / special-character notes for future EPUB/PDF conversion

- The manuscript uses Korean Hangul, Hanja, and italicized Latin-transliteration terms extensively (e.g., 호주제, 戶主, *Gyeongguk Daejeon*). Confirm the chosen EPUB/PDF toolchain and embedded font support full Hangul + CJK rendering before conversion — do not assume a default Latin ebook font/template will render these correctly.
- Several markdown tables (Chapter 1 §1.1's Hwahoe Mungi table; the Figure register table in the Appendix) will need conversion-tool-specific handling — test that pandoc or the chosen tool renders pipe-tables correctly in the target format, especially where the table contains mixed Hangul/Hanja and Latin text.
- Footnote-style bracket citations (`[1]`–`[22]`, `[3]`, `[5]`, etc.) are plain bracketed text, not linked footnotes. If the target platform supports true EPUB footnotes/endnotes, consider converting these to linked notes pointing at the corresponding `References` entry; this was left as plain text in this pass since it is a formatting enhancement, not a structural requirement, and changing citation mechanics is closer to an Editor/Production judgment call that should be confirmed with the author first.
- The blockquote-style `[PRODUCTION NOTE]` and `[EDITOR QUERY — NOT FOR PRINT]` markers must be stripped or converted to genuinely internal (non-reader-facing) annotations before any reader-facing EPUB/PDF/print file is generated — they are intentionally left visible in `manuscript-assembled.md` precisely so they cannot be missed at this stage, but they are not intended for the finished retail product once resolved.

## 8. EPUB/PDF conversion — deferred, with instructions for when it is time

Binary conversion was intentionally not attempted in this pass — see the note at the top of this file. When the author is ready (after the two open decisions above are resolved and all 19 images are either delivered or deliberately accepted as still-placeholder for a preview build), conversion can be done with `pandoc`, e.g.:

```
pandoc manuscript-assembled.md -o manuscript.epub --metadata title="Korea's Family Transformation" --metadata author="[author name]" --toc --toc-depth=3
pandoc manuscript-assembled.md -o manuscript.pdf --toc --toc-depth=3 --pdf-engine=xelatex -V mainfont="Noto Serif" -V CJKmainfont="Noto Serif CJK KR"
```

The `xelatex` engine and a CJK-capable font (e.g., Noto Serif CJK KR / Noto Sans CJK KR) are required for correct Hangul/Hanja rendering in the PDF path; the default `pdflatex` engine will fail or drop non-Latin characters. If `pandoc` or a LaTeX engine is not available in the environment where conversion is finally run, install via the system package manager (e.g., `apt-get install pandoc texlive-xetex fonts-noto-cjk` on Debian/Ubuntu) or use an equivalent EPUB/PDF export tool (e.g., Calibre's `ebook-convert`). **The Uploader stage depends on this conversion step being completed with a clean, placeholder-free manuscript** — do not hand `manuscript-assembled.md` to Uploader as-is; it still contains internal production markers and image placeholders that must not reach a retail listing.
