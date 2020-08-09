'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.6.26
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode\n')   


import sys
print('sys.platform:', sys.platform)
print('sys.version:',sys.version)

import sys
print('sys.getfilesystemencoding:',sys.getfilesystemencoding())


info = sys.getwindowsversion()
print('系统主版本:',info.major)
print('系统次版本:',info.minor)
print('系统build版本:',info.build)
print('系统platform:',info.platform)


