#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_07_delMethod.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-19 08:02:00
# Last Modified: 2018-09-19 08:36:02
################################################################# 

"""
__del__方法会在程序结束时删除对象
如果对象呗del关键字删除，那么会在删除后立即调用__del__方法
"""

class Cat:
    def __init__(self, name):
        self.name = name
        print "%s is coming !" % self.name
    def __del__(self):
        print "%s will go !" %self.name


tom = Cat("Tom")
kitty = Cat("Kitty")

del tom
print "-" * 50

