# cookie自动登录

from urllib import request,parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 创建cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建HTTPS管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登录,需要输入用户名和密码
    '''
    # 此url需要从登录from的action属性中提取
    url = 'http://www.renren.com/Plogin.do'
    # 此键值需要从登录from的两个对应input中提取name属性
    data = {
        'email':'13370704651',
        'password':'123456789'
    }
    # 把数据进行编码
    data = parse.urlencode(data).encode()
    # 创建一个请求对象
    req = request.Request(url,data=data)
    # 使用opener发送请求,得到cookie
    rsp = opener.open(req)

def getHomePage():
    # 登录后的网址
    url = 'http://www.renren.com/965187997/profile'
    # 如果已经执行了login函数,则opener自动已经包含相应的cookie信息
    response = opener.open(url)
    html = response.read().decode()
    with open('res.html', 'w') as f:
        # 保存的html文件  可直接打开进入网页
        f.write(html)
if __name__ == '__main__':
    login()
    getHomePage()
