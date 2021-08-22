from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige

"""
def logicko_brisanje():
    knjige = ucitaj_knjige()

    sifra_knjige = int(input("unesite sifru knjige koju zelite da izmenite: "))
    knjiga_za_brisanje = pronadji_knjigu_po_sifri(knjige, sifra_knjige)
    print(knjiga_za_brisanje)
    if knjiga_za_brisanje:
        print("Da li zelite ovu knjigu da obrisete?")
        print("1. Da")
        print("2. Ne")
        print()
        opcija = int(input("izaberite opciju: "))

        if opcija == 1:
            knjiga_za_brisanje["obrisanaa"] = "True"
            sacuvaj_knjige(knjige)
            print("knjiga je obrisana")
        if opcija == 2:
            print("knjiga nije obrisana")

    else:
        print('ne postoji knjiga sa unetom sifrom', sifra_knjige)
        
"""

def dodavanje_knjige():
    spisak_knjiga = ucitaj_knjige()
    knjiga = {}

    sifra = int(input("unesite sifru knjige koju zelite da dodate: "))

    if pronadji_knjigu_po_sifri(spisak_knjiga, sifra) is None:
        knjiga["sifra"] = sifra
        knjiga["naslov"] = str(input("naslov: "))
        knjiga["autor"] = str(input("autor: "))
        knjiga["isbn"] = str(input("unesite isbn knjige koju zelite da dodate: "))
        knjiga["izdavac"] = str(input("izdavac: "))
        knjiga["godina"] = int(input("godina izdanja: "))
        knjiga["cena"] = float(input("cena: "))
        knjiga["kategorija"] = str(input("kategorija: "))

        spisak_knjiga.append(knjiga)
        sacuvaj_knjige(spisak_knjiga)
    else:
        print('"knjiga sa unetom sifrom vec postoji!"')





def prikaz_knjiga_za_izmenu():
    zaglavlje()
    knjige = ucitaj_knjige()
    for knjiga in knjige:
        tabela_knjiga = str(knjiga["sifra"]).ljust(8) + "|" + knjiga["naslov"].ljust(22) + "|" + knjiga["autor"].ljust(21) + "|" + knjiga["isbn"].ljust(20) + "|" + knjiga["izdavac"].ljust(21) + "|" + str(knjiga["godina"]).ljust(15) + "|" + str(knjiga["cena"]).ljust(13) + "|" + knjiga["kategorija"] #+ knjiga["obrisana"] == "True"
        print(tabela_knjiga)
    print()


def pronadji_knjigu_po_sifri(knjige, sifra_knjige):

    for knjiga in knjige:
        if knjiga["sifra"] == sifra_knjige:
            return knjiga
    return None


def izmena_knjige():
    knjige = ucitaj_knjige()

    prikaz_knjiga_za_izmenu()

    sifra_knjige = int(input("unesite sifru knjige koju zelite da izmenite: "))
    knjiga = pronadji_knjigu_po_sifri(knjige, sifra_knjige)

    if knjiga:

        knjiga["naslov"] = input("naslov: ")
        knjiga["autor"] = input("autor: ")
        knjiga["isbn"] = input("unesite isbn: ")
        knjiga["izdavac"] = input("izdavac: ")
        knjiga["godina"] = int(input("godina: "))
        knjiga["cena"] = float(input("cena: "))
        knjiga["kategorija"] = input("kategorija: ")

        sacuvaj_knjige(knjige)
        print("knjiga je izmenjena")
    else:
        print('ne postoji knjiga sa unetom sifrom', sifra_knjige)




def zaglavlje():
    print()
    print('sifra   |naslov                |autor                |isbn                |izdavac              |godina         |cena         |kategorija')
    print('--------|----------------------|---------------------|--------------------|---------------------|---------------|-------------|----------')


def pretrazi_knjigu_range(kljuc, donja_granica , gornja_granica):
    knjige = ucitaj_knjige()

    filitrirane_knjige = []

    for knjiga in knjige:
        if knjiga[kljuc] >= donja_granica and knjiga[kljuc] <= gornja_granica:
            filitrirane_knjige.append(knjiga)

    return filitrirane_knjige


def pretrazi_knjige_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filitrirane_knjige = []  # knjige koje su prosle kriterijum za PRETRAGU

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower(): #STRING IN STRING PROVERAVA DA LI SE OVO STO SMO UNELI NALAZI BILO GDE
            filitrirane_knjige.append(knjiga)

    return filitrirane_knjige


def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]: #broj in broj nista ne znaci
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige(): #knjige

    print("\n1. Pretraga po šifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("5. Pretraga po izdavaču")
    print("6. Pretraga po opsegu cene")

    opcija = int(input("Izaberite opciju: "))

    knjige = []

    if opcija == 2:
        naslov = input("Unesite naslov: ")
        knjige = pretrazi_knjige_string("naslov", naslov)
        zaglavlje()
    elif opcija == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretrazi_knjige_brojevi("sifra", sifra)
        zaglavlje()
    elif opcija == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_string("autor", autor)
        zaglavlje()
    elif opcija == 4:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string("kategorija", kategorija)
        zaglavlje()
    elif opcija == 5:
        izdavac = input("Unesite izdavača: ")
        knjige = pretrazi_knjige_string("izdavac", izdavac)
        zaglavlje()
    elif opcija == 6:
        donja_cena = float(input("Unesite donju cenu: "))
        gornja_cena = float(input("unesite gornju cenu: "))
        if gornja_cena < donja_cena:
            print('"greska pri unosu vrednosti!"')
            return
        knjige = pretrazi_knjigu_range('cena', donja_cena, gornja_cena)
        zaglavlje()
    else:
        print('"Opcija ne postoji"')

    for knjiga in knjige:
        tabela_knjiga = str(knjiga["sifra"]).ljust(8) + "|" + knjiga["naslov"].ljust(22) + "|" + knjiga["autor"].ljust(21) + "|" + knjiga["isbn"].ljust(20) + "|" + knjiga["izdavac"].ljust(21) + "|" + str(knjiga["godina"]).ljust(15) + "|" + str(knjiga["cena"]).ljust(13) + "|" + knjiga["kategorija"].ljust(15)
        print(tabela_knjiga)


def sortiraj_knjige(kljuc): #knjige ,
    #knjige = knjige[:], sortiramo kopiju liste, ucitali smo kod administrator iz fajla pa prosledili ovde
    knjige = ucitaj_knjige() #ucitavamo knjige iz fajla

    # sortiranje

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j]= temp
    return knjige


def prikazi_knjige():

    print("\n1. Sortiranje po naslovu")
    print("2. Sortiranje po kategoriji")
    print("3. Sortiranje po autoru")
    print("4. Sortiranje po izdavaču")
    print("5. Sortiranje po ceni")

    opcija = int(input("Izaberite opciju: "))

    knjige = []

    if opcija == 1:
        zaglavlje()
        knjige = sortiraj_knjige("naslov")
    elif opcija == 2:
        zaglavlje()
        knjige = sortiraj_knjige("kategorija")
    elif opcija == 3:
        zaglavlje()
        knjige = sortiraj_knjige("autor")
    elif opcija == 4:
        zaglavlje()
        knjige = sortiraj_knjige("izdavac")
    elif opcija == 5:
        zaglavlje()
        knjige = sortiraj_knjige("cena")
    else:
        print("Opcija ne postoji")


    for knjiga in knjige:
        tabela_knjiga = str(knjiga["sifra"]).ljust(8) + "|" + knjiga["naslov"].ljust(22) + "|" + knjiga["autor"].ljust(21) + "|" + knjiga["isbn"].ljust(20) + "|" + knjiga["izdavac"].ljust(21) + "|" + str(knjiga["godina"]).ljust(15) + "|" + str(knjiga["cena"]).ljust(13) + "|" + knjiga["kategorija"].ljust(15)
        print(tabela_knjiga)





