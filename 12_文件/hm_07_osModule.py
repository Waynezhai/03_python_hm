#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_07_osModule.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 22:42:28
# Last Modified: 2019-05-06 23:30:37
################################################################# 

import os

os.mknod("123")
print "创建了空文件123"
print os.listdir("./")
print "*" * 50

os.rename("123", "1234")
print "重命名 123 为 1234"
print os.listdir("./")
print "*" * 50

os.remove("1234")
print "删除了文件 1234"
print os.listdir("./")
print "*" * 50

os.mkdir("test")
print "创建空文件夹 test"
print os.listdir("./")
print "*" * 50

print "判断 test 是否是文件夹"
print os.path.isdir("test")
print "*" * 50

print "判断 README 是否是文件夹"
print os.path.isdir("README")
print "*" * 50

os.rmdir("test")
print "删除了目录 test"
print os.listdir("./")
print "*" * 50


