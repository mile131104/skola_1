import time

# def rezerva():
#     print("Trenutno ste na rezervi")

# def vozi(gorivo, aktivacija_rezerva):
#     limit_rezerva = 10
#     while gorivo >= 0:
#         print(f"Trenutno: {gorivo}")
#         gorivo -= 5
#         if gorivo <= 10:
#             aktivacija_rezerva()
#         time.sleep(0.5)
# vozi(40, rezerva)

class Sluzba:
    pretplatnici = []

    def dodaj_preplatnika(self, korisnik):
        if isinstance(korisnik,Listener): # provera da li ima mogucnost pretplate
            self.pretplatnici.append(korisnik)
    
    def ukloni_preplatnika(self, korisnik):
        self.pretplatnici.remove(korisnik)
    
    def posalji_obavestenje(self, poruka):
        for korisnik in self.pretplatnici:
            korisnik.primi_poruku(poruka)

import abc

class Listener(abc.ABC):
    def primi_poruku(poruka):
        pass

class Korisnik(Listener):
    def __init__(self, ime):
        self.ime = ime
    def __str__(self):
        return f"Ovo je osoba, ime: {self.ime}"
    
    def primi_poruku(self, poruka):
        print(f"Korisnik {self.ime} je primio poruku: {poruka}")

class Predavac(Listener):
    def __init__(self, ime_predavaca):
        self.ime_predavaca = ime_predavaca
    def primi_poruku(self, poruka):
        print(f"Poruka stigla i predavacu: {self.ime_predavaca}, poruka: {poruka}")

sluzba = Sluzba()

kor1 = Korisnik("Aleksandra")
kor2 = Korisnik("Vladimir")
kor3 = Korisnik("Vuk")
predavac = Predavac("Aleksandra Arsic")
# Dodavanje pretplatnika
sluzba.dodaj_preplatnika(kor1)
sluzba.dodaj_preplatnika(kor2)
sluzba.dodaj_preplatnika(kor3)
sluzba.dodaj_preplatnika(predavac)

print(sluzba.pretplatnici)
# slanje poruke svima!
sluzba.posalji_obavestenje("Promena termina predavanja")
sluzba.ukloni_preplatnika(kor1)
sluzba.posalji_obavestenje("Promena termina predavanja")

# # pregled trenutnih pretplatnika
# for korisnik in sluzba.pretplatnici:
#     print(korisnik)

