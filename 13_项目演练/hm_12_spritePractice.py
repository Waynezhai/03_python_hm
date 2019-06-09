#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_12_spritePractice.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 16:22:16
# Last Modified: 2019-06-09 16:22:17
#################################################################

import pygame
from plane_sprites import *

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


# 创建敌机的精灵
enemy1 = GameSprite(r'E:\Desktop\Server Constant\images\enemy1.png')
enemy2 = GameSprite(r'E:\Desktop\Server Constant\images\enemy1.png', 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print "游戏结束……"
            #pygame.quit()
            #exit()

    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)


    # 让精灵组调用两个方法
    # update---让组中的所有精灵更新位置
    enemy_group.update()
    # draw---在screen上绘制所有的精灵
    enemy_group.draw(screen)

    pygame.display.update()

    if hero_rect.y <= -126:
        hero_rect.y = 700

pygame.quit()
exit()
