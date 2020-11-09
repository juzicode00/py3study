'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.11.1
'''
 
import os,time, multiprocessing

def func1():
    proc_id = os.getpid()
    print('进入进程:  pid = ', proc_id)
    loop_cnt=0
    while True:
        loop_cnt+=1
        print(proc_id,':loop_cnt:',loop_cnt)
        time.sleep(1)
    print('退出进程:  ' , proc_id)

if __name__ == '__main__':
    print('\n-----欢迎来到www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')   
    print('进入主进程: ', 'pid = ', os.getpid())
    #p1 = multiprocessing.Process(target=func1, name='func1',daemon=False)
    p1 = multiprocessing.Process(target=func1, name='func1',daemon=True)
    p1.start()
    while True:
        inp = input('----->')
        if inp.lower() == 'quit':
            break
    print('退出主进程: ', 'pid = ', os.getpid())