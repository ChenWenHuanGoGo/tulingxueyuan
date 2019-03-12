from urllib import request,error
url = "https://www.zhishiwo.com"
try:
    req = request.Request(url)
    html = request.urlopen(req)
    html = html.read().decode()
    print(html)
# HTTPError 必须放在 URLError前面
except error.HTTPError as e:
    print("HTTPError:",e.reason)
except error.URLError as e:
    print("URLError:",e.reason)
except Exception as e:
    print(e)