'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


with open('example-w3.txt','w+',encoding='utf8') as fileobj:
    print('fileobj.tell():',fileobj.tell())
    content=fileobj.read()
    print('content:',content)
    
    
    fileobj.write('桔子code')
    fileobj.writelines(['JUZICODE.COM','juzicode.com'])
    
