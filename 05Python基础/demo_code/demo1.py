import socket
import os
import threading


# 定义一个函数，用于扫描指定IP地址上指定端口是否开放
def port_scan(ip, port):
    # 创建一个socket对象
    s_port = socket.socket()
    try:
        # 设置超时时间为0.5秒
        s_port.settimeout(0.5)
        # 连接到指定IP地址和端口号
        s_port.connect((str(ip), int(port)))
        # 如果连接成功，则返回True
        return True
    except:
        # 如果连接失败，则返回False
        return False
# # 调用port_scan函数测试指定IP地址和端口是否开放
# print(port_scan('127.0.0.1', 7890))
# print(port_scan('127.0.0.1', 7891))


# 定义一个函数，用于检查指定IP地址是否可以ping通
def ip_scan(ip):
    # 调用系统命令执行ping操作，并将结果保存到变量res中
    res = os.popen(f"ping -n 1 {ip}").read()
    # 如果结果中包含"TTL"字符串，则表示ping通了，返回True
    if('TTL' in res):
        return True
    else:
        # 否则表示ping不通，返回False
        return False
# # 调用ip_scan函数测试指定IP地址是否可以ping通
# print(ip_scan('127.0.0.1'))
# print(ip_scan('1217.0.0.1'))


def port_scan(ip, port):
    try:
        # 创建套接字对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间为1秒
        s.settimeout(1)
        # 尝试连接到目标IP和端口
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
# # 调用端口扫描函数，扫描IP为'127.0.0.1'的80端口
# print(port_scan('127.0.0.1', 80))
# print(port_scan('127.0.0.1', 81))



# def p_sc(port):
#     if port_scan('127.0.0.1',port):
#         print(f'open {port}')
#
# from threading import Thread
# for port in range(1,8000):
#     # print(port)
#     Thread(target=p_sc,args=(port,)).start()


def port_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        print(f"Port {port} is open")
    except:
        pass
def threaded_port_scan(ip, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=port_scan, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
# # 定义要扫描的端口范围
# ports_to_scan = [80, 443, 3389, 22, 21]
# # 调用多线程端口扫描函数，扫描IP为'127.0.0.1'的指定端口范围
# threaded_port_scan('127.0.0.1', ports_to_scan)
