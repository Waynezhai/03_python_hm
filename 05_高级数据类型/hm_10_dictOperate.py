#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_10_dictOperate.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-29 14:32:00
# Last Modified: 2018-06-30 12:31:02
################################################################# 

xiaoming_dict = {"name": "xiaoming"}

#取值
print xiaoming_dict["name"]
#在取值的时候，如果指定的key不存在，程序会报错！
#print xiaoming_dict["name123"]


#增加/修改
#如果字典中没有该键，就增加键并赋值
xiaoming_dict["age"] = 18
#如果字典中原来就有这个键，则赋值即更改
xiaoming_dict["name"] = "xiaoxiaoming"
print xiaoming_dict


#删除
xiaoming_dict.pop("name")
#在删除指定键值对的时候，如果指定的key不存在，程序会报错
#xiaoming_dict.pop("name123")
print xiaoming_dict

