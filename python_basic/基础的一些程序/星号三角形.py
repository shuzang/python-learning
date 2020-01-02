"""
@title:星号三角形.py
@author:shuzang
@date:2018-8-10 9:01
@brief:
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：
第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
"""

N = eval(input("请输入一个奇数："))
i = 1
while i <= N:
    print("{:^{}}".format(i * '*', N))
    i = i + 2
