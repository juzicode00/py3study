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
pyt.trans_cp.restype=c_char_p
pyt.trans_cp.argtypes=(c_char_p,)
ret = pyt.trans_cp(b'juzicode')
print('trans_cp()=',ret)

pyt.trans_wcp.restype=c_wchar_p
pyt.trans_wcp.argtypes=(c_wchar_p,)
ret = pyt.trans_wcp('桔子code')
print('trans_wcp()=',ret)


pyt.trans_c.restype=c_char
pyt.trans_c.argtypes=(c_char,)
ret = pyt.trans_c(b'A')
print('trans_c(A)=',ret)


pyt.trans_c.restype=c_byte
pyt.trans_c.argtypes=(c_byte,)
ret = pyt.trans_c(ord('A'))
print('trans_c(A)=',ret)


pyt.trans_wc.restype=c_wchar
pyt.trans_wc.argtypes=(c_wchar,)
ret = pyt.trans_wc('桔')
print('trans_wc(A)=',ret)
#ret = pyt.trans_wc('桔子code')
#print('trans_wc(A)=',ret)