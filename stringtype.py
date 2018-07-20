"""
title:stringtype.py
author:shuzang
date:2018-7-19 17:54:07
brief:字符串类型及操作，主要包括
    - 字符串类型的表示
    - 字符串操作符
    - 字符串处理函数
    - 字符串处理方法
    - 字符串类型的格式化
"""
# -*- coding: utf-8 -*-

"""
字符串类型的表示
"""
# 使用一对单引号或双引号表示
print("学生", '学生')
# 可以使用下标进行索引和切片
stri = "我是一个学生"
print(stri[1])
print(stri[2:6])
print(stri[::2])
# 三单引号或三双引号表示多行字符串
print('''我是
             一个''')
print("""学
            生""")

"""
字符串操作符
"""
print("我是"+"一个学生")
print(5*"学生")
print("阳"*3)
print("我是" in "我是一个学生")

# 获取星期字符串
weekstr = "一二三四五六日"
weekId = eval(input("请输入星期数字（1-7）:"))
print("星期"+weekstr[weekId-1])

"""
字符串处理函数
"""
print(len("我是一个学生"))
# 此处str函数曾出现了"TypeError: 'str' object is not callable"错误
# 是因为之前的代码中已定义过str，所以此处str方法变为不可调用
print(str(3.14))
print(hex(324), oct(324))
# Unicode编码和对应字符互相转换
print(ord("s"))
print(chr(115))
# 十二星座字符输出
for i in range(12):
    print(chr(9800+i), end=" ")
print("\n")

"""
字符串处理方法
"""
# 返回字符串的副本，全部字符大写/小写
print("ShuZang".lower())
print("ShuZang".upper())
# 返回一个列表，根据函数参数分割字符串
print("S,h,u,z,a,n,g".split(","))
# 返回字串在字符串中出现的次数
print("I am a student".count("a"))
# 返回字符串副本，所有旧字串被替换为新的
print("我是一个学生".replace("学生", "咸鱼"))
# 字符串根据宽度居中，第一个参数为宽度，第二个参数是填充字符
print("学生".center(10, "="))
# 在字符串头尾两端去掉参数中的字符
print("天连水尾水连天".strip("天连"))
# 将字符串加到参数变量除最后一个元素外的每个元素后
print(",".join("我是一个学生"))

"""
字符串类型的格式化
"""
# 使用format函数进行格式控制
# 冒号为引导符，其后第一个字符填充;第二个字符为对其方式,<为左对齐,>为右对齐,^为居中；第三个字符为输出宽度
print("{:=^20}".format("shuzang"))
# ","为数字的千位分隔符，".精度"是浮点数小说精度或字符串最大输出长度，最后一位为数据类型
print("{:,.2f}".format(12345.6789))
