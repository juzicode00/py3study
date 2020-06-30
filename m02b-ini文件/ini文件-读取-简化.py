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
drivername = config['info']['drivername'] #step3读取key='drivername'的值
print('drivername:',drivername)        #得到内容为usbhub