#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: plane_main.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-06-09 17:38:40
# Last Modified: 2019-06-09 17:38:45
#################################################################

import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print "游戏初始化"
        # 1、创建游戏窗口

        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        pygame.display.set_caption("Flying Hero")
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3、调用私有方法，创建精灵和精灵组
        self.__creat_sprites()

    def __creat_sprites(self):
        pass

    def start_game(self):
        print "游戏开始……"
        running = True
        while running:
            # 1、设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞监测
            self.__check_collide()
            # 4、更新/绘制精灵组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod       # __game_over是一个静态方法
    def __game_over():
        print "游戏结束"
        pygame.quit()
        exit()

if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
