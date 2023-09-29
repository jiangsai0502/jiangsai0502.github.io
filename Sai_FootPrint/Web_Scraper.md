> 开宗明义：不是所有的网站都能用Web Scraper，有些网站反爬，能不能用可以先爬前先测一下

##### 案例实操

1. 滚动加载 + 爬取一级页信息

   > 原始需求：抓取「知乎」一个问题下所有答案的「答主昵称」「答题时间」「答案内容」
   >
   > > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309262131254.png)
   > >
   > > 需求分析：滚动加载获取一级页所有答案信息后，在一级页进行抓取
   >
   > 实现
   >
   > > 1. 创建1个爬虫项目：Create new sitemap
   > >
   > >    >1. sitemap name：ZHScrollPage
   > >    >2. Start URL 1：https://www.zhihu.com/question/619256436
   > >
   > > 2. 创建**一级页滚动加载**的选择器
   > >
   > >    > 在_root下，Add new selector
   > >    >
   > >    > 1. 选择器名称：Id设为All_Items
   > >    > 2. 选择器类型：Type设为Element scroll down，为实现向下滚动加载更多内容
   > >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一整个答案块，再选一个答案块（此时所有答案块都会被选中，都变成红色） -> 点击Done selecting 完成选择
   > >    > 4. 勾选Multiple
   > >    > 5. 滚动上限：默认500，应对有些可以无限滚动的网站，这里的值可以改小，不要改大，否则等待时间超长，电脑也会卡死
   > >    > 6. 选择器等待时间：默认2000ms
   > >    > 7. Parent Selectors：选择_root
   > >
   > > 3. 点击进入All_Items选择器
   > >
   > > 4. 创建**抓取一级页信息**的选择器
   > >
   > >    > 在_root / All_Items下，Add new selector创建1个「答主昵称」选择器
   > >    >
   > >    > 1. 选择器名称：Id设为Answer_Name
   > >    > 2. 选择器类型：Type设为text
   > >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择答案块中的昵称 -> 点击Done selecting 完成选择
   > >    > 4. Regex：默认为空
   > >    > 5. Parent Selectors：选择All_Items
   > >
   > >    > 同上创建「答题时间」「答案内容」选择器
   > >
   > > 5. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309272329730.png)

2. 滚动加载 + 爬取二级页信息

   > 原始需求：抓取「知乎搜索答案」所有搜索结果的「问题标题」「问题关注者」「问题浏览量」
   >
   > > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271408491.png)
   > >
   > > 需求分析：滚动加载获取一级页所有搜索结果后，从一级页入口进入二级页，在二级页进行抓取
   >
   > [教程1](https://www.bilibili.com/video/BV1nU4y1R7vv/?spm_id_from=333.337.search-card.all.click&vd_source=052b07ad0190d9dabdf1d78fda0168a7)，[教程2](https://www.bilibili.com/video/BV1d34y1V7id/?spm_id_from=333.337.search-card.all.click&vd_source=052b07ad0190d9dabdf1d78fda0168a7)
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   > 2. 创建**一级页滚动加载**的选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为All_Items
   >    > 2. 选择器类型：Type设为Element scroll down，为实现向下滚动加载更多内容
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一整个搜索结果条目，再选一整个搜索结果条目 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Element limit：滚动次数上限，默认500
   >    > 6. Delay (ms)：选择器等待时间，默认2000ms
   >    > 7. Parent Selectors：选择_root
   >
   > 3. 创建从**一级页入口进入二级页**的选择器
   >
   >    > 在_root 下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为Item_to_Detail
   >    > 2. 选择器类型：Type设为Link
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择一个可点击的搜索结果标题，再选一个搜索结果标题 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Link type：默认Link (read from href attribute)
   >    > 6. Parent Selectors：选择 _root
   >
   > 4. 随便点击一个搜索结果链接进入二级页
   >
   > 5. 点击进入Item_to_Detail选择器
   >
   > 6. 创建二级页的信息抓取选择器
   >
   >    > 在_root / Item_to_Detail下，Add new selector创建1个「问题标题」选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_Question
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择搜索结果条目的标题 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Regex：默认为空
   >    > 6. Parent Selectors：选择Item_to_Detail
   >
   >    > 同上创建「问题关注者」「问题浏览量」选择器
   >
   > 7. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309272334219.png)

3. 一级页网址规律递增 + 爬取一级页信息

   > 原始需求：抓取「知乎个人主页」的所有想法中的「内容」「编辑时间」
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271723166.png)
   >
   > 需求分析：【一级页】网址递增，从【一级页】获取信息
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    > 1. sitemap name：ZHMorePage
   >    > 2. Start URL 1：https://www.zhihu.com/org/hong-chen-nan-nu/pins?page=[1-4:1]
   >    >    1. [1-4:1]表示从1递增到4，步长为1，分别是1、2、3、4
   >    >    2. 豆瓣读书的步长是25：https://book.douban.com/top250?start=[0-100:25]
   >
   > 2. 创建一级页中**包含所有目标元素的容器**选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为All_Items
   >    > 2. 选择器类型：Type设为Element，因为无需进二级页，本页就有目标元素
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择一个想法元素，再选一个想法元素（此时所有想法元素都会被选中，都变成红色） -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Parent Selectors：选择 _root
   >
   > 3. 点击进入All_Items选择器
   >
   > 4. 创建**抓取一级页信息**的选择器
   >
   >    > 在_root / All_Items下，Add new selector创建1个「内容」选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_Content
   >    > 2. 选择器类型：Type设为text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择想法元素中的内容 -> 点击Done selecting 完成选择
   >
   >    > 同上，建立1个「编辑时间」选择器
   >
   > 5. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309272353060.png)

4. 分页 + 爬取一级页信息&二级页信息

   > 原始需求：抓取「B站个人空间」的所有投稿中的「作品标题」「观看量」「点赞量」「投币量」「收藏量」
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309282212373.png)
   >
   > 需求分析：【一级页】底部分页导航，从【一级页】获取信息
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    > 1. sitemap name：BLNextPage
   >    > 2. Start URL 1：https://space.bilibili.com/107861587/video
   >
   > 2. 创建一级页的**翻页&内容块**选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Items_Preview
   >    > 2. Type：选择器类型，设为Element Click
   >    > 3. Selector：待抓取的元素，点击Select ->  先选择一个作品元素，再选一个作品元素 -> 点击Done selecting 完成选择
   >    > 4. Click Selector：底部分页导航，点击Select -> 选择底部导航【下一页】-> 点击Done selecting 完成选择
   >    >    1. ~~方法二：Click Selector点击Select -> 先选择【2】再选择【3】（此时所有分页链接都会被选中变红）-> 点击Done selecting 完成选择~~
   >    > 5. Click type：选择Click more（Click once即只点击1次，Click more即一直点击知道最后一页）
   >    > 6. ~~Click element uniqueness：默认Unique Text不变~~
   >    > 7. Multiple：勾选
   >    > 8. ~~Discard initial elements：默认Never discard不变~~
   >    > 9. ~~Delay (ms)：默认2000不变~~
   >    > 10. Parent Selectors：选择 _root
   >
   > 3. 点击进入Items_Preview选择器
   >
   > 4. 创建**抓取一级页元素**选择器
   >
   >    1. 「作品标题」选择器
   >
   >       > 在_root / Items_Preview 下，Add new selector
   >       >
   >       > 1. Id：选择器名称，设为Item_Title
   >       > 2. Type：选择器类型，设为Text
   >       > 3. Selector：待抓取的元素，点击Select -> 点击作品标题  -> 点击Done selecting
   >       > 4. Multiple：不勾选
   >       > 5. ~~Regex：默认为空~~
   >       > 6. Parent Selectors：选择Items_Preview
   >
   >    2. 「观看量」选择器，同上
   >
   >    3. 「一级页入口跳转二级页」选择器
   >
   >       > 在_root / Items_Preview 下，Add new selector
   >       >
   >       > 1. Id：选择器名称，设为Preview_to_Detail
   >       > 2. Type：选择器类型，设为Link
   >       > 3. Selector：待抓取的元素，点击Select -> 点击可点击的作品标题/缩略图  -> 点击Done selecting
   >       > 4. Multiple：不勾选
   >       > 5. ~~Link type：Link (read from href attribute)~~
   >       > 6. Parent Selectors：选择Items_Preview
   >
   > 5. 随便点击一个作品链接进入二级页
   >
   > 6. 点击进入Preview_to_Detail选择器
   >
   > 7. 创建**抓取二级页元素**选择器
   >
   >    1. 「点赞量」
   >
   >       >在_root / Items_Preview / Preview_to_Detail下，Add new selector
   >       >
   >       >1. Id：选择器名称，设为Item_Thumb
   >       >2. Type：选择器类型，设为Text
   >       >3. Selector：待抓取的元素，点击Select -> 点击点赞量  -> 点击Done selecting
   >       >4. Multiple：不勾选
   >       >5. Regex：默认为空
   >       >6. Parent Selectors：选择Preview_to_Detail
   >
   >    2. 「投币量」选择器，同上
   >
   >    3. 「收藏量」选择器，同上
   >
   > 8. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309291016643.png)

5. 一级页底部分页导航 + 爬取二级页信息

   > 原始需求：抓取「人民网-综合报道」栏目所有文章的「标题」「更新时间」「文章内容」
   >
   > > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309271740088.png)
   > >
   > > 需求分析
   > >
   > > 1. 从首个【一级页】的【文章标题】进入【二级文章页】，从【二级文章页】获取相关信息，直到首个【一级页】的所有文章抓取完毕
   > > 2. 从【底部分页导航】进入下一个【一级页】，重复步骤1
   >
   > 爬取原理
   >
   > > 1. 从底部导航切换一级页
   > > 2. 从一级页的入口进入二级页
   > > 3. 从二级页抓去信息
   >
   > [教程](https://www.bilibili.com/video/BV1s7411p7gD/?spm_id_from=333.999.0.0&vd_source=052b07ad0190d9dabdf1d78fda0168a7)
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    > 1. sitemap name：CPC
   >    > 2. Start URL 1：http://cpc.people.com.cn/GB/64093/64387/index1.html
   >
   > 2. 创建**一级页翻页**的选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为Page_Navigation
   >    > 2. 选择器类型：Type设为Link
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select ->  先选择一个底部导航【1】，再选一个底部导航【2】 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Link type：默认Link (read from href attribute)
   >    >
   >    > 6. Parent Selectors：按住Shift选中 _root 和 Page_Navigation
   >
   > 3. 创建**从一级页入口进入二级页**的选择器
   >
   >    > 在_root 下，Add new selector
   >    >
   >    > 1. 选择器名称：Id设为Item_to_Detail
   >    > 2. 选择器类型：Type设为Link
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择一个可点击的文章标题，再选一个文章标题 -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Link type：默认Link (read from href attribute)
   >    > 6. Parent Selectors：按住Shift选中 _root 和 Page_Navigation
   >
   > 4. 随便点击一个文章链接进入二级页
   >
   > 5. 点击进入Item_to_Detail选择器
   >
   > 6. 创建**抓取二级页信息**的选择器
   >
   >    > 在_root / Item_to_Detail下，Add new selector创建1个**标题**选择器
   >    >
   >    > 1. 选择器名称：Id设为Item_Title
   >    > 2. 选择器类型：Type设为Text
   >    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 然后想法元素中的标题  -> 点击Done selecting 完成选择
   >    > 4. 勾选Multiple
   >    > 5. Regex：默认为空
   >    > 6. Parent Selectors：选择Item_to_Detail
   >
   >    > 同上，建立1个**发布时间**选择器，1个**内容**选择器
   >
   > 7. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309272152585.png)

6. 抓取B站个人空间

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

7. 抓取李笑来微博的全部内容

   > 分析：微博网页的结构有点特殊，不知道怎么抓

8. 抓取[留学人才网](http://www.liuxuehr.com/)的文章

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



#### 其他案例

> 原始需求：抓取「豆瓣读书榜」所有书的标题、短评数、短片链接
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
>    > 1. 选择器名称：Id设为All_Items_to_Detail
>    > 2. 选择器类型：Type设为Link，可以拿到目标元素的文字和链接（因为所有待抓取的信息都是去二级页拿，这里只是个入口）
>    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 先选择要一个可点击的书名，再选一个书名 -> 点击Done selecting 完成选择
>    > 4. 勾选Multiple
>    > 5. Link type：默认Link(read from href attribute)
>
> 3. 为父选择器创建子选择器，用子选择器承载二级页内容
>
>    > 点击任意一个一级页的书名链接进入二级页
>
>    > 点击进入All_Items_to_Detail选择器
>
>    > 在_root / All_Items_to_Detail下，Add new selector创建1个**书名**选择器
>    >
>    > 1. 选择器名称：Id设为Title
>    > 2. 选择器类型：Type设为text
>    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择作品中的标题 -> 点击Done selecting 完成选择
>
>    > 在_root / All_Items_to_Detail下，Add new selector创建1个**短评数**选择器
>    >
>    > 1. 选择器名称：Id设为Item_ShortComments
>    > 2. 选择器类型：Type设为Text
>    > 3. 选择器选择待抓取的元素：Selector 点击Select -> 然后短评数量  -> 点击Done selecting 完成选择
>
>    > 在_root / All_Items_to_Detail下，Add new selector创建1个**短评数链接**选择器
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