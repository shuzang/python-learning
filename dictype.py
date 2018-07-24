"""
@title:dictype
@author:shuzang
@date:2018-7-24 8:47:18
@brief:字典类型及操作
"""
"""
字典类型定义：
    - 键值对集合，键值对间无序
    - 采用{}和dict()创建
"""
d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
print(d)
print(d["中国"])
# 使用type可以返回变量类型
print(type(d))
"""
操作函数和方法
"""
# 删除键对应的值
del d["中国"]
print(d)
# 判断键是否在字典中
print("美国" in d)
# 返回字典中所有键信息，值信息，键值对信息
print(d.keys())
print(d.values())
print(d.items())
# 判断存在并返回或取出响应值，不在返回默认值
print(d.get("美国", '纽约'))
print(d.pop('中国', '上海'))
# 随机取出一个键值对，以元组形式返回
print(d.popitem())
# 返回元素个数
print(len(d))
# 删除所有键值对
d.clear()
print(d)
