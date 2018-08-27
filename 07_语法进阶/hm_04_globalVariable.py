#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_04_globalVariable.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 16:50:39
# Last Modified: 2018-08-10 17:05:35
################################################################# 

"""
不允许在函数内修改全局变量
"""

num = 10

def demo1():
    print "demo1 ==> %d" % num

def demo2():
    print "demo2 ==> %d" % num
    """
    num = 99        如果在函数中已经使用过全局变量，再进行修改变量，会报错
    print "demo2_fix ==> %d" % num
    """

demo1()
demo2()
demo1()
demo2()
