import re
import enum

# broj = 0
# if broj == 0:
#     print("Ne mozete deliti sa nulom")
# else:
#     print(10/broj)

# print("Nastavak programa")
# print("Kraj programa")

# unos = int(input("Unesite broj: "))
# print(unos)

# proba = ["a", "b"]
# print(proba[5])

# try:
    # print(10/0) # Ovde moze da bude problem 
    # Ovo se nikad ne izvrsava ako je problem uhvacen
    # print("Deljenje sa 0")
# except:
    # Obrada izuzetka
    # print("Neuspesno deljenje, ne smete deliti sa nulom.")

# Standardan nastavak programa
# print("Ovo je nastavak programa")
# print("Ovo je kraj programa")

# uzmete broj - input
# stampate broj
# Ne mozete uneti tekst umesto broja

# try:
#     unos = int(input("Unesite broj: "))
#     print("Vas broj je", unos)
# except:
#     print("Ne mozete uneti tekst umesto broja")

# print("Ovo je nastavak programa")
# print("Ovo je kraj programa")

# try:
#     # broj = int(input("Unesite broj: "))
#     # print(broj)
#     brojevi = [1, 2]
#     print(brojevi[5])
#     print(10/0)
# except IndexError as index_greska:
#     # U ovom bloku se hvataju greske koje su vezane za problem sa indeksom
#     # print("Greska, indeks ne postoji")
#     print(index_greska)
# except ValueError as greska_vrednost:
#     print(greska_vrednost)
# except ZeroDivisionError as greska_deljenje:
#     print(greska_deljenje)
# except Exception as greska:
#     # On hvata sve tipove izuzetka
#     print(greska)

def podeli(a, b):
    # a i b moraju biti veci od 10
    if a > 10 and b > 10:
        print(a / b)
    else:
        # Izbaci exception
        raise Exception("Greska brojevi moraju biti veci od 10")
try:
    podeli(15,0)
except Exception as ex:
    print(ex)