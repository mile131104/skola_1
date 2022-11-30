# osoba = ["Marko", 25, "iOS"]
# print(osoba)

# print(osoba[0])
# print(osoba[1])
# print(osoba[2])


# for broj in range(5):
#     print(broj)
# print()
# for broj in range(5, 20):
#     print(broj)
# print()
# for broj in range(0, 31, 2):
#     print(broj)

# kurs = "Python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])

# print(len(kurs)) # Broj clanova

# for indeks in range(len(kurs) -1):
#     print(kurs[indeks])

# ustanova = "IT Academy"
# print(len(ustanova))

# for slovo in range(len(ustanova) -1):
#     print(ustanova[slovo])

# for slovo in ustanova:
#     print(slovo)

# tip_korisnika = "Admin"
# tip_korisnika[0] = "A"
# "Tip Korisnika": + tip_korisnika

# korisnicko_ime = input("Unesite korisnicko ime: ")

# if korisnicko_ime.upper() == "Admin1":
#     print("Dobrodosli")
# else:
#     print("Neispravni podaci")


# tekst = "A*B#*C#D"

# for slovo in tekst:
#     if slovo != "*" and slovo != "#":
#         print(slovo)

# for x in range(len(tekst)-1):
#     if tekst[x] == "*":
#         print("* je na poziciji", x)
#     elif tekst[x] == "#":
#         print("# je na poziciji", x)
#     else:
#         print(tekst[x])

# slovo = "A"
# print(slovo in tekst)

# telefoni = ["iPhone 11", "Samsung A22", "iPhone 14", "Huawei Mate 50"]

# print(telefoni[1])
# telefoni[0] = "iPhone 12 Pro"

# Ponuda telefona

# for telefon in telefoni:
#     print(telefon)

# for indeks in range(len(telefoni)-1):
#     # print(indeks)
#     print(telefoni[indeks])

# indeks = 0
# duzina_liste = len(telefoni)

# while indeks < duzina_liste:
#     print(telefoni[indeks])
#     indeks += 1

# ponuda_smerova = ["Python", "PHP", "iOS", "Java"]
# zeljeni_smer = input("Unesite smer koji zelite: ")

# for smer in ponuda_smerova:
#     if zeljeni_smer == smer:
#         print("Uspesno ste se upisali!")
#         break
#     else:
#         pass


# ponuda_smerova = ["Python", "PHP", "iOS", "Java"]
# ponuda_smerova.append("C#")
# print(ponuda_smerova)

# proba = []
# proba.append(5)
# proba.append("Hello")

# print(proba)

# proba.clear() # Uklanja sve 
# proba.remove(5) # Uklanja tu vrednost
# proba.pop(0) # Uklanja vrednost na tom indeksu
# del proba[0] # Uklanja vrednost na tom indeksu

# print(proba)

# laptopovi = ["Acer", "Dell", "MacBook"]

# for i in range(len(laptopovi)):
#     print(laptopovi[i])


# for vrednost in laptopovi:
#     print(vrednost)


# for i, v in enumerate(laptopovi):
#     print("Indeks:", i, "Vrednost:", v)

# termini = ["Ponedeljak", "Sreda", "Petak"]

# for x in range(len(termini)):
#     if "Utorak" != termini[x]:
#         print("Dodajte i utorak u spisak")
#     print(termini[x])

# if "Utorak" in termini:
#     print("Utorak je medju terminima")
# else:
#     print("Dodajte i utorak")

# if not "Utorak" in termini: # Da li se ne nalazi

# smerovi = ["Python", "PHP", "iOS", "Java", "C#", "Frontend", "Android"]

# promocija = smerovi[1:4:2]
# print(promocija)

# korisnici = ["Petar", "Marija", "Jovana", "Vladimir", "Milos", "Katarina"]

# pobednici = korisnici[0:3]
# print(pobednici)
# pobednici.clear()

# for i in range(len(korisnici)):
#     if i == 0 or i == 1 or i == 2:
#         pobednici.append(korisnici[i])

# print(pobednici)

# brojevi = [1, 13, 26, 8, 5, 11, 32, 14]

# parni = []
# neparni = []

# for b in brojevi:
#     if b % 2 == 0:
#         parni.append(b)
#     else:
#         neparni.append(b)
# print("Parni:", parni)
# print("Neparni:", neparni)

# rec = input("Unesite rec za proveru: ")
# pocetni_indeks = 0
# krajnji_indeks =  len(rec)-1
# palindrom = True

# print(len(rec))

# while pocetni_indeks < krajnji_indeks:
#     if rec[pocetni_indeks] != rec[krajnji_indeks]:
#         print("Nije palindrom")
#         palindrom = False
#         break
#     pocetni_indeks += 1
#     krajnji_indeks -= 1
# else:
#     print("Jeste palindrom")

# print("Rec", rec, ("Jeste" if palindrom else "Nije", "Palindrom"))

kursevi = ["Python", "iOS", "Design"]

# unos kursa
# provera da li postoji u listi kursevi(in)
# append(dodati)
# svaki put nakon unosa ili poruke ispisati listu kurseva


while True:
    zeljeni_kurs = input("Unesite naziv kursa: ")
    if zeljeni_kurs in kursevi:
        print("Vec postoji!")
    else:
        kursevi.append(zeljeni_kurs)
        print(kursevi)

    