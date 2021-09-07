from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from datetime import datetime
from unos import *


def prikazi_tabelu(akcije):

    print("\nAKCIJE")
    print("------")
    for akcija in akcije:
        if akcija["datum"] >= datetime.now():

            print("Šifra akcije:", str(akcija["sifra"]))
            print("Akcija vazi do:", akcija["datum"].strftime("%d-%m-%Y"))

            for knjiga, cena in zip(akcija["knjige"], akcija["cene"]):
                print("Knjiga na akciji: " + knjiga["naslov"] + " | " + "Stara cena:" + str(knjiga["cena"]) + " | " + "Nova cena:" + str(cena))
            print()
    print("-----------------------------")


def pretrazi_akcije_broj(akcije, kljuc, vrednost):

    nove_akcije = []

    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            nove_akcije.append(akcija)

    return nove_akcije

def pretrazi_akcije_string(akcije, kljuc, vrednost):

    nove_akcije = []
    for akcija in akcije:
        for knjiga in akcija["knjige"]:
            if vrednost.lower() in knjiga[kljuc].lower():
                nove_akcije.append(akcija)

    return nove_akcije

def pretraga_akcija():

    akcije = ucitaj_akcije()

    print("\n1. Pretraga po šifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")

    izbor = unesi_ceo_broj(">>izaberite opciju: ")

    filtrirane = []
    if izbor == 1:
        vrednost = unesi_ceo_broj(">>Unesite sifru: ")
        filtrirane = pretrazi_akcije_broj(akcije, "sifra", vrednost)

    elif izbor == 2:
        vrednost = unesi_neprazan_string(">>Unesite naslov: ")
        filtrirane = pretrazi_akcije_string(akcije, "naslov", vrednost)

    elif izbor == 3:
        vrednost = unesi_neprazan_string(">>Unesite autora: ")
        filtrirane = pretrazi_akcije_string(akcije, "autor", vrednost)
    elif izbor == 4:
        vrednost = unesi_neprazan_string(">>Unesite kategoriju: ")
        filtrirane = pretrazi_akcije_string(akcije, "kategorija", vrednost)
    else:
        print("Loš unos.")
        return

    prikazi_tabelu(filtrirane)


def sortiraj(kljuc):
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije


def prikaz_akcija():
    # akcije = ucitaj_akcije()
    print("1. Sortirati po šifri")
    print("2. Sortirati po datumu")
    izbor = unesi_ceo_broj(">>izaberite opciju: ")

    filtrirrane = []

    if izbor == 1:
        filtrirrane = sortiraj("sifra")
    elif izbor == 2:
        filtrirrane = sortiraj("datum")
    else:
        print('"Izabrali ste nepostojecu opciju!')
        return

    prikazi_tabelu(filtrirrane)