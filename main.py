from korisnici.kosrisnici import prijava, registracija_novih_korisnika, prikaz_svih_korisnika
from knjige.knjige import prikazi_knjige, ucitaj_knjige, pretrazi_knjige, izmena_knjige, dodavanje_knjige

def meni_administrator():

    #knjige = ucitaj_knjige(), ako ovde hocemo da ucitamo pa prosledimo dalje
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Lista korisnika ")
        print("7. Dodavanje knjige ")
        print("8. Izmena knjige")
        print("9. Logičko brisanje knjige")
        print("10. Kraj")

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pass
        elif stavka == 4:
            pass
        elif stavka == 5:
            registracija_novih_korisnika()
        elif stavka == 6:
            prikaz_svih_korisnika()
        elif stavka == 7:
            dodavanje_knjige()
        elif stavka == 8:
            izmena_knjige()
        elif stavka == 10:
            return
        else:
            print("pokušajte ponovo")


def main():

    ulogovani_korisnik = prijava()
    print(ulogovani_korisnik)

    if ulogovani_korisnik is not None: #ZNACI POSTOJI
        if ulogovani_korisnik["tip_korisnika"] == 'administrator':
            meni_administrator()
        elif ulogovani_korisnik["tip_korisnika"] == "prodavac":
         pass
        elif ulogovani_korisnik["tip_korisnika"] == "menadzer":
          pass
        else:
          print("Korisnik ima nepoznatu ulogu")

main()
