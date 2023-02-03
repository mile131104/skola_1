import socket

klijent = socket.socket()
klijent.connect("127.0.0.1", 8000)

klijent.send(b"2")
odgovor = klijent.recv(256)
print(odgovor.decode())
