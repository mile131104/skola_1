import socket

c = socket.socket()
c.connect("0.0.0.0", 8000)
c.send(b"GET /dovla.txt HTTP/1.1\r\nhost: gresnik.com")

odgovor =               c.recv(1024)
zaglavlje_i_telo =      odgovor.decode().split("\r\n\r\n")
zaglavlje =             zaglavlje_i_telo[0]
telo =                  zaglavlje_i_telo[1]
print(zaglavlje, telo)
