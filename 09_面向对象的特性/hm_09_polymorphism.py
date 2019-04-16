#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_09_polymorphism.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-16 23:21:45
# Last Modified: 2019-04-16 23:36:31
################################################################# 

class Dog(object):
    
    def __init__(self, name):
        self.name = name

    def game(self):
        print "%s 蹦蹦跳跳地玩耍！" % self.name

class XiaoTianDog(Dog):
    def game(self):
        print "%s 飞到天上去玩耍！" % self.name

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print "%s 和 %s 快乐地玩耍！" %(self.name, dog.name)
        
        # 让狗玩耍
        dog.game()


xiaoTian = XiaoTianDog("啸天")
wangCai = Dog("旺财")
liMing = Person("李明")

liMing.game_with_dog(xiaoTian)
print "*" * 50
liMing.game_with_dog(wangCai)


