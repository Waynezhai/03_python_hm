#!/usr/bin/python
#coding=utf-8


"""
用循环实现 0-100 之间的所有偶数字求和
在循环内区分偶数

"""

i = 0
even_check = 0
isum = 0

while i < 101:
	even_check = i % 2
	if even_check ==  0:
		print "i = %d" % i
		isum += i
	i += 1
print "0 + 2 + 4 + ... +98 + 100 = %d" % isum

