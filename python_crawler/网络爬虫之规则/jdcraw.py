"""
@title:jdcraw.py
@author:shuzang
@date:2018-7-31 8:55
@brief:京东某个商品页面的爬取
"""

import requests

url = "https://item.jd.com/11909265.html"
try:
    r = requests.get(url, timeout=300)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:1000])  # 爬取页面内容较多时，使用序列只取一部分
except requests.HTTPError:
    print("爬取失败")
