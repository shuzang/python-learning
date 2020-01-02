"""
@title:taobaoprice.py
@author:shuzang
@date:2018-8-5 8:50
@brief:爬取淘宝商品名及价格
"""

import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        return ""


def parsePage(ilt, html):
    try:
        # \必须加，价格要用[]括起来，不然出错
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except Exception:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    goods = '笔记本电脑'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except Exception:
            continue
    printGoodsList(infoList)
