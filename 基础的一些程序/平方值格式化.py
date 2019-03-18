"""
@title:平方值格式化.py
@author:shuzang
@date:2018-8-10 8:42
@brief:
   获得用户输入的一个整数N，计算N的平方值；结果采用宽度20字符方式居中输出，空余字符采用减号(-)填充。
如果结果超过20个字符，则以结果宽度为准
"""

num = input("请输入任意一个整数:")
result = eval(num)**2
print('{:-^20}'.format(result))
