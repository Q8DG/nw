import socket

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

data, addr = s.recvfrom(1024)  # 接收客户端数据

while True:
    s.sendto(input('server > ').encode(), addr)


