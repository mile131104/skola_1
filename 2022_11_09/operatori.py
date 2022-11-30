import random 
# kurs = "Python Fundamentals"
# print(kurs)

# a = 10
# b = 5

# print("Sabiranje:", a + b)
# print("Oduzimanje:", a - b)

# rez_mnozenja = a * b
# print("Mnozenje:", rez_mnozenja)

# rez_deljenje = a / b
# print("Deljenje:", int(rez_deljenje))

# a = 5
# b = 2

# print(5 / 2)
# print(5 // 2)

# print(10 // 3)

# print(a ** 2) # 5*5
# print(a ** 3) # 5*5*5

# a = 10
# b = 2

# # Koji je ostatak pri deljenju sa dva? 10 i 2
# print(10 % 2)

# # Koji je ostatak pri deljenju sa dva? 9 i 2
# a = 9
# b = 2
# print(a % b) # Ovde se dobija samo ostatak pri deljenju

# print(-a)

# godine = 25
# # godine + 1
# godine = godine + 1
# print(godine)

# godine += 1
# print(godine)

# godine *= 2 # Mnozi sa 2 i dodeljuje
# print(godine)
# godine * 2 # Mnozi ali ne dodeljuje

# godine /= 2
# print(int(godine))

# broj1 = 10
# broj2 = 5

# print("Prvi broj:", broj1)
# print("Drugi broj:", broj2)

# print("Rezultat:", broj1 + broj2)

# Unos iz konzole
# broj1 = input("Unesi prvi broj: ")

# broj2 = input("Unesite drugi broj: ")

# print("Sabiranje: ", int(broj1) + int(broj2))

# Postavljanje vrednosti
# pi = 3.14
# povrsina_kruga = 0

# r = float(input("Unesite r: "))

# povrsina_kruga = r ** 2 * pi
# print("Povrsina kruga je:", povrsina_kruga)

# godine = 18

# print(godine <= 18)

# print(godine != 18) # Razlicito
# print(godine == 18)

# aktuelan_kurs = "pdf"

# print(aktuelan_kurs == "PPF")

# broj = int(input("Unesite broj:"))

# ostatak = broj % 2

# print(ostatak == 0) # Ako je 0 ostatak - paran broj

# moj_broj = int(input("Unesite broj: "))
# racunar = random.randint(1, 10)

# print("Korisnik:", moj_broj)
# print("Racunar:", racunar)

# print("Pogodak:", moj_broj == racunar)

# automobil_pozicija = 0
# cilj_pozicija = 50


# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# allowed_age = 13
# godine = int(input("Enter your age: "))

# print("Allowed:", godine >= 13)

# And

# uneto_ime = "admin1"
# uneta_sifra = "123456"

# ime_baza = "admin"
# sifra_baza = "12345"

# ispravna_sifra = uneta_sifra == sifra_baza #True
# ispravno_kor_ime = uneto_ime == ime_baza #True

# uspesno_logovanje = ispravna_sifra and ispravno_kor_ime
# print(uspesno_logovanje)

'''

and

true true -> true
true false -> false
false true -> false
false false -> false

or

true true -> true
true false -> true
false true -> true
false false -> false


'''

# Or

# uneto_ime = "admin"
# uneta_sifra = "123456"

# ime_baza = "admin"
# sifra_baza = "12345"

# ispravna_sifra = uneta_sifra == sifra_baza #True
# ispravno_kor_ime = uneto_ime == ime_baza #True

# uspesno_logovanje = ispravna_sifra or ispravno_kor_ime
# print(uspesno_logovanje)

# lepo_vreme = True
# print(not lepo_vreme)

# tamna_tema = True
# print(not tamna_tema)

smer = input("Smer:")
generacija = int(input("Generacija:"))

smer_unet = smer == "Python"
generacija_uneta = generacija == 2022

konacna_provera = smer_unet and generacija_uneta

print("Uspesno", konacna_provera)








