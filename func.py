"""
@title:func.py
@author:shuzang
@date:2018-7-22 8:47:54
@brief:函数相关
"""

"""
可选参数传递
"""
# 函数定义时可以为某些参数指定默认值，构成可选参数


def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m


print(fact(10))
print(fact(10, 5))
# 这里要注意的是函数定义和函数调用语句前都要空两行

"""
局部变量和全局变量：
    - 基本数据类型，无论是否重名，局部变量与全局变量不同
    - 可以通过global保留字在函数内部声明全局变量
    - 组合数据类型，如果局部变量未真实创建，则是全局变量
"""

"""
lambda函数
    - 匿名函数，返回值是函数名
    - 用于定义简单的，能够在一行内表示的函数

f = lambda x, y: x+y
print(f(10, 15))

f = lambda: "lambda函数"
print(f())
上述代码无法执行，错误为 W292:no newline at end of file
"""
