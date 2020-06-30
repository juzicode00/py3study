'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


with open('example-a3.txt','a+',encoding='utf8') as fileobj:
    print('fileobj.tell():',fileobj.tell()) #从这里
    content=fileobj.read()
    print('read():\n',content) #因为文件指针指向的是最后，读出的内容实际为空
    
    fileobj.write('a+模式增加一行')
 