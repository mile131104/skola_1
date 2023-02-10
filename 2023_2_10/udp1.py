import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 0000))

while True:
    paket, adresa = s.recvfrom(128)
    paketstring = paket.decode()
    s.sendto(f"Zdravo i tebi {paketstring}".decode(), adresa)
    print(paket,adresa)
