import socket

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

while True:
    data, addr = s.recvfrom(1024)
    print(f'{addr[0]}:{addr[1]}: {data.decode()}')
    s.sendto(input('server > ').encode, addr)

