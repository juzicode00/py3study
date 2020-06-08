'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('set实验：并集差集交集')
s1={1,2,3,4,5}
s2={4,5,6}
print('初始s1: ',s1)
print('初始s2: ',s2)
sd = s1.difference(s2)
print('s1和s2的差集: ',sd)
su = s1.union(s2)
print('s1和s2的并集: ',su)
si = s1.intersection(s2)
print('s1和s2的交集: ',si)
ssd = s1.symmetric_difference(s2)
print('s1和s2的对称差集: ',ssd)

print('s1-s2: ',s1-s2)
print('s1|s2', s1|s2)
print('s1&s2', s1&s2)
print('s1^s2', s1^s2)

#print('s1+s2: ',s1+s2)
