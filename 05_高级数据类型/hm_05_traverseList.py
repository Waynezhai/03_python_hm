#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_05_traverseList.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-28 08:37:59
# Last Modified: 2018-06-28 08:47:49
################################################################# 

name_list = ['zhangsan', 'lisi', 'wangwu', 'zhangsan']

# 使用迭代遍历列表
"""
顺序地从列表中获取数据，每一次循环过程中，数据都会保存在 my_name 这个变量中，
在循环体内部可以访问当前这一次获取到的数据
for my_name in 列表名称:
    print "my name is %s" %(my_name)
"""
for my_name in name_list:
    print "my name is %s" %(my_name)

