#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_18_sumNumsPlus.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-10 23:02:45
# Last Modified: 2018-09-10 23:03:40
################################################################# 

def sum_numbers(*args): 
    num = 0                                                         
    #print type(args[0])                                            
    for n in args:                                                  
        num += n                                                    
    return num                                                      
                                                                    
tuple_num = input("您想求几个整数的和：")                           
num_list = []                                                       
for x in range(tuple_num):                                          
    num_list.append(int(raw_input("请输入第 %d 个整数：" % (x+1)))) 
num_tuple = tuple(num_list)                                         
print num_tuple                                                     
#print type(num_tuple[0])                                           
r = sum_numbers(*num_tuple)                                         
print "求和结果为：sum = %d" % r                                    
