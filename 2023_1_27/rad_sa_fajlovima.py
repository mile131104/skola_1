# fajl = open("podaci.txt", "r+") # Otvaranje i dobavljanje 
# print(fajl.read())

# sadrzaj_fajla = fajl.read() # Citanje
# fajl.write("Ovo je novi zapis")
# print(fajl.read())
# fajl.close() # Zatvaranje 

import csv

fajl = open("podaci.csv")
reader = csv.reader(fajl)
broj_upisanih_python = 0
for red in reader:
    for podatak in range(len(red)):
        print(red[podatak])
        if red[podatak] == "python":
            broj_upisanih_python += 1
print(broj_upisanih_python)
