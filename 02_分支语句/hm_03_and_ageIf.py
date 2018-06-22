#!/usr/bin/python
#coding=utf-8

"""
1、判断一个你年龄是不是一个正确的输入
"""

age = raw_input("请输入一个年龄：")

if age.isdigit():
	age = int(age)
	if age > 0 and age <= 150:
		print "恭喜您！您还是个正常人！"
	else:
		print "不好意思，您可能活出了边界！"
else:
	print "你可能喝多了，年龄只能是正整的数字啊，大哥！"
