'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.21
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   


class Student():
    def set_name_id(self,name,id):
        self.name = name
        self.id = id 
           
s1 = Student()
s1.set_name_id('wangwu',20200505)
print('s1类型：',type(s1))
print('s1的name：',s1.name)
print('s1的id：',s1.id)