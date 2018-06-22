#!/usr/bin/python
#coding=utf-8

"""
if的嵌套是有先后的依赖的
"""


is_ticket = int(raw_input("有没有车票，有填“1”，没填“0”："))
if is_ticket:
	print "已购票，该项通过！"
	is_safe = int(raw_input("有没有过安检，有填“1”，没填“0”："))
	if is_safe:
		print "已通过安检，该项通过！"
		is_rightInport = int(raw_input("是不是在指定检票口，是填“1”，不是填“0”："))
		if is_rightInport:
			print "在指定检票口候车，没有跑偏！"
			is_onBoard = int(raw_input("是不是上车了，是填“1”，不是填“0”："))
			if is_onBoard:
				print "您已上车，等待您的将是轻松加愉快的旅行！"
				is_badTrain = int(raw_input("火车是不是故障，是填“1”，不是填“0”："))
				if not is_badTrain:
					print "恭喜您，已踏上完美的旅程！"
				else:
					print "恭喜你，你是这个世界上运气最差的人！"
			else:
				print "很遗憾 ，这几乎是最完美的擦肩而过了！"
		else:
			print "你跑错检票口了大哥，感觉你要错过整个世界！"
	else:
		print "安检没过，不能通行！"
else:
	print "没买票，快去买票！"
