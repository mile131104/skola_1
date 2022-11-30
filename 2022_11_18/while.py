import random
sekunde = 10

# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)
# sekunde -= 1
# if sekunde > 0:
#     print(sekunde)

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1

# while False:
#     print("Cao")

# baterija = 90

# while baterija > 0:
#     print("Mozete koristiti uredjaj, baterija:", baterija, "%")
#     baterija -= random.randint(5, 15)

# print("Baterija je prazna...")

zivoti = 5

# while zivoti > 0:
#     print("Igra jos traje")
#     zivoti -= 1
#     if zivoti - 1:
#         print("Izgubili ste jedan zivot")
#     else:
#         pass

# print("Igra je zavrsena, nemate vise preostalih zivota")

# for zivot in range(5, 0, -1):
#     print("Igra traje")

# print("Kraj igre")

# broj_pokusaja = 7
# poeni = 0

# while broj_pokusaja > 0:
#     srecni_broj = random.randint(1, 20)
#     moj_broj = input("Unesi broj: ")
    
#     if srecni_broj == moj_broj:
#         print("Pogodak!", "Moj Broj:", moj_broj, "Srecan broj:", srecni_broj)
#     else:
#         print("Promasaj!", "Moj Broj:", moj_broj, "Srecan broj:", srecni_broj)
#     broj_pokusaja -= 1

# print("Igra je gotova, nemas vise pokusaja!", "Broj poena:", poeni)

# for broj in range(1, 10):
#     print(broj)
#     if broj == 5:
#         break

# for broj in range(1, 10 +1):
#     if broj == 3:
#         continue
#     print(broj)

# for ime in ["Petar", "Marko", "Jovana", "Katarina"]:
#     if ime == "Jovana":
#         print("Jovana", "Pronadjena!")
#         break
#     print(ime)
# else:
#     print("Zavrseno citanje polaznika...")

# print("Ovo se izvrsava u svakom slucaju")

zbir = 0

while True:
    broj = input("Unesite broj: ")

    if broj == "":
        print("Zbir je:", zbir)
    elif broj.isnumeric():
        zbir += int(broj)
    elif broj == "Quit":
        exit(0)
    else:
        print("Proverite unos!")
