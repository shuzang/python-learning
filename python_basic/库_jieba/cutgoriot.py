"""
@title:cuthamlet.py
@author:shuzang
@date:2018-7-24 10:29:45
@brief:对中文文本高老头进行分词
"""
import jieba

txt = open("F:\python_basic\库_jieba\高老头.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
