# Episodul 003: Nimeni nu l-a atins (traducere pentru verificare)

> Traducerea în română a draftului v1 (`003-nobody-touched-it.md`), doar ca să-l verifici. Textul care se înregistrează rămâne cel în engleză. Sursele [S#] sunt aceleași ca în fișierul englezesc.

**Titlu propus:** „Inside the $116M Coldcard Hack” · text pe thumbnail: **„NOBODY TOUCHED IT.”** („Nimeni nu l-a atins.”)
**Test & Compare propus:** (A) titlul de mai sus + „NOBODY TOUCHED IT.”; (B) „The Safest Bitcoin Wallet Was Guessable for 5 Years” + „41 MINUTES.”; (C) „Inside the Coldcard Hack: $116M Gone Without a Touch” + „5 YEARS. 41 MINUTES.”
**Lungime:** 1.502 cuvinte rostite, dintre care Thomas 258 în 28 de replici (~1:30), fiecare de cel mult 12 cuvinte, adică un clip LongCat de 5 s. Estimare: ~10:40–11:00.

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

`[VO]` O bancă din Ontario. O casetă de valori. Înăuntru, un mic dispozitiv care n-a fost conectat niciodată la internet.
`[VO]` În noaptea de 29 iulie, nimeni n-a deschis caseta. Nimeni n-a atins dispozitivul.
`[VO]` În șapte minute, bitcoinii pe care îi proteja dispăruseră.
`[VO]` În următoarele cinci zile, aproximativ 116 milioane de dolari au plecat din peste 5.200 de portofele ca el.
`[VO]` Iar greșeala care a făcut posibil totul stătea în cod public. De cinci ani.

`[VIZUAL]` Tăietură la negru, bas, apoi titlul: **SIPHON FILES · NOBODY TOUCHED IT**.

## 0:35 — THOMAS (intro)

`[THOMAS]` Sunt Thomas Archer, naratorul AI al Siphon Files.
`[THOMAS]` Fiecare afirmație pe care o auziți are sursă. Lista e în descriere.
`[THOMAS]` În seara asta: cel mai sigur loc în care îți poți ține bitcoinii.
`[THOMAS]` Și singura setare care i-a făcut ghicibili.

## 0:55 — PROMISIUNEA

`[VO]` Coldcard e un portofel hardware, făcut de o firmă canadiană, Coinkite. Are un singur rol: să-ți creeze cheile offline și să le țină acolo.
`[VO]` Când îl configurezi, îți dă o listă de 12 sau 24 de cuvinte. Cuvintele alea sunt banii. Cine le are îți poate cheltui bitcoinii de oriunde.
`[VO]` Deci cuvintele trebuie să fie imposibil de ghicit. Aparatul le alege la întâmplare, cu ajutorul unui cip care are un singur rost: să producă numere aleatorii.
`[VO]` Făcut corect, numărul de liste posibile e atât de mare încât nimeni nu le-ar putea încerca vreodată pe toate.
`[VO]` Unii proprietari merg un pas mai departe. Aruncă zaruri adevărate și introduc rezultatele, adăugând hazard propriu. Cei mai mulți n-o fac. Pentru asta e cipul.
`[VO]` Dar cipul ajută doar dacă e și întrebat.

## 1:40 — MARTIE 2021

`[CARTON]` **T-MINUS 5 ANI, 4 LUNI**

`[VO]` Martie 2021. Coinkite lansează o actualizare de firmware. Pe dedesubt, introduce o bibliotecă criptografică nouă, bine cotată.
`[VO]` Și noua bibliotecă are nevoie de numere aleatorii. Așa că le cere sistemului, după nume.
`[VO]` Numai că în cod sunt două lucruri cu numele ăsta. Unul e cipul hardware. Celălalt e o rezervă software simplă, gândită pentru calculatoarele care n-au deloc un astfel de cip.
`[VO]` Coinkite nu voia rezerva. Așa că a oprit-o, cu o setare: zero.

## 2:20 — VERIFICAREA CARE A TRECUT

`[VO]` Autorii bibliotecii prevăzuseră asta. Lăsaseră în cod o pază. Dacă setarea hardware lipsea, construirea firmware-ului se oprea, cu un mesaj.
`[VIZUAL]` Linia de cod: `#error "get a HW TRNG plz"` („ia-ți un generator hardware, te rog”).
`[VO]` Dar paza verifica doar dacă setarea există. Exista. Era pusă pe zero, dar exista. Așa că firmware-ul s-a construit fără probleme.

`[THOMAS]` Gândiți-vă la un inspector de detectoare de fum.
`[THOMAS]` Verifică dacă e un detector pe tavan.
`[THOMAS]` Nu verifică niciodată dacă e pornit.
`[THOMAS]` Asta s-a întâmplat aici. Detectorul era acolo. Era oprit.

`[VO]` De atunci, pe modelele mai vechi Mk2 și Mk3, seed-urile noi au venit din rezervă, alimentată de numărul de serie al aparatului și de un cronometru. Pe amândouă un atacator le poate estima.
`[VO]` Coinkite a evaluat ulterior rezultatul la circa 40 de biți de hazard real, în loc de cei 128 pentru care era proiectat.

`[THOMAS]` Patruzeci de biți sună mult. Sunt cam o mie de miliarde de variante.
`[THOMAS]` Pentru un calculator care ghicește offline, e o căutare care se termină.

`[VO]` Pe modelele noi diferența a fost mai mică, cam 72 de biți. Tot mult sub proiect, dar nimeni n-a arătat că acelea au fost golite în atacul ăsta.

## 3:55 — CINCI ANI

`[VO]` Deci de aici încolo știți ceva ce proprietarii nu știu. Cuvintele lor n-au fost niciodată cu adevărat aleatorii.
`[VO]` Iar codul e public. Oricine îl poate citi. Cinci ani, oamenii cumpără aparatul, își notează cuvintele și le închid undeva.
`[VO]` Coinkite spune că a plătit evaluări de securitate externe, în 2022 și 2024. Iar cu câteva săptămâni înainte de furt a trecut codul critic printr-o analiză făcută cu AI. N-a prins problema.
`[CARTON]` **„It did not catch this vulnerability.”** („N-a prins această vulnerabilitate.”) — Coinkite, despre propria analiză cu AI
`[VO]` Apoi, la sfârșitul lui iulie 2026, altcineva citește firmware-ul vechi.

`[THOMAS]` Coinkite spune că trebuie să presupună că cineva a folosit AI ca s-o găsească.
`[THOMAS]` E presupunerea Coinkite. Nu e dovedită.
`[THOMAS]` Dar metoda nu avea nevoie de niciun aparat.
`[THOMAS]` Ghicești un seed. Calculezi adresele. Verifici blockchain-ul.
`[THOMAS]` O potrivire înseamnă o cheie. Repeți, până se termină banii.

`[VO]` Fără phishing. Fără malware. Fără spargere. Doar aritmetică, făcută în altă parte.

## 5:05 — 01:10

`[CARTON]` **T-MINUS 0 · 30 IULIE 2026 · 01:10:20 UTC**

`[VO]` Joi, 30 iulie. Unu și zece noaptea, ora UTC. Prima tranzacție pleacă de pe o adresă creată de un Coldcard. Apoi încă una. Apoi sute.
`[VO]` Potrivit Chainalysis, hoțul a mers întâi pe portofelele cele mai mari. Cam 30 de milioane de dolari în primele zece minute.
`[VO]` Și e ceva ciudat la tranzacțiile astea. Fiecare plătește exact aceeași taxă și trimite tot, fără să lase nimic în urmă.
`[VO]` Țineți minte taxa asta.
`[VO]` La 01:51 golirea se oprește. 41 de minute. 1.196 de adrese golite. 1.082 de bitcoini.
`[VO]` Fiecare era un portofel al cărui proprietar credea că e offline, deci în siguranță.

## 6:05 — ȘAPTE MINUTE

`[VO]` În Ontario e încă seara de 29 iulie. Jonathan Goodman, un antreprenor din Toronto, e plecat la casa lui de vacanță.
`[VO]` Coldcard-ul lui stă într-o casetă de valori la bancă. N-a atins niciodată internetul. Cuvintele lui n-au ieșit niciodată din mâinile lui.
`[VO]` Între 21:36 și 21:43, toate portofelele lui sunt golite. 18,25 bitcoini. Cam 1,6 milioane de dolari canadieni. Șapte minute.
`[CARTON]` **„I did everything right.”** („Am făcut totul corect.”) — Jonathan Goodman, pe X
`[VO]` Dar încă nu știe. Nu știe nimeni.

## 6:50 — N-A ȘTIUT

`[VO]` În orele care urmează apar relatări despre monede care pleacă din portofele reci. Inginerii de la Block, firma care face portofelul Bitkey, încep să desfacă firmware-ul.
`[VO]` Găsesc problema și anunță Coinkite chiar în aceeași zi.
`[VO]` La circa 30 de ore după prima golire, Coinkite își publică avertismentul: seed-urile făcute pe firmware-ul afectat sunt în pericol. Mutați-vă fondurile.
`[VO]` Goodman află pe 31 iulie, dintr-o postare a unui prieten pe Facebook. Verifică. Banii erau plecați de două zile.
`[VO]` Când raportează furtul, prima întrebare pe care o primește e dacă i-a spart cineva caseta de valori.
`[VO]` Nu i-a spart-o nimeni. Și o actualizare de firmware nu-l poate ajuta. Repară seed-urile noi. Un seed slab, deja scris, rămâne slab pentru totdeauna.
`[CARTON]` **„I'm sorry and I'm devastated.”** („Îmi pare rău și sunt devastat.”) — Rodolfo Novak, fondatorul Coinkite, 31 iulie
`[VO]` Așa că acum începe o cursă.

`[THOMAS]` Asta e partea crudă a unui avertisment public.
`[THOMAS]` Ajunge la proprietari și la hoți în același moment.
`[THOMAS]` Unii proprietari se mută la timp. Alții nu.

## 7:55 — CURSA

`[VO]` Al doilea val vine a doua zi. Al treilea ține de vineri până sâmbătă. Al patrulea începe luni.
`[VO]` Până atunci, Galaxy Research numără cel puțin 15 atacatori diferiți. Nu mai e un singur hoț. E o mulțime, care exploatează aceeași slăbiciune.
`[VO]` În al patrulea val, tranzacțiile hoților pot fi încă înlocuite de oricine e dispus să plătească o taxă mai mare.
`[VO]` Un proprietar, Will Owens, lasă o sumă mică drept momeală, așteaptă robotul și îl întrece la taxă. Câștigă.
`[VO]` Mai târziu, niște voluntari „white hat” scot cam 52 de bitcoini din portofele expuse și îi mută într-un fond fiduciar creat ca să-i dea înapoi victimelor.
`[VO]` O parte din monedele furate ajung în mixere, servicii făcute să încurce urma. Cele mai multe stau pe loc.
`[VO]` Când lucrurile se mai liniștesc, au dispărut cam 1.816 bitcoini, din peste 5.200 de adrese.
`[VO]` Dar cea mai mare bucată, primul val, nu s-a mișcat deloc.

## 8:55 — INDICIUL

`[THOMAS]` Vă amintiți taxa? Aceeași la fiecare tranzacție.
`[THOMAS]` Galaxy a verificat ultimele treizeci de zile. Nimeni altcineva n-a folosit tiparul ăsta.
`[THOMAS]` Deci cine a condus primul val își construise propria mașinărie.
`[THOMAS]` Iar o mașinărie ca asta trebuie să pună multe întrebări.

`[VO]` Care dintre adresele ghicite au bani? Ca să afli repede, poți plăti o firmă de date blockchain să-ți răspundă.
`[VO]` Anchetatorii de la Block spun că operatorul primului val pare să fi făcut exact asta, printr-un cont plătit la un furnizor cunoscut de date blockchain.
`[VO]` Au contactat furnizorul. Jurnalele lui interne, spun ei, s-au potrivit cu atacul „cu o precizie extraordinară”: numărul, momentul și ordinea cererilor.
`[VO]` Informațiile au ajuns la autorități. Alex Thorn de la Galaxy spune că identitatea atacatorului din primul val „s-ar putea să fie cunoscută autorităților”.
`[VO]` FBI n-a confirmat niciun suspect, nicio arestare și nicio recuperare.

## 9:50 — CINE?

`[VO]` Deci cine a făcut-o? Public, nimeni nu știe. TRM Labs nu atribuie furtul nimănui.
`[VO]` Coinkite spune că avocații ei lucrează cu autoritățile din mai multe jurisdicții ca să-i identifice pe vinovați.
`[VO]` Online, unii spun că a fost o lucrătură din interior. Nu există dovezi publice pentru asta și nu e acuzat nimeni.
`[VO]` În septembrie, un proprietar de Coldcard a depus în Ontario o propunere de proces colectiv împotriva Coinkite și a cofondatorilor ei. Acuză că firma știa din mai 2025 că generarea seed-urilor e slabă. Acuzațiile n-au fost testate în instanță.
`[VO]` Coinkite spune că defectul a afectat cam 0,17% dintre utilizatori. Iar noul ei firmware cere fiecărui proprietar să adauge hazard propriu când își face un seed.

## 10:30 — CASETA, DIN NOU

`[VO]` E un singur grup pe care Coinkite nu-l consideră în pericol din cauza acestui defect. Proprietarii care au adăugat cel puțin 50 de aruncări de zar ale lor când și-au făcut seed-ul.
`[VO]` Puținii care n-au lăsat totul pe seama cipului.

`[THOMAS]` Caseta de valori din Ontario n-a fost deschisă niciodată.
`[THOMAS]` Aparatul dinăuntru încă funcționează perfect.
`[THOMAS]` Doar că n-a cerut niciodată cipului potrivit un număr.
`[THOMAS]` Dacă ți-ai făcut un seed pe un Coldcard afectat, citește comunicatul Coinkite.
`[THOMAS]` Coinkite spune să-l consideri compromis și să treci pe un seed nou.

`[VO]` Și cei 1.082 de bitcoini din primul val? Potrivit ultimelor relatări publice, stau încă acolo unde i-a lăsat hoțul.
`[VO]` S-ar putea ca cineva să știe ai cui sunt.

`[THOMAS]` Acesta a fost Siphon Files.

---

## Ce trebuie să știi la verificare

- **Corecturi față de predare:** versiunile afectate sunt **4.0.1–4.1.9** (după Coinkite; Block include și 4.0.0), nu „4.0.0”. Reparația de urgență e **4.2.0** (31 iulie). Avertismentul Coinkite a venit **la ~30 de ore** după prima golire. Citatul „I did everything right” e al lui Jonathan Goodman, de pe X (C$1,6M, 18,25 BTC).
- **Orele lui Goodman:** 21:36–21:43 pe 29 iulie, ora Ontario = 01:36–01:43 UTC pe 30 iulie, adică în fereastra primului val. Scriptul păstrează intenționat ambele date.
- **Cifrele pierderii diferă între surse:** 1.816 BTC „potențial” (Galaxy/TRM), minim sigur 1.730 BTC (Galaxy), 1.432 BTC confirmați (CryptoQuant), ulterior ~1.830 BTC (Galaxy). Vocea spune „about 116 million”, ca în titlu. Intervalele merg în descriere.
- **Nu am deschis direct** cele 3 postări Coinkite și raportul Block: pentru citirea paginii era nevoie de acordul tău, iar tu nu erai la calculator. Conținutul lor vine din fragmente exacte citate în rezultatele de căutare și din articolele care le citează. Le citesc în Chrome înainte de generarea vocii.
- **Citatul lui Novak** apare în două variante („devastated” / „crushed”). Îl verific în postarea originală înainte să fac cartonul.
- **De reverificat înainte de randare:** dacă banii din primul val s-au mișcat, orice arestare sau acuzare, stadiul procesului, post-mortemul final Coinkite.
