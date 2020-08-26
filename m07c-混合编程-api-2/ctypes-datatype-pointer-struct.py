'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.8.1
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
import sys
from ctypes import *


 
class TsFruit(Structure):          #定义ctypes类型的“结构体”
    _fields_ = [('id', c_int), 
	            ('name', c_char*10),
	            ('weight', c_float),				
	            ]
		
pyt = CDLL('pytest.dll')  #加载dll
 
fruit = TsFruit(10001,b'juzi',50) #初始化
 
pyt.modify_struct_p.restype=c_int    #声明返回参数类型和入参类型
pyt.modify_struct_p.argtypes=(POINTER(TsFruit),)
pyt.modify_struct_p(pointer(fruit))           #执行
 
print('id:',fruit.id)             #使用成员变量
print('name:',fruit.name)
print('weight:',fruit.weight)
 
 
 
 
 