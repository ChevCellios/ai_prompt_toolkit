# Promptovi za skripte za poboljšavanje sustava

Ovi predlošci služe za Windows, Linux i macOS administrativne zadatke. Prije
pokretanja bilo koje skripte pregledaj njezin sadržaj, koristi najmanje potrebne
ovlasti i napravi sigurnosnu kopiju važnih podataka.

## 1. Sigurna dijagnostika sustava

```text
Ponašaj se kao iskusan sistemski administrator. Napravi [PowerShell/Bash]
skriptu samo za čitanje koja dijagnosticira stanje [Windowsa/Linuxa/macOS-a].

Skripta treba provjeriti:
- verziju OS-a i vrijeme rada sustava
- korištenje CPU-a, memorije i diska
- slobodan prostor na diskovima
- procese s najvećom potrošnjom resursa
- osnovno stanje mreže
- nedavne greške iz [Event Viewera/journald-a]

Zahtjevi:
- ne smije mijenjati postavke, instalirati pakete ni brisati datoteke
- svaka provjera mora biti otporna na grešku i dati razumljivu poruku
- rezultat spremi u datoteku s vremenskom oznakom u [PUTANJA]
- na kraju napiši kratak sažetak nalaza i prijedloge bez automatske primjene

Prije koda ukratko objasni što svaka provjera radi. Zatim isporuči kompletnu,
komentiranu skriptu i naredbu za pokretanje.
```

## 2. Čišćenje privremenih datoteka s pregledom promjena

```text
Napiši sigurnu [PowerShell/Bash] skriptu za oslobađanje prostora na
[Windowsu/Linuxu/macOS-u]. Ciljaj samo privremene datoteke korisnika i sustava
koje je sigurno ukloniti.

Obavezno:
- prvo izračunaj i prikaži što bi se obrisalo, uključujući veličinu po lokaciji
- koristi dry-run kao zadani način rada
- stvarno brisanje omogući isključivo uz parametar --apply i interaktivnu potvrdu
- nikada ne diraj korisničke dokumente, direktorije aplikacija, aktivne logove,
  koš za smeće ni lokacije izvan unaprijed definirane dopuštene liste
- preskoči zaključane datoteke i evidentiraj svako preskakanje ili grešku
- omogući --min-age-days [BROJ] radi zaštite novijih datoteka

Prije pisanja koda navedi dopuštene putanje za taj operacijski sustav i sve
pretpostavke. Nakon koda dodaj primjere za dry-run i za potvrđeno izvršavanje.
```

## 3. Analiza programa koji se pokreću pri prijavi

```text
Izradi skriptu za [OPERACIJSKI SUSTAV] koja popisuje stavke automatskog
pokretanja i procjenjuje njihov utjecaj na vrijeme podizanja sustava.

Prikupi naziv, putanju, izdavača/potpis kada je dostupan, izvor pokretanja,
status i procjenu rizika. Izvore prikaži odvojeno: [Registry/Startup folder/
Scheduled Tasks/systemd/launchd].

Skripta u ovoj verziji ne smije ništa onemogućiti ili mijenjati. Izvezi rezultate
u CSV i čitljiv tekstualni izvještaj. Za svaku sumnjivu ili nepotrebnu stavku
navedi preporuku, ali nemoj donositi konačnu odluku bez korisnikove potvrde.
```

## 4. Provjera i optimizacija diska

```text
Napiši [PowerShell/Bash] alat za zdravlje i optimizaciju diskova na
[OPERACIJSKI SUSTAV]. Najprije izvedi samo dijagnostiku: slobodan prostor,
SMART stanje gdje je dostupno, vrstu diska (SSD/HDD), greške datotečnog sustava
i fragmentaciju kada je relevantna.

Zatim prikaži plan preporučenih radnji. Destruktivne ili dugotrajne akcije
(popravak datotečnog sustava, defragmentacija, trim, promjena particija) ne smiju
se pokrenuti automatski. Za svaku napiši posljedice, procijenjeno trajanje,
preduvjete i točnu naredbu koju korisnik mora zasebno potvrditi.

Skripta mora imati zapisnik, provjeru administratorskih ovlasti i jasan izlazni
kôd kod greške.
```

## 5. Pregled sigurnosnih ažuriranja

```text
Kreiraj skriptu za [OPERACIJSKI SUSTAV] koja provjerava dostupna sigurnosna
ažuriranja, verzije ključnih paketa i datum posljednje uspješne nadogradnje.

Zadano ponašanje je isključivo izvještavanje. Ne instaliraj ažuriranja, ne
pokreći servis ponovo i ne restartaj računalo. Izradi sažetak s kategorijama:
kritično, sigurnosno, preporučeno i opcionalno.

Dodaj opcionalni parametar --install-security, ali prije bilo kakve instalacije
zahtijevaj eksplicitnu interaktivnu potvrdu, provjeri dostupni prostor, zabilježi
stanje i jasno reci je li potreban restart. Nemoj pokušavati zaobići pravila
organizacije, MDM ili administrativne dozvole.
```

## 6. Optimizacija mrežne dijagnostike

```text
Napiši skriptu za dijagnostiku mrežnih poteškoća na [OPERACIJSKI SUSTAV].
Provjeri IP konfiguraciju, DNS poslužitelje, zadani pristupnik, latenciju prema
[ODREDIŠTE], DNS rezoluciju, gubitak paketa i aktivne mrežne adaptere.

Skripta ne smije mijenjati DNS, resetirati mrežu ni prekidati veze. Rezultat
prikaži kao tablicu s vrijednostima, pragovima i mogućim uzrocima. Ako predlažeš
popravak, ponudi ga samo kao zasebnu ručnu naredbu s objašnjenjem rizika.
```

## Univerzalni dodatak svakom promptu

Kada želiš stroža pravila, na kraj bilo kojeg predloška dodaj:

```text
Prije generiranja skripte postavi najviše tri nužna pitanja ako nedostaju
operacijski sustav, ciljana putanja ili željeni opseg. Ako informacije nisu
nužne, napravi razumnu pretpostavku i jasno je označi. Ne koristi naredbe koje
nepovratno brišu podatke, ne mijenjaj sigurnosne postavke i ne šalji podatke na
mrežu. Razdvoji analizu, dry-run i primjenu promjena u zasebne korake.
```
