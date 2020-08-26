'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

import os,ctypes
from ctypes import *

#libc = cdll.LoadLibrary('msvcrt.dll')
#libc = windll.LoadLibrary('msvcrt.dll')  # Windows only
#libc = oledll.LoadLibrary('msvcrt.dll')  # Windows only
libc = pydll.LoadLibrary('msvcrt.dll')

libc.wprintf('TEST\n' )

#使用utf-8编码
form = bytes('%s\n', encoding='GBK')
stri = bytes('使用utf-8编码方式: Hello ctypes\n', encoding='GBK')
libc.printf(form,stri)
