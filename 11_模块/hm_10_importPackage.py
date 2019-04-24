#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_10_importPackage.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-25 06:44:13
# Last Modified: 2019-04-25 07:03:11
################################################################# 

import hm_message

hm_message.send_message.send("This is a piece of message !")
txt = hm_message.receive_message.receive()
print txt
