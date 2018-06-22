#!/usr/bin/python3


"""
认识python3的行尾换行
了解如何在python3中实现print打印不换行
"""

print("这行展示打印一个“*”之后换行：*")
print("这行展示打印一个“*”之后不换行（输入“回车”后换行）：*",end = "")
if input() == 0x0d:
	print("")
print("这行展示打印一个“*”之后不换行,并以“---”结尾,(输入“回车”后结束程序）：*",end = "---")
if input() == 0x0d:
	print("")
