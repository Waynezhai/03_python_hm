#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_importOrder.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-24 06:58:38
# Last Modified: 2019-04-24 08:00:47
################################################################# 

"""
搜索当前目录指定模块名的文件，如果有就直接导入
如果没有，再搜索系统目录
在开发时，给文件起名时，不要和系统的模块文件重名
如果在当前目录下touch 一个 random.py文件，程序就不能正常运行了
"""
import random

print random.__file__

rand = random.randint(0, 10)
print rand
