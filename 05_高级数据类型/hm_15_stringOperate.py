#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_15_stringOperate.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 14:30:41
# Last Modified: 2018-07-01 15:47:20
################################################################# 

hello_str = "Hello Hello Python"

# 1、统计字符串长度---len函数
print len(hello_str)


# 2、统计某一个字符或一个子字符串在字符串中出现的次数---count方法
# 若子字符串不存在，则计数为0
print hello_str.count("llo")
print hello_str.count("sss")


# 3、某一个子字符串出现的位置---index方法
# 若子字符串不存在，则报错
print hello_str.index("Py")
#print hello_str.index("yy")
