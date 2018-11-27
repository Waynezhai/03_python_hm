#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_12_privatePropertyOrFunction.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-27 08:58:09
# Last Modified: 2018-09-27 09:22:47
################################################################# 


import uniout

class Man:
    def __init__(self, name):
        self.name = name
        self.age = 50

    def secret(self):
        print "%s 的年龄是 %d 岁！" % (self.name, self.age)


class Woman:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print "%s 的年龄是 %d 岁！" % (self.name, self.__age)


chenlaohan = Man("陈老汉")
print chenlaohan.age
chenlaohan.secret()

xiaofang = Woman("小芳")
# 私有属性不允许在对象外部调用，仅能在对象内部的方法中使用
# print xiaofang.__age
# 私有方法也不允许在对象外部调用，仅能在对象内部的方法中被调用
# xiaofang.__secret()

# 在外界可以用“对象名._类名__属性名”“对象名._类名__方法名”强行访问，但这是不推荐的操作
print xiaofang._Woman__age
xiaofang._Woman__secret()
