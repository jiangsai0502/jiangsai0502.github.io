#### JavaScript游戏

1. 元素匀速移动

   > 1. 预备控件：开关按钮 node_btn、要移动的元素 node_div、目标位置 target、步长 step
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
           width: 30px;
           height: 30px;
           background-color: red;
           position: absolute;
           left: Opx;
           top: 100px
       }
   </style>
   
   <button id="node_btn">start</button>
   <div id='node_div'></div>
   <span style='width: 1px; height: 500px; background-color: black; position: absolute; left: 500px;'></span>
   <script>
       // 在页面 DOM 加载完成后执行的代码
       document.addEventListener('DOMContentLoaded', () => {
           let node_btn = document.querySelector('[id="node_btn"]');
             let node_div = document.querySelector('[id="node_div"]');
             let target = 470;
             let step = 40;
             let my_timer = null;
             // 点击node_btn时执行函数
             node_btn.addEventListener('click', () => {
                 // 清除上一个计时器事件，防止计时器叠加
                 clearInterval(my_timer)
                 // 定一个计时器事件，每0.5秒执行1次
                 my_timer = setInterval(() => {
                     // 距离目标的距离 = 目标纵坐标 - 方框的左边框的纵坐标
                     let distance = target - node_div.offsetLeft;
                     // 若距离目标的距离<=0时，说明到站了，结束计时器事件
                     if (distance <= 0) {
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

   > * `node_div.style.left`：元素的左外边距边缘到其父元素的左内边距边缘的距离，用于修改`node_div` 的位置，值是个字符串，如100px
   > * `node_div.offsetLeft`：元素的左外边距边缘到其父元素的左内边距边缘的距离，用于读取`node_div` 的位置，值是个数字，如100

2. 元素减速移动 - 左右钟摆运动

   > 1. 预备控件：开关按钮 node_btn、要移动的元素 node_div、目标位置 target、步长 step
   > 2. 页面加载监听事件：在页面加载时完成初始化，即获取node_btn，node_div
   > 3. 点击事件：点击 node_btn 时触发一个定时器 my_timer
   > 4. 定时器事件：动态计算与目标位置的距离 distance 和步长 step、每0.01秒给 node_div 增加1个 step 的长度

   ```html
   <style>
       * {
           margin: 0px;
           padding: 0px
       }
   
       #node_div {
           width: 30px;
           height: 30px;
           background-color: red;
           position: absolute;
           left: Opx;
           top: 100px
       }
   </style>
   
   <button id="node_btn">start</button>
   <div id='node_div'></div>
   <span style='width: 1px; height: 500px; background-color: black; position: absolute; left: 500px;'></span>
   <script>
       // 在页面 DOM 加载完成后执行的代码
       document.addEventListener('DOMContentLoaded', () => {
           let node_btn = document.querySelector('[id="node_btn"]');
           let node_div = document.querySelector('[id="node_div"]');
           let target = 470;
           let my_timer = null;
           // 点击node_btn时执行函数
           node_btn.addEventListener('click', () => {
               // 清除上一个计时器事件，防止计时器叠加
               clearInterval(my_timer)
               // 定一个计时器事件，每0.01秒执行1次
               my_timer = setInterval(() => {
                   // 方框的左边框的纵坐标
                   div_left = node_div.offsetLeft;
                   // 距离目标的距离 = 目标纵坐标 - 方框的左边框的纵坐标
                   let distance = target - div_left;
                   // 步长 = 距离目标的距离/50
                   let step = distance / 50;
                   // 计算机只能识别1px，小于1px都会被视为0px，程序会一直执行下去，故向上取整
                   step = step > 0 ? Math.ceil(step) : Math.floor(step)
                   // 到达目标时切换目标位置
                   // 若目标在右侧，且距离目标的距离<=0，则说明到达；若目标在左侧，且距离目标的距离>=0，则说明到达
                   if ((target === 470 && distance <= 0) || (target === 0 && distance >= 0)) {
                       target = target === 0 ? 470 : 0
                   }
                   // 模拟运动：方框的左边框的纵坐标走一步
                   node_div.style.left = div_left + step + 'px';
               }, 10)
           })
       });
   </script>
   ```

3. 元素淡入淡出

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

   