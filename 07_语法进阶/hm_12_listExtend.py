#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_12_listExtend.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-27 11:34:35
# Last Modified: 2018-08-27 11:47:27
################################################################# 

def demo(num_list_1, num_list_2):
    print "函数开始"
    num_list_1 = num_list_1 + num_list_1
    num_list_2 += num_list_2
    print num_list_1
    print num_list_2
    print "函数结束"

gl_num_list_1 = [1, 2, 3]
gl_num_list_2 = [4, 5, 6]
print "函数执行前"
print "=" * 50
print gl_num_list_1
print gl_num_list_2
print "=" * 50
print "=" * 50
demo(gl_num_list_1, gl_num_list_2)
print "=" * 50
print "=" * 50
print "函数执行后"
print "=" * 50
print gl_num_list_1
print gl_num_list_2

