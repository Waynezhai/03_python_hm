#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_19_delBlankChar.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 19:55:26
# Last Modified: 2018-07-01 20:35:38
################################################################# 

# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容

poem = [u"\t\n登鹳雀楼",
        u"王之涣",
        u"白日依山尽，",
        u"黄河入海流。\t\n",
        u"欲穷千里目，",
        u"更上一层楼。"
        ]

for line in poem:
    #这里使用全角的空格来填充
    #先使用strip方法去除字符串中的空白字符
    #再使用center方法居中显示文本
    line = line.strip()
    print "|%s|"%line.center(10, u"　")
