from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige



def dodavanje_knjige():
    spisak_knjiga = ucitaj_knjige()
    knjiga = {}

    sifra = input("unesite sifru knjige koju zelite da dodate: ")

    knjiga["sifra"] = sifra
    knjiga["naslov"] = input("naslov: ")
    knjiga["autor"] = input("autor: ")
    knjiga["isbn"] = input("unesite isbn knjige koju zelite da dodate: ")
    knjiga["izdavac"] = input("izdavac: ")
    knjiga["godina"] = input("godina izdanja: ")
    knjiga["cena"] = input("cena: ")
    knjiga["kategorija"] = input("kategorija: ")

    if pronadji_knjigu_po_sifri(sifra) is None:
        spisak_knjiga.append(knjiga)
        sacuvaj_knjige(spisak_knjiga)
    else:
        print('knjiga sa unetim isbn-om vec postoji')




def pronadji_knjigu_po_sifri(sifra_knjige):
    knjige = ucitaj_knjige()

    sifra = str(sifra_knjige)
    for knjiga in knjige:
        if knjiga["sifra"] == sifra:
            return knjiga


    return None

def izmena_knjige(): #kako da izbrise knjigu sa vec postojecom vrednoscu ili zamenimo
    knjige = ucitaj_knjige()

    sifra_knjige = input("unesite sifru knjige koju zelite da izmenite: ")
    knjiga = pronadji_knjigu_po_sifri(sifra_knjige)

    print(knjiga)

    knjiga["naslov"] = input("naslov: ")
    knjiga["autor"] = input("autor: ")
    knjiga["isbn"] = input("unesite ")
    knjiga["izdavac"] = input("isbn: ")
    knjiga["godina"] = input("godina: ")
    knjiga["cena"] = input("cena: ")
    knjiga["kategorija"] = input("kategorija: ")

    knjige.append(knjiga)

    sacuvaj_knjige(knjige)

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
        if vrednost.lower() == knjiga[kljuc].lower(): #broj in broj nista ne znaci
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige(): #knjige

    print("1. Pretraga po šifri")
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
    elif opcija == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretrazi_knjige_brojevi("sifra", sifra)
    elif opcija == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_brojevi("autor", autor)
    elif opcija == 4:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string("kategorija", kategorija)
    elif opcija == 5:
        izdavac = input("Unesite izdavača: ")
        knjige = pretrazi_knjige_string("izdavac", izdavac)
    elif opcija == 6:
        donja_cena = float(input("Unesite donju cenu: ")) #uradi ovo
        gornja_cena = float(input("unesite gornju cenu"))
        knjige = pretrazi_knjigu_range('cena', donja_cena, gornja_cena)

    for knjiga in knjige:
        print(knjiga)

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

    print("1. Sortiranje po naslovu")
    print("2. Sortiranje po kategoriji")
    print("3. Sortiranje po autoru")
    print("4. Sortiranje po izdavaču")
    print("5. Sortiranje po ceni")

    opcija = int(input("Izaberite opciju: "))

    knjige = []

    if opcija == 1:
        knjige = sortiraj_knjige("naslov")
    elif opcija == 2:
        knjige = sortiraj_knjige("kategorija")
    elif opcija == 3:
        knjige = sortiraj_knjige("autor")
    elif opcija == 4:
        knjige = sortiraj_knjige("izdavac")
    elif opcija == 5:
        knjige = sortiraj_knjige("cena")
    else:
        print("Opcija ne postoji")

    for knjiga in knjige: #tabela
        print(knjiga)



