#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_21_elseFinallyInObtainAbnormal.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-22 07:25:14
# Last Modified: 2019-04-23 07:27:08
################################################################# 

try:
	num = int(input("请输入一个整数："))
	result = 8.0 / num
	print result 
except ZeroDivisionError:
    print "0不能作为被除数，请更正！"
except NameError:
    print "请输入正确的整数！"
# 输入 ！ 抛出的语法错误会走以下代码
except Exception as result:
    print "未知错误 %s" % result
else:
    print "未出现错误，尝试成功！"
finally:
    print "无论是否出现错错误，代码都执行到了这里！"
