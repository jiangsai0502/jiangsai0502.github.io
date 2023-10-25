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
    > > 1. 美区iOS账号
    > > 2. 购买礼品卡：支付宝，淘宝
    >
    > 方式二：PayPal
    >
    > > PayPal用法
    > >
    > > 1. 关联卡：用于「消费」的扣钱的卡，可以是借记卡，可以是信用卡（招商双币信用卡）
    > > 2. 关联银行账户：用户「提现」的卡
    > >    1. 中国账户：无论哪个银行都有5W$额度限制、银行需要材料、手续费高、退回率高
    > >    2. 香港/美国账户：没有上述缺点
    >
    > 1. 美区iOS账号
    > 2. PayPal
    > 3. 