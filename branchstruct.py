"""
title:branchstruct.py
author:shuzang
date:2018-7-20 17:17:00
brief:程序的分支结构，主要包括
    - 单分支结构
    - 二分支结构
    - 多分支结构
    - 条件判断及组合
    - 程序的异常处理
"""

# 紧凑形式的二分支结构
guess = eval(input("请输入你猜测的分数:"))
print("猜{}了".format("对" if guess == 99 else "错"))

# 程序的异常处理
try:
    num = eval(input("请输入一个数字："))
    print(num**2)
except NameError:
    print("输入的不是数字")
else:
    print("当你看到此句时未发生异常")
finally:
    print("这一句一定会执行")
