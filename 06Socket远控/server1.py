import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

# print(s)

# 接收数据
# print(s.recv(1024))
print(s.recv(1024).decode())    # bytes



'''
# 函数
.bind() 绑定地址
.recv() 接收数据，会进入阻塞状态
.recvfrom() 接收数据(会带地址)，会进入阻塞状态
.send() 发送数据
.sendto() 发送数据(会带地址)
.close() 关闭套接字
.connect() 连接
.accept() 接受连接
.listen() 监听


所有的数据在传输的时候 都是 bytes 类型 

'''