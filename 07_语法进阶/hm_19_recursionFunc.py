#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_19_recursionFunc.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-10 23:27:11
# Last Modified: 2018-09-10 23:55:52
################################################################# 

def demo(x):
    print x
    if x == 1:
        return
    demo(x - 1)

def sum_num(y):
    if y == 1:
        return 1
    sum_total = sum_num(y - 1) + y
    return sum_total

gl_num = input("请输入一个整数：")
demo(gl_num)
result = sum_num(gl_num)
print "求和结果为：%d" % result

