#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_05_transitivityOfError.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-23 23:05:46
# Last Modified: 2019-04-23 23:20:46
################################################################# 

"""
异常具有传递性，会向上一层一层传递
可以在主程序中利用异常的传递性，在主程序传递异常
"""

def demo1():
    return int(input("输入一个整数："))

def demo2():
    return demo1()

#print demo1()
#print demo2()

try:
    print demo2()
except Exception as errorInfo:
    print "程序出错，出错信息为：%s" % errorInfo


