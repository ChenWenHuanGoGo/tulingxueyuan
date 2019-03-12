from urllib import request,parse
import json
url = "https://fanyi.baidu.com/sug"
wd = input("请输入翻译内容：")
data = {"kw":wd}
# urlencode  返回的是字符串格式，而提交的data需要bytes格式，所以要进行编码
data = parse.urlencode(data).encode('utf-8')
# 请求头必须是地点格式
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'

req = request.Request(url,data,headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
# 返回内容为json格式，将json字符串转化为字典
target = json.loads(html)
#print(target)
print('翻译结果为：')
for i in target['data']:
    print(i['k'] + "---" + i['v'])