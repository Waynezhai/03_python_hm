#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_22_traverseDictInList.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-06 22:36:03
# Last Modified: 2018-07-07 12:39:56
################################################################# 


student = [
        {"name": "Atu"},
        {"name": "Xiaomei"}
        ]

#在学员列表中搜索指定的姓名

find_name = "Wuyanzu"

for stu_dict in student:
    #print stu_dict
    if stu_dict["name"] == find_name:
        print "成员中包含学员： %s" % find_name
        break
else:
    #如果希望在遍历列表式，所有的字典检查之后，都没有查找得到搜索的目标，还希望有一个统一的提示，就需要用到for……else语句了
    print "成员中没有这个学员： %s ！！！" % find_name


print "循环结束。"
