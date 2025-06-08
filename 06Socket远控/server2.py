import socket

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

data, addr = s.recvfrom(1024)   # 获取到客户端的地址
print(f'{addr[0]}:{addr[1]}: {data.decode()}')  # 127.0.0.1:60955: hello
# 想要数据流通必须要绑定端口，否则无法接收数据，此时他会接收的时候绑定上随机端口

s.sendto(b'word', addr)  # 发数据给客户端

