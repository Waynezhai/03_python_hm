#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_10_immutableAssign.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-27 10:42:27
# Last Modified: 2018-08-27 11:19:20
################################################################# 

def demo(num,num_list):
    print "函数开始"
    num = 99
    num_list = [1, 2, 3]
    print num
    print num_list
    print "函数结束"

gl_num = 100
gl_num_list = [4, 5, 6]
print "函数执行前"
print "=" * 50
print gl_num
print gl_num_list
print "=" * 50
print "=" * 50
demo(gl_num, gl_num_list)
print "=" * 50
print "=" * 50
print "函数执行后"
print "=" * 50
print gl_num
print gl_num_list
