'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

#当文件不存在时
fileobj=open('example-r1.txt','r')
print('fileobj',fileobj)

fileobj=open('example-r2.txt','rb')
print('fileobj',fileobj)

fileobj=open('example-r3.txt','r+')
print('fileobj',fileobj)

fileobj=open('example-r4.txt','rb+')
print('fileobj',fileobj)


fileobj=open('example-w1.txt','w')
print('fileobj',fileobj)

fileobj=open('example-w2.txt','wb')
print('fileobj',fileobj)

fileobj=open('example-w3.txt','w+')
print('fileobj',fileobj)

fileobj=open('example-w4.txt','wb+')
print('fileobj',fileobj)


 
fileobj=open('example-a1.txt','a')
print('fileobj',fileobj)

fileobj=open('example-a2.txt','ab')
print('fileobj',fileobj)

fileobj=open('example-a3.txt','a+')
print('fileobj',fileobj)

fileobj=open('example-a4.txt','ab+')
print('fileobj',fileobj)
