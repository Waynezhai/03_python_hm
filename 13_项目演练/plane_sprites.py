#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: plane_sprites.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 16:05:30
# Last Modified: 2019-06-09 16:05:32
#################################################################

import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)   # 屏幕大小的常量
FRAME_PER_SEC = 60      #刷新帧率常量

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
