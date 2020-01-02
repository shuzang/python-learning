"""
title:time.py
author:shuzang
date:2018-7-20 10:08:10
brief:关于time库的基本介绍，包括以下内容
    - 时间获取函数
    - 时间格式化函数
    - 程序计时函数
"""

import time

"""
时间获取
"""
# 获取当前时间戳，是计算机内部时间值，一个浮点数
print(time.time())
# 获取当前时间并以易读的字符串方式返回表示
print(time.ctime())
# 获取当前时间并表示为计算机可处理的时间格式
print(time.gmtime())

"""
时间格式化
"""
# 根据模板字符串输出计算机内部时间
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
print(time.strftime("%B-%A-%p"))
# 根据字符串形式的时间值转化为计算机内部时间
timestr = '2018-07-20 July-Friday-AM 10:17:06'
print(time.strptime(timestr, "%Y-%m-%d %B-%A-%p %H:%M:%S"))

"""
程序计时应用
"""
# 使用perf_counter()获取时间并作差值计时，sleep()休眠
start = time.perf_counter()
# 要注意休眠单位为秒
time.sleep(3.14)
end = time.perf_counter()
print("程序运行时间为{:.10f}秒".format(end))

