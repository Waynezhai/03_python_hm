#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_07_traverseTuple.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-28 22:34:44
# Last Modified: 2018-06-28 22:59:09
################################################################# 

info_tuple = ("zhangsan", 18, 1.75)

# 使用for循环迭代遍历元组
for my_info in info_tuple:
    #使用格式字符串拼接 my_info 这个变量是不方便的
    #因为元组中常常保存不同的变量类型:w
    print my_info
