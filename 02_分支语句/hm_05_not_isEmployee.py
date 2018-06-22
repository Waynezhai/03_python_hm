#!/usr/bin/python
#coding=utf-8

"""
练习：定义一个布尔变量 is_employee，编写判断是否是本公司员工
如果不是，提示不允许入内
在开发中，通常希望某个条件不满足时，执行一些代码，可使用 not
另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到 not
"""

is_employee = True

if not is_employee:
	print "你这个外人，该快走开！"
else:
	print "自己人，里面请！"
