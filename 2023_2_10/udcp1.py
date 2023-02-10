import socket

c = socket.socket(type=socket.SOCK_DGRAM)
c.sendto(f"Hello".encode(), ("127.0.0.1", 8000))
print(c.recv(128))
