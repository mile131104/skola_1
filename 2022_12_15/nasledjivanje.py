# Ime # Prezime

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def predstavi_se(self):
        print(f"Ime: {self.ime}, Prezime: {self.prezime}")

# Self - Objekti
# Super - Roditelj klasa objekat
class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa

    def prijavi_ispit(self):
        print("Ispit prijavljen.")

o1 = Osoba("Petar", "Petrovic") # Konstruktor klase Osoba()
s1 = Student("Jovan", "Markovic", "555/22") # Konstruktor klase Student()
s1.predstavi_se()
s1.prijavi_ispit()


class Vozilo:
    # model, broj sedista
    def __init__(self, model, broj_sedista):
        self.model = model
        self.broj_sedista = broj_sedista
    
    def pokreni(self):
        print("Vozilo u pokretu.")

    def parkiraj(self):
        print("Vozilo je parkirano.")

class Automobil(Vozilo):
    def __init__(self, model, broj_sedista, boja, gorivo):
        super().__init__(model, broj_sedista)
        self.boja = boja
        self.gorivo = gorivo

a1 = Automobil("BMW", "5", "Crna", "Dizel")
a1.pokreni()
a1.parkiraj()
