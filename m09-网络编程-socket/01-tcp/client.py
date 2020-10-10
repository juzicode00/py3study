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

def client():
    #创建socket实例
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 建立连接:
    skt.connect(('127.0.0.1', 19200))
 
    current_time=time.asctime()
    msg_list = [current_time,'juzicode.com', '微信公众号：桔子code', 'Socket通信']
    for msg in msg_list:
        # 发送消息:
        data_tx = bytes(msg,encoding='utf8')
        skt.send(data_tx)
        
        # 接收消息:
        data_rx = skt.recv(1024)
        print('接收到消息：%s'%( data_rx.decode('utf8')))
        
        time.sleep(0.5)
    #退出
    skt.close()
        
        
if __name__ == "__main__":
    client()