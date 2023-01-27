class Korisnik:
    ime = ""
    prezime = ""

    def predstavi_se(self):
        print("....")

kor1 = Korisnik()
print(dir(kor1))

x = 5
print(type[x])

print(callable[x]) # da li moze da se pozove

def proba():
    print("proba")

print(callable(proba))
# x() ovo ne moze
proba() # call poziv
