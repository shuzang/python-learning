"""
title:numtype.py
author:shuzang
date:2018-7-19 11:20:20
brief:数值类型及操作，包括
    - 整数类型的无限范围及4种进制表示
    - 浮点数类型的近似无限范围、小尾数及科学计数法
    - +、-、*、/、//、%、**、二元增强赋值操作符
    - abs()、divmod()、pow()、round()、max()、min()
    - int()、float()、complex()
"""

"""
整数
"""
# 乘方计算
print(pow(2, 5))
print(pow(2, pow(2, 5)))

# 四种进制表示方式

"""
浮点数
"""
# 存在不确定尾数，不是bug
print(0.1+0.2)
print(0.1+0.3)

# 不确定尾数用round函数处理，round(x, d)，x为待处理数字，d为要截取的小数位数
print(round(0.1+0.2, 2))

"""
复数(一般用不到)
"""
print(3+2j)

"""
数值运算操作符
"""
# 一元操作符
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)
print(+2)
print(-2)
print(1 % 2)
print(9**2)
print(9**0.5)

# 二元操作符（与C语言相同）

# 类型间进行混合运算的结果为最宽类型，宽度比对为复数>浮点数>整数
print(10+4.0)

"""
数值运算函数
"""
print(abs(-10.01))
print(divmod(10, 3))     # 将余和商一起输出
print(max(1, 9, 5, 4, 3))
print(min(1, 9, 5, 4, 3))

# 强制类型转换
print(int(123.45))
print(float(12))
print(complex(4))
