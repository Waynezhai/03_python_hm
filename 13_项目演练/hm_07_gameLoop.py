#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_07_gameLoop.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-26 18:10:48
# Last Modified: 2019-05-26 18:10:52
#################################################################

import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

#绘制背景图片
bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
# bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
#pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环---可以增加很多游戏控制---意味着游戏的正式开始
i = 0
running = True
while running:
    for event in pygame.event.get():
        #print "==>",event
        if event.type == pygame.QUIT:
            running = False
        # 可以做指定循环体内部的代码执行的频率，参数为x，即1秒刷新频率为x次
        clock.tick(60)
        print i
        i += 1


pygame.quit()
