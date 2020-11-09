'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.11.1
包含2个进程的多进程方法
'''
 
import os,time, multiprocessing

def func1():
    proc_name = multiprocessing.current_process().name
    proc_id = os.getpid()
    print('进入进程:  pid = ', proc_id,' name=',proc_name)
    print('父进程id:  ', os.getppid())
    loopcnt = 0
    while loopcnt < 10:
        loopcnt = loopcnt + 1
        print('进程: %s, loopcnt=%d' % (proc_id, loopcnt))
        time.sleep(0.3)
    print('退出进程:  ' , proc_id)

def func2():
    proc_name = multiprocessing.current_process().name
    proc_id = os.getpid()
    print('进入进程:  pid = ', proc_id,' name=',proc_name)
    print('父进程id:  ', os.getppid())
    loopcnt = 0
    while loopcnt < 10:
        loopcnt = loopcnt + 1
        print('进程: %s, loopcnt=%d' % (proc_id, loopcnt))
        time.sleep(0.1)
    print('退出进程:  ' , proc_id)    
    
if __name__ == '__main__':
    print('\n-----欢迎来到www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')   
    proc_name = multiprocessing.current_process().name
    proc_id = os.getpid()
    print('进入主进程:  pid = ', proc_id,' name=',proc_name)
    p1 = multiprocessing.Process(target=func1, name='func1')
    p2 = multiprocessing.Process(target=func2, name='func2')
    p1.start()
    p2.start()
    time.sleep(5)
    print('退出主进程: ' ,proc_id)
