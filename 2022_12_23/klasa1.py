import abc

class Proizvod:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena

    def __str__(self):
        return f"Naziv: {self.naziv}, Cena: {self.cena}"
    
    def __add__(self, drugi):
        if isinstance(drugi, Proizvod) and isinstance(self, Proizvod):
            return self.cena + drugi.cena
        else:
            return "Operandi moraju biti tipa Prozivod"

    def __eq__(self, drugi):
        # Poredjenje - jednakost ==
        return self.cena == drugi.cena

p1 = Proizvod("Laptop", 500) # tip proizvod
test = 200                   # tip int
print(test)
print(p1)
p2 = Proizvod("Telefon", 200)
print(p2)

x = 10 # int
y = 20 # int
print(x + y)

poruka1 = "Cao"          # string
poruka2 = ", dobrodosao" # string
print(poruka1 + poruka2) # Sabiranje instanci tipa string

print(p1 + p2) # Sabiranje instanci tipa Proizvod
print(p1 + 15)

print(p1 == p2) # Logika za poredjenje tipa Proizvod

p3 = Proizvod("Mis", 100)
ukupan_racun = p1 + p3
print(ukupan_racun)

# import abc
from abc import * # Uklanja .

class Student(abc.ABC):
    @abstractmethod
    def prijavi_ispit(self, naziv_ispita):
        pass
    @abstractmethod
    def upisi_godinu(self):
        pass

class HarvardStudent(Student):
    def __init__(self, ime, indeks):
        self.ime = ime
        self.indeks = indeks
    
    def prijavi_ispit(self, naziv_ispita):
        return f"Prijavljen je ispit. Ime: {self.ime}, a ispit: {naziv_ispita}"
    
    def upisi_godinu(self):
        return f"Postovani/a {self.ime} upisali ste godinu."

st1 = HarvardStudent("Ana", "333-55")
print(st1.prijavi_ispit("Programiranje"))
print(st1.upisi_godinu())

# s = Student()

class Kartica(ABC):
    def __init__(self, stanje, broj_kartice):
        self.stanje = stanje
        self.broj_kartice = broj_kartice
    @abstractmethod
    def plati(self, iznos):
        pass

class Viza(Kartica):
    def plati(self, iznos):
        self.stanje -= iznos
        print(f"Placanje uspesno, Novo stanje: {self.stanje}")

v1 = Viza(500, "111")
v1.plati(100)
