"""
@title:n次方.py
@author:shuzang
@date:2018-8-7 8:54
@brief:计算输入数字N的0次方到5次方结果，并依次输出这6个结果，
       输出结果间用空格分隔。其中：N是一个整数或浮点数
"""

num = input()
a = 0
while a <= 5:
    print((pow(eval(num), a)), end=' ')
    a = a + 1
