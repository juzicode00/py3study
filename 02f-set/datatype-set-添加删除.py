'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('set实验：添加删除元素')
s={1,2,3}
print('初始s: ',s)
s.add(1)
print('add(1)后的set: ',s)
s.add(4)
print('add(4)后的set: ',s)
s.remove(1)
print('remove(1)后的set: ',s)
#s.remove(5)
#print('remove(5)后的set: ',s)
s.pop()
print('pop()后的set: ',s)
s.pop()
print('pop()后的set: ',s)
s.update({7,8,9})
print('update(7,8,9)后的set: ',s)