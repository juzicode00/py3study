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
    loop_cnt=0
    while True:
        loop_cnt+=1
        print(thread_name,':loop_cnt:',loop_cnt)
        time.sleep(1)
    print('退出线程:  ' , thread_name)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func1, name='func1-1',daemon=False)
    #t1 = threading.Thread(target=func1, name='func1-1',daemon=True)
    t1.start()
    while True:
        inp = input('----->')
        if inp.lower() == 'quit':
            break
    print('退出主线程: ' ,threading.current_thread().name)