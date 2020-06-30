'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.23
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


import winsound #导入winsound库
interval = 1000  #发声时长1000ms

freq = 500  #频率
print('freq=',freq)
winsound.Beep(freq,interval) #发出声音

freq = 1000
print('freq=',freq)
winsound.Beep(freq,interval)

freq = 0
print('freq=',freq)
winsound.Beep(freq,interval)  #频率入参必须在37-32767

'''
Traceback (most recent call last):
Traceback (most recent call last):
  File "E:\juzicode\py3study\msy01-摩斯电码\beep01.py", line 15, in <module>
    winsound.Beep(0,1000)  #频率入参必须在37-32767
ValueError: frequency must be in 37 thru 32767

'''