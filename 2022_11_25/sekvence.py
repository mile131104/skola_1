
blacklist = ["Peter", "Sally", "John"]
users = []

while True:
    ime = input("Unesi ime: ")
    if ime == "q":
        break
    elif ime in blacklist:
        print("Nedozvoljen pristup")
    else:
        users.append(ime.upper())

    print(users)
    exit(0)
