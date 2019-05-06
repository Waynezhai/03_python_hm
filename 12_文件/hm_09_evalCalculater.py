#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_09_evalCalculater.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-06 23:45:16
# Last Modified: 2019-05-06 23:51:54
################################################################# 

"""
eval()函数不能滥用
如果 __import__("os").system("终端命令") 作为eval函数的输入，则终端命令会被执行
"""

input_str = raw_input("请输入一个计算题：")

print "计算结果为：%s" % eval(input_str)

