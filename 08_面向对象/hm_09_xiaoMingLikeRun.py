#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_09_xiaoMingLikeRun.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-25 08:40:37
# Last Modified: 2018-09-25 09:12:23
################################################################# 


class Person:
    def __init__(self, name = "小美", weight = 72.50):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s , 我的体重是 %.2f ." % (self.name, self.weight)

    def __del__(self):
        pass

    def run(self):
        self.weight -= 0.5
        print "%s 跑了一次步，现在体重 %.2f ." % (self.name, self.weight)
    
    def eat(self):
        self.weight += 1
        print "%s 吃了一次东西，现在体重 %.2f ." % (self.name, self.weight)
    

xiaoming = Person("小明", 75.5)
xiaomei = Person()
print xiaoming
print xiaomei
xiaoming.eat()
xiaoming.run()
xiaomei.run()
xiaomei.run()
xiaoming.eat()
print xiaoming
print xiaomei

