'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.19
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

########没有入参
def func_just_print():
    print('这个函数不做其他的，就只打印juzicode')
    
func_just_print()

########1个入参
def func_1(x):
    print('只有1个入参x:',x)
    
func_1('桔子code')
func_1('juzicode')
func_1(3.14159265)

########2个入参
def func_2(x,y):
    print('2个入参x:',x)
    print('2个入参y:',y)    
func_2('桔子code','juzicode')
func_2(3.14159265,2.718281828459)

########无返回值函数的返回类型
y=func_2('桔子code','juzicode')
print('func_2()返回值值:',y)
print('func_2()返回值类型:',type(y))  

########1个入参，1个返回值
def circum(x):
    print('1个入参x:',x)
    temp = 2*3.14*x
    return temp
y = circum(5)
print('半径为5的圆周长为:',y)

if circum(5)>30:
    print('半径为5的圆周长大于30')
else:
    print('半径为5的圆周长不大于30')

    
########