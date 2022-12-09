class Osoba:
    ime = ""
    prezime = ""
    godine = 0

osoba1 = Osoba() # Objekat(instanta klase) - primerak
print(osoba1.ime)
osoba1.ime = "Petar"
osoba1.prezime = "Petrovic"
osoba1.godine = 25

print(osoba1.ime, osoba1.prezime, osoba1.godine)

osoba2 = Osoba()
# print(osoba2.ime,osoba2.prezime,osoba2.godine)

osoba2.ime = "Marija"
osoba2.prezime = "Petrovic"
osoba2.godine = 22

print(osoba2.ime,osoba2.prezime,osoba2.godine)

