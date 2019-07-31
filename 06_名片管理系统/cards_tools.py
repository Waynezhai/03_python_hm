#!/usr/bin/env python
#-*- coding:utf8 -*-
################################################################# 
# FileName: cards_tools.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2018-07-07 12:59:57
# Last Modified: 2018-07-14 23:48:47
################################################################# 

import sys

# 定义一个空列表变量，来存放名片
card_list = []

def show_menu():
    """
    摘要：菜单函数
    功能：显示功能菜单，每个子功能完成后会回显 菜单提示
    参数：无
    返回：无 
    """
    print "*" * 50
    print "欢迎使用【名片管理系统】V1.0.0"
    print ""
    print "1.新增名片"
    print "2.显示全部"
    print "3.搜索名片"
    print ""
    print "0.退出系统"
    print "*" * 50
    

def new_card():
    """
    摘要：对应主程序功能1，即新增名片
    功能：实现新增名片功能，包括“姓名、电话、QQ、邮箱”等四个项目
    参数：无
    返回：无
    """
    print "-" * 100
    print "新增名片"
    # 1、提示用户输入名片的详细信息
    name_str = raw_input("请输入姓名：")
    phone_str = raw_input("请输入电话号码：")
    qq_str = raw_input("请输入QQ号码：")
    email_str = raw_input("请输入邮箱地址：")
    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}
    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    print card_list
    # 4、提示用户添加成功
    print "新增 %s 的名片成功！" %name_str
    print "-" * 100


def show_cards():
    """
    摘要：对应主程序功能2，即显示名片
    功能：实现名片的标准显示，内含格式输出的一些细节问题
    参数：无
    返回：无
    """
    print "-" * 100
    print "显示所有名片"
    # 增加提示，如果名片为空，则给出提示，不输出表头
    if len(card_list) == 0:
        print "当前名片系统为空，请使用功能 1 来增加名片！"
        # 如果不用if...else...，可以直接在这里用return语句，也可达到相同目的
        # 执行return后，该函数的后续语句，则不再执行
    else:
        # 1、打印表头
        for column in ["姓名", "电话", "QQ", "邮箱"]:
            #print column + "\t\t\t",
            column_len = len(column.decode("utf-8").encode("gb2312"))
            column_fix = column + (20 - column_len) * " "
            sys.stdout.write(column_fix)
        print ""
        #print "{:<20s}{:<20s}{:<20s}{:<20s}".format("Name", "Phone", "QQ_No.", "E-mail")
        # 2、打印分割线
        print "=" * 70
        # 3、打印card_dict的值（不打印键）
        # 如果输入中文的话，可以参考表头打印的方法来解决对齐问题
        # 这里为了复习一下print的格式输出，就不再更改了
        for card_dict in card_list:
            print "{:<20s}{:<20s}{:<20s}{:<20s}".format(card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["qq"],
                                                        card_dict["email"])
    print "-" * 100


def search_card():
    """
    摘要：对应主程序功能3，即搜索名片
    功能：实现名片查找功能
    参数：无
    返回：无
    """
    print "-" * 100
    print "搜索名片"
    # 1、提示用户输入要搜索的姓名
    search_str = raw_input("请输入您要查找的姓名：")
    # 2、遍历名片，查询要搜索的姓名，如果没有找到，则给出提示
    for card_dict in card_list:
        if search_str == card_dict["name"]:
            column_print()
            print "{:<20s}{:<20s}{:<20s}{:<20s}".format(card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["qq"],
                                                        card_dict["email"])
            # 这里的break很重要，如果没有，执行完for，else还是要执行的。
            # 增加修改和删除功能
            card_deal(card_dict)
            break
    else:
        print "您要查找的姓名不存在，请确认！"
    print "-" * 100


def column_print():
    """
    摘要：表头打印函数
    功能：实现表头的格式化打印，列占20个位
    参数：无
    返回：无
    """
    for column in ["姓名", "电话", "QQ", "邮箱"]:
        column_len = len(column.decode("utf-8").encode("gb2312"))
        column_fix = column + (20 - column_len) * " "
        sys.stdout.write(column_fix)
    print ""
    print "=" * 70


def card_deal(find_dict):
    """
    摘要：主程序功能3调用，即对查找到的名片进行修改或删除
    功能：实现名片修改或删除，且设置返回上层
    参数：
        find_dict---查找到的名片对应字典
    返回：函数内处理，无返回
    """
    while True:
        action_str = raw_input("请输入您想要的操作（[1]、修改；[2]、删除；[0]、返回上级菜单）：")
        if action_str in ["1", "2", "0"]:
            if action_str == "1":
                #find_dict["name"] = raw_input("修改姓名：")
                #find_dict["phone"] = raw_input("修改电话号码：")
                #find_dict["qq"] = raw_input("修改QQ号码：")
                #find_dict["email"] = raw_input("修改邮箱地址：")
                card_fix(find_dict, "name", "姓名")
                card_fix(find_dict, "phone", "电话")
                card_fix(find_dict, "qq", "QQ")
                card_fix(find_dict, "email", "邮箱")
                print "修改 %s 名片成功"%find_dict["name"]
                break
            if action_str == "2":
                card_list.remove(find_dict)
                print "已删除 %s 的名片"%find_dict["name"]
                break
            if action_str == "0":
                print "返回初始菜单！！！"
                break
        else:
            print "您输入有误，请重新输入："  


def card_fix(find_dict, column, column_title):
    """
    摘要：card_deal函数中用到的名片修改函数
    功能：实现有实际输入即替换修改内容，无实际输入则按回车不修改内容
    参数：
        find_dict---查找到的要修改的字典
        column---要修改的键值对的键
        column_title---输入的提示信息变量
    返回：函数内返回，无实际返回值
    """
    str_fix = raw_input("修改" + column_title +"(不修改则输入回车)：")
    if str_fix == "":
        return
    else:
        find_dict[column] = str_fix
        

