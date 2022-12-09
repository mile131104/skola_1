class Car:
    # make, model, year, wheel
    wheels_num = 4 # staticko svojstvo
    def __init__(self, make, model, year, registrovan): # Konstruktor / inicijalizator
        self.make = make
        self.model = model          # dodela vrednosti svojstvima
        self.year = year
        self.registrovan = registrovan
    @staticmethod
    def broj_tockova():
        print("Informacije: svaki automobil ima 4 tocka")

    def registruj(self):
        print("Registracija je obavljena")
        print(f"Registrovan je: {self.model}")
        self.registrovan = True
        # car1.registrovan = True

# Car.broj_tockova()
# print(Car.wheels_num)

# car1 = Car("Volvo", "XC40", 2019, True) # Kreiranje objekta
# print(car1.model)
# print(car1.wheels_num)
# # car1.model = "dasdasdgfdf" - Izmena vrednosti

# car2 = Car("Opel", "Astra", 2013, False)

# car3 = Car("Citroen", "C4", 2020, False)

# vozni_park = [car1, car2, car3]

# print(car3.registrovan)
# car3.registruj()
# print(car3.registrovan)

# for auto in vozni_park:
#     auto.registruj()
