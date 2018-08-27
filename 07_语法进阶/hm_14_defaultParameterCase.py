#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_14_defaultParameterCase.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-08-27 15:17:44
# Last Modified: 2018-08-27 15:30:34
################################################################# 

def print_info(name, gender):
    gender_text = "BOY"
    if not gender:
        gender_text = "GIRL"
    print "%s is a %s" % (name, gender_text)

def print_info_super(name, gender=True):
    gender_text = "BOY"
    if not gender:
        gender_text = "GIRL"
    print "%s is a %s" % (name, gender_text)

print_info("XiaoMing", True)
print_info("XiaoMei", False)
print_info_super("XiaoMing")
print_info_super("XiaoMei", False)

