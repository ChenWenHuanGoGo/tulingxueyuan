from urllib import  request
'''
SSL证书就是指遵守SSL安全套阶层协议的服务器数字整数
CA是数字证书认证中心,发放,管理数字证书的收信人的第三方机构
'''

'''
访问非认证(不信任的SSL证书)的网站时,报错,此时需要使用ssl模块
url = 'https://www.12306.cn/mormhweb/'
response = request.urlopen(url)
html = response.read().decode()
print(html)
'''
# 导入ssl模块
import ssl
# 利用非认证的上下文环境来替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context()
url = 'https://www.12306.cn/mormhweb/'
response = request.urlopen(url)
html = response.read().decode()
print(html)