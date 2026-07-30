# Promptovi za skripte za automatizaciju

Ovi predlošci služe za ponavljajuće administrativne i organizacijske zadatke. Svaka automatizacija treba prvo jasno prikazati što će napraviti, voditi lokalni zapisnik i odvojiti pregled od primjene promjena.

## 1. Automatizacija organizacije datoteka

```text
Napiši sigurnu [PowerShell/Bash/Python] skriptu za [OPERACIJSKI SUSTAV] koja organizira datoteke iz [IZVORNA MAPA] u [ODREDIŠNA MAPA] prema pravilima: [PRAVILA, npr. ekstenzija, datum ili prefiks naziva].

Zadano radi u dry-run načinu: prikaži svaku planiranu radnju, broj datoteka i moguće kolizije naziva, ali ne mijenjaj ništa. Stvarno premještanje omogući samo s parametrom --apply i interaktivnom potvrdom.

Ne briši datoteke, ne prepisuj postojeće datoteke i ne izlazi iz navedenih mapa. Za kolizije izradi jedinstven naziv ili ih preskoči i evidentiraj. Spremi lokalni CSV i tekstualni zapisnik s vremenom, izvornom putanjom, odredištem i statusom. Prije koda objasni pretpostavke, a nakon njega dodaj primjere za dry-run i --apply.
```

## 2. Arhiviranje starih datoteka

```text
Izradi [PowerShell/Bash] skriptu koja pronalazi datoteke starije od [BROJ DANA] u [IZVORNA MAPA] i arhivira ih u [ARHIVSKA MAPA] kao [ZIP/TAR.GZ] datoteke.

Prije arhiviranja napravi dry-run izvještaj s popisom datoteka, ukupnom veličinom i nazivom planirane arhive. Stvaranje arhive zahtijeva --apply i potvrdu korisnika. Nakon stvaranja provjeri može li se arhiva pročitati i usporedi broj stavki.

Nemoj brisati izvornike, mijenjati dozvole ni slati arhivu na mrežu. Ako je ciljna arhiva već prisutna, nemoj je prepisati. Zapiši rezultat i sve greške u lokalni log.
```

## 3. Izvještaj iz CSV datoteka

```text
Napiši skriptu za obradu CSV datoteka u [ULAZNA MAPA]. Za svaki CSV provjeri strukturu stupaca, broj redaka, prazne vrijednosti, duplikate i osnovne statistike za brojčane stupce. Zatim izradi objedinjeni sažetak u [IZLAZNA MAPA].

Ulazne datoteke moraju ostati nepromijenjene. Ne šalji podatke izvan računala i ne uključuj pune vrijednosti osjetljivih stupaca u log; za [OSJETLJIVI STUPCI] prikaži samo broj zapisa ili maskirane primjere. Ako struktura datoteka nije usklađena, prijavi razliku i preskoči je umjesto da nagađa mapiranje.

Isporuči kompletnu komentiranu skriptu, opis izlaznih datoteka i primjer pokretanja.
```

## 4. Nadzor mape i obrada novih datoteka

```text
Kreiraj skriptu za [OPERACIJSKI SUSTAV] koja prati [ULAZNA MAPA] i, kada se pojavi nova datoteka tipa [EKSTENZIJE], provodi ovaj lokalni korak obrade: [RADNJA].

Prije obrade provjeri da je datoteka dovršila zapisivanje, da je unutar dopuštene mape i da ne prelazi [MAKSIMALNA VELIČINA]. Datoteke koje ne prođu provjeru samo evidentiraj i ostavi netaknute. Spriječi dvostruku obradu istog unosa.

Ne pokreći vanjske naredbe, ne šalji datoteke na mrežu i ne briši izvornike bez posebnog parametra --apply i eksplicitne potvrde. Uključi uredno zaustavljanje, lokalni log s vremenskim oznakama i upute za pokretanje u pozadini.
```

## 5. Planer ponavljajućeg zadatka

```text
Ponašaj se kao sistemski administrator i pripremi zadatak koji se izvršava [RASPORED, npr. svake nedjelje u 02:00] na [OPERACIJSKI SUSTAV]. Zadatak treba pokrenuti postojeću skriptu [PUTANJA DO SKRIPTE], spremiti standardni izlaz i greške u [PUTANJA DO LOGA] te jasno vratiti izlazni kôd.

Najprije prikaži točnu naredbu za ručno testiranje. Zatim prikaži naredbu ili konfiguraciju za [Task Scheduler/cron/systemd timer], ali je nemoj izvršiti. Objasni pod kojim korisnikom će se zadatak izvršavati, potrebne dozvole i kako ga zaustaviti ili ukloniti.

Nemoj spremati lozinke ili tajne u tekstualne datoteke. Ne konfiguriraj automatsko pokretanje bez izričite potvrde korisnika.
```

## Univerzalna sigurnosna ograničenja

```text
Najprije postavi najviše tri nužna pitanja ako nisu poznati operacijski sustav, izvorne i odredišne putanje ili pravila obrade. Zatim odvoji plan, dry-run i primjenu promjena. Ne briši ili prepisuj podatke, ne šalji ih na mrežu i ne stvaraj trajne rasporede bez zasebne, izričite potvrde korisnika.
```
