#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_06_fromImportSameModule.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-04-24 06:33:02
# Last Modified: 2019-04-24 06:45:29
################################################################# 

#from hm_01_testModule01 import say_hello
from hm_02_testModule02 import say_hello
print id(say_hello)

from hm_01_testModule01 import say_hello
print id(say_hello)

from hm_02_testModule02 import say_hello as say_hello_fake

say_hello()
say_hello_fake()

# 先后导入的模块的内存地址并不相同
# 导入模块的代码都写在文件顶部
# 如果需要导入两个名字相同的模块，可以用as关键字

