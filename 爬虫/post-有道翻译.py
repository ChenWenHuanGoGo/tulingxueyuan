import urllib.request
import urllib.parse

def translate():
    t = input("请输入翻译内容：")
    # 出现{"errorCode":50}，将url中的_o去掉
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    date = {}
    date['i'] = t
    # 在network查看网页的请求方式为POST，则在urlopen中需要加入date参数，且date参数需要用urllib.parse.urlencode来进行编码
    date['smartresult'] = 'dict'
    date['client'] = 'fanyideskweb'
    date['salt'] = '15521826306775'
    date['doctype'] = 'json'
    date['version'] = '2.1'
    date['keyfrom'] = 'fanyi.web'
    date = urllib.parse.urlencode(date).encode("utf-8")
    #添加user-agent
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"

    req = urllib.request.Request(url,date,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    '''
    # 返回的html是一个字符串格式,用字符串查找的方法将其分割出来
    a = html.find('tgt')
    b = html.find('"}]]}')
    c = html[a+6:b]
    print("翻译结果为：",c)
    '''
    #html是一种json格式的字符串，解析这个json格式即可
    import json
    #转化为字典格式
    a = json.loads(html)
    b = a['translateResult'][0][0]["tgt"]
    print("翻译结果为：",b)

if __name__ == '__main__':
    translate()