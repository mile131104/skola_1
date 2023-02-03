import socket

server = socket.socket()
adresa = ("0.0.0.0", 8000)
server.bind(adresa)
server.listen()
telefon, udaljena_adresa = server.accept()

# print(telefon, udaljena_adresa)
pitanje = telefon.recv(128)
print(pitanje)
odgovor = b"Evo nije lose"
telefon.send(odgovor)
