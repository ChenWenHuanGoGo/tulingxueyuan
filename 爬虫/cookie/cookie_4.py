# 使用filecookiejar保存cookie

from urllib import request,parse
from http import cookiejar

# 创建filecookiejar的实例
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)

# handler 是Handler的实例,用来处理复杂请求

# 创建cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建HTTPS管理器
https_handler = request.HTTPSHandler()
# 常见`创建handler之后,使用opener打开,打开后相应的业务由相应的handler来处理
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

    # ignore_discard=True表示即使cookie将要被丢弃也要保存下来
    # ignore_expires=True表示如果文件中的cookie已经过期,也要保存下来
    # 保存cookie到文件
    cookie.save(ignore_discard=True,ignore_expires=True)


if __name__ == '__main__':
    login()

