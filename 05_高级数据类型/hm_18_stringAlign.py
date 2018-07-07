#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_18_stringAlign.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 19:55:26
# Last Modified: 2018-07-01 20:20:13
################################################################# 

# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容

poem = [u"登鹳雀楼",
        u"王之涣",
        u"白日依山尽，",
        u"黄河入海流。",
        u"欲穷千里目，",
        u"更上一层楼。"
        ]

for line in poem:
    print line
print "====================================="
for line in poem:
    print line.center(10)
print "====================================="
for line in poem:
    print "|%s|"%line.center(10)
print "====================================="
for line in poem:
    #这里使用全角的空格来填充
    print "|%s|"%line.center(10, u"　")
print "====================================="
for line in poem:
    #这里使用全角的空格来填充
    print "|%s|"%line.ljust(10, u"　")
print "====================================="
for line in poem:
    #这里使用全角的空格来填充
    print "|%s|"%line.rjust(10, u"　")
