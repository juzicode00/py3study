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

class TuTest(Union):          #定义ctypes类型的“结构体”
    _fields_ = [('a', c_char), 
	            ('b', c_int),
	            ('c', c_longlong)		
	            ]

test = TuTest( b'a',100,200) #初始化
 
print('a:',test.a)              #使用成员变量
print('b:',test.b)
print('c:',test.c)

pyt = CDLL('pytest.dll')          #加载dll
pyt.trans_union.restype=c_int    #声明返回参数类型和入参类型
pyt.trans_union.argtypes=(TuTest,)
pyt.trans_union(test)            #调用
 
 

 
 
 
 
 
 
 
 
 
 