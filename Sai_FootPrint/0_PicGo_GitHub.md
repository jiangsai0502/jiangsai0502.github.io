# PicGo+GitHub 搭建图床

> 讲剪切板上的截图发送到图床，生成在线的图片链接

### 创建GitHub图床
1. 登陆GitHub
2. 创建Repository
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111135509.png)
点击"New repository"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111135617.png)

> 按照1234步骤执行，建立一个名为Figurebed的repository

3.生成一个Token用于操作GitHub repository
回到主页，点击"Settings"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111135856.png)
进入页面后，点击"Developer settings"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111135837.png)
点击"Personal access tokens"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111135915.png)
点击"Generate new token"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111140018.png)
填写描述，选择"repo",然后点击"Generate token"按钮
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111140125.png)
> 注：创建成功后，会生成一串token，这串token之后不会再显示，所以第一次看到的时候，就要好好保存



### 配置PicGo

1. 下载运行PicGo
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111140351.png)

2. 配置图床
![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200111140408.png)
> * 设定仓库名的时候，是按照“账户名/仓库名”的格式填写
>   * 如 jiangsai0502/PicBedRepo
> * 分支名统一填写“master”
> * 将之前的Token黏贴在这里
> * 存储路径可以写成img/，这样会在repository下创建一个“img”文件夹
> * 自定义域名的作用是，在上传图片后成功后，PicGo会将“自定义域名+上传的图片名”生成的访问链接，放到剪切板上https://raw.githubusercontent.com/账户名/仓库名/分支名，自定义域名需要按照这样去填写
>   * 如https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master

3. 快捷键及相关配置
> 可将快捷键设置为cmd+2

#### 总结
将上面的步骤都设置好之后，每次截图之后，都可以按一下cmd+2，这样就会将剪切板上面的截图转化为在线网络图片链接



### 图片左对齐

align='left'

`<img src="https://xxx" align='left' style="zoom:25%;" />`



### GitHub无法连接问题

> **关于GitHub的raw.githubusercontent.com无法链接的问题**
>
> 修改hosts解决掉此问题 [参考](https://www.ioiox.com/archives/62.html)
>
> 1. 进入  [`IPAddress.com`](https://www.ipaddress.com/)  首页,输入  `raw.githubusercontent.com`
>
> 2. 查询到  `raw.githubusercontent.com`  的真实IP地址
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200127165817.png)
>
>    > |              Domain | githubusercontent.com                                       |
>    > | ------------------: | ----------------------------------------------------------- |
>    > |          IP Address | 199.232.28.133                                              |
>    > | Web Server Location | ![img](https://www.ipaddress.com/flags/us.png)United States |
>
> 3. 修改hosts 
>
>    打开hosts
>
>    ```
>    sudo vi /etc/hosts
>    
>    127.0.0.1	localhost
>    255.255.255.255	broadcasthost
>    ::1             localhost
>    ```
>
>    最后插入一行上面查到的 IP Address，内容如下
>
>    ```
>    127.0.0.1	localhost
>    255.255.255.255	broadcasthost
>    ::1             localhost
>    199.232.28.133 raw.githubusercontent.com
>    ```