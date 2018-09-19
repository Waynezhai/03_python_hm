#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_08_strMethod.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-09-19 08:36:17
# Last Modified: 2018-09-19 08:43:10
################################################################# 

class Cat:                                  
    def __init__(self, name):               
        self.name = name                    
        print "%s is coming !" % self.name  
    
    def __del__(self):                      
        print "%s will go !" %self.name
    
    def __str__(self):
        return "I am a cute cat %s ^_^ !" % self.name
                                            
                                            
tom = Cat("Tom")
print tom
