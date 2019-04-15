#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_sameElementInParents.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-14 17:42:49
# Last Modified: 2019-04-15 22:55:45
################################################################# 

class A:
    def test(self):
        print "A---test 方法！"
    def demo(self):
        print "A---demo 方法！"

class B:
    def test(self):
        print "B---test 方法！"
    def demo(self):
        print "B---demo 方法！"

class C(A, B):
    """
    多继承可以让子类对象，同时具有多个父类的属性和方法
    """
    pass


class D(B, A):
    """
    多继承可以让子类对象，同时具有多个父类的属性和方法
    """
    pass

# 创建对象
c = C()
c.test()
c.demo()
# print C.__mro__

d = D()
d.test()
d.demo()
# print D.__mro__

# python3中可以用“__mro__”内置属性来查看多继承的父类引用顺序

