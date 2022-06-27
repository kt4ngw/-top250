# 拿到页面源代码
# 通过re来提有效信息

import requests
import re
import csv
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<garde>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>', re.S)
f = open("data_top250.csv", mode="w", encoding="utf-8")
for i in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(i) +"&filter="
    resp = requests.get(url, headers=header)
    page_content = resp.text
    result = obj.finditer(page_content)
    csvwrite = csv.writer(f)
    for it in result:
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwrite.writerow(dic.values())
    resp.close()
