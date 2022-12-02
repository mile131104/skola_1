# pozdrava informacija sa informacijom o datumu
# print("Cao!!!")
# print("Danasnji datum je 02.12")

# ime = "Ana"
# ime.capitalize()

# print(len(ime))

def prikazi_poruku():   # potpis funkcije
    # telo funkcije
    print("Cao")
    print("Danasnji datum je 2.12.2022")
    print("Ovo je grupa 1")

prikazi_poruku()

# deklaracija i definicija
def pokreni_motor():
    print("Ubacen kljuc")
    print("Ukljucen je motor automobila")

pokreni_motor() # poziv funkcije

# ulazni parametar funkcije / unutrasnjost zagrade

ime = "mile"

# name - ulazni parametar funkcije
def posalji_poruku(name, smer):
    print(f"Hello! {name}")
    print(f"Vi ste na smeru: {smer}")

posalji_poruku("Katarina", "Python") # poziv i prosledjivanje vrednosti

# student taj i taj ... broj poena toliko ...
def prikazi_rezultate(ime="Nepoznato ime", broj_poena=0): # Ako ne unesemo poene u prikazi_rezultate linija 40 printace poene = 0, ako unesemo nesto nase to ce da i isprinta
    print(f"Student: {ime}, Broj poena: {broj_poena}")

prikazi_rezultate("Nemanja")

prikazi_rezultate("Marko", 85)

prikazi_rezultate()

# sabiranje
# ulazni parametri su a i b i stampa se rezultat

def sabiranje(a = 0, b = 0):
    rezultat = a+b
    print(f"Rezultat: {a} + {b} = {rezultat}")
    print(a + b)

sabiranje(100, 200)

sabiranje(10, 50)

sabiranje (10)

sabiranje(b = 50)

# prvi sabirak, drugi operacija
def kalkulator(a, b, operacija):
    if operacija == "+":
        print(a + b)
    elif operacija == "-":
        print(a - b)
    elif operacija == "*":
        print(a * b)
    elif operacija == "/":
        print(a / b)
        if b == 0:
            print("Nije dozvoljeno deljenje sa 0!")
        else:
            print(a / b)
    else:
        print("Proverite operaciju (+,-,*,/)")

kalkulator(100, 300, "+")

ucesnici22 = {
    "SRB": {
        "drzava": "Srbija",
        "boja": ["plava", "zuta"],
        "pobede": 1
    },
    "FRA": {
        "drzava": "Francuska",
        "boja": ["crvena", "zuta"],
        "pobede": 2
    }
}

# OZNAKA: SRB
# detalji:
# drzava: Francuska
# boja: crvena
# boja: zuta
# pobede: 2
# --------------

def prikazi_ucesnike(spisak_ucesnika):
    for (oznaka, detalji) in spisak_ucesnika.items():
        print(f"OZNAKA: {oznaka}")
        for (kljuc, vrednost) in detalji.items():
            if kljuc == "boje":
                for boja in vrednost:
                    print(f"Boja: {boja}")
            else:
                print(kljuc.capitalize(), vrednost)

prikazi_ucesnike(ucesnici22)

ucesnici26 = {
    "SRB": {
        "drzava": "Srbija",
        "boja": ["plava", "zuta"],
        "pobede": 1
    },
    "FRA": {
        "drzava": "Francuska",
        "boja": ["crvena", "zuta"],
        "pobede": 2
    }
}

prikazi_ucesnike(ucesnici26)

