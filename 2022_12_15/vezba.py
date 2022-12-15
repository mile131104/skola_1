import random
import time # Upravljamo vremenom

class Team:
    
    def __init__(self, naziv):
        self.naziv = naziv

class Score:

    domaci = 0
    gosti = 0

class Match:
                    #   t1      t2      0       Score
    def __init__(self, domaci, gosti, minuti, rezultat):
        self.domaci = domaci
        self.gosti = gosti
        self.minuti = minuti
        self.rezultat = rezultat # Score()

    def prikazi(self):
        print(f"{self.domaci.naziv} - {self.gosti.naziv}")
        print(f"\t{self.rezultat.domaci} - {self.rezultat.gosti}")


    def start(self):
    # Pocinje utakmica
        print("Utakmica zapoceta")
        self.prikazi()
        while True:
            moj_broj = 5
            drugi_broj = 7
            
            menjam_gostima = random.randint(0, 10) == moj_broj
            menjam_domacima = random.randint(0, 10) == drugi_broj

            if menjam_gostima == True:
                self.rezultat.gosti +=1
            else:
                self.rezultat.gosti += 0
            if menjam_domacima == True:
                self.rezultat.domaci +=1
            else:
                self.rezultat.domaci +=0
            # if self.minuti == 25:
            #     self.rezultat.domaci +=1
            # elif self.minuti == 36:
            #     self.rezultat.gosti +=1
            # elif self.minuti == 88:
            #     self.rezultat.domaci +=1
            
            self.rezultat.domaci = random.randint(0, 10)
            self.rezultat.gosti = random.randint(0, 10)
            self.prikazi()
            time.sleep(0.7)
            if self.minuti > 90:
                print("Utakmica je zavrsena..")
                return
            self.minuti += 1


tim1 = Team("Argentina")
tim2 = Team("Francuska")
            #    t1     t2   int   Score
utakmica = Match(tim1, tim2, 0, Score)

utakmica.prikazi()
utakmica.start()
