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
     
if __name__ == '__main__':
    print('进入主线程: ', threading.current_thread().name)
    para1 =11
    t0 = threading.Thread(target=func_one_para, name='func-0',args=(para1))
    t0.start()
    time.sleep(1)
    
    print('退出主线程: ' ,threading.current_thread().name)