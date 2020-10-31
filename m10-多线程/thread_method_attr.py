'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.20
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
 
import time, threading

def func1():
    thread_name = threading.current_thread().name
    print('进入线程:  ', thread_name)
    print(thread_name, 'get_ident():  ', threading.get_ident())
    time.sleep(1)
    print('退出线程:  ' , thread_name)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func1, name='func1-1')
    t2 = threading.Thread(target=func1, name='func1-2')
    
    print('before t1.start() t1.is_alive():',t1.is_alive())
    t1.start()
    print('after t1.start() t1.is_alive():',t1.is_alive())
    print('t1.ident:  ', t1.ident)
    
    print('active_count():  ', threading.active_count() )        
    t2.start()
    print('t2.ident:  ', t2.ident)
    print('active_count():  ', threading.active_count() )
    print('enumerate():  ', threading.enumerate())
    
    time.sleep(3)
    print('t1.is_alive():',t1.is_alive())
    print('退出主线程: ' ,threading.current_thread().name)