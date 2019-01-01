#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_privateFunOrPropertyOfParentClass.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-11-27 21:20:36
# Last Modified: 2019-01-01 17:21:17
################################################################# 


class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 1000

    def __test_01(self):
        print "__test_01 是一个私有方法！"
        
    def test_02(self):
        print "test_02是一个公有方法！"

    def test_03(self):
        print "test_03是一个公有方法！"
        print "\t私有属性 __num2 = %d 可以在这里引用!" % self.__num2
        print "\t私有方法 __test_01也可以在这里使用!"
        self.__test_01()

class B(A):
    pass

b = B()

#1、在子类的对象中不能访问父类的私有属性
#print b.__num2
print "=" * 50

#2、在子类的对象中不能调用父类的私有方法
#b.__test_01
print "=" * 50

#3、在子类的对象中能访问父类的公有属性
print "子类的对象中可访问父类的公有属性 %d " % b.num1
print "=" * 50

#4、在子类的对象中能调用父类的公有方法
b.test_02()
print "=" * 50

#5、在子类的对象中可以通过调用父类的公有方法来间接访问父类的公有属性和公有方法
b.test_03()
print "=" * 50
