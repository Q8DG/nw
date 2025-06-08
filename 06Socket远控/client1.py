import socket

c = socket.socket(type=socket.SOCK_DGRAM)
c.connect(('localhost', 8000))

# print(c.sendto('hello', ('localhost', 8000)))   # 报错，需要编码
# print(c.sendto(b'hello', ('localhost', 8000)))    # 编码1
print(c.sendto('hello'.encode(), ('localhost', 8000)))  # 编码2



'''
目前实现了最简单的通信过程，一发一收

渗透 
很少主动连接对⽅ 
⽊⻢ 

C2：持续监听，等待⽊⻢连接


新问题出来了：对⽅能给我们发消息，我们怎么给对⽅发消息？

'''