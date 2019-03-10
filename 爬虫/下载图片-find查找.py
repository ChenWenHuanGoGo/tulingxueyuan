import urllib.request

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def find_img(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('BDE_Image" src="')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        img_addrs.append(html[a+16:b+4])
        a = html.find('BDE_Image" src="',b)
    return img_addrs

def save(img_addrs):
    for each in img_addrs:
        img = url_open(each)
        img_name = each.split('/')[-1]
        # 路径中的文件夹必须是已经存在的
        with open('/home/tlxy/tulingxueyuan/爬虫/1/'+img_name,'wb') as f:
            f.write(img)
        print("已下载图片：",img_name)

def download():
    for i in range(1,6):
        url = "https://tieba.baidu.com/p/3899060428?pn=" + str(i)
        img_addrs = find_img(url)
        save(img_addrs)


if __name__ == '__main__':
    download()