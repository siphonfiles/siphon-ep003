# Episodul 003: Nimeni nu l-a atins (traducere pentru verificare)

> Traducerea în română a draftului v2 (`003-nobody-touched-it.md`), doar ca să-l verifici. Textul care se înregistrează rămâne cel în engleză. Sursele [S#] sunt aceleași ca în fișierul englezesc.

**Titlu propus:** „Inside the $116M Coldcard Hack” · text pe thumbnail: **„NOBODY TOUCHED IT.”** („Nimeni nu l-a atins.”)
**Test & Compare propus:** (A) titlul de mai sus + „NOBODY TOUCHED IT.”; (B) „The Safest Bitcoin Wallet Was Guessable for 5 Years” + „41 MINUTES.”; (C) „Inside the Coldcard Hack: $116M Gone Without a Touch” + „5 YEARS. 41 MINUTES.”
**Lungime:** 1.559 de cuvinte rostite, dintre care Thomas 263 în 28 de replici (~1:30), fiecare de cel mult 12 cuvinte, adică un clip LongCat de 5 s. Estimare: ~10:50–11:10.

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
`[VO]` În următoarele cinci zile, aproximativ 116 milioane de dolari au plecat de pe peste 5.200 de adrese create pe dispozitive ca el.
`[VO]` Iar greșeala din spatele furtului stătea în cod public. De mai bine de cinci ani.

`[VIZUAL]` Tăietură la negru, bas, apoi titlul: **SIPHON FILES · NOBODY TOUCHED IT**.

## 0:35 — THOMAS (intro)

`[THOMAS]` Sunt Thomas Archer, naratorul AI al Siphon Files.
`[THOMAS]` Fiecare afirmație pe care o auziți are sursă. Lista e în descriere.
`[THOMAS]` De data asta: un dispozitiv construit să fie cel mai sigur loc pentru bitcoini.
`[THOMAS]` Și singura setare care i-a făcut ghicibili.

## 0:55 — PROMISIUNEA

`[VO]` Coldcard e un portofel hardware, făcut de o firmă canadiană, Coinkite. Rolul lui e să-ți creeze cheile offline și să le țină acolo.
`[VO]` Când îl configurezi, îți dă o listă de 12 sau 24 de cuvinte. Cuvintele alea sunt banii. Cine le are îți poate cheltui bitcoinii de oriunde.
`[VO]` Deci cuvintele trebuie să fie imposibil de ghicit. Aparatul le alege la întâmplare, cu ajutorul unei componente hardware făcute pentru un singur lucru: să producă numere aleatorii.
`[VO]` Făcut corect, numărul de liste posibile e atât de mare încât nimeni nu le-ar putea încerca vreodată pe toate.
`[VO]` Proprietarii pot și să arunce zaruri adevărate și să introducă rezultatele, adăugând hazard propriu. E opțional. De asta ar trebui să se ocupe aparatul.
`[VO]` Dar componenta aceea ajută doar dacă aparatul chiar o întreabă.

## 1:40 — MARTIE 2021

`[CARTON]` **T-MINUS 5 ANI, 4 LUNI**

`[VO]` Martie 2021. Coinkite lansează o actualizare de firmware. Pe dedesubt, trece la aceeași criptografie pe care o folosește chiar Bitcoin Core, printr-o bibliotecă nouă.
`[CARTON]` **„The cryptographic choice was sound. The integration was not.”** („Alegerea criptografică a fost bună. Integrarea, nu.”) — Coinkite
`[VO]` Și noua bibliotecă are nevoie de numere aleatorii. Așa că le cere, după nume.
`[VO]` Iar codul care răspunde la numele ăsta poate lucra în două feluri. Poate citi generatorul hardware. Sau poate rula un înlocuitor software simplu. O singură setare decide.
`[VIZUAL]` Două casete: **GENERATOR HARDWARE** și **ÎNLOCUITOR SOFTWARE**. Un comutator pe **0** trimite săgeata spre cel greșit.
`[VO]` Coinkite avea propriul cod pentru hardware. Așa că a pus comutatorul pe zero, crezând că oprește totul. Nu era așa. Zero însemna: folosește înlocuitorul.

## 2:20 — VERIFICAREA CARE A TRECUT

`[VO]` Autorii bibliotecii prevăzuseră un risc de felul ăsta. Lăsaseră în cod o pază. Dacă setarea hardware lipsea, construirea firmware-ului se oprea, cu un mesaj.
`[VIZUAL]` Linia de cod: `#error "get a HW TRNG plz"` („ia-ți un generator hardware, te rog”).
`[VO]` Dar paza verifica doar dacă setarea există. Exista. Era pusă pe zero, dar exista. Așa că firmware-ul s-a construit fără probleme.

`[THOMAS]` Gândiți-vă la un inspector de detectoare de fum.
`[THOMAS]` Verifică dacă e un detector pe tavan.
`[THOMAS]` Nu verifică niciodată dacă e pornit.
`[THOMAS]` Aici, setarea era acolo. Spunea zero. Verificarea a trecut.

`[VO]` De atunci, modelele mai vechi Mk2 și Mk3 au făcut seed-urile noi cu înlocuitorul. Era alimentat de un cod fix din fabrică și de câteva cronometre. Nimic din toate astea nu e cu adevărat secret sau aleatoriu.
`[VO]` Coinkite a estimat ulterior rezultatul la circa 40 de biți de hazard real, în loc de cei 128 pentru care era proiectat aparatul.

`[THOMAS]` Patruzeci de biți înseamnă cam o mie de miliarde de variante. Sună mult.
`[THOMAS]` Pentru un calculator care ghicește offline, e o căutare care se termină.

`[VO]` Modelele noi au stat mai bine, cam 72 de biți. Tot mult sub proiect, dar nu există dovezi publice că vreunul a fost golit în atacurile astea.

## 3:55 — CINCI ANI

`[VO]` Deci de aici încolo știți ceva ce proprietarii nu știu. Cuvintele lor n-au fost niciodată cu adevărat aleatorii.
`[VO]` Iar codul e public. Oricine îl poate citi. Mai bine de cinci ani, oamenii cumpără aparatul, își notează cuvintele și le închid undeva.
`[CARTON]` **T-MINUS CÂTEVA SĂPTĂMÂNI**
`[VO]` CEO-ul Coinkite spune că firma a plătit evaluări de securitate externe în 2022 și 2024. Iar cu câteva săptămâni înainte de furt, Coinkite și-a trecut codul critic printr-o analiză cu AI.
`[CARTON]` **„It did not catch this vulnerability.”** („N-a prins această vulnerabilitate.”) — Coinkite, despre propria analiză cu AI
`[VO]` Apoi altcineva găsește defectul primul.

`[THOMAS]` Coinkite spune că trebuie să presupună că cineva a folosit AI ca să-l găsească.
`[THOMAS]` E presupunerea Coinkite. Nu e dovedită.
`[THOMAS]` Oricum ar fi, metoda nu avea nevoie de niciun aparat.
`[THOMAS]` Ghicești un seed. Calculezi adresele. Verifici blockchain-ul.
`[THOMAS]` O potrivire înseamnă cheia, și banii odată cu ea.

`[VO]` Fără phishing. Fără malware. Fără spargere. Doar aritmetică, făcută în altă parte.

## 5:05 — 01:10

`[CARTON]` **T-MINUS 0 · 30 IULIE 2026 · 01:10:20 UTC**

`[VO]` Joi, 30 iulie. Unu și zece noaptea, ora UTC. Prima tranzacție pleacă de pe o adresă creată pe un Coldcard. Apoi încă una. Apoi sute.
`[VO]` Potrivit Chainalysis, hoțul merge întâi pe portofelele cele mai mari. Cam 30 de milioane de dolari în primele zece minute.
`[VO]` Și e ceva ciudat la tranzacțiile astea. Sunt construite toate la fel: același nivel al taxei, și fiecare monedă scoasă până la ultima, fără nimic lăsat în urmă.
`[VO]` Țineți minte detaliul ăsta.
`[VO]` La 01:51 se oprește. În 41 de minute, aproape o mie două sute de adrese au fost golite.
`[VO]` În spatele fiecăreia, un proprietar care credea că cheile lui sunt offline, deci în siguranță.

## 6:05 — ȘAPTE MINUTE

`[VO]` În Ontario e încă seara de 29 iulie. Jonathan Goodman, un antreprenor din Toronto, e plecat la casa lui de vacanță.
`[VO]` Coldcard-ul lui stă într-o casetă de valori la bancă. N-a atins niciodată internetul. Cuvintele lui nu le-a dat nimănui.
`[VO]` Între 21:36 și 21:43, toate portofelele lui sunt golite. Cam 1,6 milioane de dolari canadieni. Șapte minute.
`[CARTON]` **„I did everything right.”** („Am făcut totul corect.”) — Jonathan Goodman, pe X
`[VO]` Iar el habar n-are.

## 6:50 — N-A ȘTIUT

`[VO]` Mai târziu în aceeași zi încep să apară relatări despre monede care pleacă din portofele reci. Inginerii de la Block, firma care face portofelul Bitkey, încep să desfacă firmware-ul.
`[VO]` În câteva ore, ei și alți cercetători găsesc cauza. Coinkite își publică primul avertisment: seed-urile făcute pe firmware-ul afectat sunt în pericol. Mutați-vă fondurile.
`[VO]` Până atunci, primul val se terminase de mult.
`[VO]` Pe 31 iulie, Goodman e la o bibliotecă publică cu familia când vede postarea unui prieten pe Facebook: dacă folosești un Coldcard, mută-ți banii acum.
`[VO]` Verifică. Bitcoinii lui au dispărut din noaptea de miercuri. Se întoarce la Toronto să depună plângere la poliție.
`[VO]` Oamenii îl întreabă dacă i-a umblat cineva la caseta de valori.
`[VO]` Nu i-a umblat nimeni. Și pentru oricine are încă un seed ca al lui, o actualizare de firmware nu ajută. Repară seed-urile noi. Un seed slab, deja scris, rămâne slab.
`[CARTON]` **„I'm sorry and I'm devastated.”** („Îmi pare rău și sunt devastat.”) — Rodolfo Novak, CEO Coinkite, pe X, 31 iulie
`[VO]` Așa că acum începe o cursă.

`[THOMAS]` Asta e partea crudă a unui avertisment public.
`[THOMAS]` Ajunge la proprietari și la hoți în același moment.
`[THOMAS]` Unii proprietari se mută la timp. Alții nu.

## 7:55 — CURSA

`[VO]` Al doilea val vine a doua zi. Al treilea ține de vineri până sâmbătă. Al patrulea începe luni.
`[VO]` Galaxy Research numără mai târziu cel puțin 15 atacatori diferiți. Nu mai e un singur hoț. E o mulțime, care exploatează aceeași slăbiciune.
`[VO]` În al patrulea val, tranzacțiile hoților așteaptă să fie confirmate. Până atunci, oricine plătește o taxă mai mare le poate înlocui.
`[VO]` Un proprietar, Will Owens, lasă o sumă mică drept momeală, așteaptă robotul și îl întrece la taxă. Își recuperează momeala.
`[VO]` Mai târziu, niște voluntari „white hat” scot cam 52 de bitcoini din portofele expuse și îi mută într-un fond fiduciar creat ca să-i dea înapoi victimelor.
`[VO]` O parte din monedele furate ajung în mixere, servicii făcute să încurce urma. Cele mai multe stau pe loc.
`[VO]` Când lucrurile se mai liniștesc, au fost luați cam 1.816 bitcoini, de pe peste 5.200 de adrese.
`[VO]` Dar cea mai mare bucată, primul val, nu s-a mișcat deloc.

## 8:55 — INDICIUL

`[THOMAS]` Vă amintiți detaliul? Toate tranzacțiile din primul val arătau la fel.
`[THOMAS]` Galaxy n-a găsit pe nimeni altcineva cu tiparul ăsta în luna dinainte.
`[THOMAS]` Așa că primul val a putut fi urmărit ca o singură operațiune.
`[THOMAS]` Iar anchetatorii au observat și altceva la el.

`[VO]` Ca să afli care dintre adresele ghicite au bani, trebuie să le cauți, iar și iar.
`[VO]` Anchetatorii de la Block spun că operatorul primului val pare să fi făcut asta printr-un cont plătit la un furnizor cunoscut de date blockchain.
`[VO]` Au contactat furnizorul. Jurnalele lui interne, spun ei, s-au potrivit cu atacul „cu o precizie extraordinară”: numărul, momentul și ordinea cererilor.
`[VO]` Informațiile au ajuns la autorități. Alex Thorn de la Galaxy spune că identitatea atacatorului din primul val „s-ar putea să fie cunoscută autorităților”.
`[VO]` FBI n-a confirmat niciun suspect, nicio arestare și nicio recuperare.

## 9:50 — CINE?

`[VO]` Deci cine a făcut-o? Public, nimeni nu știe. TRM Labs nu atribuie furtul nimănui.
`[VO]` Coinkite spune că avocații ei lucrează cu autoritățile din mai multe jurisdicții ca să-i identifice pe vinovați.
`[VO]` Online, unii spun că a fost o lucrătură din interior. Nu există dovezi publice pentru asta și nu e acuzat nimeni.
`[VO]` În septembrie, un proprietar de Coldcard a depus în Ontario o propunere de proces colectiv împotriva Coinkite și a cofondatorilor ei. Acuză că firma știa din mai 2025 că generarea seed-urilor e slabă. Acuzațiile n-au fost testate în instanță.
`[VO]` CEO-ul Coinkite spune că defectul a afectat cam 0,17% dintre utilizatori. Iar cel mai nou firmware cere fiecărui proprietar să adauge hazard propriu când își face un seed.

## 10:30 — CASETA, DIN NOU

`[VO]` E un singur grup pe care Coinkite nu-l consideră în pericol din cauza acestui defect: proprietarii care au adăugat cel puțin 50 de aruncări de zar ale lor când și-au făcut seed-ul.
`[VO]` Cei care n-au lăsat totul pe seama aparatului.

`[THOMAS]` Caseta de valori din Ontario n-a fost deschisă niciodată.
`[THOMAS]` Aparatul dinăuntru n-a fost spart niciodată.
`[THOMAS]` Doar că n-a cerut niciodată hardware-ului lui de numere aleatorii seed-ul.
`[THOMAS]` Dacă ți-ai făcut un seed pe un Coldcard afectat, citește comunicatul Coinkite.
`[THOMAS]` Coinkite spune: consideră-l compromis și treci pe un seed nou.

`[VO]` Și cei 1.082 de bitcoini din primul val? Potrivit ultimelor relatări publice, stau încă acolo unde i-a lăsat hoțul.
`[VO]` Și s-ar putea ca cineva să știe deja cine i-a pus acolo.

`[THOMAS]` Acesta a fost Siphon Files.

---

## Ce trebuie să știi la verificare

- **Corecturi față de predare:** versiunile afectate sunt **4.0.1–4.1.9** (după Coinkite; Block include și 4.0.0), nu „4.0.0”. Reparația de urgență e **4.2.0** (31 iulie). Data avertismentului Coinkite e disputată: Coinkite și Block îl datează pe 30 iulie, Galaxy spune „la ~30 de ore” după prima golire. Scriptul ocolește diferența („primul val se terminase de mult”). Citatul „I did everything right” e al lui Jonathan Goodman, de pe X (C$1,6M, 18,25 BTC).
- **Orele lui Goodman:** 21:36–21:43 pe 29 iulie, ora Ontario = 01:36–01:43 UTC pe 30 iulie, adică în fereastra primului val. Scriptul păstrează intenționat ambele date.
- **Cifrele pierderii diferă între surse:** 1.816 BTC „potențial” (Galaxy/TRM), minim sigur 1.730 BTC (Galaxy), 1.432 BTC confirmați (CryptoQuant), ulterior ~1.830 BTC (Galaxy). Vocea spune „about 116 million”, ca în titlu. Intervalele merg în descriere.
- **Sursele primare citite direct în Chrome (23 nov):** cele 3 postări Coinkite (comunicatul, analiza tehnică, postarea despre AI) și raportul Block. Tot ce e în script se potrivește cu ele.
- **Citatul lui Novak, verificat:** originalul e articolul lui pe X din 31 iulie 2026, 15:42: „I'm sorry and I'm devastated. Our team is heartbroken about yesterday's news.” Contul e acum restricționat, așa că textul l-am confirmat din copia indexată de X și din Forbes, Bitcoin.com News și Protos. „Crushed” (Forklog) e doar o traducere.
- **De reverificat înainte de randare:** dacă banii din primul val s-au mișcat, orice arestare sau acuzare, stadiul procesului, post-mortemul final Coinkite.

## Ce s-a schimbat în v2 (revizia completă)

Lista detaliată e la finalul fișierului în engleză („Changes from v1”). Pe scurt:
- **Corecturi de fapt:** „5.200 de portofele” → „adrese”; „cinci ani” → „mai bine de cinci ani”; generatorul nu e un cip separat, ci o componentă a procesorului; explicația cu „două lucruri cu același nume” era greșită și a fost rescrisă după Block și Coinkite (un singur cod care poate merge în două feluri, ales de o setare); „cei mai mulți nu folosesc zaruri” și „în iulie cineva citește firmware-ul” erau fără sursă și au fost scoase.
- **Logică:** indiciul din final nu mai sugerează că taxa i-a dus pe anchetatori la contul plătit (sursele nu spun asta); „firmware-ul nu-l poate ajuta” (banii lui erau deja plecați) → „nu ajută pe nimeni care mai are un seed ca al lui”; „nimeni nu știe încă” (Block știa în aceeași zi) → „iar el habar n-are”; Will Owens și-a recuperat doar momeala.
- **Goodman, exact după interviul lui:** biblioteca publică, postarea prietenului pe Facebook, întoarcerea la Toronto pentru plângerea la poliție.
- **Ritm:** un carton T-minus în plus („câteva săptămâni”, analiza cu AI), mai puține cifre la vârf, finalul fără ambiguitate.
- **Fiecare întrebare din video își primește răspunsul pe ecran:** care a fost greșeala, dacă au fost lovite și modelele noi, ce înseamnă detaliul cu taxa, cine a făcut-o, unde sunt banii din primul val, ce trebuie să facă proprietarii.
