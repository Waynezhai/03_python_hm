#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_14_comprehensivFunction.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-19 06:39:07
# Last Modified: 2019-04-19 07:14:07
################################################################# 

"""
1、设计一个Game类
2、定义两个属性
    定义一个类属性，记录游戏历史最高分
    定义一个实例属性，记录当前游戏的玩家姓名
3、定义是哪个方法
    静态方法：显示游戏帮助信息
    类方法：显示历史最高分
    实例方法：开始当前玩家的游戏'
4、主程序步骤
    A、查看帮助信息
    B、查看历史最高分
    C、创建游戏对象，开始游戏
"""

class Game(object):
    scoreMax = 0
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    @staticmethod
    def helpInfo():
        print "帮助信息！"

    @classmethod
    def scoreMaxPr(cls):
        print "历史最高分为 %s !" % cls.scoreMax

    def gamePlay(self):
        print "尊敬的 %s (先生/女士)，请开始游戏！！！" % self.name
        print "ooxx，ooxx"
        print "游戏结束！！！"
        print "-" * 50
        self.score = int(raw_input("您的游戏成绩为："))
        if self.score > Game.scoreMax :
            Game.scoreMax = self.score
        Game.scoreMaxPr()
        print "*" * 50

Game.helpInfo()
Game.scoreMaxPr()
print "*" * 50

xiaoMing = Game("小明")
xiaoMing.gamePlay()
xiaoMei = Game("小美")
xiaoMei.gamePlay()




