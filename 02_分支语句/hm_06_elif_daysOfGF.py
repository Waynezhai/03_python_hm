#!/usr/bin/python
#coding=utf-8

"""
定义字符串 holiday_name 记录节日名称
不同的节日采用不同的方式庆祝
"""

holiday_name = raw_input("以点分形式输入节日，形如“2.14”：")

if holiday_name == "2.14":
	print "今天是情人节，应该送玫瑰，看电影！"
elif holiday_name == "3.8":
	print "今天是妇女节，应该送姨妈巾！"
elif holiday_name == "2.1":
	print "今天是生日，应该送蛋糕，吃大餐！"
elif holiday_name == "12.25":
	print "今天是圣诞节，应该去教堂，一起嗨！"
else:
	print "今天不是特殊节日，那这一天可能是不存在的一天！"
