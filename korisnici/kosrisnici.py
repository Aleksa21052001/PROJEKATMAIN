from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike

def sortiraj_korisnika(kljuc):
    korisnici = ucitaj_korisnike()

    for i in range(len(korisnici)):
        for j in range(len(korisnici)):
            if korisnici[i][kljuc] < korisnici[j][kljuc]:
                temp = korisnici[i]
                korisnici[i] = korisnici[j]
                korisnici[j] = temp

    kopija_korisnika = korisnici
    korisnici_bez_lozinke = []

    for korisnik in kopija_korisnika:
        korisnik.pop("lozinka")
        korisnici_bez_lozinke.append(korisnik)

    return korisnici_bez_lozinke


def prikaz_svih_korisnika():

    print("1. sortiranje po imenu")
    print("2. sortiranje po prezimenu")
    print("3. sortiranje po tipu korisnika")

    opcija = int(input("izaberite parametar sortiranja: "))

    sortirani_korisnici  = []

    if opcija == 1:
        sortirani_korisnici  = sortiraj_korisnika("ime")
    elif opcija ==2:
        sortirani_korisnici = sortiraj_korisnika("prezime")
    elif opcija ==3:
        sortirani_korisnici = sortiraj_korisnika("tip_korisnika")
    else:
        print("Izabrali ste nepostojecu opciju")

    for korisnik in sortirani_korisnici:
        print(korisnik)

def provera_korisnika():

    pass

def registracija_novih_korisnika():   #ne doda ih u listu i kako spreciti unosenje sa vec postojecim korisnickim imenom"""

    korisnici = ucitaj_korisnike()

    korisnicko_ime = input('unesite korisnicko ime novog korisnika: ')
    lozinka = input('unesite lozinku: ')
    ime = input('unesite ime novog korisnika: ')
    prezime = input('unesite prezime novog korisnika: ')
    tip_korisnika = input('tip novof korisnika je: ')

    novi_korisnik = {"korisnicko_ime":korisnicko_ime, "lozinka":lozinka, "ime":ime, "prezime": prezime , "tip_korisnika":tip_korisnika}

    korisnici.append(novi_korisnik)

    sacuvaj_korisnike(korisnici)


def prijava(): #proverava da li postoji korisnik, treba nam f-ja koja ucitava i koja proverava korisnike

    korisnici = ucitaj_korisnike()

    korisnicko_ime = input('unesite korisnicko ime: ')
    lozinka = input('unesite lozinku: ')


    for korisnik in korisnici: #namesti da tri puta moze da pogadja
        if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik #vratimo jer ce nam trebati da znamo ko je korisnik, koja mu je uloga koji meni da mu prikazemo

    print('"pogresno korisnicko ime ili lozinka, pokusajte ponovo"')
    return None
