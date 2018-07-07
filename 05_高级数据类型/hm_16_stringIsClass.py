#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_16_stringIsClass.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-01 15:47:42
# Last Modified: 2018-07-01 16:59:54
################################################################# 

# 1、判断空白字符（空格、\t、\n、\r）
space_str = " \t \r \n"
print space_str
print space_str.isspace()

# 2、判断是否是全字母
alpha_str = "abcdefg"
print alpha_str
print alpha_str.isalpha()

# 3、判断是否只有数字
# python3中海油isdecimal、isnumeriic方法可以判断是否全为数字
# 但是这三个方法都不能判断浮点数
# isdecimal仅能判断阿拉伯数字，isdigit和isnumeric还可以判断Unicode编码的数字
# isnumeric还可以判断中文的数字
num_str1 = "123"
print num_str1
print num_str1.isdigit()
num_str2 = u"123"
print num_str2
print num_str2.isdigit()

