# Promptovi za dijagnostiku i poboljšanje mrežne veze

Predlošci su usmjereni na lokalno mjerenje i razumljive izvještaje. Promjene mrežne konfiguracije uvijek moraju biti zasebne, potvrđene radnje.

## 1. Test stabilnosti veze

```text
Napiši [PowerShell/Bash] skriptu za [OPERACIJSKI SUSTAV] koja tijekom [TRAJANJE] mjeri stabilnost internetske veze prema [ODREDIŠTA]. Bilježi latenciju, jitter, gubitak paketa, DNS vrijeme odziva i prekide veze.

Prikaži sažetak s prosjekom, minimumom, maksimumom i postotkom gubitka paketa. Spremi sirove rezultate i čitljiv izvještaj s vremenskom oznakom u [PUTANJA]. Skripta ne smije mijenjati DNS, resetirati adaptere ni prekidati aktivne veze.
```

## 2. DNS dijagnostika

```text
Izradi skriptu za [OPERACIJSKI SUSTAV] koja prikazuje trenutačno korištene DNS poslužitelje te mjeri vrijeme DNS rezolucije za [DOMENE]. Po želji usporedi odziv [DNS POSLUŽITELJ A] i [DNS POSLUŽITELJ B] samo upitima za javne domene.

Jasno odvoji činjenice od preporuka. Ne mijenjaj DNS postavke. Ako predlažeš promjenu DNS-a, prikaži je kao zasebnu naredbu, opiši kako vratiti staro stanje i zahtijevaj izričitu potvrdu prije generiranja naredbe za primjenu.
```

## 3. Wi-Fi kvaliteta signala

```text
Napiši skriptu za [Windows/Linux/macOS] koja prikuplja podatke o trenutačnoj Wi-Fi vezi: SSID, jačinu signala, band, kanal, brzinu veze, adapter i povijest kratkih prekida gdje je dostupna. Izmjeri signal više puta kroz [TRAJANJE].

Napravi izvještaj s praktičnim, nedestruktivnim preporukama, primjerice bolji položaj uređaja ili provjera zagušenosti kanala. Ne mijenjaj kanal, lozinku, profil mreže ni postavke rutera.
```

## 4. Procesi koji troše mrežni promet

```text
Kreiraj lokalnu skriptu za [OPERACIJSKI SUSTAV] koja kroz [TRAJANJE] bilježi procese s najvećim mrežnim prometom. Prikaži PID, proces, putanju gdje je dostupna, smjer prometa i procijenjenu količinu poslanih/primljenih podataka.

Ne prekidaj procese, ne blokiraj promet i ne šalji prikupljene informacije izvan računala. Izvezi sažetak u CSV, a za neočekivane procese predloži samo ručnu provjeru.
```

## 5. Izvještaj za mrežnu ili ISP podršku

```text
Izradi skriptu za [OPERACIJSKI SUSTAV] koja prikuplja neosjetljive podatke za prijavu problema s internetom: vrijeme testa, javno dostupna odredišta, ping, jitter, gubitak paketa, DNS rezoluciju, IP konfiguraciju uz maskiranje lokalnih privatnih detalja i status adaptera.

Stvori kratak tekstualni izvještaj spreman za slanje podršci. Nemoj automatski slati e-mail, objavljivati IP adrese ni uključivati Wi-Fi lozinke, MAC adrese ili druge identifikatore bez jasne korisnikove odluke.
```

## 6. Plan sigurnog popravka mreže

```text
Na temelju ovog izvještaja: [ZALIJEPI IZVJEŠTAJ], sastavi plan dijagnostike i popravka mrežne veze. Prvo navedi najmanje invazivne provjere, zatim moguće promjene poput obnove DHCP-a, brisanja DNS cachea ili reseta adaptera.

Za svaku promjenu navedi učinak, mogući prekid veze, način vraćanja starog stanja i točnu naredbu. Ne izvršavaj promjene i ne predlaži reset mreže kao prvi korak. Stani nakon plana i zatraži potvrdu za svaku pojedinu promjenu.
```
