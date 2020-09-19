'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.8.15
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   


import c2pyd  #不需要pyd后缀
 
print('c2pyd.add_i(1,5)=',c2pyd.add_i(1,5),'\n') #add_i在static PyMethodDef  MethodsDef[]中定义的
print('c2pyd.add_f(1.1,5.5)=',c2pyd.add_f(1.1,5.5),'\n')
print('c2pyd.add_sub_f(1.1,5.5)=',c2pyd.add_sub_f(1.1,5.5),'\n')

print('c2pyd.ret_nothing(1.1,5.5)=',c2pyd.ret_nothing(1.1,5.5),'\n')

print('c2pyd.trans_noargs()=',c2pyd.trans_noargs(),'\n')

print('c2pyd.trans_kwargs(1.1,3.3,5.5,7.7)=',c2pyd.trans_kwargs(1.1,3.3,5.5,7.7),'\n') 
print('c2pyd.trans_kwargs(1.1,3.3,c=5.5,d=7.7)=',c2pyd.trans_kwargs(1.1,3.3,c=5.5,d=7.7),'\n') 
print('c2pyd.trans_kwargs(a=1.1,b=3.3,c=5.5,d=7.7)=',c2pyd.trans_kwargs(a=1.1,b=3.3,c=5.5,d=7.7),'\n') 
 