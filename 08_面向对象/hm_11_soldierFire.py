#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_11_soldierFire.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-26 12:59:01
# Last Modified: 2018-09-26 22:53:30
################################################################# 

import uniout

class Gun:
    def __init__(self, model, bullet_count, owner=None):
        self.model = model
        self.bullet_count = bullet_count
        self.bullet_max = 50
        self.owner = owner

    def __str__(self):
        return "%s 得到一把 %s ，子弹数量 %d ！" %(self.owner, self.model,  self.bullet_count)

    def add_bullet(self, count):
        self.bullet_count += count
        if self.bullet_count <= self.bullet_max:
            print "装弹 %d 颗，弹夹剩余子弹 %d 颗！" % (count, self.bullet_count)
        else:
            num_update = count - (self.bullet_count - self.bullet_max)
            self.bullet_count = self.bullet_max
            print "欲装弹 %d 颗，装弹 %d 颗后，弹夹已装满，当前子弹 %d 颗 ！" % (count, num_update, self.bullet_max)

    def shoot(self, count=1):
        fired = 0
        for x in range(count):
            if self.bullet_count > 0:
                self.bullet_count -= 1
                fired += 1
            else:
                print "弹药不足，",
                break
        print "开了 %d 枪，剩余子弹为 %d 颗！" % (fired, self.bullet_count)

    def token(self, owner):
        self.owner = owner

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def __str__(self):
        return "士兵 %s 到位！" % self.name

    def add_bullet(self, count):
        if self.gun == None:
            print "%s 还是个新兵，还没有枪，装个茄子的子弹！" % self.name
            return
        else:
            self.gun.add_bullet(count)

    def fire(self, count):
        if self.gun == None:
            print "%s 还是个新兵，还没有枪，开个茄子的枪！" % self.name
            return
        else:
            self.gun.shoot(count)
        


ak47 = Gun("AK47",10)
# print ak47
# ak47.add_bullet(32)
# ak47.add_bullet(28)
# ak47.shoot(3)
# ak47.shoot(25)
# ak47.shoot(100)

xusanduo = Soldier("许三多")
print xusanduo
xusanduo.gun = ak47
ak47.token(xusanduo.name)
print xusanduo.gun
xusanduo.add_bullet(32)
xusanduo.fire(13)

print "=" * 50

chenxiaoer = Soldier("陈小二")
print chenxiaoer
print chenxiaoer.gun
chenxiaoer.add_bullet(12)
chenxiaoer.fire(11)
