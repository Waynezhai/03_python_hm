#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_05_changeGlobalVariable.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 17:11:24
# Last Modified: 2018-08-10 17:16:43
################################################################# 

"""
如果在函数内部起始位置给所谓的全局变量赋值，则会重新生成一个同名的局部变量，不会影响全局变量
"""

num = 10

def demo1():
    print "demo1 ==> %d" % num

def demo2():
    num = 99
    print "demo2 ==> %d" % num

demo1()
demo2()
demo1()
demo2()
