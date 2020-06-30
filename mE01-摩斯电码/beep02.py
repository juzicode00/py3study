'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.23
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

'''
频率从37到32767Hz，步进200Hz驱动蜂鸣器
'''
import time
import winsound
for freq in range(37,32767,200):
    print('freq:',freq)
    winsound.Beep(freq,300)
    time.sleep(0.3) #等待0.3s，等待蜂鸣器响应

'''
-----欢迎来到www.juzicode.com
-----公众号: juzicode/桔子code

freq: 37
freq: 237
freq: 437
freq: 637
freq: 837
freq: 1037
freq: 1237

'''