#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: cards_main.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-07 12:59:35
# Last Modified: 2018-07-14 23:48:53
################################################################# 

import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = raw_input("请选择希望执行的操作：")
    print "您选择的操作是：%s" %action_str 
    
    # 1/2/3 表示针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str ==  "1":
            cards_tools.new_card()
        # 显示全部名片
        if action_str ==  "2":
            cards_tools.show_cards()
        # 查询名片
        if action_str ==  "3":
            cards_tools.search_card()
    
    # 0表示退出系统
    elif action_str == "0":
        print "-" * 100
        print "欢迎再次使用名片系统！"
        print "-" * 100
        break
        # pass作为一个占位符，在暂时不想编写该块代码时使用，可以保证程序结构的完整性。
        #pass
    
    #其他内容输入错误，需要提示用户
    else:
        print "-" * 100
        print "您的输入有误，请检查后重新输入！"
        print "-" * 100

