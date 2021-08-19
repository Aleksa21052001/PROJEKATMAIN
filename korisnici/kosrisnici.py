from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike

def provera_korisnika():

    pass

def registracija_novih_korisnika():


    korisnicko_ime = input('unesite korisnicko ime novog korisnika: ')
    lozinka = input('unesite lozinku: ')
    ime = input('unesite ime novog korisnika: ')
    prezime = input('unesite prezime novog korisnika: ')
    tip_korisnika = input('tip novof korisnika je: ')

    novi_korisnik = {"korisnicko_ime":korisnicko_ime, "lozinka":lozinka, "ime":ime, "prezime": prezime , "tip_korisnika":tip_korisnika}

    sacuvaj_korisnike(novi_korisnik)


def prijava(): #proverava da li postoji korisnik, treba nam f-ja koja ucitava i koja proverava korisnike

    korisnici = ucitaj_korisnike()

    korisnicko_ime = input('unesite korisnicko ime: ')
    lozinka = input('unesite lozinku: ')


    for korisnik in korisnici: #namesti da tri puta moze da pogadja
        if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik #vratimo jer ce nam trebati da znamo ko je korisnik, koja mu je uloga koji meni da mu prikazemo

    print('"pogresno korisnicko ime ili lozinka, pokusajte ponovo"')
    return None
