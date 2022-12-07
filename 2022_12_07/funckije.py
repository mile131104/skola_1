def povrsina(a, b):
    rezultat = a * b
    print(f"Povrsina pravougaonika je: {rezultat}")
    return rezultat

povrsina(a=10, b=5)

povrsina_pravougonika = povrsina(30, 15)
print("Dobijena povrsina:", povrsina_pravougonika)


brojevi = [1, 2, 3]
print(len(brojevi))

broj_clanova = len(brojevi)
    #    <<<<       3

def konvertuj(din):
    print(f"Vrednost {din} je: {int(din / 117)} evra.")
    rezultat_evri = int(din / 117)
    return rezultat_evri

# dobijeni_rezultat = konvertuj(int(input("Unesite vrednost u dinarima: ")))


# ita22.milerakic
# def kreiraj_korisnicko_ime(ime, prezime, generacija):
#     kor_ime = f"ita{generacija}.{ime.lower()}{prezime.lower()}"
#     print(f"Vase korisnicko ime je: {kor_ime}")
#     return kor_ime

# kreiraj_korisnicko_ime("Mile", "Rakic", 22)

# ime = input("Unesite ime: ")
# prezime = input("Unesite prezime: ")
# godina = int(input("Unesite godinu (21, 22, 23....): "))
# korisnicko_ime = kreiraj_korisnicko_ime(ime, prezime, godina)

# korisnik1= {"ime": ime, "prezime": prezime, "kor_ime": korisnicko_ime}

# sabira
# a i b
# rezultat povratna vrednost
# dobijena

def sabiranje(a, b):
    sabiranje1 = a + b
    return sabiranje1

dobijena = sabiranje(10, 5)

print(dobijena)

# * pretvara u tuple ** pretvara u recnik

def evidencija(*prisutni):
    #(vrednost1, vrednost2, vrednost3, vrednost4.....)
    print(prisutni)
    print(type(prisutni))
    print(prisutni[0])
    for osoba in prisutni:
        print(osoba)

evidencija("Sofija", "Marija", "Petar", "Marko")

def evidencija(**prisutni):
    print(prisutni)
    print(type(prisutni))
    print(prisutni["python"])
    # recnik se sastoji iz kljuca i vrednosti

evidencija(python="Jovana", ios="Marija", c="Katarina")

# bankomat
# ulazni_parametri: stanje, iznos
# povratna vrednost:
# "Uspesno izvrsena transakcija, trenutno stanje: ??"
# "Nemate dovoljno novca na racunu, trenutno stanje: ??"


def bankomat(stanje, iznos):
    if stanje <= iznos:
        return f"Nemate dovoljno novca na racunu, trenutno stanje: {stanje}"
    else:
        return f"Transakcija uspesno izvrsena, trenutno stanje: {stanje - iznos}"

stanje = bankomat(stanje=1000, iznos=200)

print(stanje)

# funkcija: jeParanBroj
# broj ulazni parametar
# povratna vrednost: True ili False u zavisnosti od toga da li je broj paran

def jeParanBroj(ulazni_parametar):
    if ulazni_parametar % 2 == 0:
        print(f"Broj je paran: {ulazni_parametar}")
        return True
    else:
        print(f"Broj nije paran: {ulazni_parametar}")
        return False

# a = jeParanBroj(int(input("Unesite broj: ")))

# print(a)

# neki_broj = int(input("Unesite broj: "))

# jeParanBroj(neki_broj) # True ili False

# if jeParanBroj(neki_broj):
#     print("Broj koji ste uneli je paran")
#     print("Ovde sledi logika sa parnim brojevima")
# else:
#     print("Ne radimo sa neparnim brojevima")

def skolovanje(predavanje):
    print("Skolska godina traje...")
    print("Ucionica A21")
    # Ovde nastupa predavac...
    predavanje()

def predavanje_vn():
    print("Dobrodosli na HTML i CSS")
    print("4 termina. Cilj je da napravimo sajt.")

def predavanje_vm():
    print("Danas radimo mreze.")
    print("Da li igrate LoL?")
    print("Kreiramo bazu podataka.")

def predavanje_al():
    print("Danas ipak imamo predavanje.")
    print("A takodje i u petak.")


skolovanje(predavanje_al)

def kalkulator(a, b, operacija):
    if b > 0:
        operacija(a, b)
    else:
        print("Nije dozvoljeno deljenje sa nulom.")

def deljenje(broj1, broj2):
    print(broj1 / broj2)
      #kljucna rec              # parametri     # povratna vrednost
rez = lambda           a, b:        a + b

print(rez(10, 10))

def stampaj():
    print("Cao")
    # uslov za ponovno izvrsavanje
    stampaj()

def tajmer(sekunde):
    print(sekunde)
    sekunde -=1
    if sekunde > 0:
        tajmer(sekunde)

tajmer(10)

def provera(funkcija):
    def unutrasnja_funkcija(a, b):
        if b == 0:
            print("Nije dozvoljeno deljenje sa nulom.")
            return
        else:
            funkcija(a, b)
    return unutrasnja_funkcija

@provera # dekorator 
def podeli(a, b):
    print(a / b)


podeli(10, 2)

def izmena_probe(funkcija):
    print("Hello")
    return funkcija

@izmena_probe
def proba():
    print("Cao")

proba()

def stampaj_slovo_po_slovo():
    print("A")
    yield   # Da li ima dalje?
    print("B")
    yield   # Da li ima dalje?
    print("C")
    yield   # Da li ima dalje?

dobijeno_slovo = stampaj_slovo_po_slovo()
next(dobijeno_slovo)
next(dobijeno_slovo)
next(dobijeno_slovo)

for slovo in stampaj_slovo_po_slovo():
    print(slovo)

