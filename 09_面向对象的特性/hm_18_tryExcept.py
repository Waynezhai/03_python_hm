#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_18_tryExcept.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-21 22:54:55
# Last Modified: 2019-04-22 07:26:29
################################################################# 

"""
try 后面放的是不确定能正确执行的代码
except 后面放的是出现错误时，执行的代码
try 后的代码无异常，except 后面的代码就不会被执行
无论try和excpet的哪段代码被执行，程序都会继续往下执行，不会停止
"""

try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
except:
    print "您的输入有误，请确认输入的是一个整数！！！"

print "*" * 50
#print "您输入的整数为：%d " % num
