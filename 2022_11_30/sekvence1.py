# brojevi = [2, 7, 5, 1, 4, 3, 9]

# brojevi.sort()
# print(brojevi)
# brojevi.reverse()
# print(brojevi)

# buble sort

# brojevi = [2, 7, 5, 1, 4, 3, 9]
# sortirani = [1, 2, 3, 4, 5, 7, 9]



# duzina_liste = len(brojevi)
# print(duzina_liste)
# while True:
#     zamenjena_mesta = False
#     for i in range(1, duzina_liste):
#         if brojevi [i] < brojevi [i-1]:
#             privremeno = brojevi [i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremeno
#             zamenjena_mesta = True
#     if zamenjena_mesta == False:
#         break
        
# print(brojevi)

# products = ["Phone", "Tv", "Computer"]
# prices = [155.95, 180.35, 199.99]

# for p in range(len(products)):
#     print(products[p], prices[p])

# ime = "Sofija"
# poruka = f"Cao, {ime} !!!"

# print(poruka)

# proizvodi = ["telefon", "laptop", "tablet"]

# telefoni = ["ihpone", "samsung", "huawei"]
# laptopovi = ["macbook", "acer", "dell"]
# tableti = ["ipad", "xiaomi", "samsung"]

# proizvodi = [
#                ["ihpone", "samsung", "huawei"],
#                ["macbook", "acer", "dell"],
#                ["ipad", "xiaomi", "samsung"]
# ]

# print(proizvodi[0][0])
# Ipad
# proizvodi[2][0]

# for grupa_proizvoda in proizvodi:
#     print(grupa_proizvoda) # lista
#     for proizvod_pojedinacni in grupa_proizvoda:
#         print(proizvod_pojedinacni)

# for kategorija_proizvoda in proizvodi:
#     for proizvod in kategorija_proizvoda:
#         print(proizvod)

# python22 = [
#     ["marija", "jovana", "marko", "petar"],
#     ["katarina", "aleksa", "milica", "sofija"]

# ]

# for grupa in python22:
#     # print(grupa)
#     for ime in grupa:
#         print(ime)

# for i in range(len(python22)): # spoljasna grupa stavki
#     print(python22[i])
#     for y in range(len(python22[i])): # unutrasnji element stavki
#         print(python22[i][y])

# Tuple

# osoba = ("Sofija", 30, True)
# print(osoba[0])

# ime, godine, aktivan = osoba
# print(ime, godine, aktivan)

# redni_brojevi = (1,) # Racuna kao tuple sa , kada ima 1 u zagradi

# osoba = ("Katarina",)

# br = [1, 2, 3] # Iznacuje poslednji ubacen broj i vrati sta je jos izbacio
# print(br.pop())
# print(br)

# print(br.pop(0)) # Iznacio 1 ostala 2 sama

# print(br)
while True:
    biblioteka = [
        ["Mali pric", "Link", 123],
        ["Uvod u Python", "Link", 456],
        ["Knjiga o plivanju", "Link", 789]
    ]
    print("Opcije: 1 - Unos, 2 - Prikaz, 3 - Brisanje, 10 - Izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos nove knjige - uzmi podatke od korisnika
        naslov = input("Unesite naslov: ")
        autor = input("Unesite ime autora: ")
        isbn = input("Unesite isbn: ")
        knjiga = [naslov, autor, isbn] # nova knjiga

        biblioteka.append(knjiga) # smestanje u visedimenzijonalnu listu
        print("Uspesno dodata knjiga.")
    elif komanda == 2:
        # prikazi sve knjige iz biblioteke
        for knjiga in biblioteka:
            for informacija in knjiga:
                print(informacija)
                print("--------------------------")
    elif komanda == 3:
        # ovde treba pitati za isbn obrisati tu knjigu/te knjige
        # brisanje
        isbn_za_brisanje = input("Unesite isbn knjige: ")
        for knjiga in biblioteka:
            for informacija in knjiga:
                if informacija == isbn_za_brisanje:
                    biblioteka.remove(knjiga)
    elif komanda > 3:
        break
