'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('set实验：判断')
s1={1,2,3}
s2={1,2,3,4,5,6}
print('初始s1: ',s1)
print('初始s2: ',s2)
print('s1和s2元素都不一样: ',s1.isdisjoint(s2))
print('s1是否是s2的子集: ',s1.issubset(s2))
print('s1是否是s2的超集: ',s1.issuperset(s2))
