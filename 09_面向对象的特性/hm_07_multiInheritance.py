#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_07_multiInheritance.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-14 17:42:49
# Last Modified: 2019-04-14 18:06:20
################################################################# 

class A:
    def test(self):
        print "test 方法！"

class B:
    def demo(self):
        print "demo 方法！"

class C(A, B):
    """
    多继承可以让子类对象，同时具有多个父类的属性和方法
    """
    pass


# 创建对象
c = C()
c.test()
c.demo()
