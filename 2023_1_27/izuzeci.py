class WrongOperation(Exception):
    def __str__(self):
        return "Wrong Operation (+, -, *, /)"

def Kalkulator(a, b, operacija):
    operatori = ["+", "-", "*", "/"]
    if operacija not in operatori:
        raise WrongOperation("Pogresan operator")
    else:
        if operacija == "+":
            print(a + b)
        elif operacija == "-":
            print(a - b)
        elif operacija == "*":
            print(a * b)
        elif operacija == "/":
            print(a / b)
try:
    Kalkulator(10, 5, "/")
except WrongOperation:
    print("Pogresna operacija")
except ZeroDivisionError:
    print("Nije moguce podeliti sa nulom")
except Exception:
    print("Greska")

