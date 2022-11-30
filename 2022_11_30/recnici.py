        #   0      1      2
# osoba = ["Sofija", 25, "Python"]

#       0 ime, 1 godine, 2 smer

# ime : Sofija
# godine : 25
# smer : Python

# osoba[0] -    ime
# osoba["ime"]  - ime osobe
# osoba["godine"]   - godine osobe


# kljuc : vrednost
# ime   : sofija    godine: 25  smer: Python

        # kljuc  # vrednost
# recnik = {"ime": "Sofija", "godine": 25, "smer": "Python", "Aktivan": True}
# polaznici = {333: "Petar", 222: "Jovana", 150: "Ana"}

# recnik = {"ime": "Sofija", "godine": 25, "smer": "Python", "Aktivan": True}
# print(recnik)
# print(recnik["ime"])
# print(recnik["godine"])
# print(recnik["smer"])
# print(recnik["Aktivan"])

poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}

#sr
# print(poruke["sr"])
# jezik = input("Odaberite jezik (en/sr/de): ")

# if jezik != "en" and jezik != "sr" and jezik != "de":
#     print("Dostupni su: en, sr ide")
# else:
#     print(poruke[jezik])

# print(poruke)

# poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}

# RECNIK
for kljuc in poruke:
    print(poruke[kljuc]) # "en" "sr", ... poruke["en"]

# LISTA            0        1         2
lista_jezika = ["Zdravo", "Hello", "Hallo"]

for i in range(len(lista_jezika)):
    print(lista_jezika[i]) # lista_jezika[0]

# RECNIK
# i kljuc i vrednost

for kljuc, vrednost in poruke.items():
    print(kljuc)
    print(vrednost)

# ("en" "Hello")


poeni =  {"kate": 800, "tom": 750, "john": 800}
print(poeni)

for kor, poeni in poeni.items():
    print(f"Korisnik: {kor}, je osvojio {poeni} poena.")
    