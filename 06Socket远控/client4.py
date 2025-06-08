import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'client add listen', ('localhost', 8000))     # 发数据给服务端，不加服务端会出现bug（相当于初始化操作）

while True:
    data, _ = c.recvfrom(1024)      # _ 表示地址（已知，置空）
    print(data.decode())
    


'''
实现client连接后只接收消息


'''