# Početni katalog promptova

Ovih 20 početnih ideja raspoređeno je u šest kategorija. Pri implementaciji svaki prompt treba izraditi prema [standardnom predlošku](../templates/prompt-template.md) i dopuniti testnim slučajevima.

## Pisanje

1. **Urednik jasnoće** — Preoblikuje tekst za određenu publiku uz očuvanje značenja i tona. Primjer: „Preuredi ovaj tehnički opis za upravu; najviše 250 riječi, bez žargona: `[TEKST]`.”
2. **Autor strukturiranog nacrta** — Pretvara temu, publiku i cilj u logičan nacrt članka ili dokumenta. Primjer: „Izradi nacrt vodiča o sigurnim lozinkama za male tvrtke.”
3. **Prilagodba tona** — Mijenja ton teksta bez dodavanja novih činjenica. Primjer: „Prepiši ovu poruku u smirenom i profesionalnom tonu: `[PORUKA]`.”
4. **Sažetak za donositelje odluka** — Izdvaja odluke, rizike i sljedeće korake iz duljeg materijala. Primjer: „Sažmi zapisnik u pet točaka: odluke, vlasnici, rokovi i rizici.”

## Programiranje

5. **Specifikacija prije implementacije** — Pretvara nejasan zahtjev u kriterije prihvaćanja, rubne slučajeve i plan. Primjer: „Razradi zahtjev ‘dodaj prijavu korisnika’ za Python web-aplikaciju.”
6. **Recenzent koda utemeljen na dokazima** — Pronalazi konkretne bugove i rizike bez izmišljanja problema. Primjer: „Pregledaj ovaj diff; za svaki nalaz navedi redak, posljedicu i najmanji popravak: `[DIFF]`.”
7. **Sustavni dijagnostičar grešaka** — Rangira hipoteze i predlaže najmanji test koji ih razlikuje. Primjer: „API povremeno vraća 502; koristi ove logove i ne predlaži popravak prije potvrde uzroka: `[LOGOVI]`.”
8. **Generator ciljanih testova** — Predlaže normalne, rubne i negativne testove iz ponašanja sustava. Primjer: „Napiši testne slučajeve za funkciju validacije datuma: `[KOD]`.”

## Analiza

9. **Analitičar odluka** — Uspoređuje opcije prema eksplicitnim kriterijima i težinama. Primjer: „Usporedi tri CRM rješenja prema cijeni, integracijama i jednostavnosti migracije; navedi osjetljivost preporuke na težine.”
10. **Izdvajanje tvrdnji i dokaza** — Razdvaja tvrdnje, dokaze, pretpostavke i praznine u argumentu. Primjer: „Analiziraj prijedlog i za svaku ključnu tvrdnju navedi potporu ili oznaku ‘bez dokaza’: `[TEKST]`.”
11. **Analiza uzroka problema** — Organizira simptome, moguće uzroke i provjere bez brzog zaključivanja. Primjer: „Prodaja je pala 12 %. Složi hipoteze i podatke potrebne za njihovu provjeru.”
12. **Evaluator odgovora modela** — Ocjenjuje AI odgovor po dosljednoj rubrici i predlaže konkretan popravak. Primjer: „Ocijeni odgovor od 1 do 5 za točnost, relevantnost, potpunost, jasnoću, format i sigurnost: `[ODGOVOR]`.”

## Istraživanje

13. **Plan istraživanja** — Pretvara pitanje u podupite, kriterije izvora i postupak provjere. Primjer: „Izradi plan istraživanja utjecaja četverodnevnog radnog tjedna na produktivnost, s kriterijima uključivanja izvora.”
14. **Sintetizator izvora** — Uspoređuje dostavljene izvore, bilježi slaganja, razlike i nesigurnosti. Primjer: „Sintetiziraj ova tri izvora; svaku tvrdnju poveži s izvorom: `[IZVORI]`.”
15. **Provjera činjenica** — Rastavlja tekst na provjerljive tvrdnje i određuje što treba potvrditi. Primjer: „Izdvoji provjerljive tvrdnje iz teksta i za svaku predloži primarni izvor: `[TEKST]`.”

## Produktivnost

16. **Pretvarač cilja u akcijski plan** — Razlaže cilj na male korake, vlasnike, rokove i dokaze dovršetka. Primjer: „Pretvori cilj ‘objaviti beta verziju do 30. rujna’ u tjedni plan.”
17. **Sažetak sastanka u obveze** — Iz bilješki izdvaja odluke, zadatke, odgovorne osobe i otvorena pitanja. Primjer: „Pretvori bilješke u tablicu obveza; ne nagađaj vlasnika ili rok ako nije naveden: `[BILJEŠKE]`.”
18. **Tjedni pregled prioriteta** — Pomaže odabrati realan fokus prema važnosti, hitnosti i kapacitetu. Primjer: „Od ovih 12 zadataka složi izvediv plan za 20 radnih sati i objasni što odgađaš: `[ZADACI]`.”

## Kreativni rad

19. **Generator koncepata s ograničenjima** — Stvara raznolike ideje koje zadovoljavaju zadanu publiku, ton i budžet. Primjer: „Predloži 10 koncepata kampanje za lokalnu knjižnicu, bez plaćenih oglasa i s budžetom od 300 EUR.”
20. **Kritičar i razvijač ideje** — Prepoznaje jakosti i slabe točke koncepta te predlaže različite iteracije. Primjer: „Procijeni ideju za kratku priču i predloži tri završetka koji ne ovise o neočekivanom snu: `[IDEJA]`.”

## Predloženi redoslijed implementacije

1. Evaluator odgovora modela — uspostavlja zajedničku mjeru kvalitete.
2. Generator ciljanih testova — omogućuje ponovljivu provjeru drugih promptova.
3. Urednik jasnoće — jednostavan je referentni primjer za cijeli predložak.
4. Sustavni dijagnostičar grešaka — provjerava ponašanje na nepotpunim ulazima.
