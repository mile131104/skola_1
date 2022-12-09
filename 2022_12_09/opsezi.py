x = 10 # globalna promenljiva

def proba():
    # lokalni opseg
    # print(x)
    global a
    a = 15 # lokalna promenljiva

proba()

# proba(a)

