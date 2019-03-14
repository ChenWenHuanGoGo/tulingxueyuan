
cookie & session
- 由于http协议的无记忆性，人们为了弥补这个缺憾，所以采用的补充协议
- cookie 是发送给用户（即http浏览器）的一段信息，session是保持在服务器上的对应的另一半信息，用来记录用户信息

cookie & session的区别
- 存放位置不同
- cookie 不安全
- session会保存在服务器一定时间，会过期
- 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个

使用cookie进行登录
- 在一些需要登录的网站，不添加cookie进行访问时，会自动跳转到登录界面
- 在添加cookie后，则可直接进入登录页面  
    - 手动在headers中添加cookie，案例  cookie_1
    - http 模块包含一些关于cookie的模块，通过这些可以自动使用cookie
        - cookieJar
            - 管理存储cookie，向传出的http请求添加cookie
            - cookie存储在内存中，cookieJar实例回收后cookie将消失
        - FileCookieJar(filename,delayload=None,policy=None):
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename,delayload=None,policy=None):
            - 创建与mocilla浏览器cookie.txt兼容的FIleCookJar实例
        - LwpCookieJar(filename,delayload=None,policy=None):
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        关系：cookieJar-->FileCookieJar-->MozillaCookieJar-->LwpCookieJar
    - 利用cookieJar来访问博客园  案例 cookie_2
        - 自动使用cookie登录,大致流程是:
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
        
    - 打印cookie    案例cookie_3
    - 保存cookie文件   案例cookie_4
    - 调用保存的cookie文件  案例cookie_5