1. 自制带书名号的问答题模板

   >正面
   >
   >```css
   >{{Front}}
   ><br><br>
   ><div style='font-family: Arial; font-size: 12px;float:left;color:#D3D3D3'>《{{《》}}》
   ></div>
   >```
   >
   >背面
   >
   >```css
   >{{FrontSide}}
   ><br>
   ><hr>
   >{{Back}}
   >```
   >
   >样式
   >
   >```css
   >.card {
   >font-family: arial;
   >font-size: 20px;
   >text-align: left;
   >color: black;
   >background-color: white;
   >}
   >
   >.kbd {
   > box-shadow: inset 0px 1px 0px 0px #ffffff;
   > background: -webkit-gradient(linear, left top, left bottom, color-stop(0.05, #f9f9f9)stop(1, #e9e9e9) );
   > background-color: #f9f9f9;
   > border-radius: 5px;
   > border: 1px solid #dcdcdc;
   > display: inline-block;
   > font-size: 0.8em;
   > height: 30px;
   > line-height: 30px;
   > padding: 0px 10px;
   > text-align: center;
   > text-shadow: 1px 1px 0px #ffffff;
   >}
   >```

2. 自制带书名号的填空题模版

   >正面
   >
   >```css
   >{{cloze:Question}}
   ><br>
   ><div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
   ></div>
   >```
   >
   >背面
   >
   >```css
   >{{cloze:Question}}
   ><br>
   ><div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
   ></div>
   >```
   >
   >样式
   >
   >```css
   >.card {
   >font-family: arial;
   >font-size: 20px;
   >text-align: left;
   >color: black;
   >background-color: white;
   >}
   >
   >.cloze {
   >font-weight: bold;
   >color: red;
   >}
   >```

3. 自制带书名号的浏览题模板

   > 正面
   >
   > ```
   > {{Text}}
   > <br>
   > <br>
   > <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
   > </div>
   > ```
   >
   > 背面
   >
   > ```
   > {{FrontSide}}
   > ```
   >
   > 样式
   >
   > ```
   > .card {
   > font-family: arial;
   > font-size: 20px;
   > text-align: left;
   > color: black;
   > background-color: white;
   > }

4. 自制高级阅读/填空题（加粗挖空）

   > 正面
   >
   > ```css
   > <meta content="initial-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport" />
   > 
   > <div class=bg>
   >     <div class=bg2>
   > 
   >         {{#Sai填空题}}
   >         <div style="margin:16px 0 0 0"></div>
   >         <div id="div2" style="display:block">
   >             <div id="blank" class="section2">
   >                 <div id="secstem" onclick="blockk">
   >                     <div class="mbooks-highlight-txt">{{Sai填空题}}</div>
   >                 </div>
   >             </div>
   >         </div>
   >         {{/Sai填空题}}
   > 
   >         <script type="text/javascript">
   >             divs = document.querySelectorAll('#blank');
   >             [].forEach.call(divs, function (div) {
   >                 div.innerHTML = div.innerHTML
   >                     .replace(/(<br>)(<br>)/g, "$1<div class=\"divider\"></div>$2")
   >                     .replace(/(<div>|<br>)(#)(.*)/g, "");
   >             });
   > 
   >             function step1() {
   >                 var ele = document.getElementById("secstem");
   >                 var txt = document.getElementById("secstem").innerHTML;
   >                 txt = txt.replace(/\*\*(.+?)\*\*/g, '<y id="keyy" onclick="switchh(id)">$1<\/y>');
   >                 txt = txt.replace(/\{\{c1::/g, '<y id="keyy" onclick="switchh(id)">');
   >                 txt = txt.replace(/\}\}/g, "<\/y>");
   >                 txt = txt.replace(/<b>/g, '<y id="keyy" onclick="switchh(id)">');
   >                 txt = txt.replace(/<\/b>/g, "<\/y>");
   >                 txt = txt.replace(/<y.+?\/y>/g, "$&$&");
   >                 ele.innerHTML = txt;
   >             }
   > 
   >             step1();
   > 
   >             function setn() {
   >                 var i = 1;
   >                 while (/keyy\"/.test(document.getElementById("secstem").innerHTML)) {
   >                     idd = 'keyy' + String(i);
   >                     var txt = document.getElementById("secstem").innerHTML.replace(/keyy\"/, idd + '"');
   >                     document.getElementById("secstem").innerHTML = txt;
   > 
   >                     if (i % 2 == 0) {
   >                         document.getElementById(idd).setAttribute("class", "hidden");
   >                     } else {
   > 
   >                         document.getElementById(idd).innerHTML = document.getElementById(idd).innerHTML.replace(/<[\/]?span[^>]*>/g, "").replace(/&nbsp;/g, "_").replace(/&amp;/g, "_").replace(/&gt;/g, "_").replace(/&lt;/g, "_").replace(/[^\u4e00-\u9fa5、；，。！？：—“”（）《》【】]+?/g, "_").replace(/[\u4e00-\u9fa5、；，。！？：—“”（）《》【】]+?/g, "＿");
   >                         document.getElementById(idd).setAttribute("class", "color");
   >                     }
   >                     i++;
   >                 }
   >                 return i;
   >             }
   > 
   >             var sum = setn();
   > 
   >             function switchh(id) {
   >                 idd = id.replace(/keyy/, "");
   >                 if (Number(idd) % 2 == 1) {
   >                     idd = Number(idd) + 1;
   >                     var neww = "keyy" + String(idd);
   >                 } else {
   >                     idd = Number(idd) - 1;
   >                     var neww = "keyy" + String(idd);
   >                 }
   > 
   >                 document.getElementById(id).setAttribute("class", "hiddendelay");
   >                 window.setTimeout(
   >                     function delay() {
   >                         document.getElementById(id).setAttribute("class", "hidden");
   >                         document.getElementById(neww).setAttribute("class", "cloze");
   >                     }, 20);
   >             }
   >         </script>
   >     </div>
   > </div>
   > ```
   >
   > 背面
   >
   > ```css
   > <meta content="initial-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport" />
   > 
   > <div class=bg>
   >     <div class=bg2>
   >         <div style="margin:16px 0 0 0"></div>
   >         <div id="div2" style="display:block">
   >             <div id="blank" class="section2">
   >                 <div class="mbooks-highlight-txt">{{Sai填空题}}</div>
   >             </div>
   >         </div>
   >     </div>
   > 
   >     <br>
   >     <div style='font-family: Arial; font-size: 12px;float:left;color:#A2886D'>《{{《》}}》
   >         <br>
   >     </div>
   > </div>
   > ```
   >
   > 样式
   >
   > ```css
   > <style></style>
   > 
   > <style>
   >     .card {
   >         margin: 10px;
   >         font-family: avenir next, helvetica, arial, sans-serif;
   >         font-size: 20px;
   >         text-align: left;
   >         color: #393939;
   >         background-color: #e9ebee;
   >         line-height: 128%;
   >     }
   >     
   >     ::-webkit-scrollbar {
   >         display: none
   >     }
   >     
   >     body {
   >         transform: none !important;
   >     }
   >     
   >     .bg {
   >         z-index: -1;
   >         background-image: url(_bg_texture.png);
   >         background-attachment: fixed;
   >         position: fixed;
   >         top: 0px;
   >         left: 0px;
   >         bottom: 0px;
   >         right: 0px;
   >         width: 100%;
   >         height: 100%;
   >         overflow-y: scroll;
   >         -webkit-overflow-scrolling: touch;
   >     }
   >     
   >     .bg::-webkit-scrollbar {
   >         display: none;
   >     }
   >     
   >     .bg2 {
   >         margin: 0.6em 0.65em
   >     }
   >     
   >     .ipad .bg2 {
   >         margin: 0.6em 0.65em
   >     }
   >     
   >     .android .bg2 {
   >         margin: 0.6em 0.5em
   >     }
   >     
   >     .hide {
   >         color: #fff;
   >     }
   >     
   >     .nightMode .hide {
   >         color: #222;
   >     }
   >     
   >     .hidden {
   >         display: none
   >     }
   >     
   >     #question span {
   >         display: inline-block
   >     }
   >     /* --------- 字体样式 --------- */
   >     
   >     b {
   >         /* --- 背面挖空颜色 --- */
   >         color: #D8B0B0;
   >         font-weight: normal;
   >         text-decoration: underline;
   >         margin: 0 2px;
   >         font-family: avenir next, kt;
   >         font-size: 1.05em;
   >     }
   >     
   >     .cloze {
   >         /* --- 正面挖空文字颜色 --- */
   >         color: #D8B0B0;
   >         font-size: 1.05em;
   >         margin: 0 2px;
   >         text-decoration: underline;
   >         font-family: avenir next, kt;
   >     }
   >     
   >     .color {
   >         /* --- 正面挖空横线颜色 --- */
   >         color: #D8B0B0;
   >         font-size: 1.05em;
   >         text-decoration: underline;
   >         margin: 0 2px;
   >         font-family: avenir next, kt;
   >         display: inline;
   >         -webkit-animation-name: fadeinn;
   >         -webkit-animation-duration: 0.03s;
   >         -webkit-animation-timing-fuction: linear;
   >     }
   >     
   >     .hiddendelay {
   >         color: #338eca;
   >         font-size: 1.05em;
   >         text-decoration: underline;
   >         margin: 0 2px;
   >         font-family: avenir next, kt;
   >         -webkit-animation-name: fadeoutt;
   >         -webkit-animation-duration: 0.03s;
   >         -webkit-animation-timing-fuction: linear;
   >     }
   >     
   >     .br {
   >         display: block;
   >         content: "";
   >         border-bottom: 0.6em solid transparent
   >     }
   >     
   >     .divider {
   >         margin: 5px -6px;
   >         height: 2px;
   >         background-color: #ececec
   >     }
   >     
   >     a:link {
   >         color: #007aff
   >     }
   >     
   >     th,
   >     tr,
   >     td {
   >         border-collapse: collapse;
   >         border: 1px solid #808080;
   >     }
   >     
   >     #typeans {
   >         font-size: 0.85em !important
   >     }
   >     
   >     .ios #typeans {
   >         font-size: 1em !important
   >     }
   >     
   >     @font-face {
   >         font-family: kt;
   >         src: url('_kt.ttf');
   >     }
   >     
   >     @font-face {
   >         font-family: times;
   >         src: url('_times.ttf');
   >     }
   >     /* --------- 主体部分 --------- */
   >     
   >     .mbooks-highlight-txt {
   >         margin: 8px 12px 7px;
   >         display: block;
   >         font-size: 0.9em;
   >         line-height: 165%;
   >         text-align: left;
   >     }
   >     
   >     .win .section-type {
   >         display: block
   >     }
   >     
   >     .mac .section-type {
   >         display: block
   >     }
   >     
   >     .section2 {
   >         border: 1px solid;
   >         border-color: #fff;
   >         border-radius: 5px;
   >         background-color: rgba(255, 255, 255, 0.85);
   >         margin: 5px 0;
   >         padding: 10px 12px;
   >         line-height: 100%;
   >         max-width: 828px;
   >         margin: 0 auto;
   >         box-shadow: #b7d5eb 2px 2px 5px 1px;
   >         word-break: break-word;
   >     }
   > ```

5. 

