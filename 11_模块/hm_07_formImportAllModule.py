#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_07_formImportAllModule.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-24 06:45:50
# Last Modified: 2019-04-24 06:59:31
################################################################# 

"""
这种方式虽然方便，但是不推荐使用，容易导致模块重名覆盖，不好排查问题
"""
from hm_01_testModule01 import *

print title
say_hello()
dog = Dog()
print dog
