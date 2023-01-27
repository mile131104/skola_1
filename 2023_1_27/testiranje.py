class Kalkulator:
    def saberi(self, a, b):
        return a + b
    def oduzmi(self, a, b):
        return a - b

# dobijeno == ocekivano
# test vrednost 10 + 5 = 15

kalkulator = Kalkulator()

# TEST VREDNOSTI
broj1 = 10
broj2 = 15
# OCEKIVANO
ocekivano = broj1 + broj2 # 25
# IZRACUNAVANJE
rezultat = kalkulator.saberi(broj1, broj2)

print(ocekivano == rezultat) # PROVERA
print(f"Ocekivano: {ocekivano}, Dobijeno: {rezultat}")

calc = Kalkulator()

import unittest

class TestKalkulator(unittest.TestCase):
    calc = Kalkulator()
    # Test metode
    def test_saberi(self):
        kalkulator = Kalkulator()
        rezultat = kalkulator.saberi(10, 15)
        self.assertEqual(rezultat, 25) # Proveri da li su vrednosti jednake
    
    def test_oduzmi(self):
        rezultat = self.calc.oduzmi(5, 3)
        ocekivano = 2
        self.assertEqual(rezultat, ocekivano)

unittest.main()

