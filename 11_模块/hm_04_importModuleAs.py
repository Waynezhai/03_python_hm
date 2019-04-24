#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_04_importModuleAs.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-24 05:59:58
# Last Modified: 2019-04-24 06:21:23
################################################################# 

import hm_01_testModule01 as DogModule
import hm_02_testModule02 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
cat = CatModule.Cat()

print dog
print cat

