import json
datoteka = './datoteke/akcije.json'

def sacuvaj_akcije(akcije):
    with open(datoteka, "w") as f:
        json.dump(akcije, f, indent=5)

def ucitaj_akcije():
    with open(datoteka) as f:
        akcije = json.load(f)
        return akcije

