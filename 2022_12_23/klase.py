import abc

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def predstavi_se(self):
        return f"Ja sam: {self.ime} {self.prezime}"

osoba1 = Osoba("Mile", "Rakic")
print(osoba1.ime)
print(osoba1.predstavi_se())

class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa
    
    def predstavi_se(self):
        return f"{super().predstavi_se()} moj broj indeksa je: {self.broj_indeksa}"

student1 = Student("Mile", "Rakic", "332-23")
print(student1.ime, student1.prezime, student1.broj_indeksa)
print(student1.predstavi_se())

class Profesor(Osoba):
    def __init__(self, ime, prezime, naziv_predmeta):
        super().__init__(ime, prezime)
        self.naziv_predmeta = naziv_predmeta
    
    def predstavi_se(self):
        return f"{super().predstavi_se()}, predajem: {self.naziv_predmeta}"

profesor1 = Profesor("Jovana", "Jovanovic", "Python")
print(profesor1.ime, profesor1.prezime, profesor1.naziv_predmeta)
print(profesor1.predstavi_se())

class Oblik:
    def __init__(self, boja):
        self.boja = boja
    
    def izracunaj_povrsinu(self):
        print("Racunam povrsinu...")

class Krug(Oblik):
    def __init__(self, boja, poluprecnik):
        super().__init__(boja)
        self.poluprecnik = poluprecnik

    def izracunaj_povrsinu(self):
        super().izracunaj_povrsinu()
        print(self.poluprecnik * self.poluprecnik * 3.14)

k = Krug("Crvena,", 4)
k.izracunaj_povrsinu()

#Kvadrat - Stranicu - a * a

class Kvadrat(Oblik):
    def __init__(self, boja, stranica):
        super().__init__(boja)
        self.stranica = stranica
    
    def izracunaj_povrsinu(self):
        super().izracunaj_povrsinu()
        print(self.stranica * self.stranica)

kv1 = Kvadrat("Plava", 3)
kv1.izracunaj_povrsinu()

class Kartica:
    def __init__(self, broj, stanje):
        self.broj = broj
        self.stanje = stanje

    def pay(self, suma):
        if suma <= self.stanje:
            self.stanje -= suma
        else:
            print("Nemate dovoljno.")

class Viza(Kartica):
    porez = 0.05
    def pay(self, suma):
        if suma + (suma * self.porez) <= self.stanje:
            self.stanje -= suma + (suma * self.porez)

class Master(Kartica):
    porez = 0.08
    def pay(self, suma):
        if suma + (suma * self.porez) <= self.stanje:
            self.stanje -= suma + (suma * self.porez)

viza1 = Viza("111", 500)
viza1.pay(20)
print(viza1.stanje)

master1 = Master("222", 800)
master1.pay(400)
print(master1.stanje)

class Proizvod:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena

class Racun:
    def __init__(self, stanje):
        self.stanje = stanje
    
    def plati(self, proizvod):
        if isinstance(proizvod, Proizvod):
            print(f"Kupujem {proizvod.naziv}")
            self.stanje -= proizvod.cena
        else:
            print("Molim Vas prosledite podatak tipa Proizovd.")

pr1 = Proizvod("Laptop", 500)
racun = Racun(1000)
racun.plati(pr1)
print(racun.stanje)

class Uredjaj:
    def __init__(self, naziv, seriski_broj):
        self.naziv = naziv
        self.seriski_broj = seriski_broj

class Laptop(Uredjaj):
    def __init__(self, naziv, seriski_broj, ssd):
        super().__init__(naziv, seriski_broj)
        self.ssd = ssd

class Telefon(Uredjaj):
    def __init__(self, naziv, seriski_broj, operater):
        super().__init__(naziv, seriski_broj)
        self.operater = operater

u1 = Uredjaj("Neki uredjaj", "123")
l1 = Laptop("Acer", "555", "512 GB")
t1 = Telefon("Nokia", "333", "A1")

print(isinstance(u1, Uredjaj))
print(isinstance(l1, Laptop))
print(isinstance(t1, Telefon))
print(isinstance(t1, Uredjaj))

# Abstraktna klasa - Ne moze da se instancira
class Pumpa(abc.ABC):
    @abc.abstractmethod
    def toci_gorivo(self):
        pass

class ShellPumpa(Pumpa):
    def __init__(self, naziv):
        self.naziv = naziv
    def toci_gorivo(self):
        print("Imamo dizel i benzin, cena 200 i 220")

p1 = ShellPumpa("Shell")
p1.toci_gorivo()

# pumpa = Pumpa() - Ne moze da se instancira - sablon za druge klase

