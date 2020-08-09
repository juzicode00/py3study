'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   


import os
print('os.environ:', os.environ)

import os 
print('os.getcwd():',os.getcwd())#获取当前工作目录
 
import os 
print('os.listdir():',os.listdir())

import os 
files = os.listdir()
print('files=',files)
for f in files:
    print('f:',f)
    if os.path.isdir(f):
        print('%s is dir'%f)
    if os.path.isfile(f):
        print('%s is file'%f)
     

     
import os 
print('os.getenv(PATH):',os.getenv('PATH'))


import os 
path = os.getenv('PATH')
os.putenv('PATH',path+';this\\is\\new\\path')
print('os.getenv(PATH):',os.getenv('PATH'))



print('os.listdir():',os.listdir())
path = 'hello.py'
print('hello.py exists():',os.path.exists(path))
path = 'txt'
print('txt:',os.path.exists(path))


print('__file__:',__file__)
print('type(__file__):',type(__file__))
print('realpath(__file__):',os.path.realpath(__file__))

realpath=os.path.realpath(__file__)
print('当前文件绝对路径:',realpath)
dirname = os.path.dirname(realpath)
print('目录名称:',dirname)
garder = os.path.dirname(dirname)
print("父目录:" + garder)
garder = os.path.dirname(garder)
print("父目录:" + garder)
garder = os.path.dirname(garder)
print("父目录:" + garder)
garder = os.path.dirname(garder)
print("父目录:" + garder)

print('abspath(__file__):',os.path.abspath(__file__) )

realpath=os.path.realpath(__file__)
print('realpath(__file__):',os.path.realpath(__file__))
print('basename(realpath):',os.path.basename(realpath))
print('basename():',os.path.basename('e:\\juzicode\\py3study'))
print('basename():',os.path.basename('e:\\juzicode\\py3study\\'))

print('__file__:',__file__)
print('split():',os.path.split(__file__))
print('splitext():',os.path.splitext(__file__))
print('splitdrive():',os.path.splitdrive(__file__))

print('__file__:',__file__)
print('getatime():',os.path.getatime(__file__))
print('getmtime():',os.path.getmtime(__file__))
print('getctime():',os.path.getctime(__file__))
print('getsize():',os.path.getsize(__file__))




print('重命名文件')
ret = os.rename('test.txt','juzicode.txt')
print('rename():',ret)
print('删除文件')
ret = os.remove('juzicode.txt')
print('remove():',ret)

