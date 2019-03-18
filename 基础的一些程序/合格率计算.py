"""
@title:合格率计算.py
@author:shuzang
@date:2018-8-13 10:56
@brief:
输入一个数字n作为合格标准，然后，输入一系列的数字，每次输入换行表示，空换行结束，输出合格率。
合格率指输入元素中合格元素与全部元素的比值。
"""

n1 = 0
n2 = 0
n = eval(input("请输入合格标准："))
num = input()
while num != '':
    n1 = n1 + 1
    if eval(num) >= n:
        n2 = n2 + 1
        num = input()
    else:
        num = input()
if n1 == 0:
    rate = 100.00
else:
    rate = (n2*100)/n1
print("合格率为{:.2f}%".format(rate))
