import threading
import time

class Vozilo:
    def __init__(self, naziv, brzina):
        self.naziv = naziv
        self.brzina = brzina
        self.predjeni_put = 0
        self.distanca = 0
        super().__init__()
    
    def run(self):
        while self.predjeni_put <= self.distanca:
            self.predjeni_put += self.brzina
            print(self.naziv,"je presao",self.predjeni_put,"km")
            time.sleep(0.5)

    
    def kreni(self, distanca):
        self.start()
        self.predjeni_put = 0
        self.distanca - distanca
        print(self.naziv,"je krenuo")

class Kamion(Vozilo):
    def __init__(self):
        super().__init__("Kamion", 100)

class Automobil(Vozilo):
    def __init__(self):
        super().__init__("Auto", 150)

k = Kamion()
print(k.naziv, k.brzina)

a = Automobil()
print(a.naziv, a.brzina)

a.run()
k.run()
