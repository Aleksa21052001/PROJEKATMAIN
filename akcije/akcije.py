from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije

def sortiraj_po_sifri(akcije):
    return sorted(akcije, key=lambda a: a["sifra"])

def sortiraj_po_datumu(akcije):
    return sorted(akcije, key=lambda a: a["datum"])

def prikazi_tabelu(akcije):
    for akcija in akcije:
        print(akcija)



def prikazih_svih_akcija():
    akcije = ucitaj_akcije()
    print("1. Sortirati po šifri")
    print("2. Sortirati po datumu")
    izbor = input()

    if izbor == "1":
        akcije = sortiraj_po_sifri(akcije)
    elif izbor == "2":
        akcije = sortiraj_po_datumu(akcije)
    prikazi_tabelu(akcije)


