#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_12_classFunction.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-17 07:50:51
# Last Modified: 2019-04-18 07:40:16
################################################################# 

class Tool(object):
    cnt = 0
    
    def __init__(self, name):
        self.name = name
        print "哈，增加了一个工具 %s" % self.name
        Tool.cnt += 1

    @classmethod
    def showToolCnt(cls):
        print "目前工具箱中工具的数量为 %d " % cls.cnt


banShou = Tool("扳手")
chuiZi = Tool("锤子")
luoSiDao = Tool("螺丝刀")

print "*" * 50
# print "目前工具箱中工具的数量为 %d " % Tool.cnt
Tool.showToolCnt()
