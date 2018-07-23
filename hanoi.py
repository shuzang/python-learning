"""
@title:hanoi.py
@author:shuzang
@date:2018-7-23 9:51:47
@brief:汉诺塔问题
"""

count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


hanoi(3, 'A', 'C', 'B')
print("移动总次数为{}".format(count))
