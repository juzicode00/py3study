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

#定义一种新的数组类型
c_int_10 = c_int * 10  
arr_int = c_int_10(1,2,3,4,5,6,7,8,9,10)# 赋值的长度不能大于前面声明的长度
print('arr_int:',arr_int)
for ar in arr_int:
	print(ar,end=' ')
print()


c_char_20 = c_char * 20
arr_char = c_char_20(b'j',b'u',b'z',b'i',b'c',b'o',b'd',b'e',b'.',b'c',b'o',b'm')
print('arr_char:',arr_char)
for ar in arr_char:
	print(ar,end=' ')
print()

'''
c_char_20 = c_char * 20
arr_char = c_char_20('j','u','z','i','c','o','d','e','.','c','o','m')
print('arr_char:',arr_char)
for ar in arr_char:
	print(ar,end=' ')
print()
'''

c_wchar_20 = c_wchar * 20
arr_wchar = c_wchar_20('j','u','z','i','c','o','d','e','.','c','o','m','/','桔','子','c','o','d','e')
print('arr_wchar:',arr_wchar)
for ar in arr_wchar:
	print(ar,end=' ')
print()


 