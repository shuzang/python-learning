"""
@title:genframework.py
@author:shuzang
@date:2018-7-29 18:15
@brief:爬虫的一个通用框架结构
"""

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
