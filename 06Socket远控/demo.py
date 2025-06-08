import socket

# s = socket.socket()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('localhost', 8000))

print(s)    # <socket.socket fd=3, family=2, type=1, proto=6, laddr=('127.0.0.1', 8000)>


'''
【最重要的两个参数】
1、family
套接字家族：使用什么样的协议
1. AF_INET ==> IPv4 (默认值)
2. AF_INET6 ==> IPv6
3. AF_UNIX  ==> UNIX socket


2、type
套接字样式：面向连接、非连接
socket.SOCK_STREAM ==> TCP  流套接字
socket.SOCK_DGRAM  ==> UDP  数据报套接字
socket.SOCK_RAW    ==> 原始套接字
socket.SOCK_RDM    ==> RDM  无连接的套接字
'''
