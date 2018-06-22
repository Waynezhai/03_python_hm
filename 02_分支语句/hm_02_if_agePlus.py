#!/usr/bin/python
#coding=utf-8

"""
1、输入一个变量记录年龄
2、判断是否满了18岁
3、如果满了18岁，就可以去哇昂吧happy了
"""

age = raw_input("报上你的年龄：")

if age.isdigit():
	age = int(age)
	if age >= 18:
		print "您已经满了18岁,可以进入网吧嗨皮了！"
	else:
		print "你还是个小屁孩儿，一边儿玩儿去！"
else:
	print "年龄都输不对，你可能是喝多了！"



