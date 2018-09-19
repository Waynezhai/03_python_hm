#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_02_twoObject.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-17 14:31:04
# Last Modified: 2018-09-17 23:02:25
################################################################# 

class Cat:
    def eat(self):
        print "小猫爱吃鱼！"

    def drink(self):
        print "小猫要喝水！"

tom = Cat()
tom.eat()
tom.drink()

print tom

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print lazy_cat

laaaazy_cat = lazy_cat
print laaaazy_cat
