#!/usr/bin/python
#coding=utf-8


def sum_2_num(num1,num2):
	"""对两个数求和"""
	#num1 = 10
	#num2 = 20
	result = num1 + num2
	print "这两个数求和结果为：%d + %d = %d"  %(num1, num2, result)

a = int(raw_input("请输入第一个数字：a = "))
b = int(raw_input("请输入第二个数字：b = "))
sum_2_num(a,b)
