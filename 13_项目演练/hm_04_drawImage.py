#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_04_drawImage.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-23 20:06:24
# Last Modified: 2019-05-23 20:06:26
#################################################################


import pygame

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
pygame.display.update()


# 游戏循环---可以增加很多游戏控制
while True:
    pass

pygame.quit()
