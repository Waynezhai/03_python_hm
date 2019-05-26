#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_09_heroFlyForever.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-26 18:51:58
# Last Modified: 2019-05-26 18:52:02
#################################################################

import pygame
import time

# 游戏的初始化
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 1、使用pygame.image.load()加载图像的数据
bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
# bg = pygame.image.load("./images/background.png")
# windows平台下，不能使用相对路径，且路径中不能出现中文

# 2、使用游戏屏幕对象，调用blit方法，将图像绘制到指定的位置
screen.blit(bg, (0, 0))

# 3、调用pygame.display.update()方法更新整个屏幕的显示
#pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1、定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 106)

# 游戏循环---可以增加很多游戏控制---意味着游戏的正式开始
while True:
    # 可以做指定循环体内部的diamante执行的频率
    clock.tick(60)

    # 2、修改飞机的位置
    hero_rect.y -= 1

    # 3、调用blit方法传图到窗口
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4、调用update方法更新显示
    pygame.display.update()
    if hero_rect.y <= -126:
        hero_rect.y = 700
    continue

pygame.quit()
