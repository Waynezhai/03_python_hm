#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_09___name__Module.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-25 06:18:16
# Last Modified: 2019-04-25 06:43:34
################################################################# 

"""
模块文件为导入它的程序提供全局变量、函数、类
直接执行的代码不是向外界提供的工具
文件被导入时，能够直接执行的代码不需要直接执行
使用__name__属性解决这个问题
如果直接执行模块文件，__name__即为__main__
如果执行的是导入模块的其他文件，__name__即为模块名
"""

def say_hello():
    print "你好，我是 say_hello！"

if __name__ == "__main__":
    print __name__
    print "小明开发的模块！"
    say_hello()
