'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.27
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

import csv
print('设置newline为空')   
with open('example-write.csv', 'w', encoding = 'utf-8',newline='') as f:
    writer_obj = csv.writer(f) #创建写csv对象
    records=['h1','h2','h3']
    writer_obj.writerow(records) #写入记录
    records=['www','juzicode','com']
    writer_obj.writerow(records) #写入记录
    records=['vx:','桔子code']
    writer_obj.writerow(records) #写入记录

with open('example-write.csv', 'r', encoding = 'utf-8') as f:
    records = csv.reader(f)
    for rec in records:
        print(rec)

print(' 不 设置newline为空')        
with open('example-write-newline.csv', 'w', encoding = 'utf-8') as f:
    writer_obj = csv.writer(f) #创建写csv对象
    records=['h1','h2','h3']
    writer_obj.writerow(records) #写入记录
    records=['www','juzicode','com']
    writer_obj.writerow(records) #写入记录
    records=['vx:','桔子code']
    writer_obj.writerow(records) #写入记录
    
with open('example-write-newline.csv', 'r', encoding = 'utf-8') as f:
    records = csv.reader(f)
    for rec in records:
        print(rec)
            
