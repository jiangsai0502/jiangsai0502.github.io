#### Mac使用技巧

1. Terminal中断、还原、杀死Python程序

    > * Control + z：暂停进程，并将至放入后台
    >
    >     ```
    >     [1]  + 74136 suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * Control + c：杀死进程，并将至放入后台
    >
    >     ```bash
    >     KeyboardInterrupt
    >     Future exception was never retrieved
    >     future: <Future finished exception=Error('Connection closed')>
    >     playwright._impl._api_types.Error: Connection closed
    >     ```
    >
    > * jobs：查看当前暂停的进程
    >
    >     ```bash
    >     [1]  - suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     [2]  + suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * fg %N：使进程[N]在前台进行
    >
    >     ```bash
    >     [1]  + 74845 continued  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * kill %N：杀掉后台暂停的进程[N]（最前面的数字）
    >
    >     ```bash
    >     [1]  + 73282 terminated  /Users/jiangsai/anaconda3/envs/py3/bin/python  
    >     ```
    >

1. 购买ChatGPT4

    > 方式一：[按次购买，每次买一个月](https://www.youtube.com/watch?v=kkl2YPO33qc)
    >
    > > 1. 注册Apple美国免税洲账号
    > > 2. 办理招商双币信用卡
    > > 3. Apple官网使用信用卡购买礼品卡，送给自己的美区Apple账号
    > > 4. ChatGPT iOS端内购时自动扣礼品卡金额
    >

1. Typora打印PDF格式设置

    > 1. 页边距
    >
    >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261112999.png)
    >
    > 2. [行距](https://www.twblogs.net/a/5db288f8bd9eee310d9fd66c/?lang=zh-cn)
    >
    >    > 1. 微调`body`中的`line-height`参数
    >    > 2. 关闭文件重新打开，修改即可生效
    >    >
    >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261109296.png)