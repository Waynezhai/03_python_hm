#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_01_firstOOP.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-17 14:31:04
# Last Modified: 2018-09-17 23:12:17
################################################################# 

class Cat:
    def eat(self):
        print "小猫爱吃鱼！"

    def drink(self):
        print "小猫要喝水！"

# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print tom

addr = id(tom)
print "%d" % addr 
print "0x%x" % addr 
