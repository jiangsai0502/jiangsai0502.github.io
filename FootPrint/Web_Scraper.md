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
   > >    >2. Start URL 1：https://www.zhihu.com/question/624137344
   > >
   > > 2. 创建一级页**滚动加载**的选择器
   > >
   > >    > 在_root下，Add new selector
   > >    >
   > >    > 1. Id：选择器名称，设为Items_Preview
   > >    > 2. Type：选择器类型，设为Element scroll down，为实现向下滚动加载更多内容
   > >    > 3. Selector：待抓取的元素，点击Select -> 先选择要一整个答案块，再选一个答案块（此时所有答案块都会被选中，都变成红色） -> 点击Done selecting
   > >    > 4. Multiple：勾选
   > >    > 5. ~~Element limit：滚动加载块的上限，默认500，应对有些可以无限滚动的网站，这里的值可以改小，不要改大，否则等待时间超长，电脑也会卡死~~
   > >    > 6. ~~Delay (ms)：选择器等待时间，默认2000ms~~
   > >    > 7. Parent Selectors：选择_root
   > >
   > > 3. 点击进入Items_Preview选择器
   > >
   > > 4. 创建**抓取一级页元素**的选择器
   > >
   > >    1. 「答主昵称」选择器
   > >
   > >       > 在_root / Items_Preview下，Add new selector
   > >       >
   > >       > 1. Id：选择器名称，设为Items_Name
   > >       > 2. Type：选择器类型，设为text
   > >       > 3. Selector：待抓取的元素，点击Select -> 选择答案块中的昵称（由于一个Element只有一个昵称，所以选一个即可） -> 点击Done selecting
   > >       > 4. Multiple：不勾选
   > >       > 5. ~~Regex：默认为空~~
   > >       > 6. Parent Selectors：选择Items_Preview
   > >
   > >    2. 「答题时间」「答案内容」选择器，同上
   > >
   > >    3. 「配图」选择器
   > >
   > >       > 在_root / Items_Preview下，Add new selector
   > >       >
   > >       > 1. Id：选择器名称，设为Items_Image
   > >       > 2. Type：选择器类型，设为Image
   > >       > 3. Selector：待抓取的元素，点击Select -> 先选择答案块中的一个配图，再选择一个配图（由于一个Element可能有多个配图，所以多选） -> 点击Done selecting
   > >       > 4. Multiple：勾选
   > >       > 5. ~~Regex：默认为空~~
   > >       > 6. Parent Selectors：选择Items_Load
   > >
   > > 5. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309301507310.png)
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309272329730.png)

2. 滚动加载 + 爬取一级页信息&二级页信息

   > 原始需求：抓取「知乎搜索答案」所有搜索结果的「问题标题」「搜索结果预览答案赞同数」「搜索结果预览答案评论数」「问题关注者」「问题浏览量」
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
   >    > 1. sitemap name：ZHScrollPage2
   >    > 2. Start URL 1：https://www.zhihu.com/search?q=%E6%91%A9%E6%89%98%E8%BD%A6%E4%BF%AE%E7%90%86%E4%B8%8E%E7%A6%85
   >
   > 2. 创建一级页**滚动加载**的选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Items_Preview
   >    > 2. Type：选择器类型，设为Element scroll down，为实现向下滚动加载更多内容
   >    > 3. Selector：待抓取的元素，点击Select -> 先选择要一整个答案块，再选一个答案块（此时所有答案块都会被选中，都变成红色） -> 点击Done selecting
   >    > 4. Multiple：勾选
   >    > 5. ~~Element limit：滚动加载块的上限，默认500，应对有些可以无限滚动的网站，这里的值可以改小，不要改大，否则等待时间超长，电脑也会卡死~~
   >    > 6. ~~Delay (ms)：选择器等待时间，默认2000ms~~
   >    > 7. Parent Selectors：选择_root
   >
   > 3. 点击进入Items_Preview选择器
   >
   > 4. 创建**抓取一级页元素**选择器
   >
   >    1. 「问题标题」
   >
   >       > 在_root / Items_Preview 下，Add new selector
   >       >
   >       > 1. Id：选择器名称，设为Item_Question
   >       > 2. Type：选择器类型，设为Text
   >       > 3. Selector：待抓取的元素，点击Select -> 点击首个元素的作品标题  -> 点击Done selecting
   >       > 4. Multiple：不勾选
   >       > 5. ~~Regex：默认为空~~
   >       > 6. Parent Selectors：选择Items_Preview
   >
   >    2. 「搜索结果预览答案赞同数」「搜索结果预览答案评论数」同上
   >
   > 5. 创建**一级页入口跳转二级页**选择器
   >
   >    > 在_root / Items_Preview 下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Preview_to_Detail
   >    > 2. Type：选择器类型，设为Link
   >    > 3. Selector：待抓取的元素，点击Select -> 先选择一个可点击的搜索结果标题，再选一个搜索结果标题 -> 点击Done selecting
   >    > 4. Multiple：不勾选
   >    > 5. ~~Link type：默认Link (read from href attribute)~~
   >    > 6. Parent Selectors：选择 Items_Preview
   >
   > 6. 随便点击一个搜索结果链接进入二级页
   >
   > 7. 点击进入Item_to_Detail选择器
   >
   > 8. 创建**抓取二级页元素**选择器
   >
   >    1. 「问题关注者」
   >
   >       > 在_root / Items_Preview下，Add new selector
   >       >
   >       > 1. 选择器名称：Id设为Item_Follower
   >       > 2. 选择器类型：Type设为text
   >       > 3. 选择器选择待抓取的元素：Selector 点击Select -> 选择搜索结果条目的标题 -> 点击Done selecting 
   >       > 4. Multiple：不勾选
   >       > 5. ~~Regex：默认为空~~
   >       > 6. Parent Selectors：选择Item_to_Detail
   >
   >    2. 「问题浏览量」，同上
   >
   > 9. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309301515212.png)
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309292029848.png)

3. 网址规律递增 + 爬取一级页信息&二级页信息

   > 原始需求：抓取「B站个人空间」的所有投稿中的「作品标题」「观看量」「点赞量」「投币量」「收藏量」
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309292044950.png)
   >
   > 需求分析：【一级页】网址递增，从【一级页】获取信息
   >
   > 实现
   >
   > 1. 创建1个爬虫项目：Create new sitemap
   >
   >    > 1. sitemap name：BLSiteRise
   >    >
   >    > 2. Start URL 1：https://space.bilibili.com/107861587/video?pn=[1-14:1]
   >    >
   >    >    1. [1-14:1]表示从1递增到14，步长为1，分别是1、2、3……12、13、14
   >    >    2. 豆瓣读书的步长是25：https://book.douban.com/top250?start=[0-100:25]，分别是0、25、50、75、100
   >    >
   >    >    > 不知为何Web Scraper是倒着遍历，从最后一页的最后一个item往前
   >
   > 2. 创建一级页的**内容块**选择器
   >
   >    > 在_root下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Items_Preview
   >    > 2. Type：选择器类型，设为Element
   >    > 3. Selector：待抓取的元素，点击Select -> 先选择一个想法元素，再选一个想法元素 -> 点击Done selecting 
   >    > 4. Multiple：勾选
   >    > 5. Parent Selectors：选择 _root
   >
   > 3. 点击进入Items_Preview选择器
   >
   > 4. 创建**抓取一级页信息**的选择器
   >
   >    1. 「作品标题」
   >
   >       > 在_root / Items_Preview下，Add new selector创建1个
   >       >
   >       > 1. Id：选择器名称，设为Item_Title
   >       > 2. Type：选择器类型，设为Text
   >       > 3. Selector：待抓取的元素，点击Select -> 点击作品标题  -> 点击Done selecting
   >       > 4. Multiple：不勾选
   >       > 5. ~~Regex：默认为空~~
   >       > 6. Parent Selectors：选择Items_Preview
   >
   >    2. 「观看量」，同上
   >
   > 5. 创建**一级页入口跳转二级页**选择器
   >
   >    > 在_root / Items_Preview 下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Preview_to_Detail
   >    > 2. Type：选择器类型，设为Link
   >    > 3. Selector：待抓取的元素，点击Select -> 点击可点击的作品标题/缩略图  -> 点击Done selecting
   >    > 4. Multiple：不勾选
   >    > 5. ~~Link type：Link (read from href attribute)~~
   >    > 6. Parent Selectors：选择Items_Preview
   >
   > 6. 随便点击一个作品链接进入二级页
   >
   > 7. 点击进入Preview_to_Detail选择器
   >
   > 8. 创建**抓取二级页元素**选择器
   >
   >    1. 「点赞量」
   >
   >       >在_root / Items_Preview / Preview_to_Detail下，Add new selector
   >       >
   >       >1. Id：选择器名称，设为Item_Thumb
   >       >2. Type：选择器类型，设为Text
   >       >3. Selector：待抓取的元素，点击Select -> 点击点赞量  -> 点击Done selecting
   >       >4. Multiple：不勾选
   >       >5. ~~Regex：默认为空~~
   >       >6. Parent Selectors：选择Preview_to_Detail
   >
   >    2. 「投币量」「收藏量」选择器，同上
   >
   > 9. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309301542167.png)
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309292140739.png)

4. 分页导航 + 爬取一级页信息&二级页信息

   > 原始需求：抓取「B站个人空间」的所有投稿中的「作品标题」「观看量」「点赞量」「投币量」「收藏量」
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309282212373.png)
   >
   > 需求分析：【一级页】底部分页导航，从【一级页】获取信息
   >
   > 方法一
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
   > 5. 创建**一级页入口跳转二级页**选择器
   >
   >    > 在_root / Items_Preview 下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Preview_to_Detail
   >    > 2. Type：选择器类型，设为Link
   >    > 3. Selector：待抓取的元素，点击Select -> 点击可点击的作品标题/缩略图  -> 点击Done selecting
   >    > 4. Multiple：不勾选
   >    > 5. ~~Link type：Link (read from href attribute)~~
   >    > 6. Parent Selectors：选择Items_Preview
   >
   > 6. 随便点击一个作品链接进入二级页
   >
   > 7. 点击进入Preview_to_Detail选择器
   >
   > 8. 创建**抓取二级页元素**选择器
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
   >    2. 「投币量」「收藏量」选择器，同上
   >
   > 9. 运行并实时预览
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309301546436.png)
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309291016643.png)
   >
   > 方法二
   >
   > 1. 不常用：[教程](https://www.bilibili.com/video/BV1s7411p7gD)

5. 元素属性值

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
   > 2. 创建**抓取一级页元素**选择器
   >
   >    > 在_root 下，Add new selector
   >    >
   >    > 1. Id：选择器名称，设为Item_Link
   >    > 2. Type：选择器类型，设为Element attribute
   >    > 3. Selector：待抓取的元素，点击Select -> 先选择一个作品标题，再选一个作品标题  -> 点击Done selecting
   >    > 4. Multiple：勾选
   >    > 5. Attribute name：href（这里会根据第3步选择的元素所包含的哪些属性而定）
   >    > 6. Parent Selectors：选择_root
   >
   > 3. 运行并实时预览

6. 