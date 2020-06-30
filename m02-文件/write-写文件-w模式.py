'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


with open('example-w1.txt','w') as fileobj:
    #content=fileobj.read()
    #print('content:',content)
    
    content=fileobj.write('桔子code')
    content=fileobj.writelines(['juzicode.COM','juzicode.com'])
    
