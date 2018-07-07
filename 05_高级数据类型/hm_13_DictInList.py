#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_13_DictInList.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-30 23:16:12
# Last Modified: 2018-07-01 08:21:09
################################################################# 

#使用多个键值对，存储+描述一个物体的相关信息
#描述更复杂的数据信息一般将多个字典放在一个列表中，再进行循环遍历
card_list = [
        {"name": "zhangsan",
            "qq_num": 123456,
            "phone": 10086},
        {"name": "lisi",
            "qq_num": 654321,
            "phone": 10010},
        ]

for card_info in card_list:
    print card_info

