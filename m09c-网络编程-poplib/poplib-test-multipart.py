'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.11.10
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

def parse_msg(message):
    type = message.get_content_type() 
    maintype = message.get_content_maintype()    
    subtype = message.get_content_subtype()
    print('type:',type)        
    print('maintype:',maintype)    
    print('subtype:',subtype)  

    boundary = message.get_boundary()
    print('boundary:',boundary) 
    
    #如果get_filename()返回非None,表示有附件
    filename = message.get_filename()
    if filename:
        print('找到1个附件，文件名：',filename)
        data=message.get_payload(decode=True)
        with open(filename,'wb') as pf:
            pf.write(data)        
        return filename
        
    #如果主类型为text，根据编码方式解析
    content_charset = message.get_content_charset()
    print('content_charset:',content_charset)          
    if maintype == 'text':
        mail_content = message.get_payload(decode=True).strip()
        try:
            print('mail_content:\n',mail_content.decode(content_charset))  
        except:  
            print('解码邮件错误')  

    #如果主类型为multipart，递归
    elif maintype == 'multipart':
        for message_part in message.get_payload():
            parse_msg(message_part)            
    return 

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
    #提取邮件列表信息
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
    #print('---ALL message-content:\n',message)
    #print('---ALL message-content OVER:\n')
    #解析message
    parse_msg(message)
    
    #print('mail_content:',mail_content.decode('UTF8'))  
    input('输入回车继续')
    
pop3.quit()    
    
    
    
    
    
    
    