'''
HTTP for Humans,更加简洁友好
继承了urllib的所有特征
底层使用的是urllib3
开源地址: https://github.com/requests/requests
中文文档:http://docs.python-requests.org/zh_CN/latest/index.html
安装:方法一,直接在pycharm解释器中安装
    方法二,source activate 虚拟环境名称
       进入虚拟环境
       conda install requests

get请求:
    requests.get(url)
    requests.request('get',url)
    可以带有headers和parmas参数
'''

import  requests
url = 'http://www.baidu.com/s?'
#两种请求方式

# 使用get请求
kw = {
    'wd':'重庆大学'
}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
# 使用get时,不需要将'wd'用parse进行编译,直接放入参数中即可
response = requests.get(url, params=kw, headers=headers)
print(response.text)

print('*'*20)

# 使用request请求
response = requests.request('get',url='http://www.baidu.com')
print(response.text)