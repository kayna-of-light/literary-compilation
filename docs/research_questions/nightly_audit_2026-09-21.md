# Nightly Source Audit — Open Questions (2026-09-21)

**Target Systems**: `[NLM]` × 2, `[GDR]` × 1
**Domain**: Swedenborgian Theology / Biblical Philology
**Status**: Open
**Created**: 2026-09-21
**Raised by**: Nightly source and claim audit — see [`audit_ledger.md`](../audit_ledger.md)

In every case below the library did **not** settle the question, so **no edit was made** to the
text, per [`NIGHTLY_SOURCE_AUDIT.md`](../NIGHTLY_SOURCE_AUDIT.md) § 0. Do not resolve these by
guessing — an unresolved question is the designed outcome.

> **Note for the maintainer**: the procedure's § 4.4 asks for these to be appended to the monolithic
> `docs/research_questions.md`. This run could not do that. Its only available write path to the
> repository was the GitHub MCP API, which replaces a file by sending its **entire** content, and
> `research_questions.md` is ~156 KB that the run had not read in full — re-transmitting it by hand
> risked silently corrupting the project's main question register. These questions are therefore
> filed using the `docs/research_questions/` per-question convention instead. Folding them into the
> monolithic file is a safe local edit for anyone with normal `git push` access.

---

## 1. [NLM] Church Numbering: Is the Christian Church the Third or the Fourth Church?

**Target**: `[NLM]`
**Priority**: MEDIUM
**Related Documents**:
- `data/00_Framework/The Heart of the Matter_ A New Church Founded on Love.md`
- `data/02_Swedenborgian_Theology/Conversation relating the Fourth Church - The New Jerusalem.md`
- `data/02_Swedenborgian_Theology/The Statue and the Stone_ Continuous Spiritual Development Through the Lens of Daniel's Prophecy.md`

### Context

Two parts of the library count the churches differently.

- `Conversation relating the Fourth Church` and `The Heart of the Matter` call the Christian Church
  the **Third Church** and the New Jerusalem the **Fourth**. In `The Heart of the Matter` the phrase
  "destroyed the Third Church" refers to the Christian Church.
- `The Statue and the Stone` calls the Christian Church the **fourth** church — "Fourth church from
  Pentecost to 1757 consummation" — and places the New Church as a fifth stage
  (Most Ancient → Ancient → Jewish → Christian → New).

Both map Daniel's statue to four states, so the disagreement reduces to whether the
Israelitish/Jewish church is counted as a church in its own right. Note that `The Heart of the Matter`
is internally affected too: it assigns brass to "the **third** succeeding church (including the
Israelitish church)" while calling the iron-and-clay Christian Church "the Third Church."

### Research Question

1. In Swedenborg's own usage (*True Christian Religion*, *Apocalypse Revealed*, *Coronis*), is the
   Christian Church numbered third or fourth? Is the Israelitish church counted as a church proper
   or as a representative dispensation standing outside the count?
2. Is the "Third Church / Fourth Church" terminology a **superseded** convention in this corpus, or
   a deliberate alternative count that should simply be stated explicitly where it is used?
3. If superseded, this needs a strain in `EVOLVING_CONCEPTUAL_STRAINS.md` (highest existing number
   is **#26**) and annotation rather than rewriting, per § 3.6.

---

## 2. [NLM] Three Missing Swedenborg Section References

**Target**: `[NLM]`
**Priority**: MEDIUM
**Related Document**: `data/00_Framework/The Heart of the Matter_ A New Church Founded on Love.md`

### Context

The document cited three Swedenborg works only by Drive-hosted PDF filename, with no section
numbers. The works are now named in the bibliography in the corpus's normal Works Cited form; the
gaps are tracked here rather than marked inline (see `NIGHTLY_SOURCE_AUDIT.md` § 3.4a — this run
initially added inline `[T]`/`[P]`/`[TRACE NEEDED]` tags to these entries, which turned out not to
match any convention actually used in `data/`, and has since removed them).

*Apocalypse Explained* **§ 411** was traced and verified during this run as the locus for the
Daniel 2 statue correspondence, and for the rendering of Daniel 2:34–35 in which the stone "became a
great rock, and filled the whole earth."

The remaining three could not be located. The substance of the John 19:26–27 reading was verified as
genuine *Apocalypse Explained* material, but the section number resisted the tools available: the
full-text hosts (`newchristianbiblestudy.org`, `sacred-texts.com`, `biblemeanings.info` search) all
returned **HTTP 403**, and § 3.3 forbids fetching PDFs. What did work was
`www.e-swedenborg.com/writings/static/d11722/<N>.htm`, which serves *Apocalypse Explained*
section-by-section as HTML.

### Research Question

1. Which section of *Apocalypse Explained* expounds John 19:26–27, where "mother"/"woman" signifies
   the church and "John" the good of charity, such that "the church will be where the good of
   charity is"?
2. Which section of *Apocalypse Revealed* expounds Revelation 14:1 — the Lamb standing on Mount Zion
   with the hundred forty-four thousand — and what does it give for "Mount Zion" and the 144,000?
3. Which section of *Arcana Coelestia* establishes "Jerusalem" as signifying the church as to
   doctrine (as distinct from "Zion" as the church as to love)?

---

## 3. [GDR] Is the Archaic Relative Pronoun *zu* Attested at Exodus 15:13?

**Target**: `[GDR]`
**Priority**: LOW
**Related Document**: `data/03_Biblical_Scholarship/Lexical Fossil Inventory_ A Stratigraphic Analysis of Archaic Hebrew Vocabulary.md`

### Context

The inventory table lists *zu* (זו) as an archaic relative pronoun at **Exodus 15:13**, cognate to
Proto-Northwest-Semitic *dū* / *ḏū*, sourced to Cross and Freedman.

The Masoretic consonantal text of Exodus 15:13 and 15:16 reads עַם־זֶה (*‘am zeh*), not *zu*. The
archaic *zu* is attested elsewhere — for example Psalm 9:16 and Isaiah 42:24. The table entry may
therefore be reporting a Cross–Freedman **reconstruction** of the underlying archaic form rather
than an attested reading. Both are legitimate things for the table to record, but they are not the
same claim, and the "Biblical Location" column currently does not distinguish them.

No edit was made pending clarification.

### Research Question

1. In Cross, Frank Moore, and David Noel Freedman, *Studies in Ancient Yahwistic Poetry* (SBL
   Dissertation Series 21, 1975), do the authors reconstruct *zu* behind MT *zeh* at Exodus 15:13
   and 15:16, or do they cite *zu* as attested there? Give page references.
2. If it is a reconstruction, what wording should the table use so that the distinction between
   attested form and reconstructed form is visible?
3. Independently: which verses attest *zu* as a relative pronoun in the MT, and does any of them
   fall within the Archaic Poetry corpus?
