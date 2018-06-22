#!/usr/bin/python
#coding=utf-8

"""
c_score和python_score只要有一门大于60即为及格
这里原创了一个仅输入整数或小数的函数，值得关注
"""

def input_num():
	while True:
		num = raw_input()
		if num.replace('.', '', 1).isdigit():
			num = float(num)
			#print "%.2f" % num
			return num
		else:
			print "输入出错了,请重新输入：",


if __name__ == "__main__":
	print "请输入你的C语言成绩：",
	c_score = input_num()
	print "请输入你的Pyton成绩：",
	python_score = input_num()
	if c_score >= 60 or python_score >= 60:
		print "恭喜您，您过关了，去庆祝吧！"
	else:
		print "很遗憾，您没有通过，您可以选择补考一门，或者去死！"


