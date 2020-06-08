'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('dict 内置方法/函数实验：')
d={'juzi':10,'code':'orange','com':(1,2,3)}
print('d :',d)

print('d.keys()   : ',d.keys())
print('d.keys()类型 : ',type(d.keys()))
print('d.values() : ',d.values())
print('d.values()类型: ',type(d.values()))
print('d.items()  :',d.items()) 
print('d.items()类型: ',type(d.items()))

print('d中 key=juzi 的value :',d.get('juzi')) 
print('d中 key=桔子 的value :',d.get('桔子')) 

d.setdefault('juzi',20)
d.setdefault('桔子',20)
print('d.setdefault() :',d) 

d.pop('桔子')
print('d.pop(桔子)后 :',d) 
#d.pop('香蕉')
#print('d.pop(香蕉)后 :',d) 

d2={'a':1}
print('d2 :',d2)
d2.update(d)
print('d2.update(d), d2: ',d2)

d.clear()
print('d.clear()清空后的d :',d)