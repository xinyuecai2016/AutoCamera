import socket
import time

def GetCoordinate():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#IPV4,TCP协议
    sock.bind(('127.0.0.1',54377))#绑定ip和端口，bind接受的是一个元组
    sock.listen(5)#设置监听，其值阻塞队列长度，一共可以有5+1个客户端和服务器连接
    a=[x for x in range(40960,41160)]
    print("start server")
    while True:
        a=[x + 1 for x in a]
        s=str(a)#将数据转化为String
        connection, address = sock.accept()#等待客户请求
        print("client ip is:",address)#打印客户端地址
        buf = connection.recv(40960)#接收数据,并存入buf
        connection.send(bytes(s, encoding = "utf8"))#发送数据
        print(s)
        connection.close()#关闭连接
        time.sleep(1)
    sock.close()#关闭服务器