## 1 表示类型
### raw string
原生字符串类型，表示为r'text'，不包含对转义符再次转义的字符串
### string
字符串类型，要用'\'转义，很繁琐

<br>
## 2 Re库主要功能函数
### 2.1 re.search(pattern,string,flags=0)
#### 作用
在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
#### 参数
- pattern:正则表达式的字符串或原生字符串表示
- string:待匹配字符串
- flags:正则表达式使用时的控制标记
 常用标记|说明
 -------|----
 re.I re.IGNORECASE |忽略正则表达式的大小写，[A‐Z]能够匹配小写字符
 re.M re.MULTILINE |正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
 re.S re.DOTALL |正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
#### 实例
```Python
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

结果：10081
```
### 2.2 re.match(pattern,string,flags=0)
#### 作用
从一个字符串的开始位置起匹配正则表达式，返回match对象
#### 参数
同search
#### 实例
```Python
match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))
结果：'10081'
```
### 2.3 re.findall(pattern, string, flags=0)
#### 作用
搜索字符串，以列表类型返回全部能匹配的字串
#### 参数
同search
#### 实例
```Python
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

结果：['10081', '100084']
```

### 2.4 re.split(pattern, string, maxsplit=0, flags=0)
#### 作用
将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
#### 参数
- pattern,string,flasg同re.search
- maxsplit:最大分割数，剩余部分作为最后一个元素输出
#### 实例
```Python
print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084'))
结果：['BIT', ' TSU', '']

print(re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1))
结果：['BIT', 'TSU100084']
```

### 2.5 re.finditer(pattern, string, flags=0)
#### 作用
搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
#### 参数
与re.search相同
#### 实例
```Python
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))
结果：   
    10081
    10084
```
### 2.6 re.sub(pattern,repl,string,count=0,flags=0)
#### 作用
在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字串
#### 参数
- pattern,string,flags与re.search相同
- repl:替换匹配字符串的字符串
- count:匹配的最大替换次数
#### 实例
```Python
print(re.sub(r'[1-9]\d{5}', ':zipcode','BIT100081 TSU100084'))
结果：'BIT:zipcode TSU:zipcode'
```
<br>
## 3 用法
### 函数式
使用.调用,一次性，如re.search
### 面向对象
编译后多次操作
```Python
pat = re.compile(r'[1-9]\d{5}')
rst = rat.search('BIT 100081')
```
> 编译后也可以使用所有6个功能函数

<br>
## 4 match对象
### 属性
属性|说明
---|----
.string |待匹配的文本
.re |匹配时使用的patter对象（正则表达式）
.pos |正则表达式搜索文本的开始位置
.endpos |正则表达式搜索文本的结束位置
### 方法
方法|说明
---|----
.group(0) |获得匹配后的字符串
.start() |匹配字符串在原始字符串的开始位置
.end() |匹配字符串在原始字符串的结束位置
.span() |返回(.start(), .end())
<br>
## 5 贪婪匹配和最小匹配
```Python
match = re.search(r'PY.*N', 'PYANBNCNDN')
match.group(0)
```
### 贪婪匹配
如上例，结果中包含长短不同的多个结果，默认采用贪婪匹配，即输出匹配最长的字串

### 最小匹配
想输出最短字串应作如下改动
```Python
match = re.search(r'PY.*?N', 'PYANBNCNDN')
match.group(0)
```
最小匹配操作符
操作符|说明
-----|-----
*? |前一个字符0次或无限次扩展，最小匹配
+? |前一个字符1次或无限次扩展，最小匹配
?? |前一个字符0次或1次扩展，最小匹配
{m,n}? |扩展前一个字符m至n次（含n），最小匹配

