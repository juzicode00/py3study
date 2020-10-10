'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.9.20
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
 
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import smtplib


#设置邮箱地址、密码
from_addr = input('输入发件人: ')
password = input('发件人邮箱密码: ')
to_addr = input('输入收件人: ')

#生成邮件内容
mail_cont='你好Tom, 学习Python推荐你关注桔子code公众号'
mime = MIMEText(mail_cont, _subtype='plain', _charset='utf-8')
mime['Subject'] = Header('欢迎关注公众号: 桔子code', 'utf-8').encode()
name, addr = parseaddr('Jerry <%s>' % from_addr)
mime['From'] = formataddr((Header(name, 'utf-8').encode(), addr))
name, addr = parseaddr('Tom <%s>' % to_addr)
mime['To'] = formataddr((Header(name, 'utf-8').encode(), addr))

#设置163邮箱smtp服务器
smtp_server = 'smtp.163.com'  

#创建smtp服务实例
smtp = smtplib.SMTP(smtp_server, 25)
smtp.set_debuglevel(2)
#登录
smtp.login(from_addr, password)
#发送邮件
smtp.sendmail(from_addr, [to_addr], mime.as_string())
smtp.quit()
