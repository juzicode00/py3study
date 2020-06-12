'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.11
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('字符串转换为int型')

s='100'
a=int(s,10)
print(s,'10进制方法1：',a)
a=int(s,0)
print(s,'10进制方法2：',a)
a=int(s)
print(s,'10进制方法3：',a)

a=int(s,2)
print(s,'2进制：',a)

a=int(s,8)
print(s,'8进制：',a)

a=int(s,16)

print(s,'16进制：',a)
a=int(s,17)
print(s,'17进制：',a)

a=int(s,32)
print(s,'32进制：',a)



print('0B01转换为2进制：',int('0B01',2))
print('0O71转换为8进制：',int('0O71',8))
print('0X33转换为16进制：',int('0X33',16))


print('za3的36进制表示：',int('za3',36))
