# server5.py
import socket

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

while True:
    data, addr = s.recvfrom(10240)  # 接收客户端数据
    print(f'{addr[0]}:{addr[1]}: {data.decode()}')
    s.sendto(input('server > ').encode(), addr)