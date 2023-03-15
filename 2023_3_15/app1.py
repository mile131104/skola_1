import mysql.connector as conn
import os
import time

baza = conn.connect(host="localhost",database="automobili",username="root",passwd="")

while True:
    os.system("cls")
    kurzor = baza.cursor()
    kurzor.execute("select * from automobili")

    redovi = kurzor.fetchall()


    print("Automobil u ponudi")

    for red in redovi:
        cena = float(red[4])
        print(f"Naziv: {red[1]}, cena: {cena}")
    time.sleep(0.2)
    baza.commit()


