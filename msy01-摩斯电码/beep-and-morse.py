'''
author: juzicode
address: www.juzicode.com
公众号: juzicode/桔子code
date: 2020.6.23
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: juzicode/桔子code\n')   

import time
import winsound
freq1=1500   #短音发声频率
freq2=2000   #长音发声频率
interv_short = 100  #短音“.”的发声时长
interv_long = 300   #长音“-”的发声时长
msg = input('输入要发送的消息:')
msg = msg.upper()   #转换大写，摩斯码中不区分大小写
code_dict = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
             '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
             'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
             'H': '....','I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
             'O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
             'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..', 
             '.': '.-.-.-', ':': '---...',',': '--..--', ';': '-.-.-.', '?': '..--..', 
             '=': '-...-', "'": '.----.', '/': '-..-.', '!': '-.-.--','--': '-....-', 
             '-': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-'}
for m in msg:
    print('m:',m)
    code = code_dict.get(m)
    if code is None:
        print('该符号不在字典中')
        continue
    print('code',code)
    for c in code:
        if c == '.':
            ret = winsound.Beep(freq1,interv_short)
            print('ret = ',ret)
            time.sleep(0.1) #加入0.1s延时
        elif c == '-':
            ret = winsound.Beep(freq2,interv_long)
            print('ret = ',ret)
            time.sleep(0.1)  
        else:
            print('错误编码')
        time.sleep(0.5)