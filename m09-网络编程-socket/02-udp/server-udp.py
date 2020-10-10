'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.9.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   

import socket
import time

def server():
    #创建socket服务端实例
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #绑定端口
    skt.bind(('127.0.0.1',19200))
    
    while True:
        #等待消息
        data,address = skt.recvfrom(1024)
        msg = data.decode('utf8')
        print('客户端地址：%s，消息内容：%s' %(str(address),msg) )
        if not data:
            break
        #回显消息给客户端
        skt.sendto(data,address)
        time.sleep(0.5)

        
        
if __name__ == "__main__":
    server()