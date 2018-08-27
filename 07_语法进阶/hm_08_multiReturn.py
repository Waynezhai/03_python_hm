#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_multiReturn.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-10 17:50:39
# Last Modified: 2018-08-20 13:15:00
################################################################# 

"""
模拟测量温湿度，返回温度和湿度两个返回值
"""

def measure():
    print "---测试开始---"
    temp = 39
    wetness = 50
    print "---测试结束---"
    #多个返回值以元组形式返回，括号可以省略
    #return (temp, witness)
    return temp, wetness

#返回元组可以用一个元组变量接收，再次取用时，用下标区分元素
#也可以用多个变量直接接收元组的每个变量，但是变量数目要与元组元素数目相同
result = measure()
gl_temp, gl_wetness = measure()
print result
print result[0]
print result[1]
print gl_temp
print gl_wetness
