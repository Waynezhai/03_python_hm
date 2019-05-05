#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_01_fileReadAndWrite.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-05 23:24:55
# Last Modified: 2019-05-05 23:34:38
################################################################# 

"""
在编写打开文件的同时，立即编写关闭文件的操作，以免遗忘
"""
# 1、打开文件
file = open("README")

# 2、读取文件内容
text = file.read()
print text

# 3、关闭文件
file.close()



