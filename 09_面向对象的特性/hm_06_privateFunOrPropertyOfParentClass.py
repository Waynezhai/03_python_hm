#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_privateFunOrPropertyOfParentClass.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-11-27 21:20:36
# Last Modified: 2018-11-27 21:36:43
################################################################# 


class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 1000

    def __test_01(self):
        print "这是一个私有方法！"
        
    def test_02(self):
        print "test_02是一个非私有方法！"
        print "\t私有属性 __num2 = %d 可以在这里引用!" % self.__num2
        print "\t私有方法 __test_01也可以在这里使用!"
        self.__test_01()

a = A()
print a.num1
#print a.num2
#a.__test_01()
a.test_02()
