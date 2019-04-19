#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_16_singleCase.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-19 22:46:56
# Last Modified: 2019-04-19 23:13:12
################################################################# 

class MusicPlayer(object):
    pass

# 创建多个对象
player_1 = MusicPlayer()
print player_1

player_2 = MusicPlayer()
print player_2


class MusicPlayerX(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance
    
    def __init__(self, name):
        self.name = name
        print "%s 初始化！" % self.name

#MusicPlayerX.instance = None
# 创建多个对象
player_3 = MusicPlayerX("player_3")
print player_3

player_4 = MusicPlayerX("player_4")
print player_4

player_5 = MusicPlayerX("player_5")
print player_5

