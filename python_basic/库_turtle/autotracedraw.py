"""
@title:autotracedraw.py
@author:shuzang
@date:2018-7-26 9:04
@brief:自动轨迹绘制，根据文件中提供的坐标进行轨迹绘制
"""
import turtle

turtle.setup(800, 600)
turtle.pencolor("blue")
turtle.pensize(5)
# 数据读取
xyz = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    xyz.append(list(map(eval, line.split(","))))
f.close()
# 轨迹绘制
for i in range(len(xyz)):
    turtle.pencolor(xyz[i][3], xyz[i][4], xyz[i][5])
    turtle.fd(xyz[i][0])
    if xyz[i][1]:
        turtle.right(xyz[i][2])
    else:
        turtle.left(xyz[i][2])
turtle.done()
