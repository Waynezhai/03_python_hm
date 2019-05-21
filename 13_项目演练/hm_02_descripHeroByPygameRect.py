#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_02_descripHeroByPygameRect.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-21 15:48:16
# Last Modified: 2019-05-21 16:04:09
################################################################# 

import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print "英雄的原点（%d, %d）" % (hero_rect.x, hero_rect.y)
print "英雄的尺寸（%d, %d）" % (hero_rect.width, hero_rect.height)
print "英雄的尺寸（%d, %d）" % hero_rect.size

