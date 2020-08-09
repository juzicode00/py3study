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
    b = int('xyz')
    a = 10/0
    print('a:',a)
except ValueError  :
    print('错误：ValueError:' )
except ZeroDivisionError :
    print('错误：ZeroDivisionError') 
except:
    print('错误：其他错误')
    
try:
    b = int('xyz')
    a = 10/0
    print('a:',a)
except ValueError as e:
    print('错误：ValueError:',e)
except ZeroDivisionError as e:
    print('错误：ZeroDivisionError',e)
except:
    print('错误：其他错误')