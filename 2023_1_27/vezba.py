import csv
fajl = open("vezba.csv")
reader = csv.reader(fajl)

ime = input("Unesite ime: ")
sifra = input("Unesite sifru: ")

for red in reader:
    if red[0] == ime and red[1] == sifra:
        print(f"Stanje je: {red[2]}")
        break
    else:
        print("Pogresni podaci")