#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_21_forCircle.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-06 22:29:40
# Last Modified: 2018-07-06 22:35:40
################################################################# 


for num in [1, 2, 3]:
    print num
    if num == 2:
        break
else:
    #如果for循环中使用到了break退出循环，就不会执行else中的代码
    print "会执行吗？"
    
print "循环结束"
