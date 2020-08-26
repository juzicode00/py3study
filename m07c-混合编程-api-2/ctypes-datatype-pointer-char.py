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

 
print()
print('指针： 修改单个字符，POINTER')
pyt.modify_c.restype=c_int     
pyt.modify_c.argtypes=(POINTER(c_char),)
x = c_char(b'a')
pyt.modify_c(pointer(x))           
print('in python c_char x=', x.value)

print('指针： 修改单个字符，c_char_p')
pyt.modify_c.restype=c_int     
pyt.modify_c.argtypes=(c_char_p,)
x =  b'a' 
pyt.modify_c(x)           
print('in python c_char x=', x)

print()
print('指针： 修改字符串，POINTER ')
pyt.modify_c2.restype=c_int     
pyt.modify_c2.argtypes=(POINTER(c_char),)
x =  b'abcdefghijklmno'
pyt.modify_c2(x)           
print(x)

print('指针： 修改字符串，c_char_p ')
pyt.modify_c2.restype=c_int     
pyt.modify_c2.argtypes=(c_char_p,)
x =  b'ABCDEFGHIJKLMNO'
#x =  b'abcdefghijklmno'
pyt.modify_c2(x)           
print(x)

print()
print('指针： 字符数组转换，c_char_100')
c_char_100 = c_char * 100
x = c_char_100() 
x.value = b'abcde' 
pyt.modify_c_array.restype=c_int   
pyt.modify_c_array.argtypes=(c_char_100,c_int)
pyt.modify_c_array(x,100) 
print(x.value)

print('指针： 字符数组转换，POINTER(c_char)')
x.value = b'ABCDE'
pyt.modify_c_array.restype=c_int   
pyt.modify_c_array.argtypes=(POINTER(c_char),c_int)
pyt.modify_c_array(x,100)    
print(x.value)

print('指针： 字符数组转换，c_char_p')
x.value = b'XYZ'
pyt.modify_c_array.restype=c_int  
pyt.modify_c_array.argtypes=( c_char_p ,c_int)
pyt.modify_c_array(x,100)    
print(x.value)



 
 
 
 
 
 