'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.7.10
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   
 
try:
    b = int('5')
    a = 10/b
except ValueError  :
    print('错误：ValueError:' )
except ZeroDivisionError :
    print('错误：ZeroDivisionError') 
else:
    print('一切ok')
    print('a=',a)
    print('b=',b) 
    
try:
    b = int('5')
    a = 10/b
except ValueError  :
    print('错误：ValueError:' )
except ZeroDivisionError :
    print('错误：ZeroDivisionError') 

print('一切ok')
print('a=',a)
print('b=',b) 