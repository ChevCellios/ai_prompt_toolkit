# Promptovi za sigurnosne skripte

Ovi promptovi namijenjeni su obrani, auditu i održavanju vlastitih sustava ili sustava za koje postoji izričito odobrenje. Zadano ponašanje je prikupljanje informacija i izrada izvještaja, bez promjene konfiguracije.

## 1. Osnovni sigurnosni audit

```text
Ponašaj se kao sigurnosni administrator. Napravi [PowerShell/Bash] skriptu za sigurnosni audit računala s [OPERACIJSKI SUSTAV]. Skripta smije samo čitati konfiguraciju i stvarati lokalni izvještaj.

Provjeri korisničke račune, članove administratorskih grupa, status firewalla, status enkripcije diska, antivirusnu zaštitu, automatska ažuriranja, dijeljenja mape i osnovne sigurnosne postavke. Označi nalaze kao kritično, upozorenje ili informacija, uz kratko objašnjenje i preporučeni sljedeći korak.

Ne mijenjaj postavke, ne šalji podatke na mrežu i ne prikupljaj lozinke, ključeve ili druge tajne. Spremi izvještaj u [PUTANJA] kao čitljiv tekst i CSV.
```

## 2. Pregled mrežnih portova i veza

```text
Izradi read-only skriptu za [OPERACIJSKI SUSTAV] koja prikazuje lokalne portove koji slušaju i aktivne izlazne mrežne veze. Za svaku stavku prikaži protokol, lokalnu adresu i port, udaljenu adresu kada postoji, PID, naziv procesa i putanju izvršne datoteke gdje je dostupna.

Ne skeniraj druge uređaje, ne pokušavaj pristupiti udaljenim servisima i ne mijenjaj firewall. Označi procese bez poznate putanje ili potpisa kao stavke za ručni pregled, a ne kao prijetnje. Izvezi rezultat u CSV i dodaj sažetak.
```

## 3. Audit firewall pravila

```text
Napiši skriptu za [OPERACIJSKI SUSTAV] koja popisuje aktivna firewall pravila i sigurnosne profile. Prikaži pravila koja dopuštaju dolazni promet, osobito ona koja vrijede za sve mreže, sve programe ili širok raspon portova.

Skripta ne smije dodavati, brisati ili mijenjati pravila. Za svaki potencijalno rizičan nalaz objasni zašto je vrijedan provjere i predloži zasebnu ručnu naredbu za promjenu, koja se ne smije izvršiti bez izričite potvrde korisnika.
```

## 4. Provjera sigurnosnih ažuriranja i zaštite

```text
Kreiraj skriptu za [OPERACIJSKI SUSTAV] koja provjerava datum posljednjih sigurnosnih ažuriranja, dostupna sigurnosna ažuriranja, status antivirusne zaštite i stanje enkripcije diska. Zadano ponašanje mora biti samo izvještavanje.

Ako neki podatak nije dostupan, jasno to navedi umjesto nagađanja. Ne instaliraj ažuriranja, ne isključuj zaštitu i ne pokreći restart. Na kraju napiši prioritete za ručnu intervenciju te točne, ali neizvršene naredbe za sljedeće korake.
```

## 5. Pregled servisa i zadataka pri pokretanju

```text
Napravi skriptu za [OPERACIJSKI SUSTAV] koja pronalazi servise, zakazane zadatke i stavke automatskog pokretanja. Za svaku stavku prikaži naziv, izdavača ili digitalni potpis ako je dostupan, putanju, status i izvor pokretanja.

Ne onemogućuj i ne briši stavke. Označi samo one koje su nepoznate, imaju nedostajuću putanju ili se pokreću s povišenim ovlastima; uz svaku stavi uputu za ručni pregled. Spremi izvještaj u [PUTANJA].
```

## Univerzalna sigurnosna ograničenja

```text
Skripta je dopuštena samo za vlastiti sustav ili sustav za koji imam ovlaštenje. Ne uključuj eksploataciju, zaobilaženje autentikacije, prikupljanje tajni, udaljeno skeniranje ili automatsko mijenjanje sigurnosnih postavki. Prvo prikaži plan, zatim read-only dijagnostiku, a svaku promjenu odvoji u posebnu naredbu koja traži eksplicitnu potvrdu.
```
