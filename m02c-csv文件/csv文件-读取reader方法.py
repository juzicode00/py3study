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
with open('example.csv', 'r', encoding = 'utf-8') as f:
    records = csv.reader(f)
    for rec in records:
        print(rec)