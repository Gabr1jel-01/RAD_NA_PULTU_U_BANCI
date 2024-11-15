# RAD_NA_PULTU_U_BANCI

## Pregled projekta

- [Cilj]()
- [Funkcionalnosti](#objašnjenje-funkcionalnosti)
  - [Izbornik](#izbornik)
  - [Otvaranje računa tvrtke](#objašnjenje-funkcionalnosti)
    - Naziv
    - Adresa
    - OIB
    - Ime vlasnika
    - Status
    - Početni kapital
  - [Prikaz stanja računa]()
  - [Prikaz prometa po računu]()
    - Uplate
    - Isplate
  - [Polog novca na račun]()
    - Mogućnost uplate u dvije valute
  - [Podizanje novca sa računa]()
  - [Izlaz iz programa]()

## Cilj

Rad na pultu u banci je bio zadatak od profesora sa Algebre koji mi je držao predavanje za Python Developera.
Ovo je bio prvi veći program koji sam morao napisati te mi je izrazito drag iz razloga što mi se sada čini jednostavnim no tada kada sam ga radio i nije bilo tako. Pošto je ovo prvi veći program bilo je izazovno voditi računa o puno stvari odjednom te sam ponosan što sam uspio napraviti da sve radi kako je i bilo zamišljeno. Isto tako kada se pokrene ovaj program sve se radi preko terminala što mu daje "hakerski štih" 😊.

## Izbornik

Nakon pokretanja aplikacije, u terminalu će se prikazati glavni izbornik koji sadrži:

- Naziv aplikacije
- Mogućnost:
  - Otvaranje računa tvrtke
  - Prikaza stanja računa
  - Prikaza prometa po računu
  - Pologa novca na račun
  - Podizanja novca sa računa
  - Izlaska iz aplikacije

## Objašnjenje funkcionalnosti

- Otvaranje računa tvrtke:

  - Naziv (ovdje se unosi puni naziv tvrtke)
  - Adresa (ovdje se unosi puna adresa tvrtke)
  - OIB (ovdje se unosi OIB tvrtke te mora sadržavati 11 znamenaka inače će korisnik biti upozoren na nevažeči OIB te će ga se opet pitati da unese OIB)
  - Vlasnik (ovdje se unosi ime i prezime vlasnika tvrtke)
  - Status (ovdje se unosi status)
  - Temeljni kapital (ovdje se unosi temeljni kapital za otvaranje tvrtke)

> [!NOTE]
> Nakon što je korisnik uspješno otvorio račun automatski mu je dodijeljen IBAN koji mu je isto tako i prikazan u terminalu te se kapital za otvaranje tvrtke ne dodjeljuje kao sredstvo na računu!

- Prikaz stanja računa:

  - Ukoliko prije nije položen nikakav iznos, korisnika program vraća na glavni izbornik
  - Ukoliko je korisnik prije uplatio novac na račun prikazuje mu se iznos u odgovarajućoj valuti uplate

* Prikaz prometa po računu:

  - Ukoliko prije nije položen ili podignut nikakav novac sa računa korisnika program vraća na glavni izbornik
  - Svaka uplata i isplata se prikazuje odabirom ove funkcije

* Polog novca na račun

  - Prilikom svake uplate na račun program će korisnika pitati u kojoj valuti želi uplatiti novac te koji iznos

* Podizanje novca sa računa

  - Korisniku će biti prikazan iznos novca na računu te će mu biti ponuđena opcija podizanja novca
  - Nakon podizanja novca korisniku će biti prikazan preostali iznos na računu

* Izlaz iz aplikacije
  - Ova funkcija gasi program
