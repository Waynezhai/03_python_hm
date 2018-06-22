#!/usr/bin/python
#coding=utf-8

from random import *

"""
1、从终端输入要出的拳种：1代表石头、2代表剪刀、3代表布
2、电脑随机出拳
3、比较胜负输出结果
"""


while True:
	you_hand = raw_input("请出拳(1代表石头、2代表剪刀、3代表布 )：")
	if you_hand.isdigit():
		you_hand = int(you_hand)
		if you_hand == 1:
			print "你出的是：石头 ---",
		elif you_hand == 2:
			print "你出的是：剪刀 ---",
		elif you_hand == 3:
			print "你出的是：布 ---",
		else:
			print "可能你还没理解这个游戏,再给你一次机会吧！"
			continue
	else:
		print "可能你还没理解这个游戏,再给你一次机会吧！"
		continue
	com_hand = randint(1,3)
	if com_hand == 1:
		print "电脑出的是：石头"
	elif com_hand == 2:
		print "电脑出的是：剪刀"
	elif com_hand == 3:
		print "电脑出的是：布"
	else:
		print "出现这种情况可能是因为见鬼了！"
	result = you_hand - com_hand
	if result == 1 or result == -2:
		print "很抱歉，您惨败！"
		break
	elif result == -1 or result ==2:
		print "恭喜你，你赢了！"
		break
	else:
		print "打平了，再来一局吧！"
		continue
