#coding=utf-8

#定义一个字符串变量 name，输出：我的名字叫小明，请多多关照
name = "小明"
print "我的名字叫%s" % (name)

#定义整数变量 student_num,输出：我的学号是000001
student_num = 1
print "我的学号是 %06d" % (student_num)


#定义小数 price、weight、money
#输出：苹果单价8.5元/斤，购买了7.5斤，以及需要支付金额
price = 8.5
weight = 7.5
money = price * weight
print "苹果单价为 %.2f 元/斤，您共购买了 %.2f 斤。需要支付 %.2f 元" % (price,weight,money)


#定义一个小数scale，输出数据比例为25.00%
scale = 0.25
print "所占比例为：{:.2%}" .format(scale)
print "所占比例为：%.2f%%" % (scale * 100)
