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
 
print('\n\nos.popen(\'mkdir  abc\')：')
ret = os.popen('mkdir  abc')
print(ret.readlines())
print('ret.close():',ret.close())

print('\n\nos.popen(\'mkdir  abc\')：')
ret = os.popen('mkdir  abc')
print(ret.readlines())
print('ret.close():',ret.close())

 

