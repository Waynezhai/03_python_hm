#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_10_houseAndFurniture.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-26 08:12:15
# Last Modified: 2018-09-26 12:58:39
################################################################# 

import uniout

class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[ %s ] 占地 %.2f 。" %(self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f [剩余面积：%.2f]\n家具：%s" 
                % (self.house_type, self.area, self.free_area, str(self.item_list).decode('string_escape')))
        # Python能够自动将一对小括号内部的代码链接在一起，可以换行不出语法错误
        # print 打印列表时，有中文字符的话，可以用这个方法解决---str(test_list).decode('string_escape')

    def add_item(self, item):
        print "添加家具 %s" % item
        if item.area < self.free_area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print "%s 太大了，无法添加！" % item.name
            return


bed = Furniture("席梦思", 4)
chest = Furniture("衣柜", 2)
table  = Furniture("餐桌", 150)

print bed
print chest
print table
print "=" * 50

my_home = House("两室一厅", 66.6)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print "=" * 50

print my_home
print "=" * 50

# print 打印列表有中文的第二种处理方法，import uniout模块，可以直接使用print打印，否则会以utf-8编码打印
print "家具列表：", my_home.item_list

