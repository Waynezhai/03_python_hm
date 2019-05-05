#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_02_filePointer.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-05 23:24:55
# Last Modified: 2019-05-05 23:47:35
################################################################# 

"""
在编写打开文件的同时，立即编写关闭文件的操作，以免遗忘
文件指针标记从哪个位置开始读取数据
第一次打开文件时，通常文件指针会只想文件的开始位置
当执行了read方法，文件指针会移动到读取内容的末尾（默认情况下会移动到文件末尾）
"""
# 1、打开文件
file = open("README")

# 2、读取文件内容
text = file.read()
print text
print len(text)
print "*" * 50

text = file.read()
print text
print len(text)

# 3、关闭文件
file.close()



