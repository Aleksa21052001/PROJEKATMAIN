def unesi_ceo_broj(poruka):
    while True:
        try:
            broj = int(input(poruka))
            return broj
        except ValueError:
            print("Greška. Morate uneti ceo broj. Pokušajte ponovo.")

def unesi_decimalni_broj(poruka):
    while True:
        try:
            broj = float(input(poruka))
            return broj
        except ValueError:
            print("Greška. Morate uneti decimalni broj. Pokušajte ponovo.")

def unesi_neprazan_string(poruka):
    while True:  
        string = input(poruka)
        if string.strip():
            return string
        else:
            print("Greška. Unos ne sme biti prazan. Pokušajte ponovo.")

