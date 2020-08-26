'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

from ctypes import *

a = c_double(3.0)
b = c_double(2.0)

print('a=',a)
print('a.value=',a.value)
print('b=',b)
print('b.value=',b.value)

libc = CDLL('msvcrt.dll')   #加载dll

ret = libc.pow(a,b)         #用对象名.函数名的方法调用c函数
print('pow(a,b):',ret)

 
libc.pow.restype = c_double
libc.pow.argtypes = (c_double, c_double)
ret = libc.pow(a,b)         #用对象名.函数名的方法调用c函数
print('pow(a,b):',ret)