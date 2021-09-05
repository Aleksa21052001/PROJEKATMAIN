import json
datoteka = './datoteke/korisnici.json'

def sacuvaj_korisnike(korisnici):
    with open(datoteka, "w") as f:
        json.dump(korisnici, f, indent=5)

def ucitaj_korisnike():
    with open(datoteka) as f:
        return json.load(f)