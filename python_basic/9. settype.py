"""
@title:settype.py
@author:shuzang
@date:2018-07-23 16:32:17
@brief:集合类型及相关操作
"""


"""
集合类型的定义：
    - 元素唯一、不可更改，元素间无序。与数学上集合一致
    - 用{}表示，元素间逗号分隔
    - 建立集合用{}或set(),建立空集合必须用set()
"""
A = {"shuzang", 23, ("shuzang", 23)}
print(A)
print(set("shuzang"))


"""
集合间操作：交并差补，与数学上相同
"""
A = set('shuz')  # 这里使用set()和{}的区别是set()生成单个字符，{}是字符串'shuz'
B = set('zang')
# 交
print(A & B)
# 并
print(A | B)
# 差
print(A - B)
# 补
print(A ^ B)

# 关系判断
print(set('shu') <= set('shuzang'))
print(set('shu') >= set('shuzang'))

# 更新集合，只拿交运算举例，其它三种类似
A &= B
print(A)


"""
集合处理方法
"""
A = set('shu')
# 增加元素
A.add('z')
print(A)
# 移除元素(没有该元素时不产生异常)
A.discard('a')
print(A)
# 移除元素(产生异常)
A.remove('z')
print(A)
# 随机返回一个元素
print(A.pop())
print(A)
# 返回集合的一个副本
print(A.copy())
# 返回集合元素个数
print(len(A))
# 判断是否在集合中
print('a' in A)
print('a' not in A)
# 移除集合中所有元素
A.clear()
print(A)


"""
应用场景
"""
# 包含关系比较
print('s' in set('shu'))
print(set('shu') >= set('zang'))
# 数据去重
ls = ['s', 'h', 'u', 'u', 's']
s = set(ls)
print(s)
lt = list(s)
print(lt)
