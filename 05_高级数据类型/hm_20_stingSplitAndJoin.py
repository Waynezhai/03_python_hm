#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_20_stingSplitAndJoin.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 20:36:03
# Last Modified: 2018-07-05 09:04:25
################################################################# 

# 假设：以下内容是从网络上抓取的
# 要求：
#   1、将字符串中的空白字符全部去掉
#   2、再使用“　”作为分隔符，拼接成一个整齐的字符串

poem_str = u"登鹳雀楼\t 王之涣 \t 白日依山尽\t \n 黄河入海流 \t\t欲穷千里目\t\n更上一层楼"
print poem_str
print "====================================="

# 1、拆分字符串
poem_list = poem_str.split()
print poem_list
print "====================================="

# 2、合并字符串
result = " ".join(poem_list)
print result
print "====================================="

# 3、拓展复习
for poem_line in poem_list:
    print poem_line
print "====================================="
for poem_line in poem_list:
    print "|%s|" % (poem_line.center(10, u"　"))
print "====================================="
