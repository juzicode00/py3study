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


pyt = CDLL('pytest.dll')  

 
sys.exit()
 
#x = c_char(b'a')
#pyt.modify_c(pointer(x))           
#print('in python c_char x=', x.value)

#单个宽字符可以用使用
print('指针：wchar_t')  
pyt.modify_wc.restype=c_int     
pyt.modify_wc.argtypes=(POINTER(c_wchar),)
x = c_wchar('桔')
pyt.modify_wc(pointer(x))           
print('in python c_wchar x=', x.value)
 
pyt.modify_wc.restype=c_int     
pyt.modify_wc.argtypes=(c_wchar_p,)
x = c_wchar('桔')
pyt.modify_wc(pointer(x))           
print('in python c_wchar x=', x.value)
 
 
 
 