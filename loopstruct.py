"""
title:loopstruct.py
author:shuzang
date:2018-7-20 17:54:25
brief:程序的循环结构，主要包括
    - 遍历循环
    - 无限循环
    - 循环控制保留字
    - 循环的高级用法
"""

"""
遍历循环
"""
# 计数循环（N次）
for i in range(6):
    print(i)
# 计数循环（特定次）
for i in range(1, 6, 2):
    print(i)
# 字符串遍历循环
for c in "shuzang":
    print(c, end=",")
print("\n")
# 列表遍历循环
for item in [123, "shuzang", 456]:
    print(item, end=",")
print("\n")
# 文件遍历循环

"""
无限循环
"""
a = 3
while a > 0:
    a = a-1
    print(a)

"""
循环控制保留字
"""
# 是break和continue的使用，和C一样

"""
循环的高级用法
"""
# 循环与else，这里else与异常处理中的else用法相似
for c in "PYTHON":
    if c == 'T':
        continue
    print(c, end=" ")
else:
    print("正常退出")
