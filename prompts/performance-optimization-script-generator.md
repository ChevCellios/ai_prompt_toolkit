# Generator skripti za poboljšanje performansi računala

Ovaj prompt služi za izradu **sigurnih i provjerljivih** PowerShell ili Bash skripti za dijagnostiku i postupno poboljšanje performansi računala. Namijenjen je Windowsu, Linuxu i macOS-u.

> Prije pokretanja svake generirane skripte pročitaj kôd, zatvori važne aplikacije i napravi sigurnosnu kopiju važnih podataka. Optimizacija ne smije uključivati isključivanje zaštite sustava, brisanje korisničkih podataka ili preuzimanje neprovjerenih alata.

## Glavni prompt

Kopiraj sljedeći tekst u AI alat i zamijeni vrijednosti u uglatim zagradama.

```text
Ponašaj se kao iskusan sistemski administrator i stručnjak za performanse.
Izradi sigurnu, komentiranu [PowerShell/Bash] skriptu za [Windows 10/11, Linux distribuciju ili macOS] koja pomaže poboljšati performanse računala.

Kontekst:
- simptomi: [npr. sporo pokretanje, malo slobodnog prostora, visoka potrošnja CPU-a]
- prioritet: [brzina / slobodan prostor / vrijeme pokretanja / odziv aplikacija]
- profil sigurnosti: [samo dijagnostika / konzervativne promjene / promjene uz potvrdu]
- izlazni direktorij za izvještaj: [PUTANJA]

Skripta mora raditi u tri jasno odvojene faze.

1. DIJAGNOSTIKA — uvijek se izvršava i ne smije mijenjati sustav
   - prikaži verziju sustava, vrijeme rada i dostupne resurse
   - izmjeri korištenje CPU-a, memorije, diska i slobodan prostor
   - popiši procese s najvećom potrošnjom CPU-a, memorije i diska kada je dostupno
   - provjeri programe/stavke automatskog pokretanja bez njihova onemogućivanja
   - odredi vrstu pogona (SSD/HDD), gdje je moguće, i predloži odgovarajuće radnje
   - zabilježi sažetak i sve greške u izvještaj s vremenskom oznakom

2. PLAN — prikaži radnje koje bi skripta mogla napraviti
   - svaku radnju prikaži s razlogom, očekivanim učinkom, rizikom i preduvjetima
   - uključi samo radnje primjerene operacijskom sustavu, primjerice čišćenje unaprijed poznatih privremenih datoteka, siguran trim SSD-a ili preporuku za pregled pokretačkih stavki
   - za svaku stavku jasno navedi hoće li promijeniti sustav
   - ne obećavaj mjerljivo ubrzanje ako ga nije moguće dokazati

3. PRIMJENA — dopuštena samo uz parametar --apply i potvrdu korisnika
   - zadani način rada mora biti --dry-run; bez parametra ne mijenjaj ništa
   - prije svake promjene prikaži točan opseg, procijenjeni učinak i zatraži interaktivnu potvrdu
   - prihvati --skip-confirmation samo ako je korisnik prethodno odabrao profil “promjene uz potvrdu” i ako je skripta pokrenuta interaktivno
   - evidentiraj svaku uspješnu, preskočenu i neuspješnu radnju

Sigurnosna pravila:
- nikada ne briši korisničke dokumente, fotografije, preuzimanja, direktorije aplikacija, koš za smeće, aktivne logove, ključeve registra ni sistemske datoteke
- ne isključuj antivirus, firewall, UAC, automatska ažuriranja, enkripciju, System Restore, swap/pagefile ili sigurnosne servise
- ne prekidaj procese, ne onemogućuj startup stavke i ne deinstaliraj programe bez zasebnog parametra te nove potvrde za svaku stavku
- ne preuzimaj ništa s interneta i ne šalji telemetriju ili podatke izvan računala
- provjeri administratorske ovlasti prije radnji koje ih zahtijevaju; ako nisu dostupne, preskoči radnju s jasnom porukom umjesto da skripta neuspješno stane
- koristi dopuštenu listu putanja za čišćenje i preskoči zaključane datoteke
- izbjegavaj destruktivne naredbe; ne koristi rekurzivno brisanje nad varijablama ili širokim putanjama bez prethodne provjere i eksplicitne dozvole

Tehnički zahtjevi:
- koristi funkcije, jasne nazive, komentare i kodove izlaza
- skripta mora podnijeti nedostupne naredbe, dozvole i zaključane datoteke
- na početku prikaži kratki sažetak pretpostavki i dostupnih parametara
- izlaz spremi u čitljiv tekstualni izvještaj u [PUTANJA] te ispiši njegovu lokaciju
- nakon koda dodaj: upute za pokretanje, primjer dry-run pokretanja, primjer potvrđene primjene i kratko objašnjenje kako vratiti svaku promjenu kad je moguće

Ako nedostaje samo jedan detalj, pretpostavi Windows 11 i PowerShell 7 te tu pretpostavku jasno označi. Postavi najviše tri pitanja samo ako bez njih nije moguće sigurno odrediti operacijski sustav, ciljani opseg ili izlaznu putanju.
```

## Brzi primjeri

### Windows 11: sigurno oslobađanje prostora

U glavnom promptu postavi:

```text
operacijski sustav: Windows 11
simptomi: malo slobodnog prostora i sporiji rad nakon duljeg korištenja
prioritet: slobodan prostor i odziv sustava
profil sigurnosti: konzervativne promjene
izlazni direktorij za izvještaj: C:\Users\Public\Documents\PerformanceReports
```

### Linux: analiza sporog rada

```text
operacijski sustav: Ubuntu 24.04
simptomi: ventilatori se često pojačavaju i aplikacije kasne
prioritet: pronaći uzrok visoke potrošnje CPU-a i memorije
profil sigurnosti: samo dijagnostika
izlazni direktorij za izvještaj: ~/performance-reports
```

## Kontrolna lista prije pokretanja

- Pregledaj popis planiranih radnji prije korištenja `--apply`.
- Pokreni dry-run i provjeri generirani izvještaj.
- Zatvori aplikacije prije čišćenja privremenih datoteka.
- Ne pokreći radnje nad diskom ako postoje znakovi kvara ili nema sigurnosne kopije.
- Ako se računalo i dalje usporava, prvo analiziraj izvještaj — uzrok može biti neispravan disk, manjak memorije, zlonamjerni softver ili određena aplikacija.
