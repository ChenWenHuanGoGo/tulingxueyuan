# 手动添加cook头，可直接进入登录后的页面

from urllib import request

url = 'https://home.cnblogs.com/'

headers = {
    'cookie':'_ga=GA1.2.1359909192.1550800200; __gads=ID=8409f33d5369243d:T=1550804560:S=ALNI_MZ5ldfwsmjboOGi2N3veXshc9_Eyg; .CNBlogsCookie=3DF077482081E1DE8DF2A4362FF7516C23DD574C2325738893AEB7E2313820E0352FDA941DE837964D659B20EFC400BA20A5A8DA5418D7F3E13BBD274F7E5E41F13FB4D00B8C2D1233132BAD85994369AD8F21AD59C4630D91066823DB263352927D997E; _gid=GA1.2.1042741530.1552396094; _gat=1; .Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76OpcELx0ED1HASvXDg8pIpMZC-dJgcd5kTlbsIetYlnnmfU0gp5qU3xtLRCuiN0XuNvFHL1f6xiLvWKtsFmpYToNbO_-ZSE7prHk0HG2Es2-Gfhv1ShCyKA3wp23uGisGnqg_CbwtmjBlYQ4KTZkKbOPq_PG3s9JNj0IJULoJw0e35UtwWAwRLstKzk2tvvu_O5_DsVmBUJTr-5_BKiA4uibPiaOqZrEhHdGlHQTtji34wfDKkcOOJd-DMrCNZqAdrC06SUSfKluZ19gPy0A27pjXphC1PQEtmfYIYHWHJdLA'
}
req = request.Request(url,headers = headers)
response = request.urlopen(req)
html = response.read().decode()
with open('res.html','w') as f:
    # 保存的html文件  可直接打开进入网页
    f.write(html)