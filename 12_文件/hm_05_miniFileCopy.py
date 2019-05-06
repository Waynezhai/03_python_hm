#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_05_miniFileCopy.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 22:21:18
# Last Modified: 2019-05-06 22:28:40
################################################################# 

# 1、打开文件
file_s = open("README", "r")
file_d = open("readme.bak", "w")

# 2、读取源文件，写入到目标文件中
text = file_s.read()
print "读取到的文件内容为：\n%s" % text,
print "*" * 50
print "文件写入到 readme.bak 中..."
file_d.write(text)

# 3、关闭文件
file_s.close()
file_d.close()
