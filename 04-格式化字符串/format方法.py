'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.11
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')
print('字符串转换format')
a = 3
b = 5.12345
c = '桔子code'
d = [1,2,3,4,5]
e = (1,2,3,4,5)
f = {1,2,3,4,5}
g = {1:10,2:20,3:30}
h = True
i = None
out = ' a:{0},b:{1},c:{2},d:{3},e:{4},f:{5},g:{6},h:{7},i:{8}'.format(a,b,c,d,e,f,g,h,i)
print('转换后：',out)
out = ' a:{0},b:{1},c:{2},d:{3},e:{4},f:{5},g:{6},h:{7}'.format(a,b,c,d,e,f,g,h,i)
print('转换后：',out)
out = ' a:{0},b:{1},c:{2},d:{3},e:{4},f:{5},g:{6},h:{7},i:{8}'.format(a,b,c,d,e,f,g,h)
print('转换后：',out)
 