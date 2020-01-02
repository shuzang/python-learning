"""
@title:tempconvert.py
@author:shuzang
@date:2018-8-7 9:07
@brief:
温度的刻画有两个不同体系：摄氏度（Celsius）和华氏度（Fabrenheit）。
请编写程序将用户输入华氏度转换为摄氏度，或将输入的摄氏度转换为华氏度。
转换算法如下：（C表示摄氏度、F表示华氏度）
         C = ( F - 32 ) / 1.8
         F = C * 1.8 + 32
要求如下：
(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；
(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指摄氏度87.65度；
(3) 不考虑异常输入的问题，输出保留小数点后两位；
(4) 使用input()获得测试用例输入时，不要增加提示字符串。
"""

temp = input()
if temp[0] == 'C':
    Ftemp = eval(temp[1:])*1.8+32
    print('当前温度为F{:.2f}'.format(Ftemp))
elif temp[0] == 'F':
    Ctemp = (eval(temp[1:])-32)/1.8
    print('当前温度为C{:.2f}'.format(Ctemp))
else:
    print('输入异常')
