# Episodul 003: Nimeni nu l-a atins (traducere pentru verificare)

> Traducerea în română a draftului v3.3 (`003-nobody-touched-it.md`), doar ca să-l verifici. Textul care se înregistrează rămâne cel în engleză. Sursele [S#] sunt aceleași ca în fișierul englezesc.

**Titlu propus:** „Inside the $116M Coldcard Hack” · text pe thumbnail: **„NOBODY TOUCHED IT.”** („Nimeni nu l-a atins.”)
**Test & Compare propus:** (A) titlul de mai sus + „NOBODY TOUCHED IT.”; (B) „The Safest Bitcoin Wallet Was Guessable for 5 Years” + „41 MINUTES.”; (C) „Inside the Coldcard Hack: $116M Gone Without a Touch” + „5 YEARS. 41 MINUTES.”
**Lungime:** 1.625 de cuvinte rostite, dintre care Thomas 256 în 28 de replici (~1:30), fiecare de cel mult 12 cuvinte, adică un clip LongCat de 5 s. Estimare: ~11:00–11:20.

**Linia editorială, pe scurt:**
- Nimeni nu e identificat, acuzat sau arestat. FBI n-a confirmat nimic. Citez exact ce a spus Alex Thorn (Galaxy): identitatea primului atacator „s-ar putea să fie cunoscută autorităților”.
- Sunt cel puțin 15 atacatori diferiți (Galaxy), nu unul singur. „Hoțul” înseamnă doar cel din primul val.
- Teoriile cu „inside job” apar într-o singură frază: nu există dovezi publice și nu e acuzat nimeni. Programatorul care a făcut schimbarea din 2021 **nu** e numit.
- Procesul colectiv din Ontario conține doar acuzații, netestate în instanță.
- Ideea că atacatorul a folosit AI e presupunerea Coinkite și e prezentată așa.
- Victima, Jonathan Goodman, și-a povestit singur cazul, public. Folosesc doar ce a spus el.
- Fără sfaturi de investiții. Finalul trimite la comunicatul Coinkite, ca instrucțiune a firmei.

---

## 0:00 — TEASER

`[VIZUAL]` Un seif de bancă noaptea. Un singur sertar închis. Praf într-o rază de lumină.

`[VO]` Un seif de bancă. O casetă de valori. Înăuntru, trei dispozitive mici care n-au fost conectate niciodată la internet.
`[VO]` În noaptea de 29 iulie, nimeni n-a deschis caseta. Nimeni n-a atins dispozitivele.
`[VO]` În șapte minute, bitcoinii pe care îi protejau dispăruseră.
`[VO]` În cinci zile, aproximativ 116 milioane de dolari fuseseră luați la fel.
`[VO]` Greșeala din spatele furtului stătea în cod public de mai bine de cinci ani.
`[VO]` Iar primul hoț s-ar putea să fi făcut și el o greșeală.

`[VIZUAL]` Tăietură la negru, bas, apoi titlul: **SIPHON FILES · NOBODY TOUCHED IT**.

---

## 0:35 — THOMAS (intro)

`[THOMAS]` Sunt Thomas Archer, naratorul AI al Siphon Files.
`[THOMAS]` Fiecare afirmație are o sursă. Lista e în descriere.
`[THOMAS]` Aceasta e povestea unui lacăt pe care nu l-a forțat nimeni.
`[THOMAS]` Cineva pur și simplu a aflat combinația.

---

## 0:55 — OMUL CARE A FĂCUT TOTUL CORECT

`[VO]` Jonathan Goodman e antreprenor în Toronto. După spusele lui, a pus peste un milion de dolari în bitcoin.
`[VO]` Așa că face ce spun ghidurile de securitate: își cumpără un hardware wallet, un Coldcard, făcut de o firmă canadiană, Coinkite.
`[VO]` La configurare, dispozitivul îți dă o listă de 12 sau 24 de cuvinte. Cuvintele astea sunt banii. Oricine le are îți poate cheltui bitcoinii, de oriunde.
`[VO]` Cumpără trei. Nu-și arată cuvintele nimănui și le ștanțează în metal, ca rezervă. Dispozitivele nu ating niciodată internetul. Le pune într-o casetă de valori la bancă.
`[VO]` Dar e un singur lucru pe care nu-l poate verifica singur: cum au fost alese cuvintele.

---

## 1:45 — COMBINAȚIA

`[VO]` Cuvintele trebuie să fie imposibil de ghicit. Așa că dispozitivul le alege la întâmplare, cu un circuit făcut pentru o singură treabă: să producă numere aleatorii.
`[VO]` Făcut cum trebuie, există atâtea liste posibile încât nimeni nu le-ar putea încerca pe toate.
`[CARTON]` **T-MINUS 5 ANI, 4 LUNI**
`[VO]` Dar în martie 2021, Coinkite lansează un update de firmware. Trece la aceeași criptografie pe care o folosește Bitcoin Core, printr-o bibliotecă nouă.
`[CARTON]` „Alegerea criptografică era bună. Integrarea nu era.” — Coinkite
`[VO]` Biblioteca nouă are nevoie de numere aleatorii. Iar codul care îi răspunde poate lucra în două feluri: citește circuitul sau rulează un înlocuitor simplu, din software. O singură setare decide.
`[VO]` Coinkite o pune pe zero, crezând că așa oprește totul. Nu e așa. Zero înseamnă: folosește înlocuitorul.
`[VO]` Și există în cod o verificare de siguranță, făcută exact pentru asta. Dacă setarea lipsește, compilarea se oprește, cu un mesaj.
`[VIZUAL]` `#error "get a HW TRNG plz"`
`[VO]` Dar verificarea întreabă doar dacă setarea există. Există. Spune zero. Verificarea trece.
`[THOMAS]` Gândește-te la un inspector de alarme de fum.
`[THOMAS]` Verifică dacă e o alarmă pe tavan.
`[THOMAS]` Nu verifică niciodată dacă e pornită.

---

## 3:05 — CINCI ANI

`[VO]` Din acel moment, modelele mai vechi, Mk2 și Mk3, își fac cuvintele din înlocuitor. Acesta pornește de la un ID fix din fabrică și câteva cronometre. Nimic din el nu e cu adevărat secret.
`[VO]` Coinkite estimează mai târziu cam 40 de biți de hazard real. O listă corectă are cel puțin 128.
`[THOMAS]` Patruzeci de biți înseamnă cam o mie de miliarde de posibilități. Sună mult.
`[THOMAS]` Pentru un calculator care ghicește offline, e o căutare care se termină.
`[VO]` Modelele mai noi stau mai bine, la cam 72 de biți. Tot mult sub o listă corectă, deși deocamdată nu există dovezi publice că vreunul dintre ele a fost golit în aceste atacuri.
`[VO]` Circuitul de numere aleatorii e tot acolo, în fiecare dispozitiv. Analiza tehnică a Coinkite recunoaște mai târziu că era folosit…
`[CARTON]` „…doar din întâmplare, și doar pentru lucruri mai puțin importante.” — Coinkite
`[VO]` Așa că acum știi ceva ce Goodman nu știe. Cuvintele lui n-au fost niciodată cu adevărat aleatorii. Iar codul e public. Oricine îl poate citi.
`[VO]` Timp de cinci ani, oameni ca el cumpără dispozitivul, își scriu cuvintele și le închid bine.
`[VO]` CEO-ul Coinkite spune că firma a plătit audituri externe în 2022 și 2024. Totuși, Coinkite spune că n-a știut de greșeală până în ziua furtului.
`[CARTON]` **T-MINUS CÂTEVA SĂPTĂMÂNI**
`[VO]` Apoi, cu câteva săptămâni înainte de furt, Coinkite rulează o analiză cu AI pe codul critic.
`[CARTON]` „N-a prins această vulnerabilitate.” — Coinkite
`[VO]` Dar altcineva o găsește primul.
`[THOMAS]` Coinkite spune că trebuie să presupună că cineva a folosit AI.
`[THOMAS]` E presupunerea Coinkite. N-a fost dovedită.
`[THOMAS]` Oricum, metoda nu avea nevoie de niciun dispozitiv.
`[THOMAS]` Ghicești o listă de cuvinte. Calculezi adresele. Verifici blockchain-ul.
`[THOMAS]` O potrivire înseamnă cheia, și banii odată cu ea.

---

## 4:35 — 01:10

`[CARTON]` **T-MINUS 0 · 30 IULIE 2026 · 01:10:20 UTC**
`[VO]` În Toronto e nouă și zece, miercuri seara. Goodman e plecat la casa lui de vacanță.
`[VO]` Prima tranzacție pleacă de pe o adresă făcută pe un Coldcard. Apoi încă una. Apoi sute.
`[VO]` Potrivit Chainalysis, hoțul merge întâi pe portofelele cele mai mari. Cam 30 de milioane de dolari în primele zece minute.
`[VO]` Și tranzacțiile astea au ceva ciudat. Sunt construite toate la fel: aceeași rată a taxei, și fiecare monedă e luată, fără să rămână nimic.
`[VO]` Ține minte detaliul ăsta.
`[VO]` Apoi ajunge la Goodman.
`[VO]` 9:36 seara. Primul dintre cele trei portofele ale lui se golește. Apoi al doilea. Până la 9:43 dispare și al treilea. Cam 1,6 milioane de dolari canadieni.
`[VO]` La 9:51, primul val se oprește. În 41 de minute s-au golit aproape o mie două sute de adrese.
`[VO]` Iar Goodman habar n-are.

---

## 5:45 — „O SĂ VERIFIC TOTUȘI”

`[VO]` În orele următoare apar primele semnale că monedele pleacă din cold wallets. Inginerii de la Block, firma din spatele portofelului Bitkey, desfac firmware-ul. Până la sfârșitul zilei, ei și alți cercetători găsesc cauza.
`[VO]` Coinkite publică primul avertisment: listele de cuvinte făcute pe firmware-ul afectat sunt în pericol. Mutați-vă fondurile. Până atunci, primul val se terminase de mult.
`[VO]` Pe 31 iulie, Goodman e la o bibliotecă publică, cu familia, când vede postarea unui prieten pe Facebook: dacă folosești un Coldcard, mută-ți banii acum.
`[CARTON]` „Nu are cum să mă afecteze, dar o să verific totuși.” — Jonathan Goodman, pentru Wealthsimple Magazine
`[VO]` Verifică. Bitcoinii lui dispăruseră încă de miercuri seara.
`[CARTON]` „Am făcut totul corect.” — Jonathan Goodman, pe X
`[VO]` Se întoarce la Toronto să facă plângere la poliție și o sesizare la Comisia de Valori Mobiliare din Ontario.
`[VO]` Oamenii îl întreabă dacă a intrat cineva în caseta lui de valori.
`[VO]` N-a intrat nimeni. Iar pentru oricine altcineva încă are o listă făcută la fel, un update de firmware nu ajută. Repară listele noi. O listă slabă, deja scrisă, rămâne slabă.
`[CARTON]` „Îmi pare rău și sunt devastat.” — Rodolfo Novak, CEO Coinkite, pe X, 31 iulie
`[THOMAS]` Asta e partea crudă a unui avertisment public.
`[THOMAS]` Ajunge la proprietari și la hoți în același moment.

---

## 7:00 — CURSA

`[VO]` Urmează al doilea val. Al treilea, de vineri până sâmbătă. Al patrulea începe luni.
`[VO]` Galaxy Research numără mai târziu cel puțin 15 atacatori diferiți. Nu mai e un singur hoț. E o mulțime, pe aceeași slăbiciune.
`[VO]` Dar în al patrulea val, tranzacțiile hoților așteaptă să fie confirmate. Până atunci, oricine plătește o taxă mai mare le poate înlocui.
`[VO]` Așa că un proprietar, Will Owens, ripostează. Lasă o sumă mică drept momeală, așteaptă ca botul s-o ia și îl întrece la taxă. Își recuperează momeala.
`[VO]` Mai târziu, voluntari white hat mută cam 52 de bitcoini din portofelele expuse, într-un trust făcut să-i returneze victimelor. În septembrie, trustul îi dă înapoi unui proprietar verificat peste 20 de bitcoini.
`[VO]` O parte din monedele furate merg spre mixere, servicii făcute să încurce urma. Conform ultimelor bilanțuri publice, mare parte din rest încă stă.
`[VO]` Când valurile se domolesc, fuseseră luați cam 1.816 bitcoini, de pe peste 5.200 de adrese.
`[VO]` Dar bucata cea mai mare, primul val, încă nu s-a mișcat, conform celor mai recente urmăriri publice.

---

## 8:10 — GREȘEALA

`[THOMAS]` Ții minte detaliul? Fiecare tranzacție din primul val arăta la fel.
`[THOMAS]` Galaxy n-a găsit pe nimeni altcineva cu acel tipar în luna dinainte.
`[THOMAS]` Așa că primul val putea fi urmărit ca o singură operațiune.
`[THOMAS]` Iar anchetatorii au observat și altceva.
`[VO]` Fiecare încercare trebuie verificată. Ca să afli care dintre adresele ghicite au bani, trebuie să le cauți, iar și iar.
`[VO]` Anchetatorii Block spun că operatorul primului val pare să fi făcut asta printr-un cont plătit la un furnizor cunoscut de date blockchain.
`[VO]` L-au contactat. Logurile interne, spun ei, se potriveau cu atacul „cu o precizie extraordinară”: numărul, momentul și ordinea cererilor.
`[THOMAS]` Pe blockchain, hoțul era doar un șir de adrese.
`[THOMAS]` Dar un cont plătit lasă de obicei urme.
`[VO]` Informațiile au ajuns la autorități. Alex Thorn, de la Galaxy, spune că identitatea atacatorului din primul val „s-ar putea să fie cunoscută autorităților”.
`[VO]` Dar, în momentul realizării acestui video, FBI n-a confirmat niciun suspect, nicio arestare și nicio recuperare.

---

## 9:20 — CINE?

`[CARTON]` **SITUAȚIA LA SFÂRȘITUL LUI NOIEMBRIE 2026**
`[VO]` Așa că, în momentul acestui video, nimeni n-a fost numit public. TRM Labs nu atribuie furtul nimănui. Coinkite spune că avocații ei lucrează cu autoritățile ca să-i identifice pe vinovați.
`[VO]` Online, unii spun că a fost din interior. Deocamdată nu există dovezi publice pentru asta, și nimeni n-a fost acuzat.
`[VO]` În septembrie, un proprietar de Coldcard a depus în Ontario o propunere de proces colectiv contra Coinkite și a cofondatorilor. Acuzația: firma știa din mai 2025 că generarea cuvintelor e slabă. Conform ultimelor rapoarte, un judecător nici nu l-a certificat încă drept proces colectiv, iar niciuna dintre afirmații n-a fost testată în instanță.
`[VO]` Și, din câte arată rapoartele publice, Coinkite n-a anunțat niciun fond de despăgubire. Goodman nu se bazează pe proces.
`[CARTON]` „Calculul la un proces colectiv e brutal.” — Jonathan Goodman, pentru The News Block
`[VO]` CEO-ul Coinkite spune că problema a afectat cam 0,17% dintre utilizatori. Cel mai nou firmware cere acum fiecărui proprietar să adauge hazard propriu când își face lista.

---

## 10:15 — CASETA, DIN NOU

`[VO]` Există un grup pe care Coinkite nu-l consideră în pericol din cauza acestei greșeli: cei care au adăugat cel puțin 50 de aruncări de zar proprii când și-au făcut lista.
`[VO]` Cei care n-au lăsat totul pe seama dispozitivului.
`[THOMAS]` Caseta aceea de valori n-a fost deschisă niciodată.
`[THOMAS]` Dispozitivele dinăuntru n-au fost niciodată sparte.
`[THOMAS]` Doar că n-au cerut niciodată lista circuitului lor de numere aleatorii.
`[THOMAS]` Dacă ți-ai făcut lista pe un Coldcard afectat, citește avertismentul Coinkite.
`[THOMAS]` Coinkite spune: consider-o compromisă și mută-te pe o listă nouă.
`[VO]` Și cei 1.082 de bitcoini din primul val? Conform celor mai recente urmăriri publice, stau tot unde i-a lăsat hoțul.
`[VO]` Iar undeva, în evidențele unei firme de date, s-ar putea să existe un nume.
`[THOMAS]` Acesta a fost Siphon Files.

---

## Ce s-a schimbat în v3 (pe scurt)

- **Niciun fapt nou.** Am schimbat ordinea și tensiunea, nu conținutul.
- Teaserul se termină pe o promisiune („primul hoț s-ar putea să fi făcut o greșeală”), plătită în secțiunea „Greșeala”.
- Thomas deschide cu imaginea episodului: un lacăt pe care nu l-a forțat nimeni, doar i s-a aflat combinația.
- **Goodman devine personajul principal de la 0:55,** înainte de orice tehnologie: întâi precauțiile lui, apoi singurul lucru pe care nu-l putea verifica. De aici vine „noi știm, el nu”.
- Trei secțiuni tehnice unite într-una singură („Combinația”), mai scurtă.
- Cartonul cu ironia Coinkite: circuitul era folosit „doar din întâmplare, pentru lucruri mai puțin importante”.
- Golirea e povestită în ora din Toronto, ca vârful să cadă pe portofelele lui Goodman, urmat de „Iar el habar n-are.”
- Finalul revine la casetă și se termină pe o posibilitate, nu pe o afirmație: „s-ar putea să existe un nume”.
- 1.559 → 1.489 de cuvinte (~10:30–10:50).

## Ce s-a schimbat în v3.1 (verificarea amănunțită)

- **Ordinea logică:** citatul „Am făcut totul corect” l-a scris după ce a aflat, așa că l-am mutat la momentul în care verifică (înainte stătea chiar înainte de „Iar el habar n-are”, ceea ce se contrazicea).
- „Golirea se oprește la 9:51” → „primul val se oprește” (mai urmează trei).
- „Al doilea val vine a doua zi” venea imediat după scena din 31 iulie și încurca datele → „Urmează al doilea val.”
- „Proiectul cerea 128 de biți” → „O listă corectă are cel puțin 128” (o listă de 24 de cuvinte are 256, deci vechea frază putea fi citită greșit).
- Cartonul „T-MINUS CÂTEVA SĂPTĂMÂNI” stătea înaintea unei fraze despre 2022 și 2024 → acum auditurile vin întâi, cu fraza sursată „Coinkite n-a știut de greșeală până în ziua furtului”, apoi cartonul și analiza cu AI.
- „Trei portofele” pe ecran era un număr pe care Goodman nu l-a dat → „câteva solduri (ILUSTRATIV)”.
- Două marcaje de timp la rând („mai târziu în aceeași zi… în câteva ore”) → „În orele următoare… Până la sfârșitul zilei”.
- Mici corecturi gramaticale în engleză (articole, „any of them”, „the latest”), plus o frază de legătură: „Every guess has to be checked.”
- **Întrebări și răspunsuri:** am verificat fiecare întrebare pusă în video (cum au fost alese cuvintele, dacă sunt afectate toate modelele, cine a găsit greșeala, ce era ciudat la tranzacții, greșeala hoțului, cine e vinovatul, unde sunt banii, cine a fost în siguranță). Toate primesc răspuns. 

## Ce s-a schimbat în v3.2 (verificat acum pe web)

- **Goodman n-a recuperat nimic,** conform ultimelor informații publice (interviul din The News Block, 28 aug.; postarea lui de pe X: „nu mă aștept să recuperez nimic”). Coinkite n-a anunțat niciun fond de despăgubire. Răspunsul e acum în script, la „Cine?”, cu citatul lui despre procesul colectiv.
- **O rază de speranță reală:** în septembrie, trustul white hat i-a dat înapoi unui proprietar verificat (nenumit) peste 20 de bitcoini. Apare la „Cursa”.
- **Detalii exacte, chiar de la el:** avea trei Coldcard-uri și trei portofele golite unul după altul, cuvintele ștanțate în metal, plus sesizare și la Comisia de Valori Mobiliare din Ontario.
- Postarea lui spune că a aflat „la cabană”, iar interviurile spun că a verificat la o bibliotecă, cu familia jos. Se potrivesc, deci rămâne biblioteca.

## Ce s-a schimbat în v3.3 (regula ta: „până la momentul acestui video”)

- **Regulă nouă, pentru acest episod și pentru toate de acum încolo:** orice situație care se mai poate schimba (arestări, identitatea hoțului, monedele care n-au mișcat, procesul, despăgubirile, cifra finală) se spune cu un marcaj de timp: „în momentul acestui video”, „deocamdată”, „conform celor mai recente urmăriri publice”. Ce s-a întâmplat pe 29–30 iulie nu are nevoie de marcaj.
- **Verificat azi, 23 nov.:** nicio arestare sau acuzare găsită, iar FBI n-a confirmat nimic. Monedele din primul val (~1.082,57 BTC) apar tot neatinse în ultima urmărire publică (Galaxy, ~24 sept.). Procesul colectiv e doar propus, necertificat (28 oct.). Nicio despăgubire anunțată.
- Secțiunea „Cine?” începe acum cu cartonul **„STATUS AS OF LATE NOVEMBER 2026”**.
- **În ziua publicării** reverific aceleași patru lucruri. Dacă s-a schimbat ceva, modific fraza și data de pe carton.
