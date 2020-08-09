'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   
 
print('正常情况：')
try:
    a = 10/2
except:
    print('发生异常' )
finally:
    print('不管是否发生异常')
 
print('异常情况：')
try:
    a = 10/0
except:
    print('发生异常' )
finally:
    print('不管是否发生异常')