### 1 使用bs4库的基本代码结构
```Python
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>', 'html.parser')
```

- Beautiful Soup库是解析、遍历、维护“标签树”的功能库
- 要了解HTML(超文本标记语言)的一些基本语法

### 2 解析器
解析器|使用方法|条件
-----|-------|-----
bs4的HTML解析器|BeautifulSoup(mk,'html.parser')|安装bs4库
lxml的HTML解析器|BeautifulSoup(mk,'lxml')|pip install lxml
lxml的XML解析器|BeautifulSoup(mk,'xml')|pip install lxml
html5lib的解析器|BeautifulSoup(mk,'html5lib')|pip install html5lib

### 3 BeautifulSoup类的基本元素
```html
<p class="title"> ... </p>
```
基本元素分析：
基本元素|说明
-------|----
Tag |标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
Name |标签的名字，`<p>…</p>`的名字是'p'，格式：`<tag>.name`
Attributes |标签的属性，字典形式组织，格式：`<tag>.attrs`
NavigableString |标签内非属性字符串，<>…</>中字符串,格式：`<tag>.string`
Comment |标签内字符串的注释部分，一种特殊的Comment类型

### 4 基于bs4库的HTML内容遍历方法
#### 下行遍历
- contents：子节点的列表，将<tag>所有儿子节点存入列表
- children：子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
- descendants：子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

代码：
```Python
for child in soup.body.children:
    print(child)  #遍历儿子节点
```
```Python
for child in soup.body.descendants:
    print(child)  #遍历子孙节点
```
#### 上行遍历
- parent：节点的父亲标签
- parents：节点先辈标签的迭代类型，用于循环遍历先辈节点

代码：
```Python
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
```

#### 平行遍历
- next_sibling:返回按照HTML文本顺序的下一个平行节点标签
- previous_sibling:返回按照HTML文本顺序的上一个平行节点标签
- next_siblings:迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
- previous_siblings:迭代类型，返回按照HTML文本顺序的前续所有平行节点标签

代码：
```Python
for sibling in soup.a.next_sibling:
    print(sibling)  #遍历后续节点
```
```Python
for sibling in soup.a.previous_sibling:
    print(sibling)  # 遍历前续节点
```

### 5 格式输出
> 使用prettify()方法

- .prettify()为HTML文本<>及其内容增加更加'\n'
- .prettify()可用于标签，方法：<tag>.prettify()
- bs4库将任何HTML输入都变成utf‐8编码，Python 3.x默认支持编码是utf‐8,解析无障碍