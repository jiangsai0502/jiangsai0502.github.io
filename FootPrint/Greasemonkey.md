[教程](https://blog.chrxw.com/archives/2021/02/08/1449.html)

#### Chrome开发者工具

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311101021011.png)

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

   * Chrome - Console调试代码

     ```js
     (function () {
         let temp = $x('/html/body/div[1]/div[1]/div/img')[0];
         temp.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrIqVq3yKn-U51uJXUzllr4Xbj-tuTkYC92yQk0LdW8xT2b99w';
     })();
     ```

   * 油猴子代码

     ```js
     // ==UserScript==
     // @name         Sai_BaiDu图标替换
     // @match        https://baidu.rudon.cn/*
     // ==/UserScript==
     
     (function () {
         'use strict';
         let temp = document.evaluate('/html/body/div[1]/div[1]/div/img', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
         if (temp) {
             temp.src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrIqVq3yKn-U51uJXUzllr4Xbj-tuTkYC92yQk0LdW8xT2b99w';
         }
     })();
     ```

3. 视频网站播放加速

   > 1. 使用`shift` + `↑` 、`shift` +`↓` 以 0.2 的步长增/减播放速度
   >
   >    > `ctrlKey` ：`Control`
   >    >
   >    > `shiftKey` ：`Shift`
   >    >
   >    > `altKey` ：`Option`
   >    >
   >    > `metaKey` ：`Command`
   >
   > 2. 播放面板也可增减速度

   ```js
   // ==UserScript==
   // @name         视频加速板
   // @namespace    http://tampermonkey.net/
   // @version      0.1
   // @description  try to take over the world!
   // @author       You
   // @match        https://www.bilibili.com/*
   // @match        https://www.youtube.com/*
   // @grant        none
   // ==/UserScript==
   
   // (function() { ... })(); 立即执行的函数表达式，用来封装所有js代码
   (function() {
       // 1、声明键盘事件监听函数：当按下Shift+箭头时，增减视频播放速度
       const keyboardListener = function(e) {
           const video = document.querySelector('video');
           // 如果没有找到视频元素则不执行后续代码
           if (!video) return;
   
           if (e.shiftKey && e.code === 'ArrowUp') {
               video.playbackRate = Math.min(video.playbackRate + 0.2, 16);
           }
           if (e.shiftKey && e.code === 'ArrowDown') {
               video.playbackRate = Math.max(video.playbackRate - 0.2, 0.1);
           }
       };
   
       // 2.1、创建浮动面板和按钮：创建一个浮动面板，包含加速、减速和恢复等按钮
       function createFloatingPanel(video) {
           // 创建并添加浮动面板
           var floatPanel = document.createElement('div');
           setPanelStyle(floatPanel);
   
           // 创建加速按钮
           var speedUpButton = createButton('加速', () => {
               video.playbackRate = Math.min(video.playbackRate + 0.2, 16);
           });
   
           // 创建减速按钮
           var slowDownButton = createButton('减速', () => {
               video.playbackRate = Math.max(video.playbackRate - 0.2, 0.1);
           });
   
           // 创建减速按钮
           var recoverButton = createButton('恢复', () => {
               video.playbackRate = 1.0;
           });
   
           // 将按钮添加到浮动面板
           floatPanel.appendChild(speedUpButton);
           floatPanel.appendChild(slowDownButton);
           floatPanel.appendChild(recoverButton);
   
           // 将浮动面板添加到页面
           document.body.appendChild(floatPanel);
       }
   
       // 2.2、设置浮动面板样式
       function setPanelStyle(panel) {
           panel.style.position = 'fixed'; // 设置定位为固定
           panel.style.top = '5px'; // 距离顶部
           panel.style.right = '5px'; // 距离右侧
           panel.style.border = 'none';  // 没有边框
           panel.style.zIndex = '9999';  // 确保在顶层
           panel.style.backgroundColor = 'white'; // 背景色为白色
           panel.style.padding = '10px'; // 内边距
           panel.style.boxShadow = '0px 0px 10px rgba(0, 0, 0, 0.5)'; // 设置阴影
           panel.style.width = '65px'; // 面板宽度
           panel.style.borderRadius = '5px';  // 面板圆角
       }
       // 2.3、创建按钮并设置样式：用于创建一个按钮，设置样式，并定义点击时的行为
       function createButton(text, onClick) {
           var button = document.createElement('button');
           button.textContent = text;
           setButtonStyle(button);
           button.onclick = onClick;
           return button;
       }
   
       // 2.4、设置按钮样式
       function setButtonStyle(button) {
           button.style.backgroundColor = 'red';  // 按钮背景色
           button.style.color = 'white';  // 按钮字体颜色
           button.style.marginBottom = '5px';  // 按钮间隔
           button.style.border = 'none';  // 删除按钮黑边
           button.style.padding = '5px 15px';  // 按钮大小
           button.style.fontSize = '16px';  // 按钮字体大小
           button.style.borderRadius = '5px';  // 按钮圆角
           button.style.boxShadow = '0 4px #999';  // 按钮凸出效果
       }
   
       // 3、声明DOM监听函数：当页面DOM变化时被调用。它会遍历所有变化，检查是否有视频元素被加载
       const DomListener = function(mutationsList, observer) {
           //  循环遍历所有DOM变化：每个 mutation 包含这次DOM变化的详细信息
           for (const mutation of mutationsList) {
               // 变化类型 'childList'：即子元素发生了添加或删除的变化
               if (mutation.type === 'childList') {
                   // 尝试新 Dom 中查找 video 元素
                   const video = document.querySelector('video');
                   if (video) {
                       // 为新 Dom 上的 video 元素创建一个面板来控制播放速度
                       createFloatingPanel(video);
                       // 为新 Dom 添加键盘事件监听器
                       document.addEventListener('keydown', keyboardListener);
                       // 停止观察，避免不必要的性能损耗，但是若变态网站在播放中更新dom，也可注释掉本句
                       observer.disconnect(); 
                   }
               }
           }
       };
   
       // 4、创建一个 MutationObserver 实例：MutationObserver实例用于观察页DOM变化，并绑定变化时的处理函数DomListener
       const observer = new MutationObserver(DomListener);
   
       // 5、开始观察DOM变化：使用 observer.observe 方法开始监视 document.body 元素，寻找任何子元素的添加或移除
       observer.observe(document.body, { childList: true, subtree: true });
   })();
   ```

   > 1. **自执行函数** (`(function() { ... })();`): 这是一个立即执行的函数表达式，用来封装代码
   > 2. **回调函数 `callback`**: 当页面的DOM（文档对象模型）发生变化时，这个函数会被调用。它遍历所有的变化，检查是否有视频元素被加载。
   > 3. **键盘事件监听函数 `keyboardListener`**: 此函数用于监听键盘事件。当用户按下Shift + 上/下箭头时，它会增加或减少视频的播放速度。
   > 4. **创建浮动面板的函数 `createFloatingPanel`**: 这个函数创建一个浮动面板，其中包含加速、减速和恢复播放速度的按钮。
   > 5. **设置面板样式的函数 `setPanelStyle`**: 用于设置浮动面板的CSS样式。
   > 6. **创建按钮的函数 `createButton`**: 用于创建一个按钮，设置其样式，并定义点击时的行为。
   > 7. **设置按钮样式的函数 `setButtonStyle`**: 定义按钮的CSS样式。
   > 8. **创建 `MutationObserver` 实例**: `MutationObserver`用于观察页面上的DOM变化，如新元素的添加。
   > 9. **开始观察DOM变化**: 使用 `observer.observe` 方法开始监视 `document.body` 元素，寻找任何子元素的添加或移除。

   补充

   > > ```js
   >> var video = document.querySelector('video');
   > > video = document.evaluate('//video', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   > > ```
   > 
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311091626966.png)
   > 
   > ```js
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
   >         let video = document.evaluate('//video', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   >         if (!video) return; // 如果没有找到视频元素则不执行后续代码
   >         // 当同时按下 shift + 上箭头键时，以0.2的步长提高播放速度
   >         if (e.shiftKey && e.code === 'ArrowUp') {
   >             // 确保播放速度不超过16
   >             video.playbackRate = Math.min(video.playbackRate + 0.2, 16); 
   >         }
   >         // 当同时按下 shift + 下箭头键时，以0.2的步长降低播放速度
   >         if (e.shiftKey && e.code === 'ArrowDown') {
   >             // 确保播放速度不低于0.1
   >            video.playbackRate = Math.max(video.playbackRate - 0.2, 0.1); 
   >         }
   >     });
   > })();
   > ```
   >
   > 快捷键`control`+`f`
   >
   > ```javascript
   >(function() {
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

4. 阻止CSDN和360doc的弹窗

   > 页面刚加载时弹窗元素还不存在，但当向下滚动到某个特定位置时，弹窗元素才会被添加到DOM中
   >
   > ```js
   > // ==UserScript==
   > // @name         阻止CSDN和360doc的弹窗
   > // @namespace    http://tampermonkey.net/
   > // @version      0.1
   > // @description  try to take over the world!
   > // @author       You
   > // @match        https://blog.csdn.net/*
   > // @match        http://www.360doc.com/*
   > // @grant        none
   > // ==/UserScript==
   > 
   > // (function() { ... })(); 立即执行的函数表达式，用来封装所有js代码
   > (function () {
   >     // 1、声明DOM监听函数：当页面DOM变化时被调用。它会遍历所有变化，检查是否有视频元素被加载
   >     const DomListener = function (mutationsList, observer) {
   >         //  循环遍历所有DOM变化：每个 mutation 包含这次DOM变化的详细信息
   >         for (const mutation of mutationsList) {
   >             // 变化类型 'childList'：即子元素发生了添加或删除的变化
   >             if (mutation.type === 'childList') {
   >                 // 在新 Dom 中查找指定选择器的元素
   >                 let popup_csdn = document.querySelector("div.passport-login-container");
   >                 let popup_360doc = document.querySelector("#registerOrLoginLayer")
   >                 if (popup_csdn) {
   >                     // 移除新 Dom 上的 popup 元素
   >                     popup_csdn.remove();
   >                     // 停止观察，避免不必要的性能损耗，但是若变态网站在播放中更新dom，也可注释掉本句
   >                     observer.disconnect();
   >                 }
   >                 if (popup_360doc) {
   >                     // 移除新 Dom 上的 popup 元素
   >                     popup_360doc.remove();
   >                     // 停止观察，避免不必要的性能损耗，但是若变态网站在播放中更新dom，也可注释掉本句
   >                     observer.disconnect();
   >                 }
   >             }
   >         }
   >     };
   > 
   >     // 2、创建一个 MutationObserver 实例：MutationObserver实例用于观察页DOM变化，并绑定变化时的处理函数DomListener
   >     const observer = new MutationObserver(DomListener);
   > 
   >     // 3、开始观察DOM变化：使用 observer.observe 方法开始监视 document.body 元素，寻找任何子元素的添加或移除
   >     observer.observe(document.body, { childList: true, subtree: true });
   > })();
   > ```

5. 页面自动滚动

   > Option + ↓ 每0.5秒滚动1屏；Esc 键停止滚动

   ```js
   // ==UserScript==
   // @name         页面自动滚动
   // @namespace    http://tampermonkey.net/
   // @version      0.1
   // @description  Option + ↓ 每0.5秒滚动1屏
   // @author       You
   // @match        https://www.zhihu.com/*
   // @icon         https://www.google.com/s2/favicons?sz=64&domain=zhihu.com
   // @grant        none
   // ==/UserScript==
   
   
   (function() {
       'use strict';
   
       let scrollInterval = null;
   
       function startAutoScroll() { // 开始滚动
           scrollInterval = setInterval(function() {
               window.scrollBy(0, window.innerHeight);
           }, 500);
       }
   
       function stopAutoScroll() { // 停止滚动
           clearInterval(scrollInterval);
       }
   
       document.addEventListener('keydown', function(e) {
           if (e.altKey && e.keyCode === 40) { // 检测是否按下了 Shift + ↓
               startAutoScroll();
               console.log('Auto scrolling started. Press ESC to stop.');
           }
           if (e.keyCode === 27) { // 检测是否按下了 ESC
               stopAutoScroll();
               console.log('Auto scrolling stopped.');
           }
       });
   })();
   ```

   
