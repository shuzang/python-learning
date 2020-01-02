"""
@title:Pical.py
@author:shuzang
@date:
@brief:圆周率的计算
"""
from random import random
from time import perf_counter

# 科学公式计算
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16, k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率值为{}".format(pi))
# 当上一行代码终止时有多余空格出现警告 W291:trailing whitespace
# 括号不匹配的异常是 E902:TokenError: EOF in multi-line statement

# 蒙特卡罗方法（撒点用概率算法）
darts = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, darts+1):
    x, y = random(), random()
    dist = pow(x**2+y**2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4*(hits/darts)
print("圆周率值为{}".format(pi))
print("运行时间是{:.5f}s".format(perf_counter()-start))
