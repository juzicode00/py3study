'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.10.30
'''
 
import time,threading,sys
from threading import Thread
from multiprocessing  import Manager

if __name__ == '__main__':
    print('-----网址: www.juzicode.com')
    print('-----公众号: 桔子code/juzicode \n')  

    manager = Manager()

    man_dict = manager.dict()
    print(type(man_dict)) 
    man_dict['thread_1'] = 0
    man_dict['thread_2'] = 1
    man_dict['send_to_sub_cmd']=None
    print(man_dict) 
    
    man_list = manager.list()
    print(type(man_list))
    man_list = [1,2,3,4,5]
    print(man_list)
    
    m_list=[]
    for i in range(5):
        m_list.append(Manager())
        time.sleep(1)
    while True:time.sleep(10)
