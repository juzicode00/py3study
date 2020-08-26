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
print('指针：int')    
pyt.modify_i.restype=c_int     
pyt.modify_i.argtypes=(POINTER(c_int),)
x = c_int(3)
#pyt.modify_i(pointer(x))           
pyt.modify_i(x)
print('in python x=',x.value)


print()
print('指针：int数组, C函数内部加1000')    
c_int_100 = c_int * 100

pyt.modify_i_array.restype=c_int     
pyt.modify_i_array.argtypes=(c_int_100,c_int)
x = c_int_100(10,20,30,40,50,60)
pyt.modify_i_array(x,100)           
print('in python x[0]=',x[0])

pyt.modify_i_array.argtypes=(POINTER(c_int),c_int)
x = c_int_100(11,22,33,44,55,66)
pyt.modify_i_array(x,100)           
print('in python x[0]=',x[0])

'''
pyt.modify_i_array.argtypes=(POINTER(c_int_100),c_int)
x = c_int_100(111,222,333,444,555,666)
pyt.modify_i_array(x,100)           
print('in python x[0]=',x[0])
'''

 
 
 
 
 
 