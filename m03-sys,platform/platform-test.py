'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   


import platform
print('architecture():',platform.architecture())
print('machine():',platform.machine())
print('processor():',platform.processor())
 
import platform
print('system():',platform.system())
print('platform():',platform.platform())
print('uname():',platform.uname())
print('version():',platform.version())

import platform
print('python_version():',platform.python_version())    #python版本
print('python_build():',platform.python_build())        #构建信息
print('python_compiler():',platform.python_compiler())  #编译器版本
print('python_implementation():',platform.python_implementation()) #python解释器类型
print('python_version_tuple():',platform.python_version_tuple())    #python版本元组

