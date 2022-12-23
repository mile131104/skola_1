class Automobil:
    def __init__(self, boja):
        self.__x_pozicija = 0 # Privatno svojstvo - (Private)
        self.boja = boja      # Javno svojstvo - (Public)

    def get_pozicija(self):
        print(f"Vasa trenutna pozicija je: {self.__x_pozicija}")
        return self.__x_pozicija

    def set_pozicija(self, broj_koraka):
        if isinstance(broj_koraka, int):
            self.__x_pozicija +=1
        else:
            print("Prosledite za broj koraka int vrednost")
    
a = Automobil("Crvena")
# print(a.__x_pozicija) # Nije moguce
a.get_pozicija()

a.set_pozicija(5)
a.set_pozicija("abc")

a.get_pozicija()

class Osoba:
    def __init__(self, ime):
        self.ime = ime      # Javno svojstvo
        self.__jmbg = ""    # Privatno svojstvo

    def unesi_jmbg(self, vrednost): # set_jmbg
        if isinstance(vrednost, str) and len(vrednost) == 13:
            self.__jmbg = vrednost
        else:
            print("Vrednost mora imati 13 cifara i mora biti string tipa")
    
    def prikazi_jmbg(self):     # get_jmbg
        # 1234567891011
        prikaz = self.__jmbg[0:10]
        sakriveni_prikaz = prikaz + "****"
        return sakriveni_prikaz
        # prikaz[9:12] = "******" # Na poslednja cetiri mesta imaju zvezdice
        # return prikaz

o = Osoba("Marina")
o.unesi_jmbg("1234567891011")
print(o.prikazi_jmbg())