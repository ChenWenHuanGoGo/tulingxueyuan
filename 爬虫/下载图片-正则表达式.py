import re
import urllib.request

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def find_img(url):
    html = url_open(url).decode('utf-8')
    # 正则表达式找出图片链接
    p = r'<img class="BDE_Image" src="([^"]*\.jpg)".*?>'
    # findall 返回的是一个列表
    img_addrs = re.findall(p,html)
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
        url = "https://tieba.baidu.com/p/3899060428?"
        img_addrs = find_img(url)
        save(img_addrs)


if __name__ == '__main__':
    download()