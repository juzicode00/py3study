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

def func_one_para(para1):
    print(para1)
    pass
    
def func(para1,para2,**kw):
    thread_name = threading.current_thread().name
    print('进入线程:  ', thread_name)
    print(thread_name, 'para1:  ', para1)
    print(thread_name, 'para2:  ', para2)
    print(thread_name, 'kw:  ', kw)
    print('退出线程:  ' , thread_name)

if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    para1 =1 
    t0 = threading.Thread(target=func_one_para, name='func-0',args=(para1,))

    para1 =11 
    para2 =12    
    t1 = threading.Thread(target=func, name='func-1',args=(para1 ,para2),kwargs={'age':10} )
    
    para1 =21
    para2 =22
    t2 = threading.Thread(target=func, name='func-2',args=(para1 ,para2),kwargs={'age':20}, )
    
    t0.start()
    t1.start()
    t2.start()
 
    time.sleep(1)
    
    print('退出主线程: ' ,threading.current_thread().name)