#!/usr/bin/python
#coding=utf-8


"""
用循环实现 0-100 之间的所有数字求和

"""

i = 0
isum = 0
while i < 101:
	isum += i
	i += 1
print "0 + 1 + ... +99 + 100 = %d" % isum

