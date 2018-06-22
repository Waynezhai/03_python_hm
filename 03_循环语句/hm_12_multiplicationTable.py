#!/usr/bin/python
#coding=utf-8


"""
用循环嵌套做一张九九乘法表
注意print语句中的转义字符的使用
"""

row = 1 
while row < 10:
	col = 1
	while col <= row:
		print "%d * %d = %d\t" % (col, row, row * col),
		col += 1
	print ""
	row += 1

