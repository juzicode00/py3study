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
    def __init__(self,name,id):
        print('实例化对象......')
        self.name = name
        self.id = id
 
    def get_name(self):
        return self.name
        
    def get_id(self):
        return self.id
        
    def get_name_id(self):
        n = self.get_name()
        i = self.get_id()
        return n,i
        
        
s1 = Student('wangwu',20200505)
print('s1类型：',type(s1))
print('s1的name,id：',s1.get_name_id())
 