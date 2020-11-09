'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
 
import time,threading,sys
from threading import Thread
from threading import Lock

def thread_1(lock):
    print('进入线程:  thread_1')
    loop_cout = 100
    while True:
        time.sleep(0.5)
        lock.acquire()#取钥匙
        loop_cout += 1
        print('thread_1: 取到一次钥匙lock.acquire(),loop_cout =',loop_cout)
        lock.release()#还钥匙
    
def thread_2(lock):
    print('进入线程:  thread_2')
    loop_cout = 200
    while True:     
        inp = input('\n输入"acq"取钥匙或"rel"归还钥匙: \n')
        if inp.lower() == 'acq':
            lock.acquire()#取钥匙
            print('thread_2: 取到钥匙')
        if inp.lower() == 'rel':
            lock.release()#取钥匙
            print('thread_2: 归还钥匙')
            
    print('退出线程:  thread_2' )
    
if __name__ == '__main__':
    print('-----欢迎来到 www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')  
    #创建Lock实例
    lock=Lock()
    #开启线程
    t1 = Thread(target=thread_1,args=(lock,),name='thread_1',daemon=True)
    t2 = Thread(target=thread_2,args=(lock,),name='thread_2',daemon=True)
    t1.start()
    t2.start()  
    #进入主进程循环过程
    while True:
        time.sleep(3)
        
    print('退出主线程')    