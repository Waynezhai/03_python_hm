#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_04_readline.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 07:48:07
# Last Modified: 2019-05-06 22:18:11
################################################################# 

file = open("README")

while True:
    
    text = file.readline()

    if not text:
        break

    # 打印的时候，因为每一行的行末都有\n，所以不需要避免print的时候换行 
    print text,

file.close()
