'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
 
import time, threading
inp = ''
def func_input():
    print('进入线程:  ', threading.current_thread().name)
    while True:
        global  inp
        inp = input('\n func_input: 请输入:')
        time.sleep(0.5)
def func_output():
    print('进入线程:  ', threading.current_thread().name)
    inp_temp = ''
    while True:
        global inp
        if inp_temp != inp:
            print('\n func_display: inp = ',inp)
            inp_temp = inp
        time.sleep(0.1)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func_output, name='func_output')
    t2 = threading.Thread(target=func_input, name='func_input')
    t1.start()    
    t2.start()
    while True:pass
    print('退出主线程: ' ,threading.current_thread().name)