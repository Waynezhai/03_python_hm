#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_15_defaultParameterOrder.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-28 18:38:01
# Last Modified: 2018-08-28 18:50:41
################################################################# 

"""
如果函数有缺省参数
顺序传递入函数可以依次传递
如果传递时有参数赋值动作，则按照赋值优先，顺序其次
"""

def demo(a, b="B", c="C"):
    print a
    print b
    print c

gl_a = "AAA"
gl_b = "BBB"
gl_c = "CCC"

demo(gl_a, gl_b, gl_c)
print "=" * 50
demo(gl_a, c=gl_c, b=gl_b)
