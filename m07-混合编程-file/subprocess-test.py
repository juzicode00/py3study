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
#ret = subprocess.run(['dir  '], shell=True)
#print()
#ret = subprocess.run(['ping','   www.baidu.com'],shell=True)

 
ret = subprocess.run('dir', shell=True)
print(ret)


ret = subprocess.run('ping  www.baidu.com',shell=True)
print(ret)


ret = subprocess.run(['dir'], shell=True)
ret = subprocess.run(['ping','www.baidu.com'],shell=True)


 

