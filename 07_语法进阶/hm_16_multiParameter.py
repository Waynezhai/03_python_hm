#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_16_multiParameter.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-28 18:46:46
# Last Modified: 2018-09-10 12:37:23
################################################################# 

def demo(num, *nums, **person):
    print num
    print nums
    print person

demo(1)
print "=" * 50
demo(1, 2, 3, 4)
print "=" * 50
demo(1, 2, 3, 4, name="XiaoMing")
print "=" * 50
demo(1, 2, 3, 4, name="XiaoMing", age=18)
print "=" * 50
#后续如果再输入非键值对，则会报错
#demo(1, 2, 3, 4, name="XiaoMing", 5, 6)

