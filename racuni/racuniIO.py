import json
datoteka = './datoteke/racuni.json'
from datetime import datetime

def sacuvaj_racune(racuni):
    for racun in racuni:
        racun["datum_vreme"] = racun["datum_vreme"].strftime("%d-%m-%Y %H:%M")

    with open(datoteka, "w") as f:
        json.dump(racuni, f, indent=4)

def ucitaj_racune():
    with open(datoteka) as f:
        racuni = json.load(f)
        for racun in racuni:
            racun["datum_vreme"] = datetime.strptime(racun["datum_vreme"], "%d-%m-%Y %H:%M")
        return racuni

