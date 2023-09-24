> 开宗明义：不是所有的网站都能用Web Scraper，有些网站反爬，能不能用可以先爬前先测一下

##### 功能说明

> 网页 - 右键 - 开发者工具 - 最右侧Web Scraper
>
> 1. 创建1个爬虫项目：Create new sitemap，设置1个待爬取的起始页面（之所以叫起始页面，以后后续页面都是从本页向下一级一级延展的）
>
>    * 如要获取知乎上的一个问题的回答，就创建一个 sitemap ，并将这个问题所在的地址设置为sitemap 的 Start URL，然后点击 “Create Sitemap”即可创建一个 sitemap
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221529954.png)
>
> 2. 项目看板：Sitemaps展示所有创建过的 sitemap ，从这里进入每一个 sitemap 进行数据抓取
>
>    * 如曾创建过百度，知乎，quoa等多个sitemap，本次要去抓取百度的内容
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221533055.png)
>
> 3. 项目：进入某个 具体项目sitemap后，进行进行如下操作
>
>    * selector：选择器，一个选择器对应网页上待爬取的一块区域
>
>      * 一个 sitemap 可有多个 selector；每个 selector 还可包含多个子 selector ；一个 selector 可以只对应一个标题，也可以对应一整个区域；每个区域可能包含标题、副标题、作者信息、内容等
>
>    * Selectors：查看所有的选择器
>
>    * **Scrape：开始数据抓取工作**
>
>    * **Export data as CSV:将抓取的数据以 CSV 格式导出**
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221544255.png)
>
> 4. 选择器：
>
>    1. 

##### 案例实操

1. 抓取[李笑来微博的全部内容](https://weibo.com/bylixiaolai?is_all=1)

   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    1. sitemap name：LiXiaoLaiWeiBo
   >    2. Start URL 1：https://weibo.com/bylixiaolai?is_all=1
   >
   > 2. 创建1个选择器：
   >
   >    Add new selector
   >
   >    1. 选择器名称：Id设为Element
   >    2. 选择器类型：Type设为Element scroll down，因为微博页面为下拉刷新显示更多
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 然后选择要抓取的内容，选两个同类型的内容后，所有同类型的内容都会被选中，都变成红色；3.点击Done selecting 完成选择
   >    4. 勾选Multiple
   >
   > 3. 创建1个子选择器
   >
   >    点击Element选择器后，Add new selector
   >
   >    1. 

2. 抓取[留学人才网](http://www.liuxuehr.com/)的文章

   > 需求：抓取文章列表中的所有文章
   >
   > 实现
   >
   > 1. 打开网址：https://www.newjobs.com.cn/list/1，F12调出开发者工具，定位到Web Scraper 标签栏
   >
   > 2. 创建1个爬虫项目：Create new sitemap
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221744833.png)
   >
   > 3.  只爬文章标题
   >
   >    新增选择器：Add new selector
   >
   >    1. Id：Articles_Title
   >    2. Type：选Text ，只抓取文章标题；选Link，既抓文章标题又抓文章链接
   >    3. Selector：
   >       1. 点击 Select，鼠标移到页面上，放在文章标题上时，文章标题会变成黄色，点击该区域即为选中，颜色变为红色 -> 移动到下一个文章标题，点击选中，本页所有文章标题都会自动选中，然后点击"Done selecting！”；最后选择 Multiple ；保存
   >       2. 每一个Selector选择器只能选择一个元素
   >       3. 为了选择更多信息，可以先选中小元素，然后点击[P]放大选中区域后，让选中区域囊括更多信息，后续在这个大区域中创建子选择器Selector
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221757568.png)
   >
   > 4. 爬文章标题&文章链接
   >
   >    新增选择器：Add new selector
   >
   >    1. Id：Articles_Title_Link
   >    2. Type：选Link，既抓文章标题又抓文章链接
   >    3. Selector：同上
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221801201.png)

> > 需求：抓取知乎上某个问题的所有回答 
> >
> > 分析：页面懒加载，向下滚动时才会加载后续回答
> >
> > 待爬内容结构分析
> >
> > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221604486.png)
> >
> > * 一个问题有多个答案
> >
> > * 一个答案是一个区域
> >
> > * 一个区域包括1昵称、2赞同数、3答案内容、4发布时间、5评论数，其中1、2、3为待抓取内容
> >
> > * 内容拓扑图如下
> >
> >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221609214.png)
> >
> > 1. 抓取逻辑：由起始页进入 -> 获取已加载的回答 -> 找到一个答案区域 -> 提取区域中的1、2、3 -> 完成后依次向下执行。当已加载的区域获取完成，模拟向下滚动鼠标，加载后续的部分，一直循环往复，直到全部加载完毕
>
> 1. 打开网址：https://www.zhihu.com/question/30692237，F12调出开发者工具，定位到Web Scraper 标签栏
>
> 2. 创建1个爬虫项目：Create new sitemap
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221549302.png)
>
> 3.  为该项目新增选择器：Add new selector
>
>    1. Id：随意填个项目名
>
>    2. Type：选Element scroll down ，本类型以向下滚动的方式可以加载更多
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309221622760.png)
>
>    3. Selector：
>
>       1. 点击 Select，鼠标移到页面上，鼠标放在可爬取的元素区域上时，元素区域会变成绿色/黄色，点击该区域即为选中，已选中的元素区域会变为红色；移动到下一个回答，同样当绿色框框住一个回答区域后点击鼠标；这时，除了这两个回答外，所有的回答区域都变成了红色框，然后点击"Done selecting！”；最后别忘了选择 Multiple ；之后保存
>       2. 每一个Selector选择器只能选择一块区域
>       3. 为了选择更多信息，可以选中区域后，放大该区域来囊括更多信息，后续在这个大区域中创建子选择器Selector
>
> 4. 创建子选择器
>
>    ![image-20230922163318310](/Users/jiangsai/Library/Application Support/typora-user-images/image-20230922163318310.png)
>
>    1. 创建昵称选择器，设置 id 为 name，Type 设置为 Text，Select 选择昵称部分，如果没经验的话，可能第一次选的不准，发现有错误，可以调整，保存即可；



8、接下来，单击红色区域，进入刚刚创建的 answer 选择器中，创建子选择器；

![img](https://upload-images.jianshu.io/upload_images/626258-52587ecc31e26915.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

9、创建昵称选择器，设置 id 为 name，Type 设置为 Text，Select 选择昵称部分，如果没经验的话，可能第一次选的不准，发现有错误，可以调整，保存即可；

![img](https://upload-images.jianshu.io/upload_images/626258-9055a6dad90d7ae8.gif?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

10、创建赞同数选择器；

![img](https://upload-images.jianshu.io/upload_images/626258-0c540791ee1ef26c.gif?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

11、创建内容选择器，由于内容是带有格式的并且较长，所以有个技巧，从下面选择会比较方便；

![img](https://upload-images.jianshu.io/upload_images/626258-a75931d5dd217c24.gif?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

12、执行 Scrape 操作，由于内容较多，可能需要几分钟的时间，如果是为了做测试，可以找一个回答数较少的问题做测试。

![img](https://upload-images.jianshu.io/upload_images/626258-b6fdadcaf498aab1.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

最后编辑于 ：2018.09.14 20:37:21