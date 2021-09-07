from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
from unos import *


ulogovani_korisnik = None

def zaglavlje():
    print()
    print('korisnicko_ime   |ime                |prezime                |tip_korisnika')
    print('-----------------|-------------------|-----------------------|-------------')


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

    print("\n1. sortiranje po imenu")
    print("2. sortiranje po prezimenu")
    print("3. sortiranje po tipu korisnika")

    opcija = unesi_ceo_broj(">>izaberite parametar sortiranja: ")

    sortirani_korisnici  = []
    if opcija == 1:
        sortirani_korisnici  = sortiraj_korisnika("ime")
        zaglavlje()
    elif opcija == 2:
        sortirani_korisnici = sortiraj_korisnika("prezime")
        zaglavlje()
    elif opcija == 3:
        sortirani_korisnici = sortiraj_korisnika("tip_korisnika")
        zaglavlje()
    else:
        print("Izabrali ste nepostojecu opciju")


    for korisnik in sortirani_korisnici:
        tabela_korisnika = korisnik["korisnicko_ime"].ljust(17) + "|" + korisnik["ime"].ljust(19) + "|" + korisnik["prezime"].ljust(23) + "|" + korisnik["tip_korisnika"]
        print(tabela_korisnika)


def provera_korisnika(korisnici , korisnicko_ime):

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return korisnik
    return None

def registracija_novih_korisnika():

    korisnici = ucitaj_korisnike()
    print()
    korisnicko_ime = unesi_neprazan_string('>>unesite korisnicko ime novog korisnika: ')

    if provera_korisnika(korisnici, korisnicko_ime) is None:
        lozinka = unesi_neprazan_string('>>unesite lozinku: ')
        ime = unesi_neprazan_string('>>unesite ime novog korisnika: ')
        prezime = unesi_neprazan_string('>>unesite prezime novog korisnika: ')

        print("\n'Ako zelite da napustite registraciju ukucajte: nazad'\n")

        while True:
            tip_korisnika = str(input('>>tip je (menadzer/prodavac): '))
            if tip_korisnika == "nazad":
                print("'registracija je prekinuta!'")
                return

            if tip_korisnika == "menadzer" or tip_korisnika == "prodavac":
                novi_korisnik = {"korisnicko_ime":korisnicko_ime, "lozinka":lozinka, "ime":ime, "prezime": prezime , "tip_korisnika":tip_korisnika}
                print('"korisnik je uspesno registrovan"')
                break

            print("'greska pri izboru tipa korisnika, pokusajte ponovo!'\n")

        korisnici.append(novi_korisnik)
        sacuvaj_korisnike(korisnici)
    else:
        print("Korisnik vec postoji!")

def prijava():   #proverava da li postoji korisnik, treba nam f-ja koja ucitava i koja proverava korisnike
    global ulogovani_korisnik
    korisnici = ucitaj_korisnike()

    i = 0
    while not i == 3:

        korisnicko_ime = input('>>unesite korisnicko ime: ')
        lozinka = input('>>unesite lozinku: ')

        for korisnik in korisnici:
            if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik['lozinka'] == lozinka:
                ulogovani_korisnik = korisnik
                return korisnik   #vratimo jer ce nam trebati da znamo ko je korisnik, koja mu je uloga koji meni da mu prikazemo

        if i != 2:
            print('"Pogrešno korisnčko ime ili lozinka"\n')

        i = i + 1

    print('"Previše puta ste pogrešili"')

    return None
