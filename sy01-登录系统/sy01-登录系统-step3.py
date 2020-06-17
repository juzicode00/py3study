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
retry_count = {} #重试次数

while True:
    user = input('请输入用户名: ') #基本输入函数，获取用户名，得到一个字符串类型的变量
    pasw = input('请输入密码: ')

    if user not in user_dict:   #检查某个值是否是dict的一个元素，如果不是(not in)提示用户名不存在
        print('你输入的用户名不存在')
    else:   #如果用户名存在，判断密码是否正确.
        retry_count.setdefault(user,0) #字典的setdefault操作，如果不存在user的key，新加key=user并设置为0
        if user_dict[user] == pasw:   #字典元素的引用，dict[key]
            print('密码正确，进入系统......')
            break   #如果密码正确，跳出循环
        else:
            retry_count[user] = retry_count[user]+1  #错误次数加1
            print('密码错误，拒绝进入！')
            print('user=%s已错误输入%d次! '%(user,retry_count[user]))
            if retry_count[user] >= 3:
                print('输入的错误次数已达最大次数，退出！')
                break
