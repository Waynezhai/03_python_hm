#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_11_fetchPropertyFromObject.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-17 07:50:51
# Last Modified: 2019-04-17 23:48:31
################################################################# 

class Tool(object):
    cnt = 0
    def __init__(self, name):
        self.name = name
        print "哈，增加了一个工具 %s" % self.name
        Tool.cnt += 1

banShou = Tool("扳手")
chuiZi = Tool("锤子")
luoSiDao = Tool("螺丝刀")

print "*" * 50
print "目前工具箱中工具的数量为 %d " % Tool.cnt
print "*" * 50
print "目前工具箱中工具的数量为 %d （数值来自螺丝刀.cnt） " % luoSiDao.cnt
print "*" * 50
print "目前工具箱中工具的数量为 %d （数值来自锤子.cnt）" % chuiZi.cnt

print "*" * 50
print "*" * 50
print "*" * 50
print "工具.cnt的内存地址为 %s" % id(Tool.cnt)
print "螺丝刀.cnt的内存地址为 %s" % id(luoSiDao.cnt)
luoSiDao.cnt = 5
print "给螺丝刀.cnt 赋值为 5 后，螺丝刀.cnt 的值为 %s ，螺丝刀.cnt 的内存地址为 %s " %(luoSiDao.cnt, id(luoSiDao.cnt))
print "而此时，工具.cnt 的值为 %s ，工具.cnt 的内存地址为 %s " % (Tool.cnt, id(Tool.cnt))


# 属性的向上查找机制，虽然“对象.类属性”这种方式可以访问类属性，但是为避免混淆，不推荐这么使用
# 因为如果使用“对象.类属性 = 值”这种赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
