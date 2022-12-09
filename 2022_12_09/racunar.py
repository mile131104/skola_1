class Laptop:

    touch_pad = True # Klasno svojstvo - staticko 

    def __init__(self, model, ram, ssd, cena): # Konstuktor / inicijalizator
        print("Kreiram jedan laptop")
        self.model = model
        self.ram = ram
        self.ssd = ssd
        self.cena = cena

    @staticmethod # Metod - Staticki - ne treba objekat za njegov poziv
    def ukljuci(): # Metod
        print("Laptop je ukljucen")
    
    def iskljuci(self): # Metod - instacni - treba objekat za njegov
        print("Laptop je iskljucen")

laptop1 = Laptop("Dell", "12 GB", "512 GB", 800) # konstruktor / inicijalizator
print(laptop1.model)
print(laptop1.cena)
print(laptop1.ssd)
print(laptop1.ram)



rec = "ABC" # instanca string tipa
rec.lower() # poziv metode lower() nad instancom (objektom)

len(rec)
