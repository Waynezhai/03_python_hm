#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# Filename: hm_07_globalVariableLocation.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 17:22:55
# Last Modified: 2018-08-10 17:38:20
################################################################# 

"""
全局变量的定义必须在函数调用之前
建议在代码的最前面定义全局变量
代码结构建议如下：
    1、shebang
    2、import模块
    3、全局变量
    4、函数定义
    5、执行代码
"""

gl_num = 10

def demo():
    print "gl_num ==> %d" % gl_num
    print "gl_title ==> %s" % gl_title
    print "gl_name ==> %s" % gl_name

gl_title = "heima"

#如果gl_name定义在demo调用前，则会报错
gl_name = "xiaoming"

demo()

#gl_name = "xiaoming"
