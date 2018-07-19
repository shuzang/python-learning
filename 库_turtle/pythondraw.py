"""
title:pythondraw.py
author:shuzang
date:2018-7-19 8:02:45
brief:使用turtle库提供的相关函数绘制一条蟒蛇
"""

import turtle

# 设定画布宽650个像素，高350个像素，默认位于屏幕正中
turtle.setup(650, 350)
# 提起画笔
turtle.penup()
# 反向前进250个像素
turtle.fd(-250)
# 落下画笔
turtle.pendown()
# 设定画笔宽度为20个像素
turtle.pensize(20)
# 设定画笔颜色为绿色
turtle.pencolor("green")
# 画笔朝向以直角坐标系转到-40度方向
turtle.seth(-40)
# 连续绘制四节身体，半径为正沿逆时针绘制，半径为负沿顺时针绘制
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
# 最后绘制一个四分之一圆使乌龟朝向变正
turtle.circle(40, 40)
# 前进40个像素
turtle.fd(40)
# 以16为半径逆时针画一个180度的圆，也就是一个半圆
turtle.circle(16, 180)
# 前进30个像素
turtle.fd(30)
# 绘制完成后不要马上关闭画布
turtle.done()
