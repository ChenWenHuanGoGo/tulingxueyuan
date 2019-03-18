'''
异步请求
一定会有url,请求方法,可能有数据
一般用json格式
'''
# 爬取豆瓣电影

from urllib import request
import json
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=30'
req = request.urlopen(url)
data = req.read().decode()
print(type(data))
data = json.loads(data)
print(data)