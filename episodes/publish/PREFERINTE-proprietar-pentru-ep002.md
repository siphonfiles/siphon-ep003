# Preferințele proprietarului (din ep. 003), de aplicat la ep. 002 (Bitget)

Instrucțiuni pentru chatul care lucrează la `siphonfiles/siphon-ep002`. Sunt preferințe pe care proprietarul le-a cerut după ce a văzut ep. 003 (Coldcard, `siphonfiles/siphon-ep003`). Se aplică **la toate episoadele**, deci și la ep. 002, înainte de randarea finală.

Regulile complete sunt și în `siphonfiles/siphon-core` › `CLAUDE.md` › secțiunea 8, „Preferințele vizuale ale proprietarului”. Codul care le implementează e în `siphon-core` › `graphics/motion/scenes.py` și în `siphon-ep003` (`scenes.py`, `scripts/screen_content.py`).

---

## 1. Ilustrațiile animate

1. **Orice sursă de lumină pâlpâie.** Asta înseamnă lămpi, becuri, reflectoare, LED-uri, lumină din sertare și ecrane.
   - Se folosește parametrul `flick=` al scenei `illus` (`flick_level` + `_light_mask` din `scenes.py`).
   - Lampă care se poticnește din când în când: `mode="flicker"`, adâncime ~0,3.
   - Bec mic sau LED care respiră lent: `mode="slow"`, adâncime ~0,45–0,55.
   - Raza de lumină desenată (`glows` de tip beam) pâlpâie odată cu lampa.
   - Exemplu: `flick=dict(lights=[dict(x=..., y=..., r=..., thr=0.55, amb=0.5)], depth=0.3, seed=1)`. Coordonatele sunt pe imaginea originală, de 2048x1152.
2. **Fără praf în imaginile de afară** (oraș, stradă, câmp, zăpadă, fațadă, cabană, apă): `motes=False`. În locul prafului, ce se potrivește locului:
   - pe zăpadă sau iarnă: **ninsoare măruntă** (`snow=True`);
   - pe peisaje deschise: **ceață care se vede că trece**, adică bancuri care curg, nu un voal uniform (`fog` cu `speed` ~25, `haze` ~0,15);
   - **fără abur sau ceață pe apă**: lacurile și râurile rămân curate. Proprietarul a respins aburul pe lac.
3. **Mișcare pe ecrane și pe benzile de lumină:** `ripple=`, o ondulare doar pe zonele luminoase. Masca ocolește siluetele întunecate, ca să nu se strice altceva.
4. **Niciun ecran gol.** Telefoanele, monitoarele și orice alt ecran din ilustrații arată ceva legat de scenă: un ceas, aplicații, cod sau o notificare. Niciodată alb sau o singură culoare uniformă.
   - Se desenează pe CPU cu `scripts/screen_content.py` din `siphon-ep003`. Conținutul se randează plat, se pune în perspectivă pe ecran, se mască după forma ecranului (păstrează notch-ul și colțurile rotunjite) și primește lumina lui.
   - Textul de pe ecran trebuie să se citească **din unghiul camerei**: se verifică orientarea pe un decupaj înainte de randare.
   - Codul și mesajele inventate poartă eticheta **ILLUSTRATIVE**.
   - Originalul se păstrează ca `<nume>_blank.jpg`.
5. **Fără pete de culoare rătăcite.** Sufixul de stil Z-Image pune uneori puncte sau pătrate în culoarea de accent, fără sens (la ep. 003 erau verzi; la ep. 002 accentul e cyan).
   - Fiecare ilustrație se verifică, iar petele se scot pe CPU: OpenCV `inpaint` (TELEA) pentru pete mici, iar pentru strălucirile moi se scade profilul radial al strălucirii.
   - La imaginile noi, promptul cere accentul doar pe un obiect anume.

## 2. Montajul

1. **Nimic nu se repetă în video:** nicio ilustrație, niciun design de grafic, niciun carton. Capitolele, citatele, explicațiile, T-minus, cifrele mari și frazele au fiecare varianta lui de design (la ep. 003: `chapter_v`, `quote_v`, `explainer_v` etc., cu parametrul `v=`).
   - Înainte de a trimite o randare se face o verificare automată: cadre la 0,5 s, căutând planuri asemănătoare la momente diferite.
2. **Cartonul apare exact pe cuvintele lui și stă cât se vorbește despre el.** E ancorat pe cuvântul din replică, nu pe tăietura următoare.
   - Exemplu la ep. 003: „three small devices” → cartonul apare pe acele cuvinte și stă ~6 s, nu 2 s la final.
   - Animația din carton e destul de lentă cât să poată fi urmărită.
3. **Fără flash-uri sub 1 s** după clipurile lui Thomas. Garda `check_no_flash` rămâne activă.
4. **Thomas apare doar în video, niciodată ca imagine fixă.** Clipurile cu el pe Hugging Face se fac **doar la 720p**.

## 3. Thumbnail și titlu

- Thumbnail-ul **completează titlul, nu-l repetă.** De exemplu, suma din titlu nu se mai scrie pe thumbnail.
- Textul de pe thumbnail are **3–5 cuvinte**.
- Fără logo-uri reale și fără dispozitive care să semene cu cele reale. Simbolul ₿, desenat în cod, se poate folosi.
- Elementul cheie (de exemplu moneda) **nu stă în lumina felinarului sau a spotului**, ci separat, ca să iasă în evidență.
- Imaginea vine din ilustrațiile episodului, făcută pe CPU, fără cotă.
- Se propun 2–3 variante, iar proprietarul alege.
- Titlurile: afirmații, nu întrebări, 5–8 cuvinte, fără unghiuri deja folosite de concurență. Înainte de propuneri se face research pe concurență.

## 4. Lucrul în general

- Proprietarul dă observațiile **pe rând**. Nu se schimbă nimic până nu spune că a terminat.
- După corecturi, preferințele noi se notează în `CLAUDE.md`, atât în repo-ul episodului, cât și în `siphon-core`.
- Corecturile se probează mai întâi pe segmente scurte (`preview-segments`, pe CPU). Randarea completă vine după aprobare.
- Task-urile lungi rulează în fundal, iar rezultatul se verifică cu o verificare programată, nu cu așteptare în chat.
- **Nimic „de probă” pe Hugging Face** sau pe alt serviciu cu cotă sau plată. Costul se spune proprietarului înainte de orice generare.
- La final:
  - loudness la -14 LUFS, cu vârful sub -1,5 dBFS, verificat cu `ffmpeg ebur128`;
  - cadrele modificate verificate vizual;
  - faptele care se pot schimba, reverificate în ziua publicării.
- 4K se randează doar la final, cu o zi înainte de publicare. În Release-ul cu 4K se pun și thumbnail-ul, descrierea (sub 5.000 de caractere, cu capitole și surse), subtitrările SRT și fișa de upload YouTube (model: `siphon-ep003` › `episodes/publish/003-youtube.md`).
- Proprietarul publică ep. 002 **luni, 30 noiembrie 2026**, pe la 18:00–19:00 ora României.
