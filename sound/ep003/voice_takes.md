# Ep. 003 — voice takes (final set: voice-tests `lines/ep003-final`)

Base: `lines/ep003-v3` (93 lines, seed 1). Checked with ASR on two models (medium.en + large-v3).
Number/spelling differences ("forty" vs "40", "Coldcard" vs "cold card") are not problems.

Replaced (both models clean on the new take):

| line | problem in v3 | new take |
|---|---|---|
| c12 | "Coinkite" heard as "Koinkite" (medium) | fix2 `c12_s2` |
| c13 | "Coinkite's" → "Coen Kite's" (both) | fix1 `c13_s2` |
| c15 | "a seed" → "the seed" (medium) | fix2 `c15_s2` |
| f6 | "head" → "had" (large, low confidence) | fix1 `f6_s4` |
| g6 | "Block's" → "Lox" (large) | fix1 `g6_s2` |
| g7 | "matched" → "match" | fix1 `g7_s4` (medium clean; large hears "match" at low confidence — the d is swallowed before "the", acceptable) |
| h1 | "Coinkite" → "Coen kite" (both) | fix1 `h1_s4` |
| k1 | "Coinkite" → "Coenkite" (medium) | fix2 `k1_s2` |
| k6 | "Coinkite's" → "Conkite's" (both) | fix1 `k6_s4` |

Kept: t5 "flaw" (heard "floor": same sound in British English), g5 "guessed" ("guest": homophone),
g10 "Thorn" ("Thorne": spelling only).

"Coin-kite" spelled variants were tried and rejected: no better than a new seed.
Mix: `sound/ep003/ep003_mix.py`, 636.6 s; master +2.6 dB + limiter → -14.0 LUFS, peak -2.1 dBFS
(renders `audio/ep003_audio.m4a`).
