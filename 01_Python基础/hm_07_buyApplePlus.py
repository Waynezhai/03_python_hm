#coding=utf-8

"""
输入苹果的单价
输入苹果的重量
计算支付的总金额
"""

price_str = input("输入苹果的单价：")
weight_str = input("输入苹果的重量：")

money = float(price_str) * float(weight_str)

print money 
