#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_08_renewPositionOfHero.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-26 18:30:31
# Last Modified: 2019-05-26 18:30:34
#################################################################

import pygame
import time

# 游戏的初始化
pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

# 创建背景图像
bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
# bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))

# 统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1、定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 106)

# 游戏循环---意味着游戏的正式开始
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 可以做指定循环体内部的代码执行的频率，参数为x，即1秒刷新频率为x次
    clock.tick(60)

    # 2、修改飞机的位置
    hero_rect.y -= 1

    # 3、调用blit方法传图到窗口
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4、调用update方法更新显示
    pygame.display.update()
    if hero_rect.y == -126:
        time.sleep(3)
        break

pygame.quit()
