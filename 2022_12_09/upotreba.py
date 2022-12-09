from car import *

auto1 = Car("Opel", "Astra", 2019, True)

auto2 = Car("Ford", "Focus", 2015, False)
auto2.registruj()
print(auto2.registrovan)

auto3 = Car("Ford", "Fiesta", 2010)
print(auto3.registrovan)