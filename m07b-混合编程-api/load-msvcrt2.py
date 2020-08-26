'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import os,ctypes
from ctypes import *

libc = CDLL('msvcrt.dll')#加载dll
ret = libc.isupper(ord('A'))#用对象名.函数名的方法调用c函数
print('isupper(\'A\'):',ret)
ret = libc.isupper(ord('a'))
print('isupper(\'a\'):',ret)

X=223423423423
print('0x%x'%id('C'))
ret = libc.isupper('CX')
print('isupper(\'C\'):',ret)
print('0x%x'%id('a'))
ret = libc.isupper('a')
print('isupper(\'a\'):',ret)

ret = libc.isupper(0x223440)#取最后8bit，比较
print('isupper():',ret)
ret = libc.isupper(0x1141)#取最后8bit，比较
print('isupper():',ret)