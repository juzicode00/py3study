'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.11
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('流程控制实验：循环中断')

count = 0
dict = {1:'www',2:'juzi',3:'code',4:'com',5:'juzi',6:'桔子'}
for d in dict:
    print('dict[%s]:'%d,dict[d])
    if dict[d] != 'juzi':
        continue
    count += 1 
print('循环结束. juzi出现了%d次'%count)    

