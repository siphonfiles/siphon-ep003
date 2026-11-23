# ASR check (medium.en)

| line | result | differences (script → heard) | heard |
|---|---|---|---|
| a1 | OK 1.00 |  | Jonathan Goodman is an entrepreneur in Toronto. By his own account, he has put more than a million dollars into Bitcoin. |
| a2 | CHECK 0.94 | coldcard → cold card | So, he does what the security guides tell you to do. He buys a hardware wallet, a cold card, made by a Canadian company called Coinkite. |
| a3 | CHECK 0.95 | twenty four → 24 | When you set one up, it gives you a list of 12 or 24 words. Those words are the money. Anyone who has them can spend your Bitcoin from anywhere. |
| a4 | OK 1.00 |  | He buys three of them. He never shares his words with anyone, and he stamps them into metal as a backup. The devices never touch the internet. They go into a safe deposit box at his bank. |
| a5 | OK 1.00 |  | But there's one thing he can't check for himself — how those words were chosen. |
| b1 | OK 1.00 |  | The words have to be impossible to guess, so the device picks them by pure chance, using hardware built for one job, producing random numbers. |
| b2 | OK 1.00 |  | Done properly, there are so many possible word lists that nobody could ever search through them all. |
| b3 | CHECK 0.92 | twenty twenty one → 2021 | But in March 2021, Coinkite ships a firmware update, it switches to the same cryptography that Bitcoin Core uses, through a new library. |
| b4 | OK 1.00 |  | The new library needs random numbers, and the code that answers its request can work in two ways, read the hardware or run a simple software substitute. One setting decides which. |
| b5 | OK 1.00 |  | CoinKite sets it to zero, believing that turns the whole thing off. It doesn't. Zero means use the substitute. |
| b6 | OK 1.00 |  | And there's a safety check in the code built for exactly this. If the setting is missing, the build stops, with a message. |
| b7 | OK 1.00 |  | But the check only asks whether the setting exists. It does. It says zero. The check passes. |
| b8 | OK 1.00 |  | Think of a smoke alarm inspector. |
| b9 | OK 1.00 |  | He checks that there's an alarm on the ceiling. |
| b10 | OK 1.00 |  | He never checks that it's switched on. |
| c1 | CHECK 0.91 | mark two → mk2; mark three → mk3 | So from then on, the older MK2 and MK3 models make their words from the substitute. It runs on a fixed factory ID and a few timers. Nothing in it is truly secret. |
| c2 | BAD 0.80 | forty → 40; a hundred and twenty eight → 128 | CoinKite later puts it at about 40 bits of real randomness. A proper seed has at least 128. |
| c3 | CHECK 0.92 | forty → 40 | 40 bits is about a trillion possibilities. That sounds like a lot. |
| c4 | OK 1.00 |  | For a computer guessing offline, it's a search that ends. |
| c5 | CHECK 0.95 | seventy two → 72 | Newer models fare better, at about 72 bits. Still far short of a proper seed, though so far there's no public evidence that any of them were drained in these attacks. |
| c6 | OK 1.00 |  | The hardware generator is still there, inside every device. CoinKite's own technical write-up later admits it was being used. |
| c7 | OK 1.00 |  | So now you know something Goodman doesn't, his words were never truly random, and the code is public, anyone can read it. |
| c8 | OK 1.00 |  | For five years, owners like him buy the device, write their words down, and lock them away. |
| c9 | BAD 0.87 | twenty twenty two → 2022; twenty twenty four → 2024 | Coinkite's CEO says the company paid for outside security reviews in 2022 and 2024. Yet Coinkite says it was unaware of the bug until the day of the theft. |
| c10 | OK 1.00 |  | Then, a few weeks before the theft, Coinkite runs an AI review of its critical code. |
| c11 | OK 1.00 |  | But someone else finds it first. |
| c12 | CHECK 0.92 | coinkite → koinkite | Koinkite says it must assume that someone used AI to find it. |
| c13 | BAD 0.86 | coinkite's → coenkite's | That's Coenkite's assumption. It hasn't been proven. |
| c14 | OK 1.00 |  | Either way, the method didn't need a single device. |
| c15 | BAD 0.90 | a → the | Guess the seed, work out its addresses, check the blockchain. |
| c16 | OK 1.00 |  | A match means the key and the money with it. |
| d1 | OK 1.00 |  | In Toronto, it's 10 past 9 on a Wednesday evening. Goodman is away at his cottage. |
| d2 | BAD 0.90 | coldcard → cold card | The first transaction leaves an address made on a cold card, then another, then hundreds. |
| d3 | CHECK 0.92 | thirty → 30; dollars → ∅ | According to Chainalysis, the thief goes for the biggest wallets first. About $30 million in the first 10 minutes. |
| d4 | OK 1.00 |  | And there's something odd about these transactions, they're all built the same way, the same fee rate, and every last coin swept out, with nothing left behind. |
| d5 | OK 1.00 |  | Hold on to that detail. |
| d6 | OK 1.00 |  | Then it reaches Goodman. |
| d7 | BAD 0.79 | thirty six p m → 36pm; forty three → 43; ∅ → canadian; point → ∅; canadian dollars → ∅ | 9.36pm, the first of his three wallets empties, then the second, by 9.43, the third is gone too, about Canadian$1.6 million. |
| d8 | BAD 0.72 | fifty one → 51; forty one → 41; twelve hundred → one 200 | At 9.51, the first wave stops, in 41 minutes, nearly 1,200 addresses have been emptied. |
| d9 | OK 1.00 |  | And Goodman has no idea. |
| e1 | OK 1.00 |  | Over the next few hours, reports start to appear of coins leaving cold wallets. Engineers at Block, the company behind the BitKey wallet, pull the firmware apart. Before the day is out, they and other researchers find the cause. |
| e2 | OK 1.00 |  | Coinkite publishes its first warning, seeds made on affected firmware are at risk. Move your funds. By then the first wave is long over. |
| e3 | BAD 0.89 | the thirty first → 31; coldcard → cold card | On July 31, Goodman is at a public library with his family when he sees a friend's post on Facebook. If you use a cold card, move your money now. |
| e4 | OK 1.00 |  | He checks, his bitcoin has been gone since Wednesday night. |
| e5 | OK 1.00 |  | He heads back to Toronto to file a police report and a report with the Ontario Securities Commission. |
| e6 | OK 1.00 |  | People ask him whether someone got into his safe deposit box. |
| e7 | OK 1.00 |  | Nobody did, and for anyone else still holding a seed made the same way, a firmware update won't help. It fixes new seeds. A weak seed that's already written down stays weak. |
| e8 | OK 1.00 |  | Here's the cruel part of a public warning. |
| e9 | OK 1.00 |  | It reaches the owners and the thieves at the same moment. |
| f1 | OK 1.00 |  | Wave 2 follows, Wave 3 runs from Friday into Saturday, a fourth starts on Monday. |
| f2 | CHECK 0.95 | fifteen → 15 | Galaxy Research later counts at least 15 separate attackers. Not one thief anymore. A crowd working the same weakness. |
| f3 | OK 1.00 |  | But in the fourth wave, the thieves' transactions sit waiting to be confirmed. Until they are, anyone willing to pay a higher fee can replace them. |
| f4 | OK 1.00 |  | So, one owner, Will Owens, fights back. He leaves a small amount behind as bait, waits for the bot to take it, and outbids it. He wins his bait back. |
| f5 | CHECK 0.93 | fifty two → 52; twenty → 20 | Later, volunteer white hats move about 52 Bitcoin out of exposed wallets, into a trust set up to return it to victims. In September, the trust hands more than 20 Bitcoin back to one verified owner. |
| f6 | OK 1.00 |  | Some of the stolen coins head for mixers services built to blur the trail. By the latest public tallies, much of the rest is still sitting. |
| f7 | BAD 0.78 | eighteen hundred and sixteen → 1816; fifty two hundred → 5200 | By the time the waves slow down, about 1816 Bitcoin have been taken, from more than 5200 addresses. |
| f8 | OK 1.00 |  | But the biggest piece, the first wave, still hasn't moved, according to the latest public tracking. |
| g1 | OK 1.00 |  | Remember that detail, every transaction in Wave 1 looked the same. |
| g2 | OK 1.00 |  | Galaxy found no one else using that pattern in the month before. |
| g3 | OK 1.00 |  | So wave 1 could be traced as a single operation. |
| g4 | OK 1.00 |  | And investigators noticed something else about it. |
| g5 | CHECK 0.95 | guessed → guest | Every guess has to be checked. To know which guest addresses hold money, you have to look them up, again and again. |
| g6 | OK 1.00 |  | Block's investigators say the first Wave operator appears to have done that through a paid account at a well-known blockchain data provider. |
| g7 | OK 1.00 |  | They contacted the provider, its internal logs they say, matched the attack with extraordinary specificity, the number, the timing and the order of the requests. |
| g8 | OK 1.00 |  | On the blockchain, the thief was just a string of addresses. |
| g9 | OK 1.00 |  | But a paid account usually leaves records. |
| g10 | CHECK 0.95 | thorn → thorne | The information went to law enforcement. Galaxy's Alex Thorne says the first wave attacker's identity may be known to law enforcement. |
| g11 | OK 1.00 |  | But as we make this video, the FBI has not confirmed a suspect, an arrest, or any recovery. |
| h1 | CHECK 0.91 | t r m → trm; coinkite → cohenkite | So, at the time of this video, no one has been publicly named. TRM Labs doesn't attribute the theft to anyone. Cohenkite says its lawyers are working with law enforcement to identify those responsible. |
| h2 | OK 1.00 |  | Online, some call it an inside job. So far, there's no public evidence for that, and no one has been accused. |
| h3 | CHECK 0.94 | coldcard → cold card; twenty twenty five → 2025 | In September, a cold card owner filed a proposed class action in Ontario against Coinkite and its co-founders. It alleges the company knew its seed generation was weak by May 2025. As of the latest reports, a judge hasn't even certified it as a class action yet, and none of its claims have been tested in court. |
| h4 | OK 1.00 |  | And, as far as public reports show, Coinkite hasn't announced any compensation fund. Goodman isn't counting on the lawsuit. |
| h5 | CHECK 0.92 | point one seven percent → 17 | Coinkite's CEO says the flaw affected about 0.17% of its users. The newest firmware now makes every owner add randomness of their own when they create a seed. |
| i1 | OK 1.00 |  | I'm Thomas Archer, the AI narrator of Siphon Files. |
| i2 | OK 1.00 |  | Every claim you'll hear is sourced. The list is in the description. |
| i3 | OK 1.00 |  | This is the story of a lock that nobody picked. |
| i4 | OK 1.00 |  | Somebody simply worked out the combination. |
| k1 | CHECK 0.93 | coinkite → coenkite; fifty → 50 | There's one group Coenkite doesn't consider at risk from this bug, owners who added at least 50 dice rolls of their own when they made their seed. |
| k2 | OK 1.00 |  | the ones who didn't leave it all to the device. |
| k3 | OK 1.00 |  | That safe deposit box was never opened. |
| k4 | OK 1.00 |  | The devices inside were never hacked. |
| k5 | OK 1.00 |  | They just never asked their random number hardware for the seed. |
| k6 | BAD 0.80 | coldcard → cold card; coinkite's → konkite's | If you made a seed on an affected cold card, read Konkite's advisory. |
| k7 | OK 1.00 |  | Coinkite says, treat it as compromised and move to a new seed. |
| k8 | BAD 0.88 | one thousand and eighty two → 1082 | and the 1082 Bitcoin from the first wave. As of the latest public tracking, they're still sitting where the thief left them. |
| k9 | OK 1.00 |  | and somewhere in a data company's records, there may be a name. |
| k10 | OK 1.00 |  | This was siphon files. |
| t1 | OK 1.00 |  | A bank vault, a safe deposit box, inside it, three small devices that have never been connected to the internet. |
| t2 | BAD 0.87 | the twenty ninth → 29 | On the night of July 29, nobody opened that box. Nobody touched those devices. |
| t3 | OK 1.00 |  | In seven minutes, the bitcoin they protected was gone. |
| t4 | BAD 0.79 | a hundred and sixteen → 116; dollars → ∅ | Within five days, about $116 million had been taken the same way. |
| t5 | CHECK 0.93 | flaw → floor | The floor behind it had been sitting in public code for more than five years. |
| t6 | OK 1.00 |  | And the first thief may have made one mistake of their own. |

30 lines to look at

## Words heard with low confidence (p < 0.5)

| line | words |
|---|---|
| a5 | —@2.5s p0.20 |
| b5 | use@5.6s p0.37 |
| c1 | MK2@1.8s p0.48 |
| c6 | The@0.0s p0.38 |
| c11 | But@0.0s p0.48 |
| d7 | Canadian@8.6s p0.24 |
| d8 | 9@0.7s p0.50 |
| d9 | And@0.0s p0.48 |
| e2 | seeds@2.9s p0.39 |
| e6 | People@0.0s p0.44 |
| f1 | 2@0.8s p0.49 |
| f2 | Galaxy@0.0s p0.27 |
| g4 | And@0.0s p0.12 |
| g9 | But@0.0s p0.37 |
| h5 | flaw@2.2s p0.35 |
| k7 | treat@1.7s p0.45 |
| t1 | A@0.0s p0.50 |
| t2 | On@0.0s p0.17 |
| t6 | And@0.0s p0.37 |
