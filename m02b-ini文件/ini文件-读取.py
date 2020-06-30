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
config = configparser.ConfigParser() #新建configparser实例
obj=config.read('config.ini') #读取ini文件
print('obj:',obj)
sections_obj = config.sections() #获取所有的sections名称，得到一个list
print('sections_obj:',sections_obj) #sections_obj: ['info', 'languages', 'object']
info_obj = config['info'] #得到一个名为info的section对象
print('info_obj:',info_obj)  
drivername = config['info']['drivername'] #读取key='drivername'的值
print('drivername:',drivername)   #得到内容为usbhub