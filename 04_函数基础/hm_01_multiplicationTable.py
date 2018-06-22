#!/usr/bin/python
#coding=utf-8


"""
函数快速体验
九九乘法表的函数封装
"""
def mul_table():
	row = 1 
	while row < 10:
		col = 1
		while col <= row:
			print "%d * %d = %d\t" % (col, row, row * col),
			col += 1
		print ""
		row += 1

if __name__ == "__main__":
	mul_table()
