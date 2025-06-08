import socket

c = socket.socket(type=socket.SOCK_DGRAM)
c.connect(('localhost', 8000))

while True:
    c.sendto(input('client > ').encode, ('localhost', 8000))
    print(c.recvfrom(1024))