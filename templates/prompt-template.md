# [Naziv prompta]

> Jedna rečenica koja opisuje problem koji prompt rješava i kome je namijenjen.

## Cilj

Opiši konkretan rezultat koji model treba proizvesti. Koristi provjerljive glagole poput *izradi*, *usporedi*, *izdvoji* ili *ocijeni*.

## Kontekst

- publika ili korisnik: `[PUBLIKA]`
- domena i pozadina: `[KONTEKST]`
- dostupni izvori ili podaci: `[IZVORI]`
- važne pretpostavke: `[PRETPOSTAVKE]`

## Ulazne varijable

| Varijabla | Obavezna | Opis | Primjer |
|---|---:|---|---|
| `[GLAVNI_ULAZ]` | da | Materijal ili zadatak koji treba obraditi | `Opis proizvoda` |
| `[PUBLIKA]` | da | Ciljani čitatelj ili korisnik | `Netehnički voditelj` |
| `[FORMAT]` | ne | Željeni format rezultata | `Markdown tablica` |
| `[OGRANIČENJE]` | ne | Duljina, rok ili drugo ograničenje | `Najviše 500 riječi` |

## Upute modelu

1. Provjeri jesu li dostupne informacije dovoljne za izvršenje zadatka.
2. Ako nedostaje nužna informacija, postavi najviše tri kratka pitanja. Ako nije nužna, jasno navedi razumnu pretpostavku i nastavi.
3. Izvrši zadatak te prikaži traženi rezultat i sažeto obrazloženje odluka kada je ono korisno.
4. Razlikuj činjenice iz ulaza od pretpostavki i preporuka.
5. Prije predaje provjeri rezultat prema kriterijima uspjeha.

## Ograničenja

- Ne izmišljaj činjenice, izvore, citate, rezultate testova ni podatke koji nisu dostupni u ulazu.
- Kada tvrdnju nije moguće provjeriti, označi je kao nepotvrđenu ili zatraži izvor.
- Ne izlazi iz opsega zadanog cilja.
- Poštuj `[OGRANIČENJE]` i sva sigurnosna ili pravna pravila relevantna za domenu.

## Format izlaza

```markdown
## Rezultat
[GLAVNI REZULTAT]

## Pretpostavke
- [PRETPOSTAVKA ILI "Nema"]

## Otvorena pitanja
- [PITANJE ILI "Nema"]
```

## Primjeri

### Primjer 1 — uobičajeni ulaz

**Ulaz:** `[PRIMJER ULAZA]`

**Očekivana svojstva izlaza:** `[SVOJSTVO 1]`, `[SVOJSTVO 2]`

### Primjer 2 — nepotpun ili rubni ulaz

**Ulaz:** `[NEPOTPUN ILI RUBNI ULAZ]`

**Očekivana svojstva izlaza:** prepoznaje što nedostaje, ne izmišlja podatke i postavlja pitanje samo ako bez odgovora nije moguće sigurno nastaviti.

## Kriteriji uspjeha

- [ ] Rezultat izravno ostvaruje cilj.
- [ ] Sve obavezne ulazne varijable korištene su ispravno.
- [ ] Izlaz poštuje zadani format i ograničenja.
- [ ] Činjenice, pretpostavke i preporuke jasno su razdvojene.
- [ ] Nema izmišljenih izvora, podataka ili zaključaka.
- [ ] Rezultat je dovoljno jasan da ga ciljana publika može odmah upotrijebiti.

## Metapodaci

- kategorija: `[KATEGORIJA]`
- verzija: `0.1.0`
- autor/održavatelj: `[IME ILI TIM]`
- zadnje testiranje: `[GGGG-MM-DD]`
- podržani modeli: `[MODELI ILI "model-agnostic"]`
