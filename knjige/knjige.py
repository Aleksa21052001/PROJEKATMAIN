from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from korisnici import korisnici
from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from racuni.racuniIO import ucitaj_racune, sacuvaj_racune
from datetime import datetime
from unos import unesi_ceo_broj, unesi_decimalni_broj


def logicko_brisanje():
    knjige = ucitaj_knjige()

    sifra_knjige = unesi_ceo_broj("unesite sifru knjige koju zelite da obrisite: ")
    knjiga_za_brisanje = pronadji_knjigu_po_sifri(knjige, sifra_knjige)
    print(knjiga_za_brisanje)
    if knjiga_za_brisanje:
        print("Da li zelite ovu knjigu da obrisete?")
        print("1. Da")
        print("2. Ne")
        print()
        opcija = unesi_ceo_broj("izaberite opciju: ")

        if opcija == 1:
            knjiga_za_brisanje["obrisana"] = True
            sacuvaj_knjige(knjige)
            print("knjiga je obrisana")
        if opcija == 2:
            print("knjiga nije obrisana")

    else:
        print('ne postoji knjiga sa unetom sifrom', sifra_knjige)




def dodavanje_knjige():
    spisak_knjiga = ucitaj_knjige()
    knjiga = {}

    sifra = input(">>unesite sifru knjige koju zelite da dodate: ")

    if sifra == "":
        print('"morate uneti neku vrednost!\n"')
        return

    if pronadji_knjigu_po_sifri(spisak_knjiga, sifra) is None:
        knjiga["sifra"] = sifra
        knjiga["naslov"] = str(input(">>naslov: "))
        knjiga["autor"] = str(input(">>autor: "))
        knjiga["isbn"] = str(input(">>unesite isbn knjige koju zelite da dodate: "))
        knjiga["izdavac"] = str(input(">>izdavac: "))

        godina = 0
        while godina < 1 or godina > 2021:
            try:
                godina = unesi_ceo_broj(">>godina izdanja: ")
                knjiga["godina"] = godina
            except ValueError:
                print('"nije validna godina, probajte ponovo!"')
                pass

        knjiga["cena"] = unesi_decimalni_broj(">>cena: ")
        knjiga["kategorija"] = str(input(">>kategorija: "))
        knjiga["obrisana"] = False

        spisak_knjiga.append(knjiga)
        sacuvaj_knjige(spisak_knjiga)
        print('"knjiga je uspesno dodata"')
    else:
        print('"knjiga sa unetom sifrom vec postoji!"')


def prikaz_knjiga_za_izmenu():
    zaglavlje()
    knjige = ucitaj_knjige()
    ispisi_tabelu(knjige)
    print()


def pronadji_knjigu_po_sifri(knjige, sifra_knjige):
    for knjiga in knjige:
        if knjiga["sifra"] == int(sifra_knjige):
            return knjiga
    return None


def izmena_knjige():
    knjige = ucitaj_knjige()

    prikaz_knjiga_za_izmenu()

    sifra_knjige = input(">>unesite sifru knjige koju zelite da izmenite: ")
    knjiga = pronadji_knjigu_po_sifri(knjige, sifra_knjige)

    if knjiga:
        naslov = input(">>naslov: ")
        if naslov != "":
            knjiga["naslov"] = naslov
        autor = input(">>autor: ")
        if autor != "":
            knjiga["autor"] = autor
        isbn = input(">>unesite isbn: ")
        if isbn != "":
            knjiga["isbn"] = isbn
        izdavac = input(">>izdavac: ")
        if izdavac != "":
            knjiga["izdavac"] = izdavac
        godina = input(">>godina: ")
        if godina != "":
            knjiga["godina"] = int(godina)
        cena = input(">>cena: ")
        if cena != "":
            knjiga["cena"] = float(cena)
        kategorija = input(">>kategorija: ")
        if kategorija != "":
            knjiga["kategorija"] = kategorija
        sacuvaj_knjige(knjige)
        print('"knjiga je izmenjena"')
    else:
        print('"ne postoji knjiga sa unetom sifrom"', sifra_knjige)
        #return izmena_knjige()  #da se izmena desava dok ne unesemo ispravnu sifru


def zaglavlje():
    print()
    print(
        'sifra   |naslov                |autor                |isbn                |izdavac              |godina         |cena         |kategorija')
    print(
        '--------|----------------------|---------------------|--------------------|---------------------|---------------|-------------|----------')


def pretrazi_knjigu_range(kljuc, donja_granica, gornja_granica):
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
        if vrednost.lower() in knjiga[ kljuc].lower():  # STRING IN STRING PROVERAVA DA LI SE OVO STO SMO UNELI NALAZI BILO GDE
            filitrirane_knjige.append(knjiga)

    return filitrirane_knjige


def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:  # broj in broj nista ne znaci
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():  # knjige

    print("\n1. Pretraga po šifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("5. Pretraga po izdavaču")
    print("6. Pretraga po opsegu cene")

    opcija = int(input(">>Izaberite opciju: "))

    knjige = []

    if opcija == 2:
        naslov = input(">>Unesite naslov: ")
        knjige = pretrazi_knjige_string("naslov", naslov)
        zaglavlje()
    elif opcija == 1:
        sifra = int(input(">>Unesite sifru: "))
        knjige = pretrazi_knjige_brojevi("sifra", sifra)
        zaglavlje()
    elif opcija == 3:
        autor = input(">>Unesite autora: ")
        knjige = pretrazi_knjige_string("autor", autor)
        zaglavlje()
    elif opcija == 4:
        kategorija = input(">>Unesite kategoriju: ")
        knjige = pretrazi_knjige_string("kategorija", kategorija)
        zaglavlje()
    elif opcija == 5:
        izdavac = input(">>Unesite izdavača: ")
        knjige = pretrazi_knjige_string("izdavac", izdavac)
        zaglavlje()
    elif opcija == 6:
        donja_cena = float(input(">>Unesite donju cenu: "))
        gornja_cena = float(input(">>unesite gornju cenu: "))
        if gornja_cena < donja_cena:
            print('"greska pri unosu vrednosti!"')
            return
        knjige = pretrazi_knjigu_range('cena', donja_cena, gornja_cena)
        zaglavlje()
    else:
        print('"Opcija ne postoji"')

    ispisi_tabelu(knjige)


def sortiraj_knjige(kljuc):  # knjige ,
    # knjige = knjige[:], sortiramo kopiju liste, ucitali smo kod administrator iz fajla pa prosledili ovde
    knjige = ucitaj_knjige()  # ucitavamo knjige iz fajla

    # sortiranje

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp
    return knjige


def ispisi_tabelu(knjige):
    for knjiga in knjige:
        if not knjiga["obrisana"] or korisnici.ulogovani_korisnik["tip_korisnika"] == "administrator":
            tabela_knjiga = str(knjiga["sifra"]).ljust(8) + "|" + knjiga["naslov"].ljust(22) + "|" + knjiga[
                "autor"].ljust(
                21) + "|" + knjiga["isbn"].ljust(20) + "|" + knjiga["izdavac"].ljust(21) + "|" + str(
                knjiga["godina"]).ljust(15) + "|" + str(knjiga["cena"]).ljust(13) + "|" + knjiga["kategorija"].ljust(15)
            print(tabela_knjiga)


def prodavanje_knjige_preko_sifre():
    korpa = []
    knjige = ucitaj_knjige()
    while True:
        sifra = int(input("Unesi šifru: "))
        for knjiga in knjige:
            if knjiga["sifra"] == sifra:
                trazena_knjiga = knjiga
                break
        else:
            print("Takva knjiga ne postoji.")
            continue
        kolicina = int(input("Unesi količinu:"))
        podatak = (trazena_knjiga, kolicina, trazena_knjiga["cena"], False)
        korpa.append(podatak)
        print("Da li želite uneti novu knjigu?(da/ne)")
        izbor = input()
        if izbor == "ne":
            break
    return korpa


def prodavanje_knjige_preko_akcije():
    korpa = []
    print("Unesi sifru akcije")
    sifra_akcije = int(input())
    akcije = ucitaj_akcije()
    for akcija in akcije:
        if akcija["sifra"] == sifra_akcije:
            trazena_akcija = akcija
            break
    else:
        print("Takva akcija ne postoji.")
        return
    for knjiga, cena in zip(trazena_akcija["knjige"], trazena_akcija["cene"]):
        podatak = (knjiga, 1, cena, True)
        korpa.append(podatak)
    return korpa
    

def pregled_korpe(korpa):
    ukupna_cena = 0
    for knjiga, kolicina, cena, jeste_akcija in korpa:
        print(knjiga["naslov"], "Količina:", kolicina, "Cena:", cena)
        ukupna_cena += kolicina * cena
    print("Ukupna cena:", ukupna_cena)


def prodaja_knjiga():
    korpa = []
    while True:
        print("1. Prodavanje knjige preko sifri")
        print("2. Prodavanje knjige preko akcije")
        print("3. Nastavi prodaju")
        print("4. Pregled korpe")

        izbor = input("Unesite opciju: ")
        if izbor == "1":
            korpa2 = prodavanje_knjige_preko_sifre()
            korpa.extend(korpa2)
        elif izbor == "2":
            korpa2 = prodavanje_knjige_preko_akcije()
            korpa.extend(korpa2)
        elif izbor == "3":
            break
        elif izbor == "4":
            pregled_korpe(korpa)
        else:
            print("Loš izbor")
            return
    
    trenutni_datum_vreme = datetime.now()
    knjige = []
    kolicine = []
    jedinicne_cene = []
    jeste_akcija = []
    ukupna_cena = 0
    for podatak in korpa:
        knjige.append(podatak[0])
        kolicine.append(podatak[1])
        jedinicne_cene.append(podatak[2])
        jeste_akcija.append(podatak[3])
        ukupna_cena += podatak[1]*podatak[2]
    potvrda = input("Da li želite da nastavite sa kupovinom?(da/ne): ")
    if potvrda == "ne":
        print("Odustali ste od kupovine")
        return
    racuni = ucitaj_racune()
    if len(racuni) == 0:
        sifra = 1
    else:
        sifra = racuni[-1]["sifra"] + 1
    prodavac = korisnici.ulogovani_korisnik["korisnicko_ime"]
    racun = {"sifra": sifra, 
            "knjige":knjige, 
            "kolicine": kolicine, 
            "jedinicne_cene": jedinicne_cene, 
            "datum_vreme": trenutni_datum_vreme,
            "ukupna_cena": ukupna_cena,
            "jeste_akcija": jeste_akcija,
            "prodavac": prodavac}
    racuni.append(racun)
    sacuvaj_racune(racuni)
    print("Uspešna kupovina!")


def dodavanje_akcije():
    knjige_za_akciju = []
    cene = []
    knjige = ucitaj_knjige()
    datum = input("Unesi datum vazenja akcije(dd-mm-YYYY): ")
    datum = datetime.strptime(datum, "%d-%m-%Y")
    while True:
        sifra_knjige = int(input("Unesi sifru knjige: "))
        for knjiga in knjige:
            if knjiga["sifra"] == sifra_knjige:
                trazena_knjiga = knjiga
                break
        else:
            print("Ne postoji takva knjiga.")
            continue
        nova_cena = float(input("Unesi novu cenu knjige: "))
        knjige_za_akciju.append(trazena_knjiga)
        cene.append(nova_cena)
        potvrda_nove = input("Da li zelite dodati novu knjigu?(da/ne)")
        if potvrda_nove == "ne":
            break
    akcije = ucitaj_akcije()
    if len(akcije) == 0:
        sifra = 1
    else:
        sifra = akcije[-1]["sifra"] + 1
    akcija = {"sifra": sifra, "datum": datum, "knjige":knjige_za_akciju, "cene": cene}
    akcije.append(akcija)
    sacuvaj_akcije(akcije)
    print("Uspešno napravljena akcija.")

def ukupna_prodaja_svih_knjiga():
    racuni = ucitaj_racune()
    jedinstvene_knjige = []
    for racun in racuni:
        for knjiga, kolicina, jedinstvena_cena, jeste_akcija  in zip(racun["knjige"], racun["kolicine"], racun["jedinicne_cene"], racun["jeste_akcija"]):
            for indeks, k in enumerate(jedinstvene_knjige):
                if k[0]["sifra"] == knjiga["sifra"]:
                    jedinstvene_knjige[indeks][1] += kolicina
                    jedinstvene_knjige[indeks][2] += jedinstvena_cena*kolicina
                    break
            else:
                jedinstvene_knjige.append([knjiga, kolicina, jedinstvena_cena*kolicina])
    
    for knjiga, ukupna_kolicina, ukupna_cena in jedinstvene_knjige:
        print(knjiga["naslov"], ukupna_kolicina, ukupna_cena)

def ukupna_prodaja_svih_akcija():
    racuni = ucitaj_racune()
    jedinstvene_knjige = []
    for racun in racuni:
        for knjiga, kolicina, jedinstvena_cena, jeste_akcija  in zip(racun["knjige"], racun["kolicine"], racun["jedinicne_cene"], racun["jeste_akcija"]):
            if jeste_akcija:
                for indeks, k in enumerate(jedinstvene_knjige):
                    if k[0]["sifra"] == knjiga["sifra"]:
                        jedinstvene_knjige[indeks][1] += kolicina
                        jedinstvene_knjige[indeks][2] += jedinstvena_cena*kolicina

                        break
                else:
                    jedinstvene_knjige.append([knjiga, kolicina, jedinstvena_cena*kolicina])
    
    for knjiga, ukupna_kolicina, ukupna_cena in jedinstvene_knjige:
        print(knjiga["naslov"], ukupna_kolicina, ukupna_cena)

def ukupna_prodaja_svih_knjiga_autora():
    autor = input("Unesi autora: ")
    racuni = ucitaj_racune()
    jedinstvene_knjige = []
    for racun in racuni:
        for knjiga, kolicina, jedinstvena_cena, jeste_akcija  in zip(racun["knjige"], racun["kolicine"], racun["jedinicne_cene"], racun["jeste_akcija"]):
            if knjiga["autor"] == autor:
                for indeks, k in enumerate(jedinstvene_knjige):
                    if k[0]["sifra"] == knjiga["sifra"]:
                        jedinstvene_knjige[indeks][1] += kolicina
                        jedinstvene_knjige[indeks][2] += jedinstvena_cena*kolicina

                        break
                else:
                    jedinstvene_knjige.append([knjiga, kolicina, jedinstvena_cena*kolicina])
    
    for knjiga, ukupna_kolicina, ukupna_cena in jedinstvene_knjige:
        print(knjiga["naslov"], ukupna_kolicina, ukupna_cena)

def ukupna_prodaja_svih_knjiga_izdavaca():
    izdavac = input("Unesi izdavača: ")
    racuni = ucitaj_racune()
    jedinstvene_knjige = []
    for racun in racuni:
        for knjiga, kolicina, jedinstvena_cena, jeste_akcija  in zip(racun["knjige"], racun["kolicine"], racun["jedinicne_cene"], racun["jeste_akcija"]):
            if knjiga["izdavac"] == izdavac:
                for indeks, k in enumerate(jedinstvene_knjige):
                    if k[0]["sifra"] == knjiga["sifra"]:
                        jedinstvene_knjige[indeks][1] += kolicina
                        jedinstvene_knjige[indeks][2] += jedinstvena_cena*kolicina

                        break
                else:
                    jedinstvene_knjige.append([knjiga, kolicina, jedinstvena_cena*kolicina])
    
    for knjiga, ukupna_kolicina, ukupna_cena in jedinstvene_knjige:
        print(knjiga["naslov"], ukupna_kolicina, ukupna_cena)

def pravljenje_izvestaja():
    print("1. Ukupna prodaja svih knjiga")
    print("2. Ukupna prodaja svih akcija")
    print("3. Ukupna prodaja svih knjiga odabranog autora")
    print("4. Ukupna prodaja svih knjiga odabranog izdavača")
    izbor = input("Unesite izbor: ")
    if izbor == "1":
        ukupna_prodaja_svih_knjiga()
    elif izbor == "2":
        ukupna_prodaja_svih_akcija()
    elif izbor == "3":
        ukupna_prodaja_svih_knjiga_autora()
    elif izbor == "4":
        ukupna_prodaja_svih_knjiga_izdavaca()
        

def prikazi_knjige():
    print("\n1. Sortiranje po naslovu")
    print("2. Sortiranje po kategoriji")
    print("3. Sortiranje po autoru")
    print("4. Sortiranje po izdavaču")
    print("5. Sortiranje po ceni")

    opcija = unesi_ceo_broj(">>Izaberite opciju: ")

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

    ispisi_tabelu(knjige)


