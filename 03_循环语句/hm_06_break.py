#!/usr/bin/python
#coding=utf-8

"""
用while循环实现五次打印 "Hello Python"
当i == 5时，跳出整个循环，不再进行继续循环，注意与continue的区别
"""

i = 0
while i< 50:
	if i == 5:
		break
	print "Hello Python"
	i = i + 1
print "-" * 10 + "break over" + "-" * 10
