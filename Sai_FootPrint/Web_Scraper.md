> 开宗明义：不是所有的网站都能用Web Scraper，有些网站反爬，能不能用可以先爬前先测一下

##### 案例实操

1. 滚动加载的页面：知乎

   > 需求：获取一个问题下所有答案的答主昵称、答题时间、答案内容
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309262131254.png)
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    >1. sitemap name：ZHScrollPage
   >    >2. Start URL 1：https://www.zhihu.com/question/619256436
   >
   > 2. 为项目创建父选择器，用于粗爬内容
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为All_Answers
   >    > 2. 选择器类型：Type设为Element scroll down，为实现向下滚动加载更多内容
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一整个答案块，再选一个答案块（此时所有答案块都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. 滚动上限：默认500，应对有些可以无限滚动的网站，这里的值可以改小，不要改大，否则等待时间超长，电脑也会卡死
   >    > 6. 选择器等待时间：默认2000ms
   >
   > 3. 为父选择器创建子选择器，用于从父选择器进行细晒内容
   >
   >    > 点击进入Infos选择器
   >
   >    > 在_root / All_Answers下，Add new selector创建1个**答主昵称**选择器
   >    >
   >    > 1. 选择器名称：Id设为Answer_Name
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择答案块中的昵称 -> 点击Done selecting 完成选择
   >
   >    > 在_root / All_Answers下，Add new selector创建1个**答题时间**选择器
   >    >
   >    > 1. 选择器名称：Id设为Answer_Time
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择答案块中的时间 -> 点击Done selecting 完成选择
   >
   > 4. 预览每个选择器爬取的内容
   >
   > 5. 正式爬取
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309251848381.png)

2. 爬取二级页的内容：豆瓣读书

   > 需求：抓取豆瓣读书榜，获取所有书的标题、短评数、短片链接
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271353707.png)
   >
   > 分析：页面是分页
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    > 1. sitemap name：DBSonPage
   >    > 2. Start URL 1：https://book.douban.com/top250
   >
   > 2. 为项目创建父选择器，用于跳转二级页
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为All_Item_to_Detail
   >    > 2. 选择器类型：Type设为Link，可以拿到目标元素的文字和链接（因为所有待抓取的信息都是去二级页拿，这里只是个入口）
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一个可点击的书名，再选一个书名 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Link type：默认Link(read from href attribute)
   >
   > 3. 为父选择器创建子选择器，用子选择器承载二级页内容
   >
   >    > 点击任意一个一级页的书名链接进而二级页
   >
   >    > 点击进入All_Item_to_Detail选择器
   >
   >    > 在_root / All_Item_to_Detail下，Add new selector创建1个**书名**选择器
   >    >
   >    > 1. 选择器名称：Id设为Title
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择作品中的标题 -> 点击Done selecting 完成选择
   >
   >    > 在_root / All_Item_to_Detail下，Add new selector创建1个**短评数**选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_ShortComments
   >    > 2. 选择器类型：Type设为Text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 然后短评数量  -> 点击Done selecting 完成选择
   >
   >    > 在_root / All_Item_to_Detail下，Add new selector创建1个**短评数链接**选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_ShortCommentsLink
   >    > 2. 选择器类型：Type设为Element attribute
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 然后短评数量 -> 点击Done selecting 完成选择
   >    > 4. 选择要抓取的元素属性：href（这里会根据第3步选择的元素所包含的属性而定）
   >    > 5. 预览一下：Data preview
   >
   > 4. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271350499.png)

3. 滚动加载所有条目+二级页内容爬取

   > 需求：爬取知乎搜索答案
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271408491.png)
   >
   > [教程1](https://www.bilibili.com/video/BV1nU4y1R7vv/?spm_id_from=333.337.search-card.all.click&vd_source=052b07ad0190d9dabdf1d78fda0168a7)，[教程2](https://www.bilibili.com/video/BV1d34y1V7id/?spm_id_from=333.337.search-card.all.click&vd_source=052b07ad0190d9dabdf1d78fda0168a7)
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   > 2. 为项目创建父选择器，用于粗爬内容
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为All_Items
   >    > 2. 选择器类型：Type设为Element scroll down，为实现向下滚动加载更多内容
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一整个搜索结果条目，再选一整个搜索结果条目 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. 滚动上限：默认500
   >    > 6. 选择器等待时间：默认2000ms
   >
   > 3. 为父选择器创建子选择器，用于从父选择器进行细筛内容
   >
   >    > 点击进入All_Items选择器
   >
   >    > 在_root / All_Items下，Add new selector创建1个**标题**选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_Question
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择搜索结果条目的标题 -> 点击Done selecting 完成选择
   >
   >    > 在_root / All_Items下，Add new selector创建1个**二级页**选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_to_Detail
   >    >
   >    > 2. 选择器类型：Type设为Link
   >    >
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择搜索结果条目的标题 -> 点击Done selecting 完成选择
   >    >
   >    >    > 点击任意一个搜索结果条目进而二级页
   >    >
   >    >    > 点击进入Item_to_Detail选择器
   >    >
   >    >    > 在_root / All_Items / Item_to_Detail下，Add new selector创建1个**关注者**选择器
   >    >    >
   >    >    > 1. 选择器名称：Id设为Item_Follower
   >    >    > 2. 选择器类型：Type设为text
   >    >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择搜索结果条目的标题 -> 点击Done selecting 完成选择
   >
   > 4. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309262000638.png)

4. 爬取网址递增的页面

   > 需求：抓取知乎个人主页的想法中的内容和编辑时间
   >
   > 分析：页面是分页，网址递增
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    1. sitemap name：ZHMorePage
   >    2. Start URL 1：https://www.zhihu.com/org/hong-chen-nan-nu/pins?page=[1-4:1]
   >       1. [1-4:1]表示从1递增到4，步长为1，分别是1、2、3、4
   >       2. 豆瓣读书的步长是25：https://book.douban.com/top250?start=[0-100:25]
   >
   > 2. 创建母选择器，Add new selector
   >
   >    1. 选择器名称：Id设为All_Items
   >    2. 选择器类型：Type设为Element，因为无需进二级页，本页就有目标元素
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择一个想法元素，再选一个想法元素（此时所有想法元素都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    4. 勾选Multiple
   >
   > 3. 为母选择器创建子选择器
   >
   >    点击All_Items选择器后，Add new selector创建1个**内容**选择器
   >
   >    1. 选择器名称：Id设为Item_Content
   >    2. 选择器类型：Type设为text
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 选择想法元素中的内容 -> 点击Done selecting 完成选择
   >
   >    Add new selector创建1个**编辑时间**选择器
   >
   >    1. 选择器名称：Id设为Item_Time
   >    2. 选择器类型：Type设为Text
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 然后想法元素中的时间  -> 点击Done selecting 完成选择
   >
   > 4. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309261728240.png)

5. 爬取点击下一页的网页

   > 需求：抓取知乎个人主页的想法中的内容和编辑时间
   >
   > 分析：页面是分页，网页底部可点击下一页
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    1. sitemap name：ZHNextPage
   >    2. Start URL 1：https://www.zhihu.com/org/hong-chen-nan-nu/pins?page=1
   >
   > 2. 创建母选择器，Add new selector
   >
   >    1. 选择器名称：Id设为FatherPage
   >    2. 选择器类型：Type设为Element Click，点击进入下一页
   >    3. 选择器选择待抓取的元素：Selector 点击Select ->  先选择一个想法元素，再选一个想法元素（此时所有想法元素都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    4. 选择器选择下一页点击元素：
   >       1. 方法一：Click Selector点击Select -> 选择底部导航【下一页】-> 点击Done selecting 完成选择
   >       2. 方法二：Click Selector点击Select -> 先选择【2】再选择【3】（此时所有分页链接都会被选中变红）-> 点击Done selecting 完成选择
   >    5. Click type：选择Click once（Click once即只点击1次，Click more即一直点击知道最后一页）
   >    6. Click element uniqueness：默认Unique Text不变
   >    7. 勾选Multiple
   >    8. Discard initial elements：默认Never discard不变
   >    9. Delay (ms)：默认2000不变
   >
   > 3. 为母选择器创建子选择器
   >
   >    点击FatherPage选择器后，Add new selector创建1个**内容**选择器
   >
   >    1. 选择器名称：Id设为FatherPage_Content
   >    2. 选择器类型：Type设为text
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 选择想法元素中的内容 -> 点击Done selecting 完成选择
   >
   >    Add new selector创建1个**编辑时间**选择器
   >
   >    1. 选择器名称：Id设为FatherPage_Time
   >    2. 选择器类型：Type设为Text
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 然后想法元素中的时间  -> 点击Done selecting 完成选择
   >
   > 4. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309262121468.png)

6. 抓取人民网

   > 需求
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    1. sitemap name：RMW
   >    2. Start URL 1：http://cpc.people.com.cn/GB/64093/64387/index1.html
   >
   > 2. 创建母选择器，Add new selector
   >
   >    1. 选择器名称：Id设为FatherPage
   >    2. 选择器类型：Type设为Element Click，点击进入下一页
   >    3. 选择器选择待抓取的元素：Selector 点击Select ->  先选择一个想法元素，再选一个想法元素（此时所有想法元素都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    4. 选择器选择下一页点击元素：
   >       1. 方法一：Click Selector点击Select -> 选择底部导航【下一页】-> 点击Done selecting 完成选择
   >       2. 方法二：Click Selector点击Select -> 先选择【2】再选择【3】（此时所有分页链接都会被选中变红）-> 点击Done selecting 完成选择
   >    5. Click type：选择Click once（Click once即只点击1次，Click more即一直点击知道最后一页）
   >    6. Click element uniqueness：默认Unique Text不变
   >    7. 勾选Multiple
   >    8. Discard initial elements：默认Never discard不变
   >    9. Delay (ms)：默认2000不变
   >
   >    1. 为母选择器创建子选择器
   >
   >       点击FatherPage选择器后，Add new selector创建1个**内容**选择器
   >
   >       1. 选择器名称：Id设为FatherPage_Content
   >       2. 选择器类型：Type设为text
   >       3. 选择器选择待抓取的元素：Selector 点击Select -> 选择想法元素中的内容 -> 点击Done selecting 完成选择
   >
   >       Add new selector创建1个**编辑时间**选择器
   >
   >       1. 选择器名称：Id设为FatherPage_Time
   >       2. 选择器类型：Type设为Text
   >       3. 选择器选择待抓取的元素：Selector 点击Select -> 然后想法元素中的时间  -> 点击Done selecting 完成选择
   >
   >    2. 运行并实时预览

7. 抓取B站个人空间

   > 需求：获取个人空间中所有作品的标题、标题链接
   >
   > 分析：个人空间是分页；标题链接是隐式信息不能直接抓取，[教程](https://www.bilibili.com/video/BV14F411P7DF/?spm_id_from=pageDriver&vd_source=052b07ad0190d9dabdf1d78fda0168a7)
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    1. sitemap name：BZhanTest
   >    2. Start URL 1：https://space.bilibili.com/107861587/video
   >
   > 2. 创建母选择器，Add new selector
   >
   >    1. 选择器名称：Id设为Elements
   >    2. 选择器类型：Type设为Element，因为Element只是一个信息单元，太杂了，我们想要的是其中的某些关键信息
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一整个作品块，再选一个作品块（此时所有作品块都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    4. 勾选Multiple
   >
   > 3. 为母选择器创建子选择器
   >
   >    点击Element选择器后，Add new selector创建1个标题选择器
   >
   >    1. 选择器名称：Id设为Title
   >    2. 选择器类型：Type设为text
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 然后选择作品中的标题 -> 点击Done selecting 完成选择
   >
   >    Add new selector创建1个播放量选择器
   >
   >    1. 选择器名称：Id设为Link
   >    2. 选择器类型：Type设为Element attribute
   >    3. 选择器选择待抓取的元素：Selector 点击Select -> 然后选择作品中的标题  -> 点击Done selecting 完成选择
   >    4. 选择要抓取的元素属性：href（这里会根据第3步选择的元素所包含的属性而定）
   >
   > 4. 预览每个选择器爬取的内容
   >
   > 5. 正式爬取

8. 抓取李笑来微博的全部内容

   > 分析：微博网页的结构有点特殊，不知道怎么抓

9. 抓取[留学人才网](http://www.liuxuehr.com/)的文章

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