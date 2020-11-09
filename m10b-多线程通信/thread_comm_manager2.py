'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
 
import time,threading,sys
from threading import Thread
from multiprocessing  import Manager

def thread_1(man_dict):
    print('进入线程:  thread_1')
    man_dict['thread_1'] = 0
    
    while True:
        #如果主线程发送了结束命令，结束子线程
        if man_dict['send_to_sub_cmd'] == 'quit':
            print('thread_1): 主线程发来quit指令')
            break
            
        #子线程计数增加
        time.sleep(1)
        man_dict['thread_1'] += 1
        
        #在线程1中打印线程2的计数
        print('thread_1:线程thread_2中循环计数:',man_dict['thread_2'])
        
    print('退出线程:  thread_1' )
    
def thread_2(man_dict):
    print('进入线程:  thread_2')
    man_dict['thread_2'] = 0
    
    while True:
        #如果主线程发送了结束命令，结束子线程
        if man_dict['send_to_sub_cmd'] == 'quit':
            print('thread_2: 主线程发来quit指令')
            break
            
        #子线程计数增加
        time.sleep(0.5)
        man_dict['thread_2'] += 1
        
        #在线程2中打印线程1的计数
        print('thread_2: 线程thread_1中循环计数:',man_dict['thread_1'])
        
    print('退出线程:  thread_2' )
    
if __name__ == '__main__':
    print('-----欢迎来到 www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')  
    manager= Manager()
    man_dict = manager.dict()
    man_dict['thread_1'] = 0
    man_dict['thread_2'] = 0
    man_dict['send_to_sub_cmd']=None

    t1 = Thread(target=thread_1,args=(man_dict,),name='thread_1',daemon=True)
    t2 = Thread(target=thread_2,args=(man_dict,),name='thread_2',daemon=True)
    t1.start()
    t2.start()
    
    #进入主进程循环过程
    while True:
        man_dict['send_to_sub_cmd'] = input('\n------>')
        if man_dict['send_to_sub_cmd'].lower() == 'quit':
            time.sleep(3)
            break
    print('退出主线程')    