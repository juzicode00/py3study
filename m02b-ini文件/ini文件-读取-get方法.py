'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

import configparser
config = configparser.ConfigParser()    #step1新建configparser实例
obj=config.read('config.ini')           #step2读取ini文件

drivername = config.get( 'info','drivername') 
print('drivername:',drivername)       