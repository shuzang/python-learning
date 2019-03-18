"""
@title:叠边形绘制.py
@author:shuzang
@date:2018-8-7 11:13
@brief:使用turtle库进行叠边形绘制
"""

import turtle

turtle.pensize(5)
turtle.color('green')
for i in range(9):
    turtle.fd(100)
    turtle.left(80)
turtle.done()
