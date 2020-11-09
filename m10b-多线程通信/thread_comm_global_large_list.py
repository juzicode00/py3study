'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
 
import time, threading,random
inp = []
cmd=''
def func_input():
    print('进入线程:  ', threading.current_thread().name)
    while True:
        global inp
        global cmd
        if cmd.lower() == 'quit':
            break
            
        inp.clear()
        print('\n legth = 20000' )
        for l in range(20000):
            inp.append(l)
            
        inp.clear()
        print('\n legth = 10' )
        for l in range(10):
            inp.append(l)
        time.sleep(1)
    print('退出线程: ' ,threading.current_thread().name)
    
def func_output():
    print('进入线程:  ', threading.current_thread().name)
    while True:
        global inp
        global cmd
        if cmd.lower() == 'quit':
            break
        for i in inp :
            time.sleep(0.3)
            print(i,end=',')
    print('退出线程: ' ,threading.current_thread().name)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    t1 = threading.Thread(target=func_output, name='func_output')
    t2 = threading.Thread(target=func_input, name='func_input')
    t1.start()    
    t2.start()
    while True:
        #global cmd
        cmd = input('输入命令：')
        if cmd.lower() == 'quit':
            time.sleep(5)
            break
    print('退出主线程: ' ,threading.current_thread().name)