#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_17_multiParameterSumNums.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-28 18:56:32
# Last Modified: 2018-09-10 23:22:46
################################################################# 

def sum_numbers(*args):
    num = 0
    #print type(args[0])
    print args
    for n in args:
        num += n
    return num

r = sum_numbers(1, 2, 3, 4, 5) 
print "求和结果为：sum = %d" % r 
