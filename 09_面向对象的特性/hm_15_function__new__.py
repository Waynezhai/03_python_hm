#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_15_function__new__.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-19 22:16:42
# Last Modified: 2019-04-19 22:46:31
################################################################# 

class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 1、创建对象时，__new__方法会被自动调用
        print "创建对象，分配空间！"
        
        # 2、为对象分配空间---python3中利用super().__new__(cls)分配空间
        instance = object.__new__(cls)
        #instance = super().__new__(cls)
        
        # 3、范辉对象的引用
        return instance

    def __init__(self):
        print "播放器初始化！"
    

# 创建播放器对象
player = MusicPlayer()

print player
