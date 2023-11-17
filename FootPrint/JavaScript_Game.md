#### JavaScript游戏

1. 元素移动

   > 1. 预备控件：开关按钮 node_btn、要移动的元素 node_div
   > 2. 页面加载监听事件：在页面加载时完成初始化，即获取node_btn，node_div
   > 3. 点击事件：点击 node_btn 时触发一个定时器 my_timer
   > 4. 定时器事件：每0.5秒给 node_div 增加1个 step 的长度

   ```html
   <style>
       * {
           margin: 0px;
           padding: 0px
       }
   
       #node_div {
           width: 100px;
           height: 100px;
           background-color: red;
           position: absolute;
           left: Opx;
           top: 100px
       }
   </style>
   
   <button id="node_btn">start</button>
   <div id='node_div'></div>
   
   <script>
       // 在页面 DOM 加载完成后执行的代码
       document.addEventListener('DOMContentLoaded', () => {
           let node_btn = document.querySelector('[id="node_btn"]');
           let node_div = document.querySelector('[id="node_div"]');
           let step = 50;
           let my_timer = null;
           node_btn.addEventListener('click', () => {
               // 清除上一个计时器事件，防止计时器叠加
               clearInterval(my_timer)
               // 定一个计时器事件，每0.5秒执行1次
               my_timer = setInterval(() => {
                   // 若当前左边距离窗口的距离 >= 目标位，说明到站了，结束计时器事件
                   if (node_div.style.left >= window.innerWidth) {
                       clearInterval(my_timer)
                   } else {
                       // 模拟运动：node_div的左边框增加一个step的长度
                       node_div.style.left = node_div.offsetLeft + step + 'px';
                   }
               }, 500)
           })
       });
   </script>
   ```

   > * `node_div.style.left`：`node_div` 左边距离窗口的距离，值是个字符串，如100px，可读可写，用于改变node_div的的位置
   > * `node_div.offsetLeft`：`node_div` 左边距离窗口的距离，值是个数字，如100，可读不可写，用于获取node_div的位置

2. 元素淡入淡出

   > 1. 预备控件：要移动的元素 node_div
   > 2. 页面加载监听事件：在页面加载时完成初始化，即获取 node_div
   > 3. 鼠标移入/移出事件：鼠标移入/移出时调用 move 函数
   > 4. move 函数：判断鼠标是移入还是移出，移入则目标位在右侧，step为正，移出则反之
   > 5. 定时器事件：每0.1秒给 node_div 增加1个 step 的长度

   ```html
   <style>
       #node_div {
           width: 100px;
           height: 200px;
           background-color: gray;
           position: absolute;
           left: -100px;
           top: 400px;
       }
   
       #node_div span {
           width: 20px;
           height: 60px;
           background-color: orange;
           position: absolute;
           left: 100px;
           top: 70px;
           line-height: 20px
       }
   </style>
   
   <div id='node_div'> <span>分享到</span></div>
   
   <script>
       // 在页面 DOM 加载完成后执行的代码
       document.addEventListener('DOMContentLoaded', () => {
           let node_div = document.querySelector('[id="node_div"]');
           let my_timer = null;
   
           // 鼠标移入时淡入
           node_div.addEventListener('mouseover', () => {
               move(0)
           })
           // 鼠标移入时淡出
           node_div.addEventListener('mouseout', () => {
               move(-node_div.offsetWidth)
           })
   
           function move(Target) {
               // 清除上一个计时器事件，防止计时器叠加
               clearInterval(my_timer)
               let step = 20;
               // 若当前左边距离窗口的距离 > 目标位，说明目标位在左侧，步长要设为负值
               if (parseInt(node_div.style.left) > Target) {
                   step = -step;
               }
               // 定一个计时器事件，每0.5秒执行1次
               my_timer = setInterval(() => {
                   // 若当前左边距离窗口的距离 = 目标位，说明到站了，结束计时器事件
                   if (parseInt(node_div.style.left) === Target) {
                       clearInterval(my_timer)
                   } else {
                       // 模拟运动：node_div的左边框增加一个step的长度
                       node_div.style.left = node_div.offsetLeft + step + 'px';
                   }
               }, 100)
           }
       });
   </script>
   ```
   
   