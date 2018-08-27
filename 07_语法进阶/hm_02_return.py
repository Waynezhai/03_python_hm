#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: hm_02_return.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-24 18:01:23
# Last Modified: 2018-07-24 18:26:10
################################################################# 

def test(num):
    print "在函数 test 内部，%d 对应的内存地址是：%d" % (num, id(num))
    # 定义一个字符串变量
    result = "hello"
    print "函数要返回数据的内存地址是：%d" % id(result)
    # 将字符串返回，返回的是数据的地址，而不是数据本身
    return result

# 定义一个数字的变量
a = 10
# 数据的地址本质上就是一个数字
print "a变量保存数据的内存地址是：%d" % id(a)

# 调用 test 函数，本质上是传递实参保存的数据的引用，而不是实参保存的数值
# 注意：如果函数有返回值，但是没有定义变量接收，程序不会报错，但是无法获得返回结果
r = test(a)

print "%s 的内存地址是：%d" % (r, id(r))
