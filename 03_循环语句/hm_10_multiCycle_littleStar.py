#!/usr/bin/python
#coding=utf-8


"""
1、输入十行小星星，第一行一个，第二行2个，第三行三个……
2、小星星居中显示
3、使用循环嵌套处理
4、python2的print后不换行不空格的方法参考：https://segmentfault.com/q/1010000000095970
"""

row = 1 
while row <= 10:
	col = 1
	while col <= row:
		print "\b*",
		col += 1
	print ""
	row += 1

