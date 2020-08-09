'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   

import datetime
 
now = datetime.datetime.now()#系统当前时间 
print('datetime.datetime:',datetime.datetime)
print('datetime.datetime.now():',now)
print('type of now:',type(now))

print('datetime.datetime.date():',now.date())#当前时间的日期 
print('datetime.datetime.time():',now.time())#当前时间的时分秒

print('datetime.datetime.ctime():',now.ctime())#转化成标准格式时间字符串
print('datetime.datetime.strftime():',now.strftime('%Y-%m-%d-%H:%M:%S'))#转换为自定义格式时间字符串

tm = datetime.datetime.strptime('2020-1-20-14-42-36','%Y-%m-%d-%H-%M-%S')
print('type of tm:',type(tm))
print('datetime.datetime.strptime():',tm)