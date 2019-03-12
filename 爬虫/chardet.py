import urllib.request
import chardet
# 自动检测网页编码
url = "https://tieba.baidu.com/p/3899060428?"
res = urllib.request.urlopen(url)
html = res.read()

# 返回一个字典
cs = chardet.detect(html)
print(type(cs))
print(cs)

#  chardet可能会出错，所以不推荐这种方式
#  html = html.decode(cs["encoding"])

# 用get函数保证不会出错，若没有检测到“encoding”，就使用后面默认的解码方式“gbk”
html = html.decode(cs.get("encoding","gbk"))
print(html)
