# Episode 003: Nobody Touched It

**Title (proposed): Inside the $116M Coldcard Hack** · thumbnail text: **NOBODY TOUCHED IT.**
**Test & Compare at publishing (proposed):** (A) this title + "NOBODY TOUCHED IT."; (B) "The Safest Bitcoin Wallet Was Guessable for 5 Years" + "41 MINUTES."; (C) "Inside the Coldcard Hack: $116M Gone Without a Touch" + "5 YEARS. 41 MINUTES."

**Subject:** the Coldcard hardware-wallet thefts (30 July – early August 2026). A build error in Coinkite's March 2021 firmware made some Coldcard devices create wallet seeds from a predictable software generator instead of the hardware random-number chip. Attackers rebuilt the seeds offline and swept about 1,816 BTC (about $116M) from more than 5,200 addresses in four waves, without touching a single device.
**Angle:** the device built to be the safest place for bitcoin was, for more than five years, predictable. The safety check that should have stopped the build was there, and it passed. The first thief may have left a trail, not on the blockchain, but in a paid account.
**Status:** DRAFT v3.2, written 2026-11-23 (v1 and v2 the same day; v3 = story rewrite on the same verified facts, see "Changes from v2"; v3.1 = full grammar/logic/question-and-answer review, see "Changes in v3.1"; v3.2 = Goodman facts verified on the web, see "Changes in v3.2"). Facts checked against the sources below (see "Notes for proprietarul's check"). Proprietarul must check it before any generation (rule 10).
**Target length:** about 10:45–11:15 with cards, pauses, music beats and end card (rule 13).
**Length:** 1,581 spoken words (automatic count, cards and cues excluded), Thomas 256 words in 28 lines (~1:30), each ≤ 12 words so every line fits one 5 s LongCat clip (≤ 4.7 s of speech). Ep. 002 ran 11:11 with 1,577 words, so this lands at about 10:50–11:10.

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
- Proposed chapters: The box · The man who did everything right · The combination · Five years · 01:10 · "I'll just check" · The race · The mistake · Who? · The box, again.
- v3 spine: Goodman is the protagonist from 0:55; the seed is a combination nobody picked; the teaser promises the thief's mistake and "The mistake" pays it; the sweep is told in Toronto time so the peak lands on his wallets; the close returns to the box.

---

## 0:00 — TEASER

`[MUSIC: full]` About 13 dB under the voice. Bass hit on every cut-off line. Fade over 5 s after the last line.

`[VIS]` A bank vault at night. One small drawer, closed. Dust in a single beam of light.

`[VO]`
A bank vault. A safe-deposit box. Inside it, three small devices that have never been connected to the internet. [S12][S30]

`[VO]`
On the night of July 29th, nobody opened that box. Nobody touched those devices. [S12]

`[VO]`
In seven minutes, the bitcoin they protected was gone. [S12]

`[VO]`
Within five days, about 116 million dollars had been taken the same way. [S7]

`[VO]`
The flaw behind it had been sitting in public code for more than five years. [S2][S4]

`[VO]`
And the first thief may have made one mistake of their own. [S19]

*(Every line generated with a full stop; the cut is made in the edit, on the bass hit.)*

`[VIS]` Hard cut to black. ~1.6 s of bass. Title fades in: **SIPHON FILES · NOBODY TOUCHED IT**.

---

## 0:35 — THOMAS (intro)

`[MUSIC: out]`

`[THOMAS]` I'm Thomas Archer, the AI narrator of Siphon Files.
`[THOMAS]` Every claim you'll hear is sourced. The list is in the description.
`[THOMAS]` This is the story of a lock that nobody picked.
`[THOMAS]` Somebody simply worked out the combination.

---

## 0:55 — THE MAN WHO DID EVERYTHING RIGHT

`[VO]`
Jonathan Goodman is an entrepreneur in Toronto. By his own account, he has put more than a million dollars into bitcoin. [S13]

`[VO]`
So he does what the security guides tell you to do. He buys a hardware wallet: a Coldcard, made by a Canadian company called Coinkite. [S13][S11]

`[VO]`
When you set one up, it gives you a list of 12 or 24 words. Those words are the money. Anyone who has them can spend your bitcoin, from anywhere. [S2]

`[VIS]` A blank card with 24 numbered lines, the words blurred.

`[VO]`
He buys three of them. He never shares his words with anyone, and he stamps them into metal as a backup. The devices never touch the internet. They go into a safe-deposit box at his bank. [S12][S30]

`[VO]`
But there's one thing he can't check for himself: how those words were chosen.

---

## 1:45 — THE COMBINATION

`[VO]`
The words have to be impossible to guess. So the device picks them by pure chance, using hardware built for one job: producing random numbers. [S2][S4]

`[VO]`
Done properly, there are so many possible word lists that nobody could ever search through them all. [S2][S7]

`[CARD]` **T-MINUS 5 YEARS, 4 MONTHS**

`[VO]`
But in March 2021, Coinkite ships a firmware update. It switches to the same cryptography that Bitcoin Core uses, through a new library. [S2][S4]

`[CARD]` **"The cryptographic choice was sound. The integration was not."** — Coinkite [S2]

`[VO]`
The new library needs random numbers. And the code that answers its request can work in two ways: read the hardware, or run a simple software substitute. One setting decides which. [S2][S4]

`[VIS]` Two boxes: **HARDWARE RANDOM GENERATOR** (cyan, idle) and **SOFTWARE SUBSTITUTE** (grey). A switch marked **0** sends the arrow from "seed generation" to the wrong one.

`[VO]`
Coinkite sets it to zero, believing that turns the whole thing off. It doesn't. Zero means: use the substitute. [S2]

`[VO]`
And there's a safety check in the code, built for exactly this. If the setting is missing, the build stops, with a message. [S4]

`[VIS]` A code line types itself out: `#error "get a HW TRNG plz"` · source: Block Engineering [S4]

`[VO]`
But the check only asks whether the setting exists. It does. It says zero. The check passes. [S2][S4]

`[THOMAS]` Think of a smoke alarm inspector.
`[THOMAS]` He checks that there's an alarm on the ceiling.
`[THOMAS]` He never checks that it's switched on.

---

## 3:05 — FIVE YEARS

`[VO]`
So from then on, the older Mk2 and Mk3 models make their words from the substitute. It runs on a fixed factory ID and a few timers. Nothing in it is truly secret. [S4][S6]

`[VO]`
Coinkite later puts it at about 40 bits of real randomness. A proper seed has at least 128. [S1][S2]

`[THOMAS]` Forty bits is about a trillion possibilities. That sounds like a lot.
`[THOMAS]` For a computer guessing offline, it's a search that ends.

`[VO]`
Newer models fare better, at about 72 bits. Still far short of a proper seed, though there's no public evidence that any of them were drained in these attacks. [S1][S2]

`[VO]`
The hardware generator is still there, inside every device. Coinkite's own technical write-up later admits it was being used… [S2]

`[CARD]` **"…just by chance, and only for less important things."** — Coinkite [S2]

`[VO]`
So now you know something Goodman doesn't. His words were never truly random. And the code is public. Anyone can read it. [S2]

`[VO]`
For five years, owners like him buy the device, write their words down, and lock them away.

`[VO]`
Coinkite's CEO says the company paid for outside security reviews in 2022 and 2024. Yet Coinkite says it was unaware of the bug until the day of the theft. [S22][S2]

`[CARD]` **T-MINUS A FEW WEEKS**

`[VO]`
Then, a few weeks before the theft, Coinkite runs an AI review of its critical code. [S3]

`[CARD]` **"It did not catch this vulnerability."** — Coinkite, on its own AI-assisted review [S3]

`[VO]`
But someone else finds it first. [S2][S3]

`[THOMAS]` Coinkite says it must assume that someone used AI to find it.
`[THOMAS]` That's Coinkite's assumption. It hasn't been proven.
`[THOMAS]` Either way, the method didn't need a single device.
`[THOMAS]` Guess a seed. Work out its addresses. Check the blockchain.
`[THOMAS]` A match means the key, and the money with it.

---

## 4:35 — 01:10

`[CARD]` **T-MINUS 0 · 30 JULY 2026 · 01:10:20 UTC**

`[MUSIC: vault]` Feature level. Fades out ~2.9 s before "Then it reaches Goodman".

`[VO]`
In Toronto, it's ten past nine on a Wednesday evening. Goodman is away at his cottage. [S5][S14]

`[VO]`
The first transaction leaves an address made on a Coldcard. Then another. Then hundreds. [S5][S8]

`[VIS]` A block-explorer timeline: blocks **960,183 → 960,191**, address dots draining to three collector points.

`[VO]`
According to Chainalysis, the thief goes for the biggest wallets first. About 30 million dollars in the first ten minutes. [S10]

`[VO]`
And there's something odd about these transactions. They're all built the same way: the same fee rate, and every last coin swept out, with nothing left behind. [S9]

`[VO]`
Hold on to that detail.

`[VO]`
Then it reaches Goodman.

`[VIS]` Three balance lines on a dark screen (ILLUSTRATIVE), each turning red in sequence: **9:36 PM → 9:43 PM**.

`[VO]`
9:36 pm. The first of his three wallets empties. Then the second. By 9:43, the third is gone too. About 1.6 million Canadian dollars. [S12][S31]

`[VO]`
At 9:51, the first wave stops. In 41 minutes, nearly twelve hundred addresses have been emptied. [S5]

`[VO]`
And Goodman has no idea.

---

## 5:45 — "I'LL JUST CHECK"

`[VO]`
Over the next few hours, reports start to appear of coins leaving cold wallets. Engineers at Block, the company behind the Bitkey wallet, pull the firmware apart. Before the day is out, they and other researchers find the cause. [S4][S10]

`[VO]`
Coinkite publishes its first warning: seeds made on affected firmware are at risk. Move your funds. By then, the first wave is long over. [S1][S5]

`[VO]`
On July 31st, Goodman is at a public library with his family when he sees a friend's post on Facebook: if you use a Coldcard, move your money now. [S13][S29]

`[CARD]` **"There's no way this affects me, but I'll just check."** — Jonathan Goodman, to Wealthsimple Magazine [S13]

`[VO]`
He checks. His bitcoin has been gone since Wednesday night. [S12][S13]

`[CARD]` **"I did everything right."** — Jonathan Goodman, on X [S12]

`[VO]`
He heads back to Toronto to file a police report, and a report with the Ontario Securities Commission. [S12][S13]

`[VO]`
People ask him whether someone got into his safe-deposit box. [S13]

`[VO]`
Nobody did. And for anyone else still holding a seed made the same way, a firmware update won't help. It fixes new seeds. A weak seed that's already written down stays weak. [S1][S2]

`[CARD]` **"I'm sorry and I'm devastated."** — Rodolfo Novak, Coinkite CEO, on X, 31 July [S28]

`[THOMAS]` Here's the cruel part of a public warning.
`[THOMAS]` It reaches the owners and the thieves at the same moment.

---

## 7:00 — THE RACE

`[VO]`
Wave two follows. Wave three runs from Friday into Saturday. A fourth starts on Monday. [S11][S16]

`[VO]`
Galaxy Research later counts at least 15 separate attackers. Not one thief anymore. A crowd, working the same weakness. [S6]

`[VO]`
But in the fourth wave, the thieves' transactions sit waiting to be confirmed. Until they are, anyone willing to pay a higher fee can replace them. [S16]

`[VO]`
So one owner, Will Owens, fights back. He leaves a small amount behind as bait, waits for the bot to take it, and outbids it. He wins his bait back. [S17]

`[VO]`
Later, volunteer white hats move about 52 bitcoin out of exposed wallets, into a trust set up to return it to victims. In September, the trust hands more than 20 bitcoin back to one verified owner. [S18][S32]

`[VO]`
Some of the stolen coins head for mixers, services built to blur the trail. Much of the rest just sits. [S7]

`[VO]`
By the time the waves slow down, about 1,816 bitcoin have been taken, from more than 5,200 addresses. [S7]

`[VO]`
But the biggest piece, the first wave, hasn't moved at all.

---

## 8:10 — THE MISTAKE

`[THOMAS]` Remember that detail? Every transaction in wave one looked the same.
`[THOMAS]` Galaxy found no one else using that pattern in the month before.
`[THOMAS]` So wave one could be traced as a single operation.
`[THOMAS]` And investigators noticed something else about it.

`[VO]`
Every guess has to be checked. To know which guessed addresses hold money, you have to look them up, again and again. [S19]

`[VO]`
Block's investigators say the first-wave operator appears to have done that through a paid account at a well-known blockchain data provider. [S19]

`[VO]`
They contacted the provider. Its internal logs, they say, matched the attack "with extraordinary specificity": the number, the timing and the order of the requests. [S19]

`[THOMAS]` On the blockchain, the thief was just a string of addresses.
`[THOMAS]` But a paid account usually leaves records.

`[VO]`
The information went to law enforcement. Galaxy's Alex Thorn says the first-wave attacker's identity "may be known to law enforcement". [S19]

`[VO]`
But the FBI has not confirmed a suspect, an arrest, or any recovery. [S20]

---

## 9:20 — WHO?

`[VO]`
So, publicly, no one knows who did it. TRM Labs doesn't attribute the theft to anyone. Coinkite says its lawyers are working with law enforcement to identify those responsible. [S7][S27]

`[VO]`
Online, some call it an inside job. There's no public evidence for that, and no one has been accused. [S7][S20]

`[VO]`
In September, a Coldcard owner filed a proposed class action in Ontario against Coinkite and its co-founders. It alleges the company knew its seed generation was weak by May 2025. Those claims have not been tested in court. [S23]

`[VO]`
As of the latest reports, Coinkite hasn't announced any compensation fund. And Goodman isn't counting on the lawsuit. [S33][S30]

`[CARD]` **"The math on a class action is brutal."** — Jonathan Goodman, to The News Block [S30]

`[VO]`
Coinkite's CEO says the flaw affected about 0.17 percent of its users. The newest firmware now makes every owner add randomness of their own when they create a seed. [S24][S25]

---

## 10:15 — THE BOX, AGAIN

`[VO]`
There's one group Coinkite doesn't consider at risk from this bug: owners who added at least 50 dice rolls of their own when they made their seed. [S1]

`[VO]`
The ones who didn't leave it all to the device.

`[THOMAS]` That safe-deposit box was never opened.
`[THOMAS]` The devices inside were never hacked.
`[THOMAS]` They just never asked their random-number hardware for the seed.
`[THOMAS]` If you made a seed on an affected Coldcard, read Coinkite's advisory.
`[THOMAS]` Coinkite says: treat it as compromised, and move to a new seed.

`[MUSIC: full]` Heist theme returns, fades over 5 s.

`[VO]`
And the 1,082 bitcoin from the first wave? As of the latest public reports, they're still sitting where the thief left them. [S19]

`[VO]`
And somewhere, in a data company's records, there may be a name.

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
- [S12] Jonathan Goodman (@itscoachgoodman) on X, ~31 Jul 2026 (9:36–9:43 pm; safe-deposit box; police report and Ontario Securities Commission report; "I don't expect to recoup anything"): https://x.com/itscoachgoodman/status/2083527082223563157 · IBTimes UK, *$1.6M Bitcoin gone in seven minutes…* (Goodman's X post: 9:36–9:43 pm, 29 July, 18.25245043 BTC, bank safety deposit box, never online): https://www.ibtimes.co.uk/canadian-entrepreneur-bitcoin-loss-hardware-wallet-flaw-1811995
- [S13] Wealthsimple Magazine, *How I lost $1 million in bitcoin in 8 minutes* (Goodman interview: discovered 31 July in a public library with his family, from a friend's Facebook post; went back to Toronto to file a police report; the safe-deposit-box question. The headline says 8 minutes; his own X post gives 9:36–9:43 pm, so the script says seven): https://www.wealthsimple.com/en-ca/magazine/how-i-lost-1-million-in-bitcoin-in-8-minutes
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
- [S29] BTC-ECHO, *Alles richtig gemacht und trotzdem Bitcoin im Millionenwert verloren* (Goodman learned of the attack from a friend's Facebook post): https://www.btc-echo.de/news/alles-richtig-gemacht-und-trotzdem-bitcoin-im-millionenwert-verloren-236786/
- [S28] Rodolfo Novak (@nvk), *To all Coinkite users and the entire Bitcoin community*, X, 31 Jul 2026: https://x.com/nvk/status/2083216713693151552 · quoted by Forbes, 4 Aug 2026: https://www.forbes.com/sites/boazsobrado/2026/08/04/i-did-everything-right-ai-warning-after-116-million-bitcoin-hack/
- [S27] Forklog, *Kraken CSO says Coldcard flaw exposes gap in hardware wallet testing* (Coinkite advisory: its lawyers will work with law enforcement in various jurisdictions): https://forklog.com/en/kraken-cso-says-coldcard-flaw-exposes-gap-in-hardware-wallet-testing/

- [S30] The News Block, *He did everything right. Then he lost everything.*, 28 Aug 2026 (Goodman interview: three Coldcard devices in a bank safe-deposit box, seed phrases stamped into metal; not sure there is a legal path to recover; "The math on a class action is brutal"; not counting on recovery; cooperating with police and Galaxy's Alex Thorn): https://thenewsblock.substack.com/p/he-did-everything-right-then-he-lost
- [S31] VT / LADbible, 13 Aug 2026 (all three of his wallets drained in seven minutes): https://vt.co/news/world/man-loses-1-6-million-bitcoin-coldcard-hack-100-percent-secure-warning · AlphaWire (18.25 BTC from three wallets): https://alphawire.xyz/news/bitcoin/coldcard-seed-flaw-three-bitcoin-wallets/
- [S32] Steptoe, *Crypto Recovery Trust… returns bitcoin to its owner after Coldcard exploit*, 24 Sep 2026 (more than 20 BTC returned on 23 Sep to one verified, unnamed owner; ~50 BTC deposited by white hats): https://www.steptoe.com/en/news-publications/crypto-recovery-trust-advised-by-steptoe-attorneys-returns-dollar17m-in-bitcoin-to-its-owner-after-coldcard-exploit.html
- [S33] Crypto Briefing (Coinkite "has not announced any compensation fund or insurance mechanism"): https://cryptobriefing.com/coinkite-coldcard-bitcoin-hack-130m/ · BIT Knowledge Hub (no official compensation plan as of early August): https://www.bit.com/insights/knowledge-hub/coldcard-the-security-first-wallet-that-got-hacked

---

## Notes for proprietarul's check

- **Primary sources read directly:** TRM Labs [S7], Galaxy Research [S6], and on 23 Nov in Chrome: Coinkite's advisory [S1], technical deep dive [S2] ("We were unaware of the bug until today"; the hardware RNG code "was being used, but just by chance, and only for less important things"), the AI post [S3] ("including in the weeks before the exploit"; later tests with frontier models also missed it), and Block's report [S4] (timeline: v4.0.0 released 17 Mar 2021; on 30 Jul Block and others independently found the root cause, Coinkite published its advisory, Block disclosed its findings to Coinkite). Everything in the script matches.
- **Date of the warning:** Coinkite and Block date the first advisory **30 July**; Galaxy and several outlets say it came "about 30 hours" after the first sweep (which would put it on 31 July UTC). The script avoids the gap and says only "by then, the first wave is long over".
- **Corrections to the handoff:** (1) the affected range is **4.0.1–4.1.9** per Coinkite (Block includes Mk2/Mk3 from 4.0.0), not "firmware 4.0.0"; (2) the emergency fix is **4.2.0** (31 Jul) for Mk3, later 5.6.1 / 1.5.1Q with mandatory user entropy; (3) the timing of Coinkite's warning is disputed (see below); (4) the Forbes victim quote "I did everything right" is Jonathan Goodman's own X post (C$1.6M, 18.25 BTC).
- **Goodman's times:** 9:36–9:43 pm on 29 July, Ontario time (EDT) = 01:36–01:43 UTC on 30 July, inside Galaxy's first-wave window. The script keeps both dates on purpose ("still the evening of July 29th").
- **Loss figures:** wave 1 = 1,082.65 BTC / 1,196 addresses (Galaxy); waves 1–3 = 1,367.05 BTC / 4,585 addresses; four waves ≈ 1,816 BTC / 5,200+ addresses (Galaxy/TRM "potential"); Galaxy's high-confidence minimum 1,730 BTC; CryptoQuant confirms 1,432 BTC; Galaxy later ~1,830 BTC from ~9,200 addresses [S24]. USD values differ with the BTC price used ($114M–$130M). The voice uses "about 116 million" (TRM, title).
- **"About a trillion"**: 2^40 ≈ 1.1 trillion. Block says that with a known device ID and boot timing the practical search can be far smaller [S4]; we don't claim a time ("a search with an end").
- **"No one else used that pattern in 30 days"**: Galaxy's finding on the 30 sat/vB, no-change signature [S9]. Later waves used other fees (10/50 sat/vB), so the fee is a wave-1 fingerprint only.
- **The paid-account lead** is Block's (Clay Garrett) account via Bitcoin Magazine [S19]; the provider is unnamed. The script attributes it ("they say") and adds the FBI non-confirmation.
- **"Wave 1 coins unmoved"**: true as of the August–September reports [S19]. **To re-check before rendering** (on-chain, Galaxy's latest), together with: any arrest or charge, the class action's status, Coinkite's final post-mortem, the latest loss total.
- **Novak's apology — verified 23 Nov:** the original is an X article by @nvk, 31 Jul 2026, 3:42 PM, beginning "To all Coinkite users and the entire Bitcoin community, I'm sorry and I'm devastated. Our team is heartbroken about yesterday's news." (https://x.com/nvk/status/2083216713693151552; the account is now restricted, so the text was confirmed from X's indexed copy and from Forbes, Bitcoin.com News and Protos, which notes the post stayed pinned while others were deleted). Forklog's "crushed" is a translation. The card keeps "I'm sorry and I'm devastated." and is sourced to [S28].
- **0.17% of users** is Coinkite's CEO's figure [S24]; worded as Coinkite's.
- **Not used (true but off-angle or weak sourcing):** the developer's alias and name (never named), Ledger's/Trezor's commentary (competitors), the 210,000 BTC moved by long-term holders, Kraken's CSO, Coinkite halting shipments, the 64.9 BTC Wasabi and 200 ETH Tornado Cash deposits (could go back into "THE RACE" if the episode runs short).

---

## Changes from v1 (23 Nov 2026, full review requested by proprietarul)

Facts (each checked against the primary source):
1. **"5,200 wallets" → "5,200 addresses"** (teaser). Galaxy and TRM count addresses; one wallet has many.
2. **"For five years" → "for more than five years"**: March 2021 to July 2026 is 5 years 4 months.
3. **"a chip whose only purpose…" → "hardware built for one purpose"**: the random-number generator is part of the main processor (STM32), not a separate chip. Thomas's close changed to match ("its random-number hardware").
4. **"Two things in the code with that name" was wrong.** Block shows Coldcard's own hardware code did not even use that name; the name led to one MicroPython file that can either read the hardware or run a software substitute, chosen by one setting. Rewritten as such, with Coinkite's own words: it set the switch to zero "thinking we didn't need either version, but that's not what it does" [S2]. Removed the unsourced "meant for computers without a chip".
5. **"well-respected cryptography library" → "the same cryptography that Bitcoin Core itself uses, through a new library"** + Coinkite's card "The cryptographic choice was sound. The integration was not." [S2].
6. **"fed by the device's serial number and a timer" → "a fixed factory ID and a few timers"** (Block: MCU UID + SysTick + RTC registers).
7. **"Most don't [roll dice]"** removed: no source for how many owners used dice. Now "It's optional" (advisory).
8. **"Then, in late July 2026, someone else reads the old firmware"** removed: nobody knows when the attacker found the bug. Now "Then someone else finds the bug first" (Coinkite was unaware until 30 July [S2]).
9. **"Coinkite says it paid for outside reviews"** → "Coinkite's CEO says" (the source is NVK's X post [S22]).
10. **The fee:** "pays exactly the same fee" → "the same fee rate" (Galaxy: 30 sat/vB, no change output). "Hold on to that fee" → "Hold on to that detail".
11. **The tell was implying something the sources don't say.** v1 suggested the fee pattern led investigators to the paid account. Block only says investigators noticed "an unusual pattern" in wave one. Thomas now says the pattern let wave one be traced as one operation, "and investigators noticed something else about it".
12. **"Nobody does [know yet]"** removed: Block and others saw the reports the same day. Now "And he has no idea."
13. **Goodman's discovery** made exact (Wealthsimple): a public library with his family, a friend's Facebook post, then back to Toronto to file a police report. "Gone for two days" → "gone since Wednesday night" (29 July 2026 was a Wednesday; he checked on Friday the 31st).
14. **"The first question he gets is whether someone broke in"** → "People ask him whether someone got into his safe-deposit box" (his words don't say who asked first).
15. **"A firmware update can't help him"** was illogical (his money was already gone). Now: "for anyone still holding a seed like his, a firmware update won't help".
16. **"Coinkite publishes its warning… about 30 hours after"** removed (dates disagree, see notes); "By then, the first wave is long over" kept.
17. **Will Owens:** "He wins" → "He wins his bait back" (he had already moved his funds; he recovered only the bait).
18. **Galaxy's 15 attackers** "by then" → "later" (the count is from 7 Aug, after wave four).
19. **"The device inside still works perfectly"** (unsourced) → "The device inside was never hacked." (Coinkite: "The COLDCARD devices themselves were not hacked").
20. **"Newest firmware requires…"**: only the latest releases (5.6.1 / 1.5.1Q) require user entropy; "newest" says that.
21. **Last line** "Someone may know whose they are" was ambiguous → "And someone may already know who put them there."

Story and retention:
22. Second countdown card added (**T-MINUS A FEW WEEKS**, the AI review), so the T-minus line has a middle step.
23. Fewer numbers in "01:10": 1,196 / 1,082 → "nearly twelve hundred addresses"; the 1,082 is kept for the ending, where it pays off. "18.25 bitcoin" removed from Goodman's peak (the dollar figure stays).
24. "Tonight" → "This time" (people watch at any hour); "the safest place to keep bitcoin" → "a device built to be the safest place for bitcoin" (not our verdict).
25. Every open question now gets an answer on screen: what the mistake was (2:20), whether newer models were hit (3:40), what the fee detail means (8:55), who did it (9:50), where wave one's coins are (end), what owners should do (end, as Coinkite's instruction).

---

## Changes from v2 (23 Nov 2026, story rewrite requested by proprietarul: "a very captivating story")

No new facts were added; every line still maps to the sources above. What changed is the order and the drive:
1. **Teaser ends on a promise:** "And the first thief may have made one mistake of their own." [S19]. The episode now pays it in a section called "The mistake".
2. **Thomas intro sets the image of the episode:** "a lock that nobody picked / somebody simply worked out the combination".
3. **Goodman becomes the protagonist at 0:55** ("The man who did everything right"), before any technology. His precautions come first, then the one thing he can't check: how the words were chosen. This creates the knowledge gap the whole middle runs on.
4. **"The promise", "March 2021" and "The check that passed" merged into "The combination"** (one continuous scene, shorter).
5. **Irony card added** from Coinkite's own write-up: the hardware generator was used "just by chance, and only for less important things" [S2].
6. **Knowledge gap spelled out:** "So now you know something Goodman doesn't."
7. **The sweep is told in Toronto time** (01:10 UTC = 9:10 pm Wednesday) and cuts to Goodman at 9:36 pm, so the peak is his wallets emptying, followed by "I did everything right" and "And he has no idea."
8. **"He didn't know" renamed "I'll just check"**, with Goodman's own words as a card [S13].
9. **"The tell" renamed "The mistake"**, with a Thomas mirror line: on the blockchain the thief was a string of addresses, but a paid account usually leaves records.
10. **Close:** returns to the box, then a hedged last line: "And somewhere, in a data company's records, there may be a name." It's framed as a possibility, in line with Block's and Thorn's statements and the FBI non-confirmation [S19][S20].
11. Removed "So now there's a race" and the Thomas line "Some owners move in time. Some don't." (the race section now starts on its own hook). 1,559 → 1,489 words.

---

## Changes in v3.1 (23 Nov 2026, full review: grammar, logic, every question answered)

**Logic and fact precision**
1. "where the design called for 128" → "A proper seed has at least 128." (a 12-word seed has 128 bits, a 24-word seed 256; the old line could read as wrong for 24 words).
2. The T-MINUS A FEW WEEKS card stood before a sentence about 2022 and 2024. The reviews now come first, followed by Coinkite's own statement that it was "unaware of the bug until" 30 July [S2]; then the card, then the AI review.
3. The "I did everything right" card sat right before "And he has no idea", but he posted it after he found out. It moved to the moment he checks.
4. "At 9:51, the sweep stops" → "the first wave stops" (three more waves follow).
5. "Wave two comes the next day" came right after the 31 July library scene and made the dates read wrong → "Wave two follows." (Friday–Saturday and Monday stay.)
6. "Most just sit" → "Much of the rest just sits" (consistent with wave 1 unmoved, without claiming a share we don't have).
7. The on-screen visual "Three wallet balances" assumed a number Goodman never gave → "A few balance lines (ILLUSTRATIVE)".
8. "Later that day… Within hours" (two time markers in a row, and "that day" was ambiguous between 29 July local and 30 July UTC) → "Over the next few hours… Before the day is out".
9. "a seed like his" → "a seed made the same way" (his seed was already emptied; the warning is for others).
10. "The newest firmware now requires every owner to add randomness" → "…when they create a seed".

**Grammar and flow**
11. "what every security guide tells you" → "what the security guides tell you" (no absolute claim).
12. "fare better, about 72 bits" → "fare better, at about 72 bits"; "any were drained" → "any of them were drained".
13. "But someone else finds the bug first" → "finds it first"; "the last public reports" → "the latest public reports".
14. Added "Every guess has to be checked." at the start of the paid-account scene, so it links back to Thomas's "Check the blockchain".

**Questions raised in the video and where they are answered**
- "How were the words chosen?" (0:55) → The combination (switch on zero, check passes) and Five years (40 bits).
- "Is it every Coldcard?" → Five years (Mk2/Mk3 40 bits; newer ~72 bits, no public evidence of drains).
- "Who found it, and how?" → end of Five years (Coinkite's AI assumption, flagged as unproven; the guessing method).
- "What was odd about the transactions?" (planted at 01:10) → paid in The mistake (single operation, then the paid account).
- "The first thief's mistake" (teaser) → The mistake.
- "Who did it?" → Who? (publicly unknown; FBI unconfirmed; inside-job theory without evidence).
- "Where is the money?" → The race (mixers, white hats) and the close (wave 1 unmoved).
- "Could anyone have been safe?" → the close (50 dice rolls).
- **Did Goodman get anything back?** Checked on 23 Nov and now answered in Who?: no compensation fund announced, and Goodman says he isn't counting on recovery [S30][S33]; plus the trust's one return in The race [S32].

**Checked 23 Nov (web search):** no public report of Goodman recovering anything (latest: The News Block, 28 Aug; his own X post: "I don't expect to recoup anything"). Nor of a Coinkite compensation fund. New facts added from these sources: three devices/three wallets, seeds stamped in metal, the Ontario Securities Commission report, the trust's >20 BTC return (23 Sep), the class-action quote. Goodman's X post says he heard about the hack "at our cottage"; Wealthsimple and The News Block place the moment he checked at a library while his family was downstairs. Both fit, so the script keeps the library. Still to re-check right before voice: wave 1 coins, arrests, the class action, final loss figures.

---

## Changes in v3.2 (23 Nov 2026, the open question checked now)

The question "did Goodman get anything back?" has been checked, and the answer is in the script:
1. **Who?**: "As of the latest reports, Coinkite hasn't announced any compensation fund. And Goodman isn't counting on the lawsuit." + his card "The math on a class action is brutal." [S30][S33].
2. **The race**: the white-hat trust handed more than 20 BTC back to one verified owner in September [S32] (a real moment of hope, before the close).
3. **Precise facts from Goodman himself:** three Coldcards (teaser and close now say "three devices"), words stamped into metal, three wallets emptied one after another, report to the Ontario Securities Commission as well as the police [S12][S30][S31].
1,527 → 1,581 words (~10:50–11:10). Thomas's lines are unchanged except two words in the close ("devices", "They… their"), still ≤12 words.
