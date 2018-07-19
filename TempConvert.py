"""
title:TempConvert.py
author:shuzang
date:2018-7-18 8:36:55
brief:输入摄氏或华氏温度值，将其转换为另一种温度体系并输出
"""

temp = input("请输入当前的温度值，单位为摄氏度或华氏度，如32C/32F:")
while True:
    if temp[-1] in ['F', 'f']:
        Ctemp = (eval(temp[0:-1])-32)/1.8
        print("当前温度值为摄氏{:.2f}度,华氏{:.2f}度".format(Ctemp, eval(temp[0:-1])))
        break
    elif temp[-1] in ['C', 'c']:
        Ftemp = 1.8*eval(temp[0:-1])+32
        print("当前温度值为摄氏{:.2f}度,华氏{:.2f}度".format(eval(temp[0:-1]), Ftemp))
        break
    else:
        print("输入的温度值格式错误")
        temp = input("请再次输入当前的温度值，单位为摄氏度或华氏度，如32C/32F:")

"""
调试问题总结：
1. 要注意与C语言的不同，分支循环语句后记得加":"，每个语句后不必加";"
2. 区别分支循环结构、数组类型与C语言的不同
3. 格式化输出format函数的使用，字符串转数值类型的eval函数的使用
4. 屡次出现的'elif'关键字invalid syntax错误，其实是由于if语句中小括号未匹配
"""
