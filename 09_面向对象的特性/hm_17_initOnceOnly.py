#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_17_initOnceOnly.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-19 22:46:56
# Last Modified: 2019-04-19 23:34:11
################################################################# 

class MusicPlayerX(object):
    # 实例引用标记
    instance = None
    # 记录初始化是否执行过
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance
    
    def __init__(self, name):
        # 1、判断是否执行过初始化动作
        if MusicPlayerX.init_flag:
            return
        # 2、如果没有执行过初始化，再执行初始化动作
        self.name = name
        print "%s 初始化！" % self.name
        # 3、修改类属性init_flag的标记
        MusicPlayerX.init_flag = True

#MusicPlayerX.instance = None
# 创建多个对象
player_1 = MusicPlayerX("player_1")
print player_1

player_2 = MusicPlayerX("player_2")
print player_2

player_3 = MusicPlayerX("player_3")
print player_3

