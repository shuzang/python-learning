"""
@title:amazoncraw.py
@author:shuzang
@date:2018-7-31 9:18
@brief:亚马逊商品页面的爬取
       亚马逊商城页面具有反爬取手段，拒绝User-Agent为python的爬取，我们需要将其改为浏览器的标识
"""

import requests

url = "https://www.amazon.cn/dp/B07F36BLCK/ref=sr_1_1_sspa?s=amazon\
       -global-store&ie=UTF8&qid=1532999791&sr=1-1-spons&psc=1"
hd = {"User-Agent": "Mozilla/5.0"}
"""
以下是会出错的代码
r = requests.get(url)
print(r.status_code)  # 503
r.encoding = r.apparent_encoding
print(r.text[:500])
print(r.headers)
"""
try:
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.headers)
    print(r.text[-1000:])
except requests.HTTPError:
    print("爬取失败")
