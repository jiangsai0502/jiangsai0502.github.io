# PicGo+GitHub 搭建图床

> 将剪切板上的截图发送到图床，生成在线的图片链接

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



### 创建Gitee图床

[参考](https://zhuanlan.zhihu.com/p/102594554)

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200709230723.png)

* repo：jiangsai0502/PicBedRepo
* token：37ad7df3148561d78e096ce8ce9af044

### 将Gitee与Github保持同步

[参考](https://blog.csdn.net/idsof/article/details/105005158)

> 描述：本地1个代码库，远端2个代码库（Github，Gitee），保持同步
>
> **总结操作**
>
> 1. 进入项目目录：`cd ~/Documents/GitHub/PicBedRepo`
> 2. 先讲远程仓库全部合并到本地
>    1. `git pull GiteePicbed master`
>    2. `git pull GithubPicbed master`
> 3. 本地修改
> 4. 提交到本地仓库
>    1. `git add .`
>    2. `git commit -am "删除测试文件"`
> 5. 再将本地仓库全部推送到远程
>    1. `git push GiteePicbed master`
>    2. `git push GithubPicbed master`

#### 案例（从新建库开始）

1. 新建库

   > | GitHub新建库PicBed                                           | Gitee新建库PicBed                                            |
   > | ------------------------------------------------------------ | ------------------------------------------------------------ |
   > | ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425105755.png) | ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425105827.png) |

2. 创建项目目录：`mkdir ~/Documents/GitHub/PicBed && cd ~/Documents/GitHub/PicBed`

3. 克隆项目到本地

   1. `git clone https://gitee.com/jiangsai0502/PicBed.git`
   2. `git clone https://github.com/jiangsai0502/PicBed.git`

4. 关联`Gitee`和`GitHub`远程库并设置远程库的本地名称

   1. 设置`Gitee`远程库的本地名称为`GiteePicbed`

      `git remote add GiteePicbed https://gitee.com/jiangsai0502/PicBed.git`

   2. 设置`GitHub`远程库的本地名称为`GithubPicbed`

      `git remote add GithubPicbed https://github.com/jiangsai0502/PicBed.git`

5. 查看远程库地址和在本地的默认名称：`git remote -v`

6. 删除远程库在本地的默认名称：`git remote rm origin`

7. 将本地代码推送到远程仓库

   1. `git push GiteePicbed master`
   2. `git push GithubPicbed master`

8. 从远程仓库拉取代码到本地

   1. `git pull GiteePicbed master`
   2. `git pull GithubPicbed master`



### 配置PicGo

[参考](https://picgo.github.io/PicGo-Doc/zh/guide/config.html)

![anX8GM](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/anX8GM.png)

> * 设定仓库名的时候，是按照“账户名/仓库名”的格式填写
>   * 如 jiangsai0502/PicBedRepo
> * 分支名统一填写“master”
> * 将之前的Token黏贴在这里：`74d803fcee14a9c36a8f1f387e5085446c2489f1`
> * 存储路径可以写成img/，这样会在repository下创建一个“img”文件夹
> * 自定义域名的作用是，在上传图片后成功后，PicGo会将“自定义域名+上传的图片名”生成的访问链接，放到剪切板上https://raw.githubusercontent.com/账户名/仓库名/分支名，自定义域名需要按照这样去填写
>   * 如https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master



### 配置upic

[参考](https://blog.svend.cc/upic/)

![V1fBdf](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/V1fBdf.png)



### 保存图片在blog中

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/image-20200420204547297.png)





### 图片左对齐

`align='left'`

`<img src="https://xxx" align='left' style="zoom:25%;" />`



### GitHub无法连接问题

> **关于GitHub的raw.githubusercontent.com无法链接的问题**
>
> 方法1：修改hosts解决掉此问题 [参考](https://www.ioiox.com/archives/62.html)
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
>    ```bash
> sudo vi /etc/hosts    #打开hosts文件
>    
>    127.0.0.1	localhost
>    255.255.255.255	broadcasthost
>    ::1             localhost
>    199.232.68.133 raw.githubusercontent.com
>    ```
>    
>    : wq 存盘并退出vi
> > 最后插入一行上面查到的 IP Address
>
> 方法2：修改DNS
>
> 设置DNS为114.114.114.114或者8.8.8.8
>
> ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200709230841.png)

