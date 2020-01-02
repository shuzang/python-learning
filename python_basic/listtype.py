"""
@title:listtype.py
@author:shuzang
@date:2018-7-23 17:15:04
@brief:序列类型及操作
"""
"""
序列是一个基类类型，分字符串类型、元组类型、列表类型三种
序列是一维元素向量，元素类型可不同，通过下表访问
序列有一些通用的操作符和函数
"""
# 操作符：in和not in；使用+连接；使用*复制；使用下标索引和切片
# 通用函数:len,min,max,index,count
ls = [1, 2, 3, 2, 1]
print(ls.index(2, 0, 2))

"""
元组类型及操作
    - 一旦创建不能修改，元素间逗号分隔
    - 使用()或tuple()创建
    - 继承序列的所有操作，因为创建后不能修改，没有特殊操作
"""
color = ('red', 'blue', 'black')
print(color)

"""
列表类型及操作
    - 与C数组类似，操作更简单
    - 使用[]或list()创建
    - 继承序列的操作，但有自己的操作
"""
ls = ['cat', 'dog', 'tiger', 1024]
# 删除第i个元素(也可以像切片一样删除固定步长的元素)
del ls[1]
print(ls)
# 更新列表
ls += color
print(ls)
# 重复列表
ls *= 2
print(ls)
# 在列表最后增加元素
ls.append(2)
print(ls)
del ls[::2]
# 生成新列表并复制旧列表所有元素
print(ls.copy())
# 插入删除第i位置的元素
ls.insert(2, 4)
print(ls)
ls.pop(4)
print(ls)
# 将列表出现的第一个指定元素删除
ls.remove('red')
print(ls)
# 将列表ls的元素反转
ls.reverse()
print(ls)

# 如果不希望数据被改变，可以转换为元组类型
print(tuple(ls))
