"""
@title:filerw.py
@author:shuzang
@date:2018-7-26 8:27
@brief:文件的相关操作
"""


"""
文件打开关闭
"""
f = open("test.txt", "rt")
print(f.read())
f.close()
# 读文本文件，是默认模式
print(open("test.txt", "rt").read())
# 写二进制文件
# print(open("test.txt", "rb").read())
# 覆盖写+读
# print(open("test.txt", "w+").read())
# 追加写+读
# print(open("test.txt", "a+").read())
# 创建写+读
# print(open("Mtest.txt", "x+").read())
# 写文本文件+读
# print(open("test.txt", "wt+").read())


"""
写文件
"""
# 写一个字符串或字节流
f = open("test.txt", "a+")
f.write("\n我正在家里学习")
print(f.readlines(2))
# 将一个元素全为字符串的列表写入文件
ls = ["中国", "法国", "美国"]
f.writelines(ls)
print(f.read())
# 改变当前文件操作指针位置,0,1,2分别为文件开头，当前位置，文件结尾
f.seek(0)
print(f.readline())
f.close()

"""
读文件
"""
# 使用read(),readline()，readlines()三个函数
fo = open("test.txt")
# 遍历全文本1：一次读入，统一处理
txt = fo.read()
print(txt)
# 遍历全文本2：按数量读入，逐步处理
fo.seek(0)
txt = fo.read(2)
while txt != "":
    txt = fo.read(2)
# 逐行遍历1：一次读入，分行处理
fo.seek(0)
for line in fo.readlines():
    print(line)
# 逐行遍历2：分行读入，逐行处理
fo.seek(0)
for line in fo:
    print(line)
fo.close()
