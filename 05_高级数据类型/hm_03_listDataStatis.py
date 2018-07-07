#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_03_listDataStatis.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-06-21 00:07:26
# Last Modified: 2018-06-27 23:37:49
################################################################# 

name_list = ["zhangsan","lisi","wangwu","zhangsan"]         
print name_list                                   
                                                  
# len 方法统计列表中的元素总数                    
list_len = len(name_list)                         
print "列表中包含了 %d 个元素" %(list_len)        
                              
# count 方法可以统计列表中某一个数据出现的次数    
zs_count = name_list.count("zhangsan")            
print "“zhangsan”在列表中出现了 %d 次" %(zs_count)

# 从列表中删除数据，remove方法仅删除第一个元素
name_list.remove("zhangsan")
print "删除“zhangsan”---",
print name_list
