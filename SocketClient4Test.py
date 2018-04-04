import socket
import time
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 54377))
i=0
while True:
    i=i+1
    buffer = [i, i*100, i*200, i*300, i*400]
    s.send(bytes(str(buffer),'utf8'))
    time.sleep(2)
    if(i==5):
        s.close()
        break