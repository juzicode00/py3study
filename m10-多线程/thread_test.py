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
    while loopcnt < 10:
        loopcnt = loopcnt + 1
        print('线程: %s, loopcnt=%d' % (threading.current_thread().name, loopcnt))
        time.sleep(0.3)
    print('退出线程:  ' , threading.current_thread().name)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func1, name='func1')
    t1.start()
    #t1.join()
    print('退出主线程: ' ,threading.current_thread().name)