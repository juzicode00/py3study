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
    print('进入线程:  ', threading.current_thread().name)
    loopcnt = 0
    while loopcnt < 5:
        loopcnt = loopcnt + 1
        print('线程: %s, loopcnt=%d' % (threading.current_thread().name, loopcnt))
        time.sleep(0.2)
    print('退出线程:  ' , threading.current_thread().name)

def func2():
    print('进入线程:  ', threading.current_thread().name)
    loopcnt = 0
    while loopcnt < 5:
        loopcnt = loopcnt + 1
        print('线程: %s, loopcnt=%d' % (threading.current_thread().name, loopcnt))
        time.sleep(0.3)
    print('退出线程:  ' , threading.current_thread().name)
    
if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func1, name='func1')
    t2 = threading.Thread(target=func2, name='func2')
    t1.start()    
    t2.start()
    #t1.join()
    print('退出主线程: ' ,threading.current_thread().name)