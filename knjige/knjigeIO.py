import json
datoteka = './datoteke/knjige.json'

def sacuvaj_knjige(korisnici):
    with open(datoteka, "w") as f:
        json.dump(korisnici, f, indent=4)

def ucitaj_knjige():
    with open(datoteka) as f:
        knjige = json.load(f)
        return knjige

