'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.11.1
'''
 
import os,time, multiprocessing

def func1():
    proc_name = multiprocessing.current_process().name
    proc_id = os.getpid()
    print('进入进程:  pid = ', proc_id,' name=',proc_name)
    print('父进程id:  ', os.getppid())
    loopcnt = 0
    while loopcnt < 5:
        loopcnt = loopcnt + 1
        print('进程: %s, loopcnt=%d' % (proc_id, loopcnt))
        time.sleep(0.2)
    print('退出进程:  ' , proc_id)

    
if __name__ == '__main__':
    print('\n-----欢迎来到www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')   
    proc_name = multiprocessing.current_process().name
    proc_id = os.getpid()
    print('进入主进程:  pid = ', proc_id,' name=',proc_name)
    print('主进程的父进程id:  ', os.getppid())    
    p1 = multiprocessing.Process(target=func1, name='func1')
    p2 = multiprocessing.Process(target=func1, name='func2')
    p1.start()
    p2.start()
    print('子进程1的名称：',p1.name)
    print('子进程2的名称：',p2.name)
    print('当前活动子进程数：', multiprocessing.active_children())
    print('子进程1是否存活：',p1.is_alive())
    print('子进程2是否存活：',p2.is_alive())
    time.sleep(5)
    print('主进程延时5s后：')
    print('子进程1是否存活：',p1.is_alive())
    print('子进程2是否存活：',p2.is_alive())    
    print('退出主进程: ' ,proc_id)
