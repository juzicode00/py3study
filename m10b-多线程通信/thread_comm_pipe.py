'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
 
import time,threading,sys
from threading import Thread
from multiprocessing  import Pipe

def thread_1(conn1):
    print('进入线程:  thread_1')
    loop_cout = 100
    while True:
        time.sleep(0.5)
        
        #发送自身计数
        loop_cout += 1
        conn1.send(loop_cout)
        
        #接收线程2的计数
        msg = conn1.recv()
        print('thread_1:线程thread_2中循环计数:',msg)
        
    print('退出线程:  thread_1' )
    
def thread_2(conn2):
    print('进入线程:  thread_2')
    loop_cout = 200
    while True:     
        time.sleep(0.5)

        #接收线程1的计数
        msg = conn2.recv()
        print('thread_2: 线程thread_1中循环计数:',msg)
        
        #发送自身计数
        loop_cout += 1
        conn2.send(loop_cout)

    print('退出线程:  thread_2' )
    
if __name__ == '__main__':
    print('-----欢迎来到 www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')  
    #创建Pipe实例
    conn1,conn2=Pipe()
    #开启线程
    t1 = Thread(target=thread_1,args=(conn1,),name='thread_1',daemon=True)
    t2 = Thread(target=thread_2,args=(conn2,),name='thread_2',daemon=True)
    t1.start()
    t2.start()  
    #进入主进程循环过程
    while True:
        cmd = input('\n------>')
        if cmd == 'quit':
            time.sleep(1)
            break
    print('退出主线程')    