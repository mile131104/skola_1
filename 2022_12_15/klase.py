# class Osoba:
#     def __init__(self, ime, prezime, godine, ulogovan=False):
#         self.ime = ime
#         self.prezime = prezime
#         self.godine = godine
#         self.ulogovan = ulogovan
    
#     def prikazi_informacije(self):
#         je_ulogovan = "Korisnik je ulogovan" if self.ulogovan else "Korisnik nije ulogovan" # Proverava da li je svojstvo ulogovan True ili False
#         return f"Ime: {self.ime},\nPrezime: {self.prezime},\nGodine: {self.godine},\n{je_ulogovan}"

#     def uloguj_se(self): # False - > True
#         if self.ulogovan: # Provera svojstva ulogovan objekta koji zove metod
#             return "Vec ste ulogovani.."
#         else:
#             self.ulogovan == False
#             return "Ulogovani ste"

#     def izloguj_se(self): # True - > False
#         if self.ulogovan == False:
#             return "Izlogovani ste"
#         else:
#             self.ulogovan == True
#             return "Vec ste izlogovani"

#     @staticmethod
#     def broj_ociju(): # Odnosi se na celu klasu Osoba i na sve osobe
#         print("Covek ima 1 par ociju.")

# Osoba.broj_ociju()

# osoba1 = Osoba("Petar", "Petrovic", 22, True)

# osoba2 = Osoba("Marija", "Markovic", 20)

# print(osoba1.ime)

# print(osoba1.prikazi_informacije())

# print(osoba1.uloguj_se())

# print(osoba2.izloguj_se())

class Kalkulator:
    # Postavka brojeva - broj1 i broj2
    def __init__(self, broj1, broj2):

        self.broj1 = broj1
        self.broj2 = broj2

    def add(self):
        return self.broj1 + self.broj2
    
    def sub(self):
        return self.broj1 - self.broj2

    def mul(self):
        return self.broj1 * self.broj2
    
    def div(self):
        if self.broj2 == 0:
            return "Ne mozete deliti sa nulom"
        else:    
            return self.broj1 / self.broj2

# kalk1 = Kalkulator(int(input("Prvi broj:")), int(input("Drugi broj: "))) # Konkretan kalkulator operande preuzima putem input-a

# Kalk1: operand1 ??? operand2 ???
# print(kalk1.add()) # Sabiranje

kalk2 = Kalkulator(10, 2)
print(kalk2.div()) # Poziv metode

kalk2.broj1 = 15 # Izmena vrednosti
kalk2.broj2 = 20 # Izmena vrednosti

print(kalk2.div())

class Aplikacija:
    
    def __init__(self, tip, broj_korisnika, mockup, gotova=False):
        self.tip = tip
        self.broj_korisnika = broj_korisnika
        self.mockup = mockup
        self.gotova = gotova

app1 = Aplikacija("Web", 1000, True)
app2 = Aplikacija("iOS", 2000, True)
app3 = Aplikacija("Android", 1000, False)

class Firma:
    def __init__(self, naziv, broj_zaposlenih, aktivan_projekat=True):

        self.naziv = naziv
        self.broj_zaposlenih = broj_zaposlenih
        self.aktivan_projekat = aktivan_projekat

    def otpustiti_zaposlene(self, broj_radnika):

        if broj_radnika <= self.broj_zaposlenih:
            self.broj_zaposlenih -= broj_radnika
            print("Prekinuti su ugovori u radu.")
            print(f"Trenutan broj zaposlenih je: {self.broj_zaposlenih}")
        else:
            print("Naveliste ste veci broj od broja zaposlenih")

    def zaposli_nove(self, novi_zaposleni):

        if novi_zaposleni >= 0:
            self.broj_zaposlenih += novi_zaposleni
            print(f"Uspesno ste zaposlili nove ljude. Novi broj zaposlenih je: {self.broj_zaposlenih}")
        else:
            print("Molim Vas prosledite broj koji je veci od 0.")

    def preuzmi_projekat(self, aplikacija):
        # Provera mockup-a da li je True - da li postji
        if aplikacija.mockup == True:
            print(f"Preuzimam projekat {aplikacija.tip} aplikacije, i krecem da radim..")
        else:
            print("Molim Vas da dostavite i mockup")

moja_firma = Firma("Link", 100, False) # Inicijalna postavka

moja_firma.zaposli_nove(10)     # Ovde je dodato novih 10 (10)
print(moja_firma.broj_zaposlenih)
moja_firma.otpustiti_zaposlene(50)      # Izbaceno (50)

moja_firma.preuzmi_projekat(app2)


