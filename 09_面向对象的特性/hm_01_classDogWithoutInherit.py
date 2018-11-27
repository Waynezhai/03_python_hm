#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_01_classDogWithoutInherit.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-11-27 20:12:17
# Last Modified: 2018-11-27 20:24:16
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

class Dog:
    def eat(self):
        print "吃！"

    def drink(self):
        print "喝！"

    def run(self):
        print "跑！"

    def sleep(self):
        print "睡！"

    def bark(self):
        print "汪！"

class XiaoTianQuan:
    def eat(self):
        print "吃！"

    def drink(self):
        print "喝！"

    def run(self):
        print "跑！"

    def sleep(self):
        print "睡！"

    def bark(self):
        print "汪！"

    def fly(self):
        print "咻！"

miao = Animal()
miao.eat()

xiaotian = XiaoTianQuan()
xiaotian.fly()
