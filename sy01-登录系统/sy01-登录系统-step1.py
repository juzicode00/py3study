'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.11
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')

user_dict = {'orange':'juzicode','apple':'123','banana':'456'} #这里用字典的key保存了用户名，字典的value保存密码

user = input('请输入用户名: ')
pasw = input('请输入密码: ')

if user not in user_dict:
    print('你输入的用户名不存在')
else:
    if user_dict[user] == pasw:
        print('密码正确，进程系统......')
    else:
        print('密码错误，拒绝进入！')