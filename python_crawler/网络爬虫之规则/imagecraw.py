"""
@title:imagecraw.py
@author:shuzang
@date:2018-7-31 10:45
@brief:网络图片的下载
"""

import requests
import os

root = "F:/github/python_crawler/网络爬虫之规则/"
url = "https://desk-fd.zol-img.com.cn/t_s1920x1200c5/g5/M00/0F/07/ChMkJlauymeIYMI3AAhS3aKLXp4AAH8tQD5_3oACFL1729.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(path)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except requests.HTTPError:
    print("爬取失败")
