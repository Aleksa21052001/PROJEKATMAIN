from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from datetime import datetime

def sortiraj_po_sifri(akcije):
    return sorted(akcije, key=lambda a: a["sifra"])

def sortiraj_po_datumu(akcije):
    return sorted(akcije, key=lambda a: a["datum"])

def prikazi_tabelu(akcije):
    print("Akcije:")
    for akcija in akcije:
        if akcija["datum"] >= datetime.now():
            print("Šifra:", str(akcija["sifra"]))
            print("Datum do kad važi:", akcija["datum"].strftime("%d-%m-%Y"))
            for knjiga, cena in zip(akcija["knjige"], akcija["cene"]):
                print("Naslov:",knjiga["naslov"], "Stara cena:", knjiga["cena"], "|", "Nova cena:", cena)
    print("-----------------------------")


def prikaz_akcija():
    akcije = ucitaj_akcije()
    print("1. Sortirati po šifri")
    print("2. Sortirati po datumu")
    izbor = input()
    if izbor == "1":
        akcije = sortiraj_po_sifri(akcije)
    elif izbor == "2":
        akcije = sortiraj_po_datumu(akcije)
    prikazi_tabelu(akcije)

def pretraga_po_sifri(akcije, kljuc):
    akcije = [akcija for akcija in akcije if int(kljuc) == akcija["sifra"]]
    return akcije

def pretraga_po_naslovu(akcije, kljuc):
    nove_akcije = []
    for akcija in akcije:
        for knjiga in akcija["knjige"]:
            if kljuc.lower() in knjiga["naslov"].lower():
                nove_akcije.append(akcija)
                break
    return nove_akcije


def pretraga_po_autoru(akcije, kljuc):
    nove_akcije = []
    for akcija in akcije:
        for knjiga in akcija["knjige"]:
            if kljuc.lower() in knjiga["autor"].lower():
                nove_akcije.append(akcija)
                break
    return nove_akcije


def pretraga_po_kategoriji(akcije, kljuc):
    nove_akcije = []
    for akcija in akcije:
        for knjiga in akcija["knjige"]:
            if kljuc.lower() in knjiga["kategorija"].lower():
                nove_akcije.append(akcija)
                break
    return nove_akcije

def pretraga_akcija():
    akcije = ucitaj_akcije()
    print("1. Pretraga po šifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    izbor = input("Izbor: ")
    kljuc = input("Unesite kljuc pretrage: ")
    if izbor == "1":
        akcije = pretraga_po_sifri(akcije, kljuc)

    elif izbor == "2":
        akcije = pretraga_po_naslovu(akcije, kljuc)

    elif izbor == "3":
        akcije = pretraga_po_naslovu(akcije, kljuc)
    elif izbor == "4":
        akcije = pretraga_po_kategoriji(akcije, kljuc)
    else:
        print("Loš unos.")
        return
    prikazi_tabelu(akcije)



