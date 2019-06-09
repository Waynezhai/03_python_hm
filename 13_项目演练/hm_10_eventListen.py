#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_10_eventListen.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 12:19:12
# Last Modified: 2019-06-09 12:19:16
#################################################################

import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))

# 统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 106)

# 游戏循环---游戏的正式开始
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # tick方法指定代码的执行频率，参数表示1s刷新多少次
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print event_list

    # 修改飞机的位置
    hero_rect.y -= 1

    # 调用blit方法传图到窗口
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用update方法更新显示
    pygame.display.update()
    if hero_rect.y <= -126:
        hero_rect.y = 700

pygame.quit()
