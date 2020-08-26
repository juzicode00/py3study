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

pyt = CDLL('pytest.dll')   #加载dll

#int型的返回值和入参可以不声明类型
ret = pyt.addi(55,22)
print('addi(55,22)=',ret)

#以下其他类型的返回值和入参必须声明类型
pyt.addd.restype=c_double
pyt.addd.argtypes=(c_double,c_double)
ret = pyt.addd(5.55555555,2.22222222)
print('addd(5.55555555,2.22222222)=',ret)
 
pyt.addf.restype=c_float
pyt.addf.argtypes=(c_float,c_float)
ret = pyt.addf(5.55,2.22)
print('addf(5.55,2.22)=',ret)

pyt.addll.restype=c_longlong
pyt.addll.argtypes=(c_longlong,c_longlong)
ret = pyt.addll(5555555555555555555,2222222222222222222)
print('addll(5555555555555555555,2222222222222222222)=',ret)

