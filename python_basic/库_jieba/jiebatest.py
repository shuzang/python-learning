"""
@title:jiebatest.py
@author:shuzang
@date:2018-7-24 9:10:54
@brief:jieba库的相关函数使用
"""
import jieba

# 精确模式：切分文本，不存在冗余
print(jieba.lcut("中国是一个伟大的国家"))

# 全模式：扫描所有可能的词语，有冗余
print(jieba.lcut("中国是一个伟大的国家", cut_all=True))

# 搜索引擎模式：在精确模式基础上进一步切分长词
print(jieba.lcut_for_search("中国是一个伟大的国家"))

# 向分词词典增加新词
jieba.add_word("书葬")

"""
文件名不能命名为jieba.py，import导入时会冲突，执行出现
AttributeError: module 'jieba' has no attribute 'lcut'错误
"""
