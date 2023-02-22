import socket

s = socket.socket()
s.connect(("localhost", 3306))
s.send(b"cao")
print(s.recv(256))
