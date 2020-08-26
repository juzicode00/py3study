'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   

from ctypes import *
#加载dll
pyt = CDLL('pytest.dll')   
#定义新的数据类型
c_int_10 = c_int * 10  
arr_int = c_int_10(1,2,3,4,5,6,7,8,9,10)# 赋值的长度不能大于前面声明的长度
#声明c函数的返回值和入参类型
pyt.trans_array_i.restype=c_longlong
pyt.trans_array_i.argtypes=(c_int_10,)
#调用c函数
ret = pyt.trans_array_i(arr_int)
print('trans_array_i()=',ret)


c_char_20 = c_char * 20  
arr_char = c_char_20(b'j',b'u',b'z',b'i',b'c',b'o',b'd',b'e',b'.',b'c',b'o',b'm')
pyt.trans_array_c.restype=c_char
pyt.trans_array_c.argtypes=(c_char_20,)
#调用c函数
ret = pyt.trans_array_c(arr_char)
print('trans_array_c()=',ret)
