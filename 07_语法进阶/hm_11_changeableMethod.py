#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_11_changeableMethod.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-27 11:21:18
# Last Modified: 2018-08-27 11:34:16
################################################################# 

def demo(num_list):
    print "函数开始"
    num_list.append(9)
    print num_list
    print "函数结束"

gl_num_list = [1, 2, 3]
print "函数执行前"
print "=" * 50
print gl_num_list
print "=" * 50
print "=" * 50
demo(gl_num_list)
print "=" * 50
print "=" * 50
print "函数执行后"
print "=" * 50
print gl_num_list
