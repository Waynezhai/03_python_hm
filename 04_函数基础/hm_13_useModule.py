#!/usr/bin/python
#coding=utf-8

"""
.py文件都可以作为一个模块被导入
模块中的函数和全局变量都可以提供给外界使用
"""

import hm_13_linesModule

c = raw_input("请输入分割线字符：")
t = input("请输入分割线长度：")
hm_13_linesModule.print_lines(c, t)

print hm_13_linesModule.name
