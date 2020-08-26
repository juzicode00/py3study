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
 
pyt = CDLL('pytest.dll')              #加载dll
pyt.void_pointer.restype=c_int        #声明返回参数类型和入参类型
pyt.void_pointer.argtypes=(c_void_p,)

a = c_char(b'j')                      #字母'j'
b = cast(pointer(a),c_void_p)         #转换为c_void_p
pyt.void_pointer(b)                   #执行

a = c_int(117)                        #字母'u'的ascii值
b = cast(pointer(a),c_void_p)         #转换为c_void_p
pyt.void_pointer(b)                   #执行

 
 
 
 
 
 