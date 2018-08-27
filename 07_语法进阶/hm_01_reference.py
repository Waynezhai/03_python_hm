#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_01_reference.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-24 18:01:23
# Last Modified: 2018-07-24 18:18:41
################################################################# 

def test(num):
    print "在函数 test 内部，%d 对应的内存地址是：%d"%(num, id(num))

# 定义一个数字的变量
a = 10
# 数据的地址本质上就是一个数字
print "a变量保存数据的内存地址是：%d" % id(a)

# 调用 test 函数
test(a)
