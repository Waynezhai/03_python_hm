#!/usr/bin/python
#coding=utf-8


def sum_2_num(num1,num2):
	"""对两个数求和"""
	result = num1 + num2
	return result
	print "%d + %d = %d"  %(num1, num2, result)
	#return是函数的结束，后续的代码是不会被执行的。

a = int(raw_input("请输入第一个数字：a = "))
b = int(raw_input("请输入第二个数字：b = "))
c = sum_2_num(a,b)
print "计算结果为：%d" %(c)
