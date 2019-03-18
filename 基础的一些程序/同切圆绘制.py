"""
@title:同切圆绘制.py
@author:shuzang
@date:2018-8-7 11:13
@brief:使用turtle库进行同切圆绘制
"""

import turtle

num = eval(input('请输入要绘制的同切圆层数:'))
turtle.pensize(2)
turtle.pencolor('purple')
turtle.penup()
turtle.goto(-50, -200)
turtle.pendown()
for i in range(num):
    turtle.circle(i*20)
turtle.done()
