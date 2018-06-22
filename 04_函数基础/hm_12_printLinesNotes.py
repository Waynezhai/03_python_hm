#!/usr/bin/python
#coding=utf-8


def print_line(char, times):
	print char * times

def print_lines(char,times):
	"""打印多行分割线
	:param char: 分割线使用的字符
	:param times: 分隔线重复的次数
	
	"""
	row = 0
	while row < 5:
		print_line(char,times)
		row += 1

print print_lines.__doc__
c = raw_input("请输入一个字符：")
t = input("请输入重复次数：")
print_lines(c,t)

