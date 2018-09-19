#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_04_selfExplain.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-17 14:31:04
# Last Modified: 2018-09-17 23:31:27
################################################################# 

"""
可以在类外部用“对象.属性 = xxx”的方法定义对象的属性
且属性能传回类中使用
但是这种方法并不推荐
因为定义属性在使用方法之后，则会报错
建议在类中初始化好所有用到的属性，对象个体的属性以参数形式传回类中使用
"""

class Cat:
    def eat(self):
        print "%s爱吃鱼！" % self.name

    def drink(self):
        print "%s要喝水！" % self.name

tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
