#!/usr/bin/python
#coding=utf-8

"""
验证def定义的函数执行的时机
python 解释器知道def下方定义了一个函数，并不实际执行
只有在程序中，主动调用函数，才会让函数执行
def定义函数须在使用函数之前，否则将会报错
"""

name = "小明"

#say_hello()

def say_hello():
	print "Hello 1"
	print "Hello 2"
	print "Hello 3"

print name
say_hello()
print name
