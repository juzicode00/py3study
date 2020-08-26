'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.8.1
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   


from ctypes import *

class TsFruit(Structure):          #定义ctypes类型的“结构体”
    _fields_ = [('id', c_int), 
	            ('name', c_char*10),
	            ('weight', c_float),				
	            ]

fruit = TsFruit(10001,b'juzi',50) #初始化
print('id:',fruit.id)             #使用成员变量
print('name:',fruit.name)
print('weight:',fruit.weight)

pyt = CDLL('pytest.dll')          #加载dll
pyt.trans_struct.restype=c_int    #声明返回参数类型和入参类型
pyt.trans_struct.argtypes=(TsFruit,)
pyt.trans_struct(fruit)           #执行
 
 
 
 
 
 
 
 
 
 
 
 
 