#!/usr/bin/python
#coding=utf-8


name_list = ["zhangsan", "lisi", "wangwu"]
print name_list

#1、取值和索引
#索引从0开始，注意索引不要超出范围，否则会报错
print "name_list[1]的值为-----------%s" % name_list[1]
#知道数据的内容，想确定数据在列表中的位置，可以使用index方法。
#需要注意，如果传递的数据不在列表中，程序会报错
print "\"lisi\"的索引值为-----------%d" % name_list.index("lisi")

#2、修改
#列表制定的索引超出范围，程序会报错
name_list[1] = "lishifu"
#name_list[3] = "王小二"
print "修改“lisi”为“lishifu”------------",
print name_list

#3、增加
#三个方法来增加列表内容
#append方法在列表末尾增加内容
name_list.append("maoliu")
#insert方法可以在列表指定位置增加内容
name_list.insert(1,"xiaomeimei")
#extend方法可以在列表末尾追加一个完整列表
temp_list = ["sunwukong","zhuerge","shashidi"]
name_list.extend(temp_list)
print "append(“maoliu”) + insert(“xiaomeimei”) + extend(“ThreeBros”)-------------",
print name_list

#4、删除
#三个方法可以删除列表内容
#remove可以删除指定内容，参数为列表数据
name_list.remove("wangwu")
print "remove(“wangwu”)------------",
print name_list
#pop方法默认弹出最后一个元素，也可以删除指定索引的元素
name_list.pop()
name_list.pop(2)
print "pop + pop(index=2)-----------",
print name_list

#clear方法可以清空整个列表，但这个方法在python2中是没有的，在python3中有该方法
#name_list.clear()
#print "clear-------------",
#print name_list



# print输出中文的方法
#print unicode(name_list[1],encoding="utf-8")
