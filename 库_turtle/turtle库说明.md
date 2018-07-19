## 前言
　　turtle库是入门级的图形绘制函数库，同时是Python的标准库之一，官方的文档介绍地址为[tuttle-Turtle graphics](https://docs.python.org/3/library/turtle.html#turtle.done)

　　turtle绘图的原理是想象一只海龟在窗体正中心，在画布上游走，走过的轨迹形成绘制的图形，海龟由程序控制，可以变换颜色、宽度等等，对海龟的控制反映到绘图上就是各种作图控制

## turtle绘图窗体布局
　　画布空间单位为像素，turtle.setup(width, height, startx, starty)是最常使用的画布初始设置函数，如下图所示  
![turtle绘图窗体说明](https://github.com/shuzang/image/blob/master/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E5%AD%A6MOOC_python/turtle%E7%BB%98%E5%9B%BE%E7%AA%97%E4%BD%93%E8%AF%B4%E6%98%8E.jpg?raw=true)

　　其中width和height两个参数为整数时，代表像素；为浮点数时，代表百分比，默认百分比width为50%，height为75%

## turtle空间坐标体系
　　就是我们的直角坐标体系，海龟最开始的位置是零点，使用turtle.goto(x,y)函数可以到达(x,y)坐标处，会留下笔迹，不是飞行。默认情况下x轴正向为前进方向，x轴反向为后退方向，y轴正向为左侧方向，y轴反向为右侧方向常用的三个函数为turtle.circle(radiu,angle),turtle.fd(d),turtle,bk(d)

## turtle角度坐标体系
　　是以角度为单位的直角坐标体系，使用turtle.seth(angle)可以改变海龟行进方向，但不前进，angle为绝对度数，同时还有turtle.left(angle),turtle.right(angle)两个左转向和右转向的函数

## RGB色彩体系
　　除了RGB的基本知识，提供turtle.colormode(mode)切换两种模式，小数模式RGB值为0-1.0，整数模式RGB值为0-255；提供turtle.pencolor()控制画笔颜色，turtle.fillcolor()控制填充颜色，turtle.color可同时完成两种颜色设置

> 以上提到的所有函数和未提到turtle库函数都在官方文档中有详细介绍，使用时仔细查看即可