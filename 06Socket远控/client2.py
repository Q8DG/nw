import socket

c = socket.socket(type=socket.SOCK_DGRAM)
c.connect(('localhost', 8000))

print(c.sendto(b'hello', ('localhost', 8000)))  # 发数据给服务端

print(c.recvfrom(1024))     # (b'word', ('127.0.0.1', 8000))