









> 1. 加载本地cookie
>    1. 若本地有cookie，则在SaiBrowser中创建一个context（网页管理器），并加载该cookie，实现免登陆；若本地没有，则在SaiBrowser中创建一个空的context
>    2. 每个context是一个独立会话，用于环境隔离，每个context可使用1套代理，登录1套账号