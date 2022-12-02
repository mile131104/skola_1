poruke = {"sr": "Zdravo", "en": "Hello", "de": "Hallo"}
poruke["sr"] = "Cao"
poruke["it"] = "Ciao"
# print(poruke["sr"])
# jezik = input("Unesite jezik: (sr/en/de): ")

# if jezik == "sr" or jezik == "en" or jezik == "de" or jezik == "it":
#     print(poruke[jezik.lower()])
# else:
#     print("Nemamo ovaj prevod.")


selekcija = {
    "drzava": "Srbija",
    "boja_dresa": ["Crvena", "Bela"],
    "broj_pobeda": 1,
    "igraci": ["Jovic", "Mitrovic", "Grujic", "Tadic"]
}

# for i in selekcija:
#     # print(i, selekcija[i])
#     print(f"{i.capitalize():}: {selekcija[i]}")

for (kljuc, vrednost) in selekcija.items():
    if kljuc == "boja_dresa":
        for boja in vrednost:
            print(f"Boja dresa: {boja}")
    elif kljuc == "igraci":
        for igrac in vrednost:
            print(f"Igrac: {igrac}")
        print(f"{kljuc}: {vrednost}")
    else:
        print(f"{kljuc.capitalize()}: {vrednost}")

ucesnici = {
    "SRB": {
        "drzava": "Srbija", 
        "boje": ["crvena", "bela"],
        "broj_pobeda": 1,
        "igraci":["Jovic", "Mitrovic", "Grujic", "Tadic"]
        },
    "FRA": {
        "drzava": "Francuska", 
        "boje": ["plava", "bela"],
        "broj_pobeda": 2,
        "igraci":["Pogba", "Coma", "Benzema"]
        },
    "SWI": {
        "drzava": "Svajcarska", 
        "boje": ["crvena", "bela"],
        "broj_pobeda": 1,
        "igraci":["Zomer", "Aknaz", "Cuber"]
        }
}
print("SELEKCIJE:")
for (oznaka, detalji) in ucesnici.items():
    #print(oznaka) # skracenica string, kljuc
    #print(detalji) # info o selekciji, recnik
    for (kljuc, vrednost) in detalji.items():
        if kljuc == "boje":
            for boja in vrednost:
                print(f"Boja: {boja}")
        elif kljuc == "igraci":
            for igrac in vrednost:
                print(f"Igrac: {igrac}")
        else:
            print(f"{kljuc.capitalize()}: {vrednost}")
    print("---------------------")
# registracija: karakteristike
#                       kljuc: vrednost
# registracija:
# karakteristike:
# "Marka": ....
# "Model": ....
# "Godiste": ....
# "Tip goriva": ....
# ------------------
automobili = {
    "BG-123": {
        "marka": "BMW",
        "model": "X1",
        "godiste": 2019,
        "tip_goriva": "dizel"
    },
    "BG-321": {
        "marka": "Citroen",
        "model": "C3",
        "godiste": 2017,
        "tip_goriva": "dizel"
    },
    "BG-543": {
        "marka": "Mercedes",
        "model": "A klasa",
        "godiste": 2018,
        "tip_goriva": "benzin"
    }
}

for (auta, detalji) in automobili.items():
    for (a, vrednost) in detalji.items():
        print(f"{a.capitalize()}: {vrednost}")
    print("----------------------")

