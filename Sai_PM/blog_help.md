### Agile 帮助文档如何新增修改

#### 如何修改文档

1. 克隆代码库到本地

   从文档在 icode 上的地址： `http://icode.baidu.com/repos/baidu/agile/help-doc/tree/master` 获取 copy 链接

   ![](http://bj.bcebos.com/ibox-thumbnail98/a1422ceb63c9c81a03850567b44aef10?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-02T09%3A43%3A08Z%2F1800%2F%2F3e5d290d1ad45a1f4ff56fb97f616d6de74654ddd27d0edbf94e9cef792530c4)

   * `cd ~/Documents`
   * `git clone ssh://jiangsai02@icode.baidu.com:8235/baidu/agile/help-doc baidu/agile/help-doc && scp -p -P 8235 jiangsai02@icode.baidu.com:hooks/commit-msg baidu/agile/help-doc/.git/hooks/ && git config -f baidu/agile/help-doc/.git/config user.name jiangsai02 && git config -f baidu/agile/help-doc/.git/config user.email jiangsai02@baidu.com`

2. 修改文档

3. 本地预览变更

   * `cd ~/Documents/baidu/agile/help-doc`
   * `ydoc serve`

4. 查看变更：`git diff`

5. 将变更提交到暂存区：`git add .`

6. 提交：`git commit -m "自己编辑变更注释"`

7. 推送到服务器：`git push origin HEAD:refs/for/master`

8. 执行完第7步，终端会给出一个链接，同时icode公众号给个人hi发送一条包含icode评审详情页链接的消息，两种方式都可以

   1. 终端会给出的链接格式是`http://icode.baidu.com/myreview/changes/xxxxxxx`，该链接会跳转到icode评审详情页，在icode评审详情页内点击`持续集成-ChangePipeline`，即进入agile详情页，在agile详情页内点击左上角的`master`

      > | <img src="http://bj.bcebos.com/ibox-thumbnail98/4ac72265974ceff41de115b101a5cd29?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A40%3A23Z%2F1800%2F%2Fbad03514a8b4f2d527d3939b0dab825a966f890f5cdb3653073878bcf8f68e33" style="zoom:50%;" /> | <img src="http://bj.bcebos.com/ibox-thumbnail98/5706108c6b3fa5117867e2b5e13c07af?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A41%3A14Z%2F1800%2F%2F6607956e5a73dcf9702e2be024ecf288a57fde71b857e5820db9c41386ebfd5d" style="zoom:50%;" /> |
      > | ------------------------------------------------------------ | ------------------------------------------------------------ |
      > | <img src="http://bj.bcebos.com/ibox-thumbnail98/de381f802bcad0ebb498b0476af7c0f5?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A42%3A37Z%2F1800%2F%2F9b97313e9fb16aad795601b3a34594cc8338040750285ed9d40c9fbc53c83fdb" style="zoom:50%;" /> |                                                              |

   2. icode公众号给个人hi发送一条消息，点击消息中的[查看详情]，该链接会跳转到icode评审详情页，在icode评审详情页内点击`持续集成-ChangePipeline`，即进入agile详情页，在agile详情页内点击左上角的`master`

      > | <img src="http://bj.bcebos.com/ibox-thumbnail98/dca19c38fcc3aa9df79b6f5b933a21ab?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A44%3A24Z%2F1800%2F%2Fadaec31957203ba1d88368d0828b7b8f47ff424a3a00b159d9cd17b07ce06315" style="zoom:50%;" /> | <img src="http://bj.bcebos.com/ibox-thumbnail98/5706108c6b3fa5117867e2b5e13c07af?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A41%3A14Z%2F1800%2F%2F6607956e5a73dcf9702e2be024ecf288a57fde71b857e5820db9c41386ebfd5d" style="zoom:50%;" /> |
      > | ------------------------------------------------------------ | ------------------------------------------------------------ |
      > | <img src="http://bj.bcebos.com/ibox-thumbnail98/de381f802bcad0ebb498b0476af7c0f5?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A42%3A37Z%2F1800%2F%2F9b97313e9fb16aad795601b3a34594cc8338040750285ed9d40c9fbc53c83fdb" style="zoom:50%;" /> |                                                              |

9. 进入Agile的[ChangePipeline](http://agile.baidu.com/#/builds/baidu/agile/help-doc@ChangePipeline@master)，等待流水线完成第一阶段"编译" ，然后点击第二阶段"部署测试版本"，其下方会展开新的区域，点击`Promotion/Deploy`任务的`执行`，等待执行完成。完成后icode公众号给个人hi发送一条包含icode评审详情页链接的消息，提示"持续集成通过"

   > <img src="http://bj.bcebos.com/ibox-thumbnail98/77df319416236390da36887805d4e45e?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A49%3A24Z%2F1800%2F%2F013252683fd38e5337b2fdb94c1853a1ae8cd09396682d7a17912a9a5aeb43d9" style="zoom:50%;" />
   >
   > <img src="http://bj.bcebos.com/ibox-thumbnail98/87583f51635486fd95635cc0cab85080?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T04%3A10%3A40Z%2F1800%2F%2F88f7abf3acf803cd99d2cafc55738388c7bd3b591326d7ac7417d18e3062c8b1" style="zoom:50%;" />

   

10. 查看[测试环境](http://help.agile.baidu-int.com/pipetest/)的更改是否成功

11. 回到第8步的icode评审详情页，页面右侧有2个按钮`合入`和`打分/评论`，点击`打分/评论`，选择`2`，点击`发表`，页面刷新后，点击`合入`

    > <img src="http://bj.bcebos.com/ibox-thumbnail98/5740ac26ed774d4ca28f1d388f743aa5?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A56%3A19Z%2F1800%2F%2F88f8b8f8f4effca6104b2a357f31aa82406d20d749edb576a1a3377d12e08f83" style="zoom:50%;" />

    

12. 进入Agile的[MasterPipeline](http://agile.baidu.com/#/builds/baidu/agile/help-doc@MasterPipeline@branches)，等待流水线完成第一阶段"编译" ，然后点击第二阶段"部署测试版本"，其下方会展开新的区域，点击`Promotion/Deploy`任务的`执行`，等待执行完成（点击第1行的"执行"是执行该`Promotion/Deploy`任务，点击第2行的"执行"是跳过该`Promotion/Deploy`任务），然后点击第三阶段"部署正式版本"阶段，点击`Promotion/Deploy`任务的`执行`，等待执行完成

    > <img src="http://bj.bcebos.com/ibox-thumbnail98/93a8654ea61632d9ef7b0eda5fff431c?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A58%3A29Z%2F1800%2F%2F978b9e8e183ad7ac0c51cc15a2624307f89a5ae6c5befc9835cdbba449c6e601" style="zoom:50%;" />
    >
    > <img src="http://bj.bcebos.com/ibox-thumbnail98/55170bf8a99a4cb84c94d577bf0f6be3?authorization=bce-auth-v1%2Ffbe74140929444858491fbf2b6bc0935%2F2020-02-13T03%3A59%3A40Z%2F1800%2F%2F63e5a6ecc11f8ab4ec6363d956b4e08118ade1325615187447a32a222a673f4c" style="zoom:50%;" />

13. 查看[正式环境](http://help.agile.baidu-int.com/pipe/)





### YDoc系统

1. 环境搭建

   > 详细请参照[帮助文档](https://hellosean1025.github.io/ydoc/documents/index.html)   

   简易教程如下

   * 安装node.js：brew install node

   * 安装ydoc：npm install -g ydoc

   * 创建YDoc目录：mkdir ~/Documents/MyYDoc && cd ~/Documents/MyYDoc

   * 安装rc版本：npm install ydoc@rc

     > 在当前目录生成一个 'node_modules' 目录和package-lock.json文件

   * 创建站点目录：mkdir AgileDoc && cd AgileDoc

   * 初始化：ydoc init

     > 在当前目录生成一个 'docs' 目录，用于存放文档(markdown)文件

   * 构建：ydoc build

     > 使用 'docs' 目录中的文件进行文档站的构建，构建成功后会在当前目录生成一个 '_site' 目录，打开 '_site' 目录中的 index.html 文件即可访问构建的文档站首页

   * 启动服务：ydoc serve

     > 启动一个服务，默认是http://127.0.0.1:9999。修改docs目录下的文档，可实时看到变化

   * 安装插件

     > 插件网址：https://hellosean1025.github.io/ydoc/plugin/index.html  
     > 安装点击图片放大功能的插件：npm i ydoc-plugin-img-view  
     > 在 'docs' 和 '_site' 同级目录下创建ydoc.js文件  
     >
     > ```json
     > {
     > "plugins": ["img-view"]
     > }
     > ```

   

2. 系统目录结构

   一个基本的 ydoc 目录结构如下:

   ```markdown
   ├── docs/
       ├── index.jsx
       ├── NAV.md
       ├── book-1/
           ├── index.md
           └── SUMMARY.md
       └── book-2/
           ├── index.md
           ├── SUMMARY.md
   ```

   | 文件              | 描述                                                         |
   | ----------------- | ------------------------------------------------------------ |
   | `index.jsx`       | 首页 (**必需**)                                              |
   | `NAV.md`          | 导航 (**必需**)                                              |
   | `book/index.md`   | 文档页首页 (**必需**)                                        |
   | `book/SUMMARY.md` | 文档目录，SUMMARY.md 引用的所有 markdown 文件将会被转换成 html 文件 (__可选__) |

   > 所有的目录名称都必须是英文，包括各个文件名，想要在网页上显示中文名，要配置每个目录中的SUMMARY.md
   > 注：`NAV.md` 和 `SUMMARY.md` 文件名大写

3. 顶端导航

   在 NAV.md 文件中可配置网站的顶端导航标题、logo、菜单列表信息，简单示例如下：

   ```markdown
   # YDoc
   ![logo](ydoc/images/logo.png)
   
   * [文档](/documents/index.md)
   * [文档规范](/style-guide/index.md)
   * [插件](/plugins/index.md)
   ```

   上面的 markdown 内容可生成如下导航信息：

   ```markdown
   标题：YDoc
   Logo：ydoc/images/logo.png
   导航：文档 文档规范 插件
   ```

4. 首页

   执行 init 命令后生产 `docs` 目录中的 `index.jsx` 就是首页的文档文件，在这个文件中我们可以通过简单的配置来完善首页信息：

   * banner 网站标语栏

     | 属性              | 描述                         |
     | ----------------- | ---------------------------- |
     | `name`            | 标语标题                     |
     | `desc`            | 标语描述信息                 |
     | `btns`            | 按钮组，可设置多个按钮       |
     | `caption`         | 说明信息，例如“当前版本信息” |
     | `btns[n].name`    | 按钮名称                     |
     | `btns[n].href`    | 按钮链接                     |
     | `btns[n].primary` | 是否为主按钮                 |

   * features 特性

     | 属性               | 描述     |
     | ------------------ | -------- |
     | `features[n].name` | 特性名称 |
     | `features[n].desc` | 特性描述 |

   * footer 底部信息

     | 属性                | 描述         |
     | ------------------- | ------------ |
     | `copyRight`         | 版权信息     |
     | `copyRight.name`    | 版权主体名称 |
     | `copyRight.href`    | 版权主体链接 |
     | `links`             | 友情链接     |
     | `links.xxx`         | 链接组标题   |
     | `links.xxx[n]`      | 链接项       |
     | `links.xxx[n].name` | 链接项名称   |
     | `links.xxx[n].href` | 链接项名称   |

5. 文档页

   YDoc 借鉴了 Gitbook 中 `"书"` 的概念：

   - YDoc 的每个导航项都是不同的 `"书"`

   - 每本 `"书"` 都是由目录和页面组成

   - YDoc 文档站就是由若干本书及其他页面组成的网站

     使用 SUMMARY.md 文件生成一本书的目录，SUMMARY 文件包含了一本书的所有章节信息，具体的文档页面是若干 markdown 文件

     SUMMARY.md 由一组链接列表组成，将一个列表嵌套到父章节将创建子章节，简单示例如下：

     ```js
     # 目录
     
     ### 章节 1
     
     * [快速开始](start.md)
       * [安装](installation.md)
     * [项目设置](setting.md)
       * [配置文件](config.md)
     ```

   * 锚点

     > 目录中的章节可以使用锚点指向文件的特定部分。

     ```js
     # 目录
     
     ### 章节 2
     
     * [API](api.md)
       * [a](api.md#anchor1)
       * [b](api.md#anchor2)
     ```

   * 章节

     > 目录可以分为多个部分

     ```js
     # 目录
     
     ### 章节 1
     
     * [快速开始](start.md)
       * [安装](installation.md)
     * [项目设置](setting.md)
       * [配置文件](config.md)
     
     ### 章节 2
     
     * [API](api.md)
       * [a](api.md#a)
       * [b](api.md#b)
     ```

