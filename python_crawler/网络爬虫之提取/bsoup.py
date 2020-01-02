"""
@title:bsoup.py
@author:shuzang
@date:2018-8-2 9:30
@brief:关于bs4库使用的一些练习
"""

from bs4 import BeautifulSoup

"""
调用tag可以使用.<tag>，继续调用tag的属性或内容需要bs4库的函数
"""
soup = BeautifulSoup(open("F:\\github\\python_crawler\\网络爬虫之提取\\test.html"), "html.parser")
print(soup, '\n')
# tag标签
print(soup.h1)
tag = soup.a
print(tag, '\n')
# tag的name
print(soup.a.name, soup.a.parent.name, soup.a.parent.parent.name, '\n')
# tag的attrs
print(tag.attrs, '\n', tag.attrs['href'], tag.attrs['class'], tag.attrs['id'])
print(type(tag.attrs), type(tag))
# tag的NavigableString
print(tag.string, soup.p.string)
print('\n', type(soup.p.string), '\n')
# tag的comment
print(soup.b.string, '\t', type(soup.b.string), '\n')


"""
三种遍历
"""
# 下行遍历
print(soup.head, '\n', soup.head.contents, '\n', soup.body.contents, '\n')
print(len(soup.body.contents), soup.body.contents[1])

for child in soup.body.children:
    print(child, '\t')  # 遍历儿子节点
for child in soup.body.descendants:
    print(child, '\t')  # 遍历子孙节点

# 上行遍历
print(soup.h1.parent, '\n', soup.html.parent, '\n')
print(soup.parent, '\n')

for parent in soup.a.parents:
    if parent is None:
        print(parent, '\t')
    else:
        print(parent.name, '\t')

# 平行遍历
print(soup.p.next.sibling, '\t', soup.p.next_sibling.next_sibling, '\n')
print(soup.a.previous_sibling, '\t', soup.a.previous_sibling.previous_sibling, '\n')

for sibling in soup.p.next_sibling:
    print(sibling)  # 遍历后续节点
for sibling in soup.a.previous_sibling:
    print(sibling)  # 遍历前续节点

"""
格式化输出
"""
print(soup.prettify())
