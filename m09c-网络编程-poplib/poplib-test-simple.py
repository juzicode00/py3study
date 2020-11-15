'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.11.10
接收到的邮件简单处理，未考虑编码、附件等
'''

print('\n-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   
 
import os,sys
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
import email
import poplib
import getpass

#输入邮箱地址、密码
to_addr = input('输入收件人: ')
password = getpass.getpass('收件人邮箱密码: ')

#连接邮箱，设置调试等级
try:
    pop3 = poplib.POP3('pop.163.com')
    pop3.set_debuglevel(1) 
    print(pop3)
except:
    print('连接服务器失败')
    sys.exit(1)
#登录邮箱
try:
    ret=pop3.user(to_addr) 
    print(ret)
    ret=pop3.pass_(password)
    print(ret)
except :  
    print('登录邮箱失败')
    sys.exit(1)
print('登录邮箱成功')

#获取邮件清单
mail_list = response, listings, octets = pop3.list()
print(mail_list)
for listing in listings:
    #print(listing)
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #提取邮箱列表信息
    mesg_num, size = listing.split()
    mesg_num = bytes.decode(mesg_num)
    size = bytes.decode(size)
    print(mesg_num,size)
    
    #提取邮件头
    res = response, lines, octets = pop3.top(mesg_num, 0)
    #print(lines)
    lines_post=[]
    for l in lines:
        lines_post.append(bytes.decode(l))
        
    #构造message
    message = email.message_from_string('\n'.join(lines_post))
    print('type(message):',type(message))
    print('From:',message['From'])
    print('To:',message['To'])
    print('Subject:',message['Subject'])
    print('Date:',message['Date'])
    
    print('*******************')
    #提取邮件内容
    res = response, lines, octets = pop3.retr(mesg_num)
    lines_post=[]
    for l in lines:
        lines_post.append(bytes.decode(l))
        
    #构造message
    message = email.message_from_string('\n'.join(lines_post))    
    maintype = message.get_content_maintype()    
    print('maintype:',maintype)    
    if maintype == 'multipart':
        for part in message.get_payload():
            print('multipart:',part.get_content_maintype())
            if part.get_content_maintype() == 'text':
                mail_content = part.get_payload(decode=True).strip()
                try:
                    print('mail_content:',mail_content.decode('UTF8'))  
                except:
                    try:
                        print('mail_content:',mail_content.decode('GBK'))  
                    except:
                        continue
    elif maintype == 'text':
        mail_content = message.get_payload(decode=True).strip()
        try:
            print('mail_content:',mail_content.decode('UTF8'))  
        except:  
            try:
                print('mail_content:',mail_content.decode('GBK'))  
            except:
                continue 
    #print('mail_content:',mail_content.decode('UTF8'))  

pop3.quit()    
    
    
    
    
    
    
    