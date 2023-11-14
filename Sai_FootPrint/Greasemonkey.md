[教程](https://blog.chrxw.com/archives/2021/02/08/1449.html)

#### Javascript初探

1. Chrome开发者工具

   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101021011.png)

2. 获取Dom

   > 1. 通过 `css` 查询
   >
   >    `JSPath_var = document.querySelector("body > div.container > div.beian-wrapper > a:nth-child(1)")`
   >
   > 2. 通过 `Xpath` 查询
   >
   >    方法1：`XPath_var= $x('/html/body/div[1]/div[3]/a[1]')[0]`
   >
   >    方法2：`XPath_var= document.evaluate('/html/body/div[1]/div[3]/a[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue`
   >
   >    > 方法1：`$x()` 是简写，仅用于Chrome - Console中调试 `XPath` 查询，注意`[0]`
   >    >
   >    > 方法2：`document.evaluate('xpath', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue` 是完整写法，用于任何场景
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101219851.png)

3. DOM的增删改查

   > > 无论通过哪种方式获取Dom，修改Dom属性的方式都一样
   > >
   > > 获取Dom节点
   > >
   > > `temp = $x('/html/body/div[1]/div[3]')[0]`
   >
   > 查询
   >
   > > 获取Dom节点文本内容
   > >
   > > `temp.textContent`
   > >
   > > > 文本包含自身的文本和所有子元素的文本，用换行符隔开
   > >
   > > `temp.innerText`
   > >
   > > > 文本包含自身的文本和所有子元素的文本，去掉了多余的换行符
   >
   > 修改
   >
   > > 修改Dom节点文本内容
   > >
   > > `temp.textContent = "Sai修改了textContent内容"`
   > >
   > > `temp.innerText = "Sai修改了innerText内容"`
   > >
   > > > 修改会替换了自身的文本内容，同时删除所有子元素
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101359845.png)
   >
   > 新增
   >
   > > 1. 尾部新增子元素
   > >
   > >    ```javascript
   > >    b1 = document.createElement('button')
   > >    b1.id = 'tail'
   > >    b1.textContent='我插在尾上'
   > >    temp.appendChild(b1)
   > >    ```
   > >
   > > 2. 任意位置新增子元素
   > >
   > >    ```javascript
   > >    b2 = document.createElement('button')
   > >    b1.id = 'head'
   > >    b2.textContent='我插在头上'
   > >    temp.insertBefore(b2,temp.children[0])
   > >    ```
   > >    
   > >    > `DOM.insertBefore( [要插入的DOM节点] , [被插队的DOM节点])`，插在`被插队的Dom节点`之前
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101409433.png)
   >
   > 删除
   >
   > > 删除某个节点
   > >
   > > `tail = $x('/html/body/div[1]/div[3]/button[2]')[0]`
   > >
   > > `tail.remove()`
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101425048.png)

4. DOM增删事件监听器

   > 增加事件监听器
   >
   > >`head = $x('/html/body/div[1]/div[3]/button')[0]`
   > >
   > >```javascript
   > >head.addEventListener('click',() => {
   > >    alert('增加响应click事件');
   > >})
   > >```
   > >
   > >`DOM.addEventListener( [事件名称] , [回调函数])`
   > >
   > >> Javascript函数的3种写法
   > >>
   > >> 1. `推荐` 匿名函数的缩略写法，见上
   > >>
   > >>    > 唯一的问题，因为匿名函数是无法被引用的，因此匿名函数声明后需要立刻执行，且将来无法删除这个时间监听器
   > >>    >
   > >>    > 若考虑到未来可能会删除该事件监听器，可使用方法3普通函数
   > >>
   > >> 2. 匿名函数的完整写法
   > >>
   > >>    ```javascript
   > >>    head.addEventListener('click',function(){
   > >>        alert('增加响应click事件');
   > >>    })
   > >>
   > >> 3. 普通函数
   > >>
   > >>    ```javascript
   > >>    head.addEventListener('click',SaiFun);
   > >>    function SaiFun(){
   > >>        alert('增加响应click事件');
   > >>    }
   >
   > 删除事件监听器
   >
   > >只能删除普通函数的事件监听器，匿名函数的事件监听器无法删除
   > >
   > >```javascript
   > >head.addEventListener('click',SaiFun);
   > >function SaiFun(){
   > >    alert('增加响应click事件');
   > >}
   > >
   > >head.removeEventListener("click", SaiFun)
   > >```

5. 模拟鼠标点击

   > `head.click()`

#### 油猴脚本初探

1. 脚本元信息

   1. 默认元信息
      * `name` ：必填；脚本名称
      * `namespace` ：选填；命名空间；类似文件夹概念；命名空间和名称都相同时会被当做同一脚本
      * `version` ：选填；版本号
      * `description` ：选填；上传到脚本商城时给别人看的
      * `author` ：选填；作者
      * `match` ：必填；在什么网址下启用该脚本
      * `icon`： 选填；脚本的图标（显示在脚本列表里）
      * `grant` ：选填；特殊权限（调用GM_开头的函数需要先申请权限）
   2. 补充元信息
      * `include`： 和@match差不多，但是支持正则表达式，我更喜欢用这个
      * `connect`： 如果脚本需要访问跨域资源，需要提前申明
      * `license`： 脚本的授权许可信息

2. 百度图标替换

   > Chrome - Console调试代码
   >
   > ```javascript
   > (function() {
   >     let temp = $x('/html/body/div[1]/div[1]/div/img')[0];
   >     temp.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrIqVq3yKn-U51uJXUzllr4Xbj-tuTkYC92yQk0LdW8xT2b99w';
   > })();
   > ```
   >
   > 油猴子代码
   >
   > ```javascript
   > // ==UserScript==
   > // @name         Sai_BaiDu图标替换
   > // @match        https://baidu.rudon.cn/*
   > // ==/UserScript==
   > 
   > (function() {
   >     'use strict';
   >     let temp = document.evaluate('/html/body/div[1]/div[1]/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   >     if (temp) {
   >         temp.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrIqVq3yKn-U51uJXUzllr4Xbj-tuTkYC92yQk0LdW8xT2b99w';
   >     }
   > })();
   > ```

3. 视频网站播放加速

   > > 使用`shift` + `↑` 、`shift` +`↓` 以0.2的步长增减播放速度
   >
   > ```javascript
   > // ==UserScript==
   > // @name         视频网站播放加速
   > // @description  Shift + ↑ 加速；Shift + ↓ 减速
   > // @match        https://www.bilibili.com/*
   > // @match        http://*/*
   > // ==/UserScript==
   > 
   > (function() {
   >     'use strict';
   >     document.addEventListener('keydown', function(e) {
   >         // 获取视频元素
   >         // var video = document.querySelector('video');
   >         let video = document.evaluate('//video', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   >         if (!video) return; // 如果没有找到视频元素则不执行后续代码
   > 
   >         // 当同时按下 shift + 上箭头键时，以0.2的步长提高播放速度
   >         if (e.shiftKey && e.code === 'ArrowUp') {
   >             video.playbackRate = Math.min(video.playbackRate + 0.2, 16); // 确保播放速度不超过16
   >         }
   > 
   >         // 当同时按下 shift + 下箭头键时，以0.2的步长降低播放速度
   >         if (e.shiftKey && e.code === 'ArrowDown') {
   >             video.playbackRate = Math.max(video.playbackRate - 0.2, 0.1); // 确保播放速度不低于0.1
   >         }
   >     });
   > })();
   > ```
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311091626966.png)
   >
   > 快捷键`control`+`f`
   >
   > ```javascript
   > (function() {
   >  'use strict';
   >  document.addEventListener('keydown', function(e) {
   >      // 当同时按下 control + 小写f 键时
   >      if (e.ctrlKey && e.key === 'f') {
   >          // 获取视频元素
   >          var video = document.querySelector('video');
   >          if (video) {
   >              // 设置播放速度为倍数
   >              video.playbackRate = 2.2;
   >          }
   >      }
   >  });
   > })();
   > ```
   >
   > 快捷键`shift`+`F`
   >
   > > 当同时按下 shift + F 时，因shift会影响大小写，故必须用大写F
   >
   > > `e.ctrlKey` 对应 `control`
   > > `e.shiftKey` 对应 `shift`
   > >
   > > `e.metaKey` 对应 `command`，一般不单独使用`command`与其他键的组合，因为`command`+其他键的常规组合太多，会冲突
   > >
   > > `e.altKey` 对应 `option`，一般不单独使用`option`与其他键的组合，因为`option`+其他键会输出特殊字符

