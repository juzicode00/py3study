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

a = c_int(100)
print('a=',a)
print('a.value=',a.value)
 
b = c_long(100)
print('b=',b)
print('b.value=',b.value)
 