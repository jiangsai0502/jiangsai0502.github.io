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

4. 阻止CSDN和360doc的弹窗

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
   > (function() {
   >     'use strict';
   >     // 查找具有指定选择器的元素
   >     var popup_csdn = document.querySelector("div.passport-login-container");
   >     var popup_360doc = document.querySelector("#registerOrLoginLayer")
   > 
   >     // 检查是否找到了元素
   >     if (popup_csdn) {
   >         // 如果找到了元素，删除它
   >         popup_csdn.remove();
   >     }
   >     if (popup_360doc) {
   >         // 如果找到了元素，删除它
   >         popup_360doc.remove();
   >     }
   > })();
   > ```

