"""
@title:四叶玫瑰数.py
@author:shuzang
@date:2018-8-13 11:17
@brief:
四叶玫瑰数是4位数的自幂数。自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身。
(例如：当n为3时，有1^3 + 5^3 + 3^3 = 153，153即是n为3时的一个自幂数，3位数的自幂数被称为水仙花数)
"""

for num in range(1000, 10000):
    a = num // 1000
    b = (num % 1000) // 100
    c = (num % 100) // 10
    d = num % 10
    m = pow(a, 4) + pow(b, 4) + pow(c, 4) + pow(d, 4)
    if m == num:
        print(num)
