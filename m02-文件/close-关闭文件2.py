'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


with open('example-r2.txt','r') as fileobj:
    print('fileobj',fileobj)
    fileobj.read()

print('fileobj',fileobj)
fileobj.read()
