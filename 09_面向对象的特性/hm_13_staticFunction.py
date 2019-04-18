#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_13_staticFunction.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-18 07:46:10
# Last Modified: 2019-04-18 07:51:17
################################################################# 

class Dog(object):

    @staticmethod
    def run():
        print "小狗要跑..."

Dog.run()
wangCai = Dog()
wangCai.run()

# 静态方法中，不需要访问实例属性，也不需要访问实例属性
# 调用时，可以用“类.”，也可以用“实例.”调用
