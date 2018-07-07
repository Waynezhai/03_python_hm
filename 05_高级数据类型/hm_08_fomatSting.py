#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_fomatSting.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-28 22:59:29
# Last Modified: 2018-06-28 23:06:34
################################################################# 

#格式化字符串后面的“（）”本质上就是元组
info_tuple = ("小明", 18, 1.75)

print "%s 年龄是 %d，身高是 %.2f" %("小明", 18, 1.75)
print "%s 年龄是 %d，身高是 %.2f" % info_tuple

info_str = "%s 年龄是 %d，身高是 %.2f" % info_tuple
print info_str

