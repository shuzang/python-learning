"""
title:Textprobar.py
author:shuzang
date:2018-7-20 10:29:52
brief:写一个动态变化的文本进度条
"""

import time

# 单行动态刷新
for i in range(100):
    print("\r{}%".format(i+1), end=" ")  # end=" "的意思是末尾不换行，加一个空格
    time.sleep(0.1)
print("\n")

# 完整效果的文本进度条
scale = 347
print("执行开始".center(110, " "))
start = time.perf_counter()
for i in range(scale + 1):
    a = int((i/scale)*100)*'-'
    b = int((1-i/scale)*100)*'*'
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.2f}%[{}>{}]{:.2f}s".format(c, a, b, dur), end=' ')
    time.sleep(0.1)
print("\n"+"执行结束".center(110, ' '))

"""
程序要点：
1. 字符串居中函数、复制函数的使用
2. 利用time库计算时间间隔和休眠
3. 字符串的格式化输出
4. 实现文本进度条的基本思路：使用end=' '控制输出结束不换行，使用\r覆盖上一个输出结果
"""
