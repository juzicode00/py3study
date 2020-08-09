'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import time

print('延时2s前......')
#time.sleep(2)
print('延时2s结束')
 
print('time.time():',time.time())


print('获取UTC时间：')
print('time.gmtime():',time.gmtime())
print('获取本地时间：')
print('time.localtime():',time.localtime())

print('epoch为0的时间：')
print('time.gmtime(0):',time.gmtime(0))
print('time.localtime(0):',time.localtime(0))

print('本地时间转换为epoch秒数')
b = time.localtime()
print('time.mktime():',time.mktime(b))
 
 
b = time.localtime()
print('time.asctime():',time.asctime(b))

c = time.time()
print('time.ctime():',time.ctime(c))

print('自定义格式化')
c=time.localtime()
print(time.strftime("%Y-%m-%d-%H:%M:%S", c))
print(time.strftime("%Y,%m,%d %H:%M:%S", c))

print('格式化时间转struct_time')
x='2019-01-02-22:20:33'
s=time.strptime(x,'%Y-%m-%d-%H:%M:%S')
print(s)

x='2019,01,02 22:20:33'
s=time.strptime(x,'%Y,%m,%d %H:%M:%S')
print(s)