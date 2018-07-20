"""
@title:random.py
@author:shuzang
@date:2018-7-20 21:12:27
@brief:random的相关函数练习，常用的主要包括两类共8个函数
    - 基本随机数函数： seed(), random()
    - 扩展随机数函数： randint(), getrandbits(), uniform(),
                      randrange(), choice(), shuffle()
"""

import random as r

"""
基本随机数函数
"""
r.seed()  # seed()不带参数时默认为当前系统时间
print(r.random())  # random函数产生一个[0.0, 1.0]之间的随机小数

r.seed(10)  # seed()是初始化给定的随机数种子，得到的结果是无法输出的
print(r.random())
print(r.random())  # 初始化种子后可多次调用

"""
扩展随机数函数
"""
# 生成一个两个参数范围之间的整数
print(r.randint(10, 100))
# 生成一个前两个参数范围内以第三个参数为步长的随机整数
print(r.randrange(10, 100, 10))
# 生成一个参数比特长的随机整数
print(r.getrandbits(5))
# 生成一个两个参数范围内的随机小数
print(r.uniform(10, 100))
# 从参数代表的序列中随机选择一个元素
print(r.choice(['s', 'h', 'u', 'z', 'a', 'n', 'g']))
# 将参数序列中的元素随机排列，返回打乱后的序列，很有用
str = ['s', 'h', 'u', 'z', 'a', 'n', 'g']
r.shuffle(str)
print(str)

"""
注意：shuffle函数的使用不能直接用print(r.shuffle(str))，输出会是none
      因为函数改变的是原字符串，这样输出的是一个新字符串
"""
