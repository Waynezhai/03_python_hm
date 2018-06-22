#!/usr/bin/python
#coding=utf-8


def test1():
	print "*" * 50

def test2():
	print "-" * 50
	test1()
	print "+" * 50


test2()
