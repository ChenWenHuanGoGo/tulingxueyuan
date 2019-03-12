'''
百度首页搜索时，https://www.baidu.com/s?wd=想搜索的内容
但是在请求时，直接输入内容会出错，需要对内容编码后再进行搜索
如 https://www.baidu.com/s?wd=大熊猫  这样请求时会出错
需要编码为 https://www.baidu.com/s?wd=%E5%A4%A7%E7%86%8A%E5%90%97
'''
from urllib import request,parse
url = "https://www.baidu.com/s?"
wd = input("请输入你想查找的内容：")
data = {"wd":wd}
data = parse.urlencode(data)
#  print(data)
#  print(type(data))  parse返回字符串格式
#  结果为 wd=%E5%A4%A7%E7%86%8A%E7%8C%AB
full_url = url + data
print(full_url)
# www.baidu.com/s?wd=%E5%A4%A7%E7%86%8A%E5%90%97
response = request.urlopen(full_url)
html = response.read().decode()
print(html)