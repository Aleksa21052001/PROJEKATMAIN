from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike




def zaglavlje():
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

    print("1. sortiranje po imenu")
    print("2. sortiranje po prezimenu")
    print("3. sortiranje po tipu korisnika")

    opcija = int(input("izaberite parametar sortiranja: "))

    sortirani_korisnici  = []

    if opcija == 1:
        sortirani_korisnici  = sortiraj_korisnika("ime")
        zaglavlje()
    elif opcija ==2:
        sortirani_korisnici = sortiraj_korisnika("prezime")
        zaglavlje()
    elif opcija ==3:
        sortirani_korisnici = sortiraj_korisnika("tip_korisnika")
        zaglavlje()
    else:
        print("Izabrali ste nepostojecu opciju")


    for korisnik in sortirani_korisnici:
        tabela_korisnika = korisnik["korisnicko_ime"].ljust(17) + "|" + korisnik["ime"].ljust(19)  + "|" + korisnik["prezime"].ljust(23)  + "|" + korisnik["tip_korisnika"]
        print(tabela_korisnika)


def provera_korisnika(korisnici , korisnicko_ime):

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime:
            return korisnik
    return None

def registracija_novih_korisnika():

    korisnici = ucitaj_korisnike()

    korisnicko_ime = str(input('unesite korisnicko ime novog korisnika: '))
    if provera_korisnika(korisnici, korisnicko_ime) is None:
        lozinka = input('unesite lozinku: ')
        ime = input('unesite ime novog korisnika: ')
        prezime = input('unesite prezime novog korisnika: ')

        while True:
            tip_korisnika = str(input('tip je menadzer/prodavac: '))

            if tip_korisnika == "menadzer" or tip_korisnika == "prodavac":
                novi_korisnik = {"korisnicko_ime":korisnicko_ime, "lozinka":lozinka, "ime":ime, "prezime": prezime , "tip_korisnika":tip_korisnika}
                print("korisnik je uspesno registrovan")
                break

            print("greska pri izboru tipa korisnika, pokusajte ponovo\n")

        korisnici.append(novi_korisnik)
        sacuvaj_korisnike(korisnici)
    else:
        print("korisnik vec postoji!")

def prijava(): #proverava da li postoji korisnik, treba nam f-ja koja ucitava i koja proverava korisnike

    korisnici = ucitaj_korisnike()

    i = 0
    while not i == 3:

        korisnicko_ime = input('unesite korisnicko ime: ')
        lozinka = input('unesite lozinku: ')

        for korisnik in korisnici:
            if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik['lozinka'] == lozinka:
                return korisnik #vratimo jer ce nam trebati da znamo ko je korisnik, koja mu je uloga koji meni da mu prikazemo

        if i != 2:
            print("Pogrešno korisnčko ime ili lozinka\n")

        i = i + 1

    print('"Previše puta ste pogrešili"')

    return None
