#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_04_rewriteParentClass.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-11-27 20:12:17
# Last Modified: 2018-11-27 20:56:34
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

class Dog(Animal):
    def bark(self):
        print "汪！"

class XiaoTianQuan(Dog):
    def bark(self):
        print "神汪！"

    def fly(self):
        print "咻！"

gouzi = Dog()
gouzi.bark()

xiaotian = XiaoTianQuan()
xiaotian.fly()
xiaotian.bark()
