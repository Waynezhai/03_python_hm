#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_05_initMethod.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-17 14:31:04
# Last Modified: 2018-09-17 23:56:44
################################################################# 

"""
这个初始化方法就是“__init__”方法，__init__是对象的内置方法
__init__方法是专门用来定义一个类具有哪些属性的方法！！！
使用类名创建对象是，会自动引用__init_方法
"""

class Cat:
    def __init__(self):
        # print "这是初始化方法"
        self.name = "Tom"

    def eat(self):
        print "%s爱吃鱼！" % self.name

    def drink(self):
        print "%s要喝水！" % self.name

tom = Cat()
tom.eat()
tom.drink()
