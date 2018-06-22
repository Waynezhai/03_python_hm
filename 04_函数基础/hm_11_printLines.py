#!/usr/bin/python
#coding=utf-8


def print_line(char, times):
	print char * times

def print_lines(char,times,lines):
	row = 0
	while row < lines:
		print_line(char,times)
		row += 1

c = raw_input("请输入一个字符：")
t = input("请输入重复次数：")
l = input("请输入分割线的行数：")
print_lines(c,t,l)

