from korisnici.korisnici import prijava, registracija_novih_korisnika, prikaz_svih_korisnika
from knjige.knjige import prikazi_knjige, ucitaj_knjige, pretrazi_knjige, izmena_knjige, dodavanje_knjige, prodaja_knjiga, dodavanje_akcije, pravljenje_izvestaja, logicko_brisanje
from akcije.akcije import prikaz_akcija, pretraga_akcija
from unos import unesi_ceo_broj



def zajednici_meni():
    print("\n1. Prikaz knjiga")
    print("2. Pretraga knjiga")
    print("3. Prikaz akcija")
    print("4. Pretraga akcija")

def meni_menadzer():

    while True:
        zajednici_meni()
        print("5. Registracija")
        print("6. Lista korisnika")
        print("7. Dodavanje akcijske ponude")
        print("8. kreiranje izvestaja")
        print("10. Kraj")

        stavka = unesi_ceo_broj(">>Izaberite stavku: ")


        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikaz_akcija()
        elif stavka == 4:
            pretraga_akcija()
        elif stavka == 5:
            registracija_novih_korisnika()
        elif stavka == 6:
            prikaz_svih_korisnika()
        elif stavka == 7:
            dodavanje_akcije()
        elif stavka == 8:
            pravljenje_izvestaja()
        elif stavka == 10:
            print()
            print('"Hvala sto ste koristili aplikaciju"')
            return
        else:
            print('"izabrali ste nepostojecu opciju, pokušajte ponovo"')


def meni_prodavac():

    while True:
        zajednici_meni()
        print("5. Prodaja knjiga")
        print("6. Dodavanje knjige")
        print("7. Izmena knjige")
        print("8. Logičko brisanje knjige")
        print("10. Kraj")

        opcija = unesi_ceo_broj(">>Izaberite stavku: ")

        if opcija == 1:
            prikazi_knjige()
        elif opcija == 2:
            pretrazi_knjige()
        elif opcija == 3:
            prikaz_akcija()
        elif opcija == 4:
            pretraga_akcija()
        elif opcija == 5:
            prodaja_knjiga()
        elif opcija == 6:
            dodavanje_knjige()
        elif opcija == 7:
            izmena_knjige()
        elif opcija == 8:
            logicko_brisanje()
        elif opcija == 10:
            print()
            print('"Hvala sto ste koristili aplikaciju"')
            return
        else:
            print('"izabrali ste nepostojecu opciju, pokušajte ponovo"')


def meni_administrator():

    #knjige = ucitaj_knjige(), ako ovde hocemo da ucitamo pa prosledimo dalje
    while True:
        zajednici_meni()
        print("5. Registracija")
        print("6. Lista korisnika")
        print("7. Dodavanje knjige")
        print("8. Izmena knjige")
        print("9. Logičko brisanje knjige")
        print("10. Kraj")

        stavka = unesi_ceo_broj(">>Izaberite stavku: ")

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikaz_akcija()
        elif stavka == 4:
            pretraga_akcija()
        elif stavka == 5:
            registracija_novih_korisnika()
        elif stavka == 6:
            prikaz_svih_korisnika()
        elif stavka == 7:
            dodavanje_knjige()
        elif stavka == 8:
            izmena_knjige()
        elif stavka == 9:
            logicko_brisanje()
        elif stavka == 10:
            print()
            print('"Hvala sto ste koristili aplikaciju"')
            return
        else:
            print('"izabrali ste nepostojecu opciju, pokušajte ponovo"')


def main():

    ulogovani_korisnik = prijava()

    print()

    if ulogovani_korisnik is not None: #ZNACI POSTOJI
        if ulogovani_korisnik["tip_korisnika"] == 'administrator':
            print("Ulogovani korisnik je:", ulogovani_korisnik['tip_korisnika'].upper())
            meni_administrator()
        elif ulogovani_korisnik["tip_korisnika"] == "prodavac":
            print("Ulogovani korisnik je:", ulogovani_korisnik['tip_korisnika'].upper())
            meni_prodavac()
        elif ulogovani_korisnik["tip_korisnika"] == "menadzer":
            print("Ulogovani korisnik je:", ulogovani_korisnik['tip_korisnika'].upper())
            meni_menadzer()
        else:
            print('"Korisnik ima nepoznatu ulogu"')


main()
