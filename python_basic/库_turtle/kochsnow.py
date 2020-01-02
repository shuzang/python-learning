"""
@title:kochsnow.py
@author:shuzang
@date:2018-7-23 10:35:11
@brief:科赫雪花绘制并使用pyinstaller打包
"""

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3  # 3阶科赫雪花，阶数
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()


main()

"""
使用pyinstaller打包时，默认会弹出命令框界面，调试时可以从这里看到bug提示，
若想不出现命令框，可加入-w参数，
"""
