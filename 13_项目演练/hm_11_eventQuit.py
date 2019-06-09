#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_11_eventQuit.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 12:30:02
# Last Modified: 2019-06-09 12:30:05
#################################################################

import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
screen.blit(bg, (0, 0))
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(150, 300, 102, 106)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.quit()
            #exit()

    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

    if hero_rect.y <= -126:
        hero_rect.y = 700

pygame.quit()
exit()
