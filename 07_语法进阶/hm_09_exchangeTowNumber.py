#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_09_exchangeTowNumber.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-20 13:16:44
# Last Modified: 2018-08-20 13:32:04
################################################################# 

#交换两个数字的多种方法

a = int(raw_input("请输入数字a："))
b = int(raw_input("请输入数字b："))
print "a = %d" % a
print "b = %d" % b

def way_1(a, b):
    c = a
    a = b
    b = c
    print "用第一种方法做数字交换，交换后的结果为："
    print "a = %d" % a
    print "b = %d" % b

def way_2(a, b):
    a = a + b
    b = a - b
    a = a - b
    print "用第二种方法做数字交换，交换后的结果为："
    print "a = %d" % a
    print "b = %d" % b

def way_3(a, b):
    a, b = (b, a)
    #这里用到了变量直接接收元组中的值的知识点
    #当然，这里(b, a)的()是可以省略掉的，即可以写成：
    #a, b = b, a
    print "用第三种方法做数字交换，交换后的结果为："
    print "a = %d" % a
    print "b = %d" % b


way_1(a, b)
way_2(a, b)
way_3(a, b)
