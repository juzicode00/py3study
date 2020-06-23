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
        
    def get_score(self):
        return self.score        
        
s1 = Student('wangwu',20200505)
print('s1的name：',s1.get_name())
print('s1的id  ：',s1.get_id()) 
#s1.score = 95
print('s1的score：',s1.get_score()) 