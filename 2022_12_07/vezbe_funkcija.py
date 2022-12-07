# funkcija: nacrtaj
# x i y
# ############### nacrtati pravugaonik

def nacrtaj(sirina, visina):
    for x in range(visina):
        for y in range(sirina):
            if x == 0 or x == visina -1 or y == 0 or y == sirina -1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

nacrtaj(10, 10)




