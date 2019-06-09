#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_06_functionUpdate.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-26 17:47:23
# Last Modified: 2019-05-26 17:47:50
#################################################################

import pygame

pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
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


# 游戏循环---可以增加很多游戏控制
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
