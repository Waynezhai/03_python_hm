#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_bigFileCopy.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 22:21:18
# Last Modified: 2019-05-06 22:37:51
################################################################# 

# 1、打开文件
file_s = open("README", "r")
file_d = open("readme.bak", "w")

# 2、读取源文件，写入到目标文件中
while True:
    line = file_s.readline()
    if not line:
        break
    else:
        file_d.write(line)
    print line,


# 3、关闭文件
file_s.close()
file_d.close()
