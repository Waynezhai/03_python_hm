#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_02_tryExceptType.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-22 07:25:14
# Last Modified: 2019-04-23 23:03:53
################################################################# 

try:
	num = int(input("请输入一个整数："))
	result = 8.0 / num
	print result 
except ZeroDivisionError:
    print "0不能作为被除数，请更正！"
except (NameError, SyntaxError):
    print "请输入正确的整数！"
