from urllib import request,error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    # 添加代理
    # 1 设置代理ip
    proxy = {'http':'111.205.46.29:80'}
    # 2 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 3 创建opener
    opener = request.build_opener(proxy_support)
    # 4 安装opener
    request.install_opener(opener)

    try:
        response = request.urlopen(url)
        html = response.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
