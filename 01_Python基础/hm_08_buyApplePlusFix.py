#coding=utf-8

"""
输入苹果的单价
输入苹果的重量
计算支付的总金额
"""

price = float(input("输入苹果的单价："))
weight = float(input("输入苹果的重量："))

money = price * weight

print "You should pay %.2f YUAN" % (money)
