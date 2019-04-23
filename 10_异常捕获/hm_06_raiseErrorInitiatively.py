#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_raiseErrorInitiatively.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-23 23:22:39
# Last Modified: 2019-04-23 23:38:11
################################################################# 

def input_pwd():
    # 提示用户输入密码
    pwd = raw_input("请输入密码：")
    
    # 判断用户密码长度，若 >=8，则输出密码
    if len(pwd) >= 8:
        return pwd

    # 如果 <8 则主动抛出异常
    #print "主动抛出异常"
    # 创建一个异常对象
    error_info = Exception("密码长度不够！！！")
    # 主动抛出异常
    raise error_info

try:
    print input_pwd()
except Exception as errorInfo:
    print errorInfo
