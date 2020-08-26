'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import os
'''
print('执行popen......')
ret = os.popen('ipconfig')
print('执行popen结果：',ret)
print('执行system......')
ret = os.system('ipconfig')
print('执行system结果：',ret)
'''
print('执行popen......')
ret = os.popen('dir')
print('执行popen结果：',ret)

buffers = ret.readline()
print(buffers)

print('执行system......')
ret = os.system('dir')
print('执行system结果：',ret)


print('执行popen......')
ret = os.popen('ping www.baidu.com')
print('执行popen结果：',ret)
buffers = ret.readlines()
print(buffers)


print('执行system......')
ret = os.system('ping www.baidu.com')
print('执行system结果：',ret)

