#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_03_addProperty.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-17 14:31:04
# Last Modified: 2018-09-17 23:12:41
################################################################# 

class Cat:
    def eat(self):
        print "小猫爱吃鱼！"

    def drink(self):
        print "小猫要喝水！"

tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
print "这只小猫的名字是 %s" % tom.name
