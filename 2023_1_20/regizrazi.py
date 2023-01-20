import re

# sablon = re.compile("ita")

# tekst = "Ovo je neki tekst, rade polaznici na ita akademiji"

# if sablon.search(tekst):
#     print("Tekst sadrzi trazenu rec")
# else:
#     print("Tekst ne sadrzi rec koju trazite")

# Proveri da li se nalaze samo brojevi u stringu 
# jmbg = "1234567891011"

# sablon = re.compile("[0-9]") # Pretrazi da li sadrzi brojeve

# if sablon.findall(jmbg):
#     print("Ovaj string sadrzi brojeve")
# else:
#     print("Nema brojeva")

# print(sablon.findall(jmbg))

# [a-z] [A-Z] [0-9] _ . $ # @
# ita22.aleksandra
# ^pocetak(pocinje sa tim) $kraj(zavrsava se sa tim)

# kor_ime = "ita22.aleksandra"
# sablon = re.compile("^[a-z][0-9][a-z]$")

# if sablon.match(kor_ime):
#     print("Sadrzi")
# else:
#     print("Ne sadrzi")

# tekst_za_proveru = "Python"
# sablon = re.compile("[a-zA-Z0-9]")

# if sablon.search(tekst_za_proveru):
#     print("Sadrzi")
# else:
#     print("Ne sadrzi")

# jmbg = "1234567891011" # 13 cifara
# sablon = re.compile("^[0-9]{13}")

# if sablon.match(jmbg):
#     print("OK")
# else:
#     print("Nije ok")

# # 064/123-4567          064    / 123   - 4567
# sablon = re.compile("^[0-9]{3}/[0-9]{3}-[0-9]{4}$")

# broj_telefona = input("Unesite broj telefona: ")

# if sablon.search(broj_telefona):
#     print("Ok")
# else:
#     print("Proverite jos jednom")

# korisnicko ime
# ita22.proba
# 2 slova 2 broja . slovo (jedno ili vise)
# + jedno ili vise
# (3) - odredjeni broj npr 3 
# . jedno pojavljivanje 
# ^ i $ - pocetak i kraj

proba = "ita22.mile"

sablon = re.compile("^[a-z]+22\.[a-z]+$")

if sablon.search(proba):
    print("OK")
else:
    print("Nije OK")

# proba@proba.com

email = "mile4@proba.com"

sablon = re.compile("^[a-z0-9]+@[a-z.]+.com$")

if sablon.search(email):
    print("OK")
else:
    print("Nije OK")
