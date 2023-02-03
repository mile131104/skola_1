import socket

mecevi = {
    1:"Zvezda : Partizan (1:1)",
    2:"Bastonia : CSK (3:2)",
    3:"Real : Barcelona (1:3)"
}

server = socket.socket()
server.bind("0.0.0.0", 8000)
server.listen()
while True:
    klijent, adresa = server.accept()
    pitanje = klijent.recv(128)
    id_meca = int(pitanje.decode().strip())
    print(id_meca)
    odgovor = mecevi[id_meca]
    klijent.send(odgovor.encode())
