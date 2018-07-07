#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_17_stringFindAndReplace.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 17:09:11
# Last Modified: 2018-07-01 19:54:04
################################################################# 

hello_str = "Hello Hello Python"

# 1、判断是否以指定字符串开始
print hello_str.startswith("Hello")
print hello_str.startswith("hello")

# 2、判断是否以指定字符串结束
print hello_str.endswith("thon")

# 3、查找指定字符串
# index方法和find方法很相似，但是对于找不到的字符串，find方法返回“-1”，index方法会报错
print hello_str.find("llo")
print hello_str.find("abc")

# 4、替换字符串
# replace方法不会改变原有的字符串
new_hello = hello_str.replace("Python", "World")
print hello_str
print new_hello
