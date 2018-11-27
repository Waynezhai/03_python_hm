#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_03_classXiaoTianQuanCannotInheritCat.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-11-27 20:12:17
# Last Modified: 2018-11-27 20:46:18
################################################################# 

class Animal:
    def eat(self):
        print "吃！"

    def drink(self):
        print "喝！"

    def run(self):
        print "跑！"

    def sleep(self):
        print "睡！"

class Cat(Animal):
    def bark(self):
        print "喵！"

class Dog(Animal):
    def bark(self):
        print "汪！"
"""
XiaoTianQuan虽然可以继承父类Dog，但是不能继承父类的父类Animal的其他子类的属性和方法
"""
class XiaoTianQuan(Dog):
    def fly(self):
        print "咻！"

miao = Cat()
miao.bark()

xiaotian = XiaoTianQuan()
xiaotian.fly()
xiaotian.bark()
