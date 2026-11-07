# Research Question: A Coptic-First Reading of the Apocryphon of John's Angel List

> **Target System**: [NLM] / in-session (Coptic sources on disk) — see "Resources" below
> **Status**: Open
> **Created**: 2026-11-07
> **Priority**: Medium
> **Domain**: Correspondential Texts / Coptic philology / Swedenborgian body-part correspondences

---

## Why this is open

*The Unnamed Cartography* (`data/08_Correspondential_Texts/`) compared 43 angel names of the body-creation passage (NHC II 15,13–19,10) with Swedenborg's body-part correspondences and found no contradictions. Its etymologies were derived from the English transliterations in Robinson 1990 (Wisse's translation). Its §3.8 now checks that text against the Coptic of both manuscripts (Linssen 2024) and finds it sound: the names are the scribes' names, the body parts and substance-souls are the same, and right–left differences are between Codex II and Codex IV, not errors of the translation.

That check confirms what was already scored. It does not do the larger work it opens up: **reading the list from the Coptic outward**, which is the author's standing rule for NHL work (ledger, 2026-10-31: quote and translate from the Coptic, never from Robinson's English). A separate thesis (*The Letters They Dropped*, withdrawn 2026-11-07) claimed to have done this but had read Robinson's Codex IV parentheses as errors and the linking particle as dropped letters; nothing of it survives except what is now in §3.8.

## The research opportunity — five parts

1. **The opaque names from the Coptic.** About 30 of the scored-or-attempted names (and most of the 365) were rated tentative or opaque from the English. Derive each afresh from the Coptic spelling of both codices, with Crum (1939) and Černý (1976) for any Egyptian element, LSJ/BDB/Jastrow for Greek and Semitic, and the Coptic word division settled first (a final ⲛ/ⲙ before a body part is usually the linker ⲛ̅/ⲙ̅ — Codex IV writes it apart). Then compare with Swedenborg as *The Unnamed Cartography* does. **What would count as a miss**: names newly translatable from the Coptic whose quality contradicts Swedenborg's correspondence for the part.
2. **The readings that differ from the English.** ⲫⲛⲏⲙⲏ (II 17,2; English "Phnene") and ⲁⲅⲣⲟⲙⲁⲩⲙⲁ (II 16,20; IV 25,23; English "Agromauna") — Linssen and Wisse read differently. Settle against the photographic facsimile (*The Facsimile Edition of the Nag Hammadi Codices*, Codex II and Codex IV volumes) or the Waldstein–Wisse synopsis (1995). The Agromauna score in §3.4 depends on it (see the monolithic-file entry).
3. **Codex II against Codex IV, name by name.** Codex II lacks the right-hand entry at the shoulder, elbow and hip (IV 25,4–7, 19–20), and spells some names differently (ⲙⲛⲓⲁⲣⲭⲱⲛ / ⲙⲛⲓⲁⲭⲱⲣ; ⲥⲏⲛⲁⲫⲓⲙ / ⲥⲏⲛⲁⲫⲑⲓ). A full collation would show which copy is closer to the archetype, and whether any of the paired right/left names carries Swedenborg's right = good / left = truth distinction (*AC* §10061). Codex IV's lacunae limit this; record what is lost.
4. **The body-part words themselves.** Several labels are uncertain in translation: ⲕⲗⲗⲉ ("knee" in Robinson; Crum's attestations point to the ankle, S ⲕⲉⲗⲉ = ἀστράγαλος), ⲡⲉⲧ (Robinson "leg"; Crum ⲡⲁⲧ/ⲡⲉⲧ "knee"), ⲑⲱⲙⲉ (Robinson "underarm"; Crum ϩⲱⲙⲉ palm, πῆχυς), ⲡⲉⲕⲟⲩⲛϥ ("womb"; Crum ⲕⲟⲩⲛ⸗ bosom). A wrong body part moves a name's comparison to a different Swedenborgian locus.
5. **The second list and the rulers.** The second list (II 17,8–29, part-then-name), the seven over all (17,29–32), the rulers of the senses (17,32–18,2) and the passion demons (18,14–19,1) have not been compared with Swedenborg except the four elemental rulers and the four chief demons.

## What is already settled (do not redo)

- Word division at Asterechme, Thaspomocha, Achcha, Kriman, Tupelon, Areche: Robinson follows Codex IV (*Unnamed Cartography* §3.8).
- Substance-souls: envy → skin (ϣⲁⲁⲣⲉ), understanding → hair (ϥⲟⲩϩⲉ); understanding = ⲙⲛⲧⲣⲙⲛϩⲏⲧ, built on ϩⲏⲧ.
- Marrow ⲁⲗⲧⲕⲁⲥ/ⲁⲧⲕⲁⲥ = "pain-remover" (Černý); "boneless" is a folk etymology (Crum). ϫⲓⲥⲉ in "spine of the body" = the noun "back". Navel = ⲑⲟⲗⲡⲉ (ϩⲉⲗⲡⲉ).
- Swedenborg's sides: right = good, left = truth (*AC* §10061; §4410).
- The four passions are the Stoic tetrad (DL 7.110); fear is the Akhmimic ϩⲛⲱϩⲉ.

## Resources

- Coptic: `nag-hammadi-analysis/output/coptic/II_1_apocryphon_john.md` (folios 15–19 = II 15–19) and `IV_1_apocryphon_john.md` (folios 24–29). Grep fails on Coptic; use a Python pass (strip combining marks with `unicodedata.combining`).
- Crum: `https://remnqymi.com/crum/crum.json` (search the `WIKI` text). Černý: archive.org FTS `copticetymologic0000ernj`.
- English: `nag-hammadi-analysis/output/english/tractates/II_1_apocryphon_john.md` ll. 103–115 (Codex IV variants in parentheses).
- Not on disk: the facsimile volumes and Waldstein–Wisse 1995 — check the author's Drive `Books` folders first.
- Other repository (not edited by this job): `nag-hammadi-analysis/findings/tractates/AJ_angel_name_translations.yaml` carries the withdrawn thesis's misreadings in its header and entries; it should be corrected before it is used as a source.
