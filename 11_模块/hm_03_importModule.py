#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_03_importModule.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-24 05:59:58
# Last Modified: 2019-04-24 06:11:33
################################################################# 

import hm_01_testModule01
import hm_02_testModule02

hm_01_testModule01.say_hello()
hm_02_testModule02.say_hello()

dog = hm_01_testModule01.Dog()
cat = hm_02_testModule02.Cat()

print dog
print cat

