#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_03_localVariable.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 16:06:06
# Last Modified: 2018-08-10 16:47:55
################################################################# 

"""
局部变量的生命周期：
出生：执行到函数内部的代码时创建
死亡：函数执行完结后释放
"""

def demo1():
    num = 10
    print "demo1函数中 num 的值为：%d" % num

def demo2():
    pass
    #print "demo2函数中 num 的值为：%d" % num

demo1()
demo2()
#print "在函数外部 num 的值为：%d" % num

