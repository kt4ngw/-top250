"""
本文爬取北京新发地 市场商品价格行情， 参考B站爬虫公开网课，仅当练习使用，如侵权删除
"""

import requests
import csv

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

url = "http://www.xinfadi.com.cn/getPriceData.html" # 网站数据来源
resp = requests.post(url, headers=header)
result = resp.json()["list"]
f = open("xinfadi.csv", mode="w",)
csvwrite = csv.writer(f)
csvwrite.writerow(resp.json()["list"][0].keys()) # 写入标签行
resp.close()

for s in range(2, 11, 1): # 此处只爬取10页，如需更多 将11更改
    data = {
        "limit": "20",
        "current": str(s),
        "pubDateStartTime":"",   # 筛选变量；选择开始时间
        "pubDateEndTime":"",   # 筛选变量；选择结束时间
        "prodPcatid":"",   #
        "prodCatid":"",   #
        "prodName":"",   #
    }
    resp = requests.post(url, headers=header, data=data)
    result = resp.json()["list"]

    for i in result:
        csvwrite.writerow(i.values())
        resp.close() # 关门链接