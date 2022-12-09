# Nacrt (sema)
class Automobil:
    marka = "" # instancni osobine
    model = "" # instancni osobine
    godiste = 0 # instancni osobine
    broj_tockova = 4 # staticko svojstvo odnosi se na ceo tip sve automobile u toj klasi

print(Automobil.broj_tockova)    

automobil1 = Automobil() # Ovo je promenljiva koja cuva objekat
automobil1.marka = "Citroen" # Postavljanje osobina
automobil1.model = "C3"
automobil1.godiste = 2021

print("Marka automobila je", automobil1.marka) # Upotreba

# __ private, _ protected