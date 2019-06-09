#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_03_createWindow.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-23 18:59:56
# Last Modified: 2019-05-23 19:01:29
#################################################################

import pygame

pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

# 游戏循环---可以增加很多游戏控制
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
