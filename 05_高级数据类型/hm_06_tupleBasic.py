#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_tupleBasic.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-28 08:59:47
# Last Modified: 2018-06-28 09:08:15
################################################################# 

info_tuple = ("zhangsan", 18,  1.78, "zhangsan")

# 1、取值和取索引
print "元组的第0个元素为：" + info_tuple[0]
print "元组中“zhangsan”的索引值为：%d " %(info_tuple.index("zhangsan"))

# 2、统计计数
print "元组中“zhangsan”出现的次数为：%d" %info_tuple.count("zhangsan")

#3、统计元组中元素个数
print "元组中元素个数为：%d" %len(info_tuple)
