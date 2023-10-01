##### 虚拟环境检查、配置，使用

1. 查看当前系统下的虚拟环境，安装路径
	`conda info --envs`
2. 创建名为 py3 的python3的虚拟环境
	`conda create -n py3 python=3.10`
3. 激活虚拟环境py3
	`conda activate py3`
4. py3中Python的位置
	`which python`

##### Playwright安装、配置，使用

1. 为当前的虚拟环境安装playwright包

	> 坑：[conda虚拟环境使用pip慎重](https://www.cnblogs.com/zhangxingcomeon/p/13801554.html)
	>
	> 1. 查看此时要用的pip在哪个环境
	>
	>    `which -a pip`
	>
	>    >base环境的pip：可能在/root/anaconda3/bin/pip
	>    >
	>    >而其他conda环境的pip：可能在/root/anaconda3/envs/my_env/bin/pip
	>
	>    > 尽量不使用base环境的pip，用哪个环境，就用哪个环境的pip，如果切到py3环境后，`which -a pip`仍显示用的base环境的pip，则可能是py3没安装pip
	>    >
	>    > `conda install pip`
	
	`pip install playwright`

##### VScode配置，使用

4、第一个爬虫工具
5、第一个自动化操作工具：鼠标、键盘