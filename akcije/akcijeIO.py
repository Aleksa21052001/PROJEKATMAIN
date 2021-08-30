import json
from datetime import datetime
datoteka = './datoteke/akcije.json'

def sacuvaj_akcije(akcije):
    with open(datoteka, "w") as f:
        for akcija in akcije:
            akcija["datum"] = akcija["datum"].strftime("%d-%m-%Y")

        json.dump(akcije, f, indent=4)

def ucitaj_akcije():
    with open(datoteka) as f:
        akcije = json.load(f)
        for akcija in akcije:
            akcija["datum"] = datetime.strptime(akcija["datum"], "%d-%m-%Y")
        return akcije

