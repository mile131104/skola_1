import socket

klijent = socket.socket()
adresa = ("127.0.0.1", 8000)
klijent.connect(adresa)
poruka = b"Dobar dan"
klijent.send(poruka)
odgovor = klijent.recv(128)
print(odgovor)
