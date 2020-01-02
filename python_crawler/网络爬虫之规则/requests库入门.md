- [ ] Requests库：自动爬取HTML页面，自动网络请求提交
> The Website is the API...

<br>
## 1 HTTP协议
### 1.1 基础知识
Hypertext Transfer Protocol,超文本传输协议  
“请求与响应”模式，无状态，应用层协议  
采用URL作为定位网络资源的标识  
### 1.2 HTTP协议对资源的操作
方法|说明
---|---
GET|请求获取URL位置的资源
HEAD|请求获取URL位置资源的相应消息报告，即获得该资源的头部信息
POST|请求向URL位置的资源后附加新的数据
PUT|请求向URL位置存储一个资源，覆盖原URL位置的资源
PATCH|请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE|请求删除URL位置存储的资源

<br>
## 2 Requests库的七个主要方法
### 2.1 requests.request(method, url, **kwargs)
#### 2.1.1 方法说明
构造一个请求，支撑其它各方法的基础方法
#### 2.1.2 参数说明
- method:请求方式，对应get/put/post等7种
- url:拟获取页面的url链接
- **kwargs:控制访问的参数，共13个
#### 2.1.3 method参数
是请求方式，共七种，列举如下
- r = requests.request('GET', url, **kwargs)
- r = requests.request('HEAD', url, **kwargs)
- r = requests.request('POST', url, **kwargs)
- r = requests.request('PUT', url, **kwargs)
- r = requests.request('PATCH', url, **kwargs)
- r = requests.request('delete', url, **kwargs)
- r = requests.request('OPTIONS', url, **kwargs)
#### 2.1.4 **kwargs参数
控制访问的参数，均为可选项，一共13个
- params：字典或字节序列，作为参数增加到url中
 ```Python
 kv = {'key1': 'value1', 'key2': 'value2'}
 r = requests.request('GET', 'http://python123.io/ws',params=kv)
 print(r.url)
 
 运行结果：http://python123.io/ws?key1=value1&key2=value2
 ```
- data：字典、字节序列或文件对象，作为Request的内容
 ```Python
 kv = {'key1': 'value1', 'key2': 'value2'}
 r = requests.request('POST', 'http://python123.io/ws', data=kv)
 body = '主体内容'
 r = requests.request('POST', 'http://python123.io/ws', data=body)
 ```
- json：JSON格式的数据，作为Requests的内容
 ```Python
 kv = {'key1': 'value1'}
 r = requests.request('POST', 'http://python123.io/ws', json=kv)
 ```
- headers：字典，HTTP定制头
 ```Python
 hd = {'user‐agent': 'Chrome/10'}
 r = requests.request('POST', 'http://python123.io/ws', headers=hd)
 ```
- cookies：字典或CookieJar，Request中的cookie
- auth：元祖，支持HTTP认证功能
- files：字典类型，传输文件
 ```Python
 fs = {'file': open('data.xls', 'rb')}
 r = requests.request('POST', 'http://python123.io/ws', files=fs)
 ```
- timeout：设定超时时间，秒为单位
 ```Python
 r = requests.request('GET', 'http://www.baidu.com', timeout=10)
 ```
- proxies：字典类型，设定访问代理服务器，可以增加登录认证
 ```Python
 pxs = { 'http': 'http://user:pass@10.10.10.1:1234'
'https': 'https://10.10.10.1:4321' }
 r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)
 ```
- allow_redirects：True/False，默认为True，重定向开关
- stream：True/False，默认为True，获取内容立即下载开关
- verify：True/False，默认为True，认证SSL证书开关
- cert：本地SSL证书路径

### 2.2 requests.get(url, params=None, **kwargs)
#### 2.2.1 方法说明
获取HTML网页的主要方法，对应于HTTP的GET
#### 2.2.2 参数说明
- url : 拟获取页面的url链接
- params : url中的额外参数，字典或字节流格式，可选
- **kwargs: 12个控制访问的参数

### 2.3 requests.head(url, **kwargs)
#### 2.3.1 方法说明
获取HTML网页头信息的方法，对应于HTTP的HEAD
#### 2.3.2 参数说明
- url : 拟获取页面的url链接
- **kwargs: 12个控制访问的参数

### 2.4 requests.post(url, data=None, json=None, **kwargs)
#### 2.4.1 方法说明
向HTML网页提交POST请求的方法，对应与HTTP的POST
#### 2.4.2 参数说明
- url : 拟更新页面的url链接
- data : 字典、字节序列或文件，Request的内容
- json : JSON格式的数据，Request的内容
- **kwargs: 12个控制访问的参数

### 2.5 requests.put(url, data=None, **kwargs)
#### 2.5.1 方法说明
向HTML网页提交PUT请求的方法，对应于HTTP的PUT
#### 2.5.2 参数说明
- url : 拟更新页面的url链接
- data : 字典、字节序列或文件，Request的内容
- **kwargs: 12个控制访问的参数

### 2.6 requests.patch(url, data=None, **kwargs)
#### 2.6.1 方法说明
向HTML页面提交局部修改请求，对应于HTTP的PATCH
#### 2.6.2 参数说明
- url : 拟更新页面的url链接
- data : 字典、字节序列或文件，Request的内容
- **kwargs: 12个控制访问的参数

### 2.7 requests.delete(url, **kwargs)
#### 2.7.1 方法说明
向HTML页面提交删除请求，对应于HTTP的DELETE
#### 2.7.2 参数说明
- url : 拟获取页面的url链接
- **kwargs: 12个控制访问的参数

<br>
## 3 Requests库的2两个重要对象
### 3.1 综述
r = requests.get(url)
- r:返回一个包含爬虫返回的服务器资源的Response对象
- requests.get(url):构造一个向服务器请求资源的Request对象
### 3.2 Response对象
#### 3.2.1 实例
```Python
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(type(r))
print(r.headers)

运行结果：
200
<class 'requests.module.Response'>
{'Cache-Control':'private, no-cache, no-store, proxy-revalidate, ection':'Keep-Alive','Transfer-Encoding':'chunked','Server':
```

> Response对象包含服务器返回的所有信息，也包含请求的Request信息

#### 3.2.2 Response对象的属性
属性|说明
---|---
r.status_code | HTTP请求的返回状态，200表示连接成功，404表示失败
r.text | HTTP响应内容的字符串形式，即，url对应的页面内容
r.encoding | 从HTTP header中猜测的响应内容编码方式
r.apparent_encoding | 从内容中分析出的响应内容编码方式（备选编码方式）
r.content | HTTP响应内容的二进制形式

### 3.3 Request对象
调用request可能会出现各种异常，我们也需要对异常进行处理
异常 | 说明
----|-----
requests.ConnectionError | 网络连接错误异常，如DNS查询失败、拒绝连接等
requests.HTTPError | HTTP错误异常
requests.URLRequired | URL缺失异常
requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常
requests.ConnectTimeout | 连接远程服务器超时异常
requests.Timeout | 请求URL超时，产生超时异常

最常用到的是r.raise_for_status()，它在方法内部判断r.status_code是否等于200，如果不是，产生异常request.HTTPError,不需要增加额外的if语句，该语句便于利用try‐except进行异常处理
