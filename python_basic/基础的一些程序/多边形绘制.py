"""
@title:多边形绘制.py
@author:shuzang
@date:2018-8-7 9:45
@brief:使用turtle库进行多边形绘制
"""

import turtle

num = eval(input('请输入要绘制的多边形边数:'))
turtle.setup()
turtle.pensize(5)
turtle.pencolor('red')
turtle.penup()
turtle.goto(-50, -200)
turtle.pendown()
for i in range(num):
    turtle.fd(100)
    turtle.left(360/num)
turtle.done()
