import enum

#Enumeracija
# class TipSkolovanja(enum.Enum):
#     ONLINE = "Online skolovanje"
#     TRADICIONALNO = "Tradicionalno skolovanje"

#     # Sta ce biti odstanpano u konzoli kada stanpamo clana enumeracije
#     def __str__(self) -> str:
#         return f"Naziv: {self.name}, Pridruzena vrednost: {self.value}"

# upisano = TipSkolovanja.ONLINE
# print(upisano.value)

# class Korisnik:
#     def __init__(self, ime, tip_skolovanja) -> None:
#         self.ime = ime
#         self.tip_skolovanja = tip_skolovanja

# kor1 = Korisnik("Mile", TipSkolovanja.ONLINE)

# for tip in TipSkolovanja:
#     print(tip, tip.value)

# print(TipSkolovanja.ONLINE)

# class NacinPlacanja(enum.Enum):
#     KARTICOM = 1
#     KES = 2

#     def __str__(self) -> str:
#         return f"{self.name}, Tip: {self.value}"
    
# class User:
#     def __init__(self, name, payment_method) -> None:
#         self.name = name
#         self.payment_method = payment_method

# i = User("Mile", NacinPlacanja.KARTICOM)
# print(i.name, i.payment_method)


# Boje
# Pozadina #329ba8
# Tekst #32a881
# Zaglavlje #32a881

class Boje(enum.Enum):
    POZADINA = "#329ba8"
    TEKST = "#32a881"
    ZAGLAVLJE = "#32a889"

    def __str__(self) -> str:
        return f"Tip: {self.name}, Vrednost: {self.value}"
    
b1 = print(Boje.POZADINA)

        

