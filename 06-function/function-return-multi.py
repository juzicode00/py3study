'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.19
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

########无返回值函数的返回类型
def func_2(x,y):
    print('2个入参x:',x)
    print('2个入参y:',y)    
y=func_2('桔子code','juzicode')
print('func_2()返回值值:',y)
print('func_2()返回值类型:',type(y))  


########多个返回值
def circum_area(x):
    print('1个入参x:',x)
    temp = 2*3.14*x
    area = 3.14 * x * x
    return temp,area
y = circum_area(5)
print('circum_area(5)返回值:',y)
print('circum_area的返回值类型:',type(y))
 
 

    
########