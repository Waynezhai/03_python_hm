#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_changeGlobalVariableSucess.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 17:15:57
# Last Modified: 2018-08-10 17:18:19
################################################################# 

"""
如果要在函数内部修改全局变量，需要用到global关键字
"""

num = 10

def demo1():
    print "demo1 ==> %d" % num

def demo2():
    global num
    num = 99
    print "demo2 ==> %d" % num

demo1()
demo2()
demo1()
demo2()
