'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('dict 修改元素实验：')
d={'juzi':10,'code':'orange','com':(1,2,3)}
print('修改前的d:',d)
d['juzi'] = '桔子code'
d['code'] = 'apple'
d['com'] = 20
d['桔子'] = '美味'
print('修改后的d:',d)
