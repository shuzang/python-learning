"""
@title:moneyconvert.py
@author:shuzang
@date:2018-8-7 9:07
@brief:
人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：
人民币和美元间汇率固定为：1美元 = 6.78人民币。
程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。
注意：
(1) 这是一个OJ题目，获得输入请使用input()
"""
money = input('请输入钱币数量(格式举例:USD12或RMB12):')
if money[:3] == 'RMB':
    print('USD{:.2f}'.format(eval(money[3:])/6.78))
elif money[:3] == 'USD':
    print('RMB{:.2f}'.format(eval(money[3:])*6.78))
else:
    print('出错')
