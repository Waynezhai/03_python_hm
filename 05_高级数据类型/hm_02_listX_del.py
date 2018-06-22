#!/usr/bin/python
#coding=utf-8


name_list = ["zhangsan", "lisi", "wangwu"]
print name_list

#del删除列表内容，del是从内存中删除，使用这个方法，就不能再用这个变量了，不建议用这个方法删除列表内容
del name_list[1]
print "del name_list[1]-----------",
print name_list

