"""
@title:baidukeyword.py
@author:shuzang
@date:2018-7-31 10:28
@brief:百度搜索关键词提交
"""

import requests

url = "http://www.baidu.com/s?"  # 这里/s后面加不加？都可以
kw = {"wd": "apple"}
try:
    r = requests.get(url, params=kw)
    # print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.headers)
    print(len(r.text))
    print(r.url)
    # print(r.text[:500])
except requests.HTTPError:
    print("爬取失败")
