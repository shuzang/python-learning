"""
@title:整数加减和
@author:shuzang
@date:2018-8-13 10:38
@brief:
编写程序计算如下数列的值：
1-2+3-4...966
其中，所有数字为整数，从1开始递增，奇数为正，偶数为负
"""

sum = 0
for i in range(1, 967):
    if i % 2 == 1:
        sum += i
    else:
        sum -= i
print(sum)
