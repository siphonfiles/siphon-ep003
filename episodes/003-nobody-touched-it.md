# Episode 003: Nobody Touched It

**Title (proposed): Inside the $116M Coldcard Hack** · thumbnail text: **NOBODY TOUCHED IT.**
**Test & Compare at publishing (proposed):** (A) this title + "NOBODY TOUCHED IT."; (B) "The Safest Bitcoin Wallet Was Guessable for 5 Years" + "41 MINUTES."; (C) "Inside the Coldcard Hack: $116M Gone Without a Touch" + "5 YEARS. 41 MINUTES."

**Subject:** the Coldcard hardware-wallet thefts (30 July – early August 2026). A build error in Coinkite's March 2021 firmware made some Coldcard devices create wallet seeds from a predictable software generator instead of the hardware random-number chip. Attackers rebuilt the seeds offline and swept about 1,816 BTC (about $116M) from more than 5,200 addresses in four waves, without touching a single device.
**Angle:** the device built to be the safest place for bitcoin was, for more than five years, predictable. The safety check that should have stopped the build was there, and it passed. The first thief may have left a trail, not on the blockchain, but in a paid account.
**Status:** DRAFT v1, written 2026-11-23. Facts checked against the sources below (see "Notes for proprietarul's check"). Proprietarul must check it before any generation (rule 10).
**Target length:** about 10:45–11:15 with cards, pauses, music beats and end card (rule 13).
**Length:** 1,502 spoken words (automatic count, cards and cues excluded), Thomas 258 words in 28 lines (~1:30), each ≤ 12 words so every line fits one 5 s LongCat clip (≤ 4.7 s of speech). Ep. 002 ran 11:11 with 1,577 words, so this lands at about 10:40–11:00.

Notation (same as ep. 001/002):
- `[THOMAS]` = Thomas on camera, one line = one clip. `[VO]` = voice over b-roll. `[VIS]` = on screen. `[CARD]` = quote shown as text, never voiced as the real person. `[S#]` = source.
- Numbers are written as digits; the pipeline normalizes them.

**Editorial line for this episode (important):**
- **No one has been identified, charged or arrested.** The FBI has not confirmed a suspect [S20]. Galaxy's Alex Thorn says the first-wave attacker's identity "may be known to law enforcement" [S19]: the script quotes exactly that and adds that it is unconfirmed.
- **Several attackers, not one.** Galaxy counts at least 15 separate attackers [S6]; TRM sees different transaction construction across waves and does not attribute [S7]. The script says "the first thief" only for wave 1.
- **"Inside job" theories** circulate online. There is no public evidence for them and nobody is accused. The script says so in one line and names no one. The developer who made the 2021 change is **not** named.
- **The class action (Ontario, 11 Sep 2026) is allegations only** [S23]. "Alleges", "has not been tested in court".
- **AI:** Coinkite says it "must assume" someone used AI on old firmware [S3][S21]; that is Coinkite's assumption, worded as such. Coinkite's own AI review weeks earlier missed the bug [S3] (fact, from Coinkite).
- **Loss figures differ** (Galaxy potential 1,816 BTC; Galaxy high-confidence minimum 1,730 BTC [S8]; later ~1,830 BTC [S24]). The voice says "about 116 million", the TRM/Galaxy figure used by most outlets and the title [S7]. Ranges go in the description.
- **Mk4, Mk5 and Q** had a smaller weakness (~72 bits) and were not shown to be exploited in these sweeps [S1][S2]. The script never says "every Coldcard".
- **The victim is real and public:** Jonathan Goodman told his own story on X and to Wealthsimple Magazine [S12][S13]. Only what he said publicly. No invented scenes.
- **No investment advice.** The close points to Coinkite's own advisory, worded as Coinkite's instruction.
- **No Coldcard/Coinkite logo or real device design in illustrations.** The device is a generic small black hardware wallet; names appear only as text.

**Structure (after `research/suspense-storytelling.md` and `research/retention-psychology.md`):**
- First line = a small concrete image: a bank safe-deposit box with a device inside that has never been online. The ending returns to it.
- A person to care about, from facts only: Goodman, who "did everything right", at his cottage while it happens, finding out two days later.
- Knowledge gap: from March 2021 *we* know the seeds are guessable; the owners don't, for five years. At 01:10 UTC we watch the sweep; Goodman doesn't know until 31 July.
- T-minus countdown to **01:10:20 UTC, 30 July**.
- Planted before the peak, paid after: the **fixed fee** on every first-wave transaction ("hold on to that fee") → the tell that leads to a paid account.
- Every section ends on "but"/"so", never a conclusion. Max 2–3 numbers spoken per section.
- Designed peak: the 41 minutes, seen from Goodman's addresses (9:36 to 9:43 pm, Ontario time).
- Proposed chapters: The box · The promise · March 2021 · The check that passed · Five years · 01:10 · Seven minutes · He didn't know · The race · The tell · Who? · The box, again.

---

## 0:00 — TEASER

`[MUSIC: full]` About 13 dB under the voice. Bass hit on every cut-off line. Fade over 5 s after the last line.

`[VIS]` A bank vault at night. One small drawer, closed. Dust in a single beam of light.

`[VO]`
A bank in Ontario. A safe-deposit box. Inside it, a small device that has never been connected to the internet. [S12]

`[VO]`
On the night of July 29th, nobody opened that box. Nobody touched that device. [S12][S14]

`[VO]`
In seven minutes, the bitcoin it protected was gone.

`[VO]`
Over the next five days, about 116 million dollars left more than 5,200 wallets just like it. [S7]

`[VO]`
And the mistake that made it possible had been sitting in public code. For five years.

*(Every line generated with a full stop; the cut is made in the edit, on the bass hit.)*

`[VIS]` Hard cut to black. ~1.6 s of bass. Title fades in: **SIPHON FILES · NOBODY TOUCHED IT**.

---

## 0:35 — THOMAS (intro)

`[MUSIC: out]`

`[THOMAS]` I'm Thomas Archer, the AI narrator of Siphon Files.
`[THOMAS]` Every claim you'll hear is sourced. The list is in the description.
`[THOMAS]` Tonight: the safest place to keep bitcoin.
`[THOMAS]` And the one setting that made it guessable.

---

## 0:55 — THE PROMISE

`[VO]`
The Coldcard is a hardware wallet, made by a Canadian company called Coinkite. It has one job: create your keys offline, and keep them there. [S7][S11]

`[VO]`
When you set one up, it gives you a list of 12 or 24 words. Those words are the money. Anyone who has them can spend your bitcoin, from anywhere. [S2]

`[VIS]` A blank card with 24 numbered lines, the words blurred.

`[VO]`
So the words have to be impossible to guess. The device picks them from pure chance, using a chip whose only purpose is to produce random numbers. [S2][S4]

`[VO]`
Done properly, the number of possible word lists is so large that nobody could ever search through them all. [S2][S7]

`[VO]`
Some owners go one step further. They roll physical dice and type the results in, adding randomness of their own. Most don't. The chip is supposed to do that. [S1]

`[VO]`
But the chip only helps if it's actually asked.

---

## 1:40 — MARCH 2021

`[CARD]` **T-MINUS 5 YEARS, 4 MONTHS**

`[VO]`
March 2021. Coinkite ships a firmware update. Under the hood, it swaps in a new, well-respected cryptography library. [S2][S4]

`[VO]`
The new library needs random numbers too. So it asks the system for them, by name. [S4]

`[VIS]` Two boxes: **HARDWARE RANDOM CHIP** (cyan, idle) and **SOFTWARE FALLBACK** (grey). An arrow from "seed generation" lights up the wrong one.

`[VO]`
And there are two things in the code with that name. One is the hardware chip. The other is a simple software fallback, meant for computers that don't have a chip at all. [S4]

`[VO]`
Coinkite didn't want the fallback. So it switched it off, with a setting: zero. [S2][S4]

---

## 2:20 — THE CHECK THAT PASSED

`[VO]`
The library's authors had seen this coming. They left a guard in the code. If the hardware setting was missing, the build would stop, with a message. [S4]

`[VIS]` A code line types itself out: `#error "get a HW TRNG plz"` · source: Block Engineering [S4]

`[VO]`
But the guard only checked whether the setting existed. It did. It was set to zero, but it existed. So the build went through. [S4]

`[THOMAS]` Think of a smoke alarm inspector.
`[THOMAS]` He checks that there's an alarm on the ceiling.
`[THOMAS]` He never checks that it's switched on.
`[THOMAS]` That's what happened here. The alarm was there. It was off.

`[VO]`
From then on, on the older Mk2 and Mk3 models, new seeds came from the fallback, fed by the device's serial number and a timer. Both are things an attacker can estimate. [S4][S6]

`[VO]`
Coinkite later put the result at about 40 bits of real randomness, instead of the 128 it was designed for. [S1][S2]

`[THOMAS]` Forty bits sounds like a lot. It's about a trillion possibilities.
`[THOMAS]` For a computer guessing offline, that's a search with an end.

`[VO]`
On newer models the gap was smaller, about 72 bits. Still far below the design, but no one has shown those were drained in this attack. [S1][S2]

---

## 3:55 — FIVE YEARS

`[VO]`
So from here on, you know something the owners don't. Their words were never truly random. [S7]

`[VO]`
And the code is public. Anyone can read it. For five years, people buy the device, write their words down, and lock them away. [S7][S11]

`[VO]`
Coinkite says it paid for outside security reviews, in 2022 and 2024. And weeks before the theft, it ran an AI review of its critical code. It did not catch this. [S3][S22]

`[CARD]` **"It did not catch this vulnerability."** — Coinkite, on its own AI-assisted review [S3]

`[VO]`
Then, in late July 2026, someone else reads the old firmware. [S3]

`[THOMAS]` Coinkite says it must assume that someone used AI to find it.
`[THOMAS]` That's Coinkite's assumption. It hasn't been proven.
`[THOMAS]` But the method didn't need a single device.
`[THOMAS]` Guess a seed. Work out its addresses. Check the blockchain.
`[THOMAS]` A match means a key. Repeat, until the money runs out.

`[VO]`
No phishing. No malware. No break-in. Just arithmetic, done somewhere else. [S7][S6]

---

## 5:05 — 01:10

`[CARD]` **T-MINUS 0 · 30 JULY 2026 · 01:10:20 UTC**

`[MUSIC: vault]` Feature level. Fades out ~2.9 s before "Every one of them".

`[VO]`
Thursday, July 30th. Ten past one in the morning, UTC. The first transaction leaves a Coldcard-made address. Then another. Then hundreds. [S5][S8]

`[VIS]` A block-explorer timeline: blocks **960,183 → 960,191**, address dots draining to three collector points.

`[VO]`
According to Chainalysis, the thief went for the biggest wallets first. About 30 million dollars in the first ten minutes. [S10]

`[VO]`
And there's something odd about these transactions. Every single one pays exactly the same fee, and sends everything, leaving nothing behind. [S9]

`[VO]`
Hold on to that fee.

`[VO]`
At 01:51 the sweep stops. 41 minutes. 1,196 addresses emptied. 1,082 bitcoin. [S5]

`[VO]`
Every one of them was a wallet whose owner believed it was offline, and safe.

---

## 6:05 — SEVEN MINUTES

`[VO]`
In Ontario, it's still the evening of July 29th. Jonathan Goodman, an entrepreneur from Toronto, is away at his cottage. [S12][S14]

`[VO]`
His Coldcard sits in a bank safe-deposit box. It has never touched the internet. His words have never left his hands. [S12]

`[VIS]` Three wallet balances on a dark screen, each line turning red in sequence: **9:36 PM → 9:43 PM**.

`[VO]`
Between 9:36 and 9:43 pm, every wallet he has is emptied. 18.25 bitcoin. About 1.6 million Canadian dollars. Seven minutes. [S12]

`[CARD]` **"I did everything right."** — Jonathan Goodman, on X [S12]

`[VO]`
But he doesn't know yet. Nobody does.

---

## 6:50 — HE DIDN'T KNOW

`[VO]`
Over the next hours, reports trickle in of coins moving out of cold wallets. Engineers at Block, the company behind the Bitkey wallet, start pulling the firmware apart. [S10][S4]

`[VO]`
They find the bug, and tell Coinkite the same day. [S10]

`[VO]`
About 30 hours after the first sweep, Coinkite publishes its warning: seeds made on affected firmware are at risk. Move your funds. [S10][S26]

`[VO]`
Goodman learns about it on July 31st, from a friend's post on Facebook. He checks. The money has been gone for two days. [S13]

`[VO]`
When he reports it, the first question he gets is whether someone broke into his safe-deposit box. [S13]

`[VO]`
Nobody did. And a firmware update can't help him. It fixes new seeds. A weak seed that's already written down stays weak forever. [S1][S7]

`[CARD]` **"I'm sorry and I'm devastated."** — Rodolfo Novak, Coinkite founder, 31 July [S14]

`[VO]`
So now there's a race.

`[THOMAS]` Here's the cruel part of a public warning.
`[THOMAS]` It reaches the owners and the thieves at the same moment.
`[THOMAS]` Some owners move in time. Some don't.

---

## 7:55 — THE RACE

`[VO]`
Wave two comes the next day. Wave three runs from Friday into Saturday. A fourth starts on Monday. [S11][S16]

`[VO]`
By then, Galaxy Research counts at least 15 separate attackers. Not one thief anymore. A crowd, working the same weakness. [S6]

`[VO]`
In the fourth wave, the thieves' transactions can still be replaced by anyone willing to pay a higher fee. [S16]

`[VO]`
One owner, Will Owens, leaves a small amount behind as bait, waits for the bot, and outbids it. He wins. [S17]

`[VO]`
Later, volunteer white hats move about 52 bitcoin out of exposed wallets, into a trust set up to return it to victims. [S18]

`[VO]`
Some of the stolen coins head for mixers, services built to blur the trail. Most just sit. [S7]

`[VO]`
By the time it slows down, about 1,816 bitcoin are gone, from more than 5,200 addresses. [S7]

`[VO]`
But the biggest piece, the first wave, hasn't moved at all.

---

## 8:55 — THE TELL

`[THOMAS]` Remember that fee? The same on every transaction.
`[THOMAS]` Galaxy checked the previous thirty days. Nobody else used that pattern.
`[THOMAS]` So whoever ran wave one had built their own machine.
`[THOMAS]` And a machine like that has to ask a lot of questions.

`[VO]`
Which of these guessed addresses hold money? To find out fast, you can pay a blockchain data company to answer. [S19]

`[VO]`
Block's investigators say the first-wave operator appears to have done exactly that, through a paid account at a well-known blockchain data provider. [S19]

`[VO]`
They contacted the provider. Its internal logs, they say, matched the attack "with extraordinary specificity": the number, the timing and the order of the requests. [S19]

`[VO]`
The information went to law enforcement. Galaxy's Alex Thorn says the first-wave attacker's identity "may be known to law enforcement". [S19]

`[VO]`
The FBI has not confirmed a suspect, an arrest, or any recovery. [S20]

---

## 9:50 — WHO?

`[VO]`
So who did it? Publicly, no one knows. TRM Labs doesn't attribute the theft to anyone. [S7]

`[VO]`
Coinkite says its lawyers are working with law enforcement in various jurisdictions to identify those responsible. [S27]

`[VO]`
Online, some call it an inside job. There's no public evidence for that, and no one has been accused. [S7][S20]

`[VO]`
In September, a Coldcard owner filed a proposed class action in Ontario against Coinkite and its co-founders. It alleges the company knew its seed generation was weak by May 2025. Those claims have not been tested in court. [S23]

`[VO]`
Coinkite says the flaw affected about 0.17 percent of its users. And its new firmware now requires every owner to add randomness of their own when making a seed. [S24][S25]

---

## 10:30 — THE BOX, AGAIN

`[VO]`
There's one group Coinkite doesn't consider at risk from this bug. Owners who added at least 50 dice rolls of their own when they made their seed. [S1]

`[VO]`
The few who didn't leave it all to the chip.


`[THOMAS]` The safe-deposit box in Ontario was never opened.
`[THOMAS]` The device inside still works perfectly.
`[THOMAS]` It just never asked the right chip for a number.
`[THOMAS]` If you made a seed on an affected Coldcard, read Coinkite's advisory.
`[THOMAS]` Coinkite says treat it as compromised, and move to a new seed.

`[MUSIC: full]` Heist theme returns, fades over 5 s.

`[VO]`
And the 1,082 bitcoin from the first wave? As of the last public reports, they're still sitting where the thief left them. [S19]

`[VO]`
Someone may know whose they are.

`[THOMAS]` This was Siphon Files.

`[VIS]` End card.

---

## Sources

- [S1] Coinkite, *COLDCARD Mk2/Mk3 seed generation security advisory* (affected firmware, ~40 bits Mk2/Mk3, ~72 bits Mk4/Mk5/Q, dice/passphrase exceptions, migration): https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/
- [S2] Coinkite, *Technical deep dive into the entropy issue*, 1 Aug 2026 (`ckcc.rng_bytes()` → `ngu.random.bytes()`; `MICROPY_HW_ENABLE_RNG=0` "was intended to disable the software path"): https://blog.coinkite.com/entropy-technical-backgrounder/
- [S3] Coinkite, *Adding to the public record* (AI-assisted review "including in the weeks before the exploit… did not catch this vulnerability"): https://blog.coinkite.com/adding-to-public-record/
- [S4] Block Engineering, *Predictable RNG fallback and 32-bit reseed in COLDCARD firmware* (board config, the `#ifndef` guard, Yasmarang fallback, Mk2/Mk3 "no cryptographic entropy"): https://engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware
- [S5] The Block, *Bitcoin losses linked to Coldcard vulnerability grow to $70 million, Galaxy Research says*, 31 Jul 2026 (1,196 addresses, 1,082.65 BTC, 01:10:20–01:51:26 UTC, pattern from Block's Clay Garrett): https://www.theblock.co/post/410332/bitcoin-losses-linked-coldcard-vulnerability-70-million-galaxy-research
- [S6] Galaxy Research, *Your keys, not your coins: Coldcard wallets hacked for $130M and counting*, 7 Aug 2026 (≥15 separate attackers; fallback seeded by fixed device info and timer registers; 18.25 BTC victim): https://www.galaxy.com/insights/research/your-keys-not-your-coins-coldcard-wallets-hacked-for-130m-and-counting
- [S7] TRM Labs, *The largest hardware wallet exploit of 2026: inside the USD 116 million Coldcard hack*, 5 Aug 2026 (1,816 BTC, 5,200+ addresses, four waves, no attribution, multiple attackers, laundering so far): https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack
- [S8] Cointelegraph, *Coldcard Bitcoin loss estimate rises to $70M after Galaxy analysis* (blocks 960,183–960,191; ~30 hours before the advisory): https://cointelegraph.com/news/coldcard-bitcoin-loss-estimate-70-million-galaxy-analysis · and *How investigators trace stolen bitcoin* (high-confidence minimum 1,730 BTC): https://cointelegraph.com/news/coldcard-losses-how-investigators-trace-stolen-bitcoin
- [S9] The Hacker News, *Coldcard hardware wallet flaw linked to…* (Galaxy: no other transactions in the previous 30 days with the same 30 sat/vB, no-change signature): https://www.thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html
- [S10] BleepingComputer, *Coldcard wallet RNG flaw likely linked to $88 million bitcoin theft* (Chainalysis: ~$30M in the first ten minutes, high-value wallets first; Block disclosed to Coinkite on 30 Jul; ~30 hours): https://www.bleepingcomputer.com/news/security/coldcard-wallet-rng-flaw-likely-linked-to-88-million-bitcoin-theft/
- [S11] Fortune, *Bitcoin owners lose $116 million in Coldcard hack*, 3 Aug 2026 (waves 3 and 4; device description): https://fortune.com/2026/08/03/bitcoin-owners-116-million-hack-coldcard-coinkite-exploit/
- [S12] IBTimes UK, *$1.6M Bitcoin gone in seven minutes…* (Goodman's X post: 9:36–9:43 pm, 29 July, 18.25245043 BTC, bank safety deposit box, never online): https://www.ibtimes.co.uk/canadian-entrepreneur-bitcoin-loss-hardware-wallet-flaw-1811995
- [S13] Wealthsimple Magazine, *How I lost $1 million in bitcoin in 8 minutes* (Goodman interview: discovered 31 July; the safe-deposit-box question): https://www.wealthsimple.com/en-ca/magazine/how-i-lost-1-million-in-bitcoin-in-8-minutes
- [S14] Silicon Canals (Goodman at his cottage; Novak's apology, 31 July): https://siliconcanals.com/?p=107725
- [S15] Decrypt, *Coldcard bitcoin exploit balloons to $88 million* (Thorn: sweeps deliberate, programmatic): https://decrypt.co/374817/coldcard-bitcoin-exploit-88-million-attackers-draining-wallets
- [S16] Analytics Insight (CoinDesk/Thorn), *Coldcard bitcoin sweeps hit $114 million as rescue window opens* (fourth wave, replace-by-fee): https://www.analyticsinsight.net/news/coldcard-bitcoin-sweeps-hit-114-million-as-rescue-window-opens
- [S17] Galaxy, podcast *Inside the COLDCARD entropy failure w/ Alex Thorn*, 4 Aug 2026 (Will Owens baited a drainer bot and won an RBF fee race): https://www.galaxy.com/insights/podcasts/galaxy-grid/inside-the-coldcard-entropy-failure-w-alex-thorn
- [S18] Cointelegraph, *White hats outrun Coldcard hackers in 52-Bitcoin evacuation*, 22 Sep 2026 (Wyoming trust for victims): https://cointelegraph.com/news/white-hats-coldcard-btc-exploit-galaxy
- [S19] Bitcoin Magazine, *Hunting down the Coldcard hacker: wave 1 thief may be known to FBI*, 18 Aug 2026 (Block's Clay Garrett: paid account; logs "with extraordinary specificity"; Thorn quote; wave 1 coins unmoved): https://bitcoinmagazine.com/technical/hunting-down-the-coldcard-hacker-wave-1-thief-may-be-known-to-fbi
- [S20] crypto.news, *Coldcard theft: FBI may know 1,082 BTC attacker* (FBI has not confirmed a suspect, case, arrest or recovery): https://crypto.news/coldcard-theft-fbi-may-know-1082-btc-attacker/
- [S21] Decrypt, *$38M in bitcoin drained by Coldcard key flaw its maker thinks AI found* (Coinkite: has to assume "someone used AI to review previous versions of our firmware"): https://decrypt.co/374766/38m-in-bitcoin-drained-by-coldcard-key-flaw-its-maker-thinks-ai-found
- [S22] crypto.news, *Coldcard's $116M exploit renews dispute over security reviews*, 9 Nov 2026 (NVK cites paid third-party reviews: Mk4 in 2022, Q in 2024): https://crypto.news/coldcard-116m-exploit-nvk-security-review-dispute/
- [S23] Startup Fortune, *Lawsuit says ColdCard's random number flaw exposed $116 million in bitcoin*, 22 Oct 2026 (Ontario Superior Court, CV-26-00018158-0000, filed 11 Sep 2026; allegation: knew by May 2025): https://startupfortune.com/lawsuit-says-coldcards-random-number-flaw-exposed-116-million-in-bitcoin/
- [S24] Crypto Briefing, *Coinkite CEO says Coldcard flaw hit 0.17% of users…*, 18 Nov 2026: https://cryptobriefing.com/coldcard-firmware-flaw-116m-bitcoin-stolen/
- [S25] Decrypt, *Coldcard adds new security measures after $130 million bitcoin exploit* (firmware 5.6.1 / 1.5.1Q require user-supplied entropy): https://decrypt.co/376270?amp=1
- [S26] Forklog (Coinkite's warning ~30 hours after the first outflows; Block's analysis): https://forklog.com/en/?p=101360
- [S27] Forklog, *Kraken CSO says Coldcard flaw exposes gap in hardware wallet testing* (Coinkite advisory: its lawyers will work with law enforcement in various jurisdictions): https://forklog.com/en/kraken-cso-says-coldcard-flaw-exposes-gap-in-hardware-wallet-testing/

---

## Notes for proprietarul's check

- **Primary sources read directly:** TRM Labs [S7], Galaxy Research [S6]. **Not yet opened directly** (the fetch needed your approval and you were away): Coinkite's three blog posts [S1–S3] and Block's write-up [S4]; their content here comes from verbatim excerpts in search results and several outlets quoting them. I'll open them in Chrome before the voice is generated.
- **Corrections to the handoff:** (1) the affected range is **4.0.1–4.1.9** per Coinkite (Block includes Mk2/Mk3 from 4.0.0), not "firmware 4.0.0"; (2) the emergency fix is **4.2.0** (31 Jul) for Mk3, later 5.6.1 / 1.5.1Q with mandatory user entropy; (3) Coinkite's warning came **~30 hours after** the first sweep, i.e. on 31 Jul, though some outlets date it 30 Jul; the script says "about 30 hours after"; (4) the Forbes victim quote "I did everything right" is Jonathan Goodman's own X post (C$1.6M, 18.25 BTC).
- **Goodman's times:** 9:36–9:43 pm on 29 July, Ontario time (EDT) = 01:36–01:43 UTC on 30 July, inside Galaxy's first-wave window. The script keeps both dates on purpose ("still the evening of July 29th").
- **Loss figures:** wave 1 = 1,082.65 BTC / 1,196 addresses (Galaxy); waves 1–3 = 1,367.05 BTC / 4,585 addresses; four waves ≈ 1,816 BTC / 5,200+ addresses (Galaxy/TRM "potential"); Galaxy's high-confidence minimum 1,730 BTC; CryptoQuant confirms 1,432 BTC; Galaxy later ~1,830 BTC from ~9,200 addresses [S24]. USD values differ with the BTC price used ($114M–$130M). The voice uses "about 116 million" (TRM, title).
- **"About a trillion"**: 2^40 ≈ 1.1 trillion. Block says that with a known device ID and boot timing the practical search can be far smaller [S4]; we don't claim a time ("a search with an end").
- **"No one else used that pattern in 30 days"**: Galaxy's finding on the 30 sat/vB, no-change signature [S9]. Later waves used other fees (10/50 sat/vB), so the fee is a wave-1 fingerprint only.
- **The paid-account lead** is Block's (Clay Garrett) account via Bitcoin Magazine [S19]; the provider is unnamed. The script attributes it ("they say") and adds the FBI non-confirmation.
- **"Wave 1 coins unmoved"**: true as of the August–September reports [S19]. **To re-check before rendering** (on-chain, Galaxy's latest), together with: any arrest or charge, the class action's status, Coinkite's final post-mortem, the latest loss total.
- **Novak's apology** is quoted as "I'm sorry and I'm devastated" by Silicon Canals [S14] and as "I'm sorry, and I'm crushed" by Forklog; to check against his original X post before the card is made.
- **0.17% of users** is Coinkite's CEO's figure [S24]; worded as Coinkite's.
- **Not used (true but off-angle or weak sourcing):** the developer's alias and name (never named), Ledger's/Trezor's commentary (competitors), the 210,000 BTC moved by long-term holders, Kraken's CSO, Coinkite halting shipments, the 64.9 BTC Wasabi and 200 ETH Tornado Cash deposits (could go back into "THE RACE" if the episode runs short).
