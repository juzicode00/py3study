'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import os,time,sys

import subprocess
 
print('执行 dir')
ret = subprocess.run('dir', shell=True,capture_output=True)
print('args:',ret.args)
print('returncode:',ret.returncode) 
print('stdout:',ret.stdout)
print('stderr:',ret.stderr)

print('执行 dir --notfound')
ret = subprocess.run('dir --notfound', shell=True, capture_output=True, text=True)
print('args:',ret.args)
print('returncode:',ret.returncode) 
print('stdout:',ret.stdout)
print('stderr:',ret.stderr)


print('执行 mkdir abc')
ret = subprocess.run(' mkdir abc', shell=True, capture_output=True, text=True)
print('args:',ret.args)
print('returncode:',ret.returncode) 
print('stdout:',ret.stdout)
print('stderr:',ret.stderr)