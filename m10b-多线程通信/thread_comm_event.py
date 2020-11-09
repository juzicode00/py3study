'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
 
import time,threading,sys
from threading import Thread
from threading import Event

def thread_1(event):
    print('进入线程:  thread_1')
    loop_cout = 100
    while True:
        time.sleep(0.5)
        event.wait()#无入参表示无限等待，有入参时必须是float类型的时长
        loop_cout += 1
        print('接收到一次evnet.set(),loop_cout =',loop_cout)
        event.clear()#清除event标志位，为下次触发做准备
    print('退出线程:  thread_1' )
    
def thread_2(event):
    print('进入线程:  thread_2')
    loop_cout = 200
    while True:     
        inp = input('\n输入"set"触发一次事件: ')
        if inp.lower() == 'set':
            event.set()
        
    print('退出线程:  thread_2' )
    
if __name__ == '__main__':
    print('-----欢迎来到 www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')  
    #创建event实例
    event=Event()
    #开启线程
    t1 = Thread(target=thread_1,args=(event,),name='thread_1',daemon=True)
    t2 = Thread(target=thread_2,args=(event,),name='thread_2',daemon=True)
    t1.start()
    t2.start()  
    #进入主进程循环过程
    while True:
        time.sleep(3)
        
    print('退出主线程')    