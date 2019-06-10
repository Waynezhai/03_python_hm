#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: plane_sprites.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 16:05:30
# Last Modified: 2019-06-09 16:05:32
#################################################################

import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)   # 屏幕大小的常量
FRAME_PER_SEC = 60      # 刷新帧率常量
CREATE_ENEMY_EVENT = pygame.USEREVENT       # 创建敌机的定时器常量

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1、调用父类方法实现精灵的创建
        GameSprite.__init__(self, r'E:\Desktop\Server Constant\images\background.png')
        # 2、判断是否是交替图像，如果是，需要设置初始位置
        if is_alt == True:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类的方法实现
        GameSprite.update(self)
        # 2、判断图像是否移出屏幕，如果图像移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1、调用父类方法，创建敌机精灵，同时制定敌机图片
        GameSprite.__init__(self, r'E:\Desktop\Server Constant\images\enemy1.png')
        # 2、指定敌机的初始随机速度 1~3
        self.speed = random.randint(1, 3)
        # 3、指定敌机的初始随机位置
        #self.rect.y = -self.rect.height
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1、调用父类方法，保持垂直方向的飞行
        GameSprite.update(self)
        # 2、判断是否飞出屏幕，一旦飞出，从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print "飞出屏幕，需要从精灵组中删除……"
            # kill 方法可以将精灵从所有精灵组中移出，精灵就会自动销毁
            self.kill()

    def __del__(self):
        print "敌机挂了 %s" % self.rect
