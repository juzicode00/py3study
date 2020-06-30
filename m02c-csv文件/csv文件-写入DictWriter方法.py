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
with open('example-DictWrite.csv', 'w', encoding = 'utf-8',newline='') as f: #step1 创建文件对象
    headers=['h1','h2','h3']
    #headers=['h1','h2']#,'h3']
    writer_obj = csv.DictWriter(f,headers) #step2 创建写csv对象
    writer_obj.writeheader()               #step3 写表头，不需要传入headers，在创建对象时已传入
    record = {'h1':'www','h2':'juzicode' ,'h3':'com'}
    writer_obj.writerow(record)            #step4 写单行
    
    records = [{'h1':'WWW','h2':'JUZICODE','h3':'COM'},
                {'h1':'vx:','h2':'桔子code'},
                {'h1':'vx:','h2':'juzicode','h3':'csvtest'},
                ]
    writer_obj.writerows(records)          #step4.2 写多行
    
    
with open('example-DictWrite.csv', 'r', encoding = 'utf-8') as f:
    records = csv.reader(f)
    for rec in records:
        print(rec)
            
