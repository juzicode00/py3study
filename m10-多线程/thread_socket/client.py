'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.20
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   

import os,sys,socket,time,threading

def client_send(skt):
    thread_name=threading.current_thread().name
    print(thread_name, ':进入线程')     
    while True:
        message = input('\n%s: 输入要发送的消息: \n'%thread_name)#输入要发送的消息
        data = bytes(message,encoding='utf8')#转换为bytes数据
        skt.send(data)#发送数据

        
def client_rec(skt):
    thread_name=threading.current_thread().name
    print(thread_name, ':进入线程')     
    while True: 
        data = skt.recv(1024)#阻塞方式接收数据
        message = data.decode('utf8')#转换为string数据
        print( '\n%s: 接收到消息：%s'%(thread_name,message))
 
 
if __name__ == '__main__':
    print('开启客户端.....')
    #创建socket实例
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接，重试连接服务端
    connected = False
    for x in range(5):
        try:
            skt.connect(('127.0.0.1', 19200))
            connected = True
            break
        except:
            print('等待重连服务端.....')
    if not connected:
        print('服务端未开启')
        sys.exit(-1)
        
    #开启接收和发送线程
    t1 = threading.Thread(target=client_send, name='client_send',args=(skt ,))
    t2 = threading.Thread(target=client_rec, name='client_rec',args=(skt,  ) )
    t1.start()
    t2.start()
 
    while True:pass
        