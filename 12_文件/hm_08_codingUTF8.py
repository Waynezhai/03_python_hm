#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_codingUTF8.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 23:31:40
# Last Modified: 2019-05-06 23:39:24
################################################################# 

# 在定义字符串时，在字符串前加一个 u ，这样就可以告诉解释器，这是一个Unicode编码的字符串
# 这样一来，这个字符串在遍历和切片的时候，就能识别其中的中文了
hello_str = u"hello 世界"

print hello_str
print(hello_str)
print (hello_str)

for c in hello_str:
    print c

print "*" * 50
print hello_str[0]
print hello_str[6]
print hello_str[7]
