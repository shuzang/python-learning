"""
@title:同符合数学运算.py
@author:shuzang
@date:2018-8-10 8:42
@brief:
读入一个整数N，分别计算如下内容：
1. N的绝对值；
2. N与10进行同符号加法、减法和乘法运算，同符号运算指使用N的绝对值与另一个数进行运算，运算结果的绝对值被赋予N相同的符号，其中，0的符号是正号。
将上述4项结果在一行输出，采用空格分隔，输出结果均为整数。
"""

num = eval(input("请输入一个整数:"))
if num >= 0:
    print(num, abs(num + 10), abs(num - 10), num * 10)
else:
    print(abs(num), -(abs(abs(num) + 10), -(abs(abs(num) - 10), -(abs(num) * 10))
