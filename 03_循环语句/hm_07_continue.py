#!/usr/bin/python
#coding=utf-8

"""
continue跳出本次循环，进入下次循环
用while 循环中，用continue需要注意循环条件的变化，否则很容易产生死循环
"""

i = 0
while i< 10:
	if i % 2 == 1:
		print "-" * 10 +("i = %d now" % i) + "-" * 10,
		print "-" * 10 + "continue once" + "-" * 10
		i += 1
		continue
	else:
		print "Hello Python"
	i = i + 1
