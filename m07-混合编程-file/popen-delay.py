'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import os,time
 
print('\n\nos.popen(\'dir\'),延时2s：')
ret = os.popen('dir')
time.sleep(2)
print('ret.close():',ret.close())

print('\n\nos.popen(\'dir\'),无延时：')
ret = os.popen('dir')
print('ret.close():',ret.close())
 

print('\n\nos.popen(\'ping juzicode.com\'),无延时：')
ret = os.popen('ping juzicode.com')
print('ret.close():',ret.close())

 

