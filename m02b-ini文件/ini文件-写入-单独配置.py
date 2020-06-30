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
#step1新建configparser实例
config = configparser.ConfigParser()    
#step2设置ini文件内容，内容格式为dict型数据
config['info'] = {'address': 'juzicode.com', '微信公众号':'桔子code'} 
config['info2'] = {'address': 'www.juzicode.com', 'weixin':'juzicode'} 
config['info3']={} #先添加一个section
config['info3']['port_no']= '65535'#设置单独的配置项
config['info3']['ip']= '127.0.0.1'
#step3打开文件并写入到ini文件
with open('config-write.ini','w') as pf: 
    config.write(pf) #z注意这里write()的入参是打开的文件实例  