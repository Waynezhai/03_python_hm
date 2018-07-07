#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_12_traverseDict.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-30 23:06:21
# Last Modified: 2018-06-30 23:15:54
################################################################# 

xiaoming_dict = {"name": "xiaoming",
                "age": 18,
                "phone": 10086,
                "qq_num": 123456789}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print "%s --- %s"% (k,xiaoming_dict[k])

