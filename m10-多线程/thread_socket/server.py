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

def server_rec(connet):
    thread_name=threading.current_thread().name
    print(thread_name, ':进入线程')     
    while True:
        data = connet.recv(1024)#阻塞方式接收数据
        message = data.decode('utf8')#转换为string数据
        print('\n%s: 接收到消息：%s' %(thread_name, message) )
        
def server_send (connet):
    thread_name=threading.current_thread().name
    print(thread_name, ':进入线程')     
    while True:
        message = input('\n%s: 输入要发送的消息: \n'%thread_name)#输入要发送的消息
        data = bytes(message,encoding='utf8')#转换为bytes数据
        connet.send(data)#发送数据
 
if __name__ == '__main__':
    print('开启服务端.....')
    #创建socket服务端实例
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #绑定端口
    skt.bind(('127.0.0.1',19200))
    #监听端口
    skt.listen(100)
    #等待连接
    print('\n等待连接......')
    connet, address = skt.accept()
    print('客户端地址：%s，建立连接' % str(address))

    #开启接收和发送线程
    t1 = threading.Thread(target=server_send, name='server_send',args=(connet,)  )
    t2 = threading.Thread(target=server_rec, name='server_rec',args=(connet,) )
    t1.start()
    t2.start()
    
    while True:pass
    #关闭连接
    #connet.close()
 