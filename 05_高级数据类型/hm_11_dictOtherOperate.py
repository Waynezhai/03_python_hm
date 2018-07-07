#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_11_dictOtherOperate.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-30 12:31:23
# Last Modified: 2018-06-30 23:05:42
################################################################# 

xiaoming_dict = {"name": "xiaoming",
                "age": 18}
print xiaoming_dict

#1、统计键值对数目
print len(xiaoming_dict)


#2、合并字典
#update方法可以用于合并一个dict到原有dict，但是如果有重复key，会更新到原有dict
tmp_dict = {"height": 1.75,
            "age": 20}
xiaoming_dict.update(tmp_dict)
print xiaoming_dict


#3、清空字典
#clear方法可以清空字典中的所有键值对
xiaoming_dict.clear()
print xiaoming_dict

