##### 虚拟环境检查、配置，使用

1. 查看当前系统下的虚拟环境，安装路径
	
	> `conda info --envs`
2. 创建名为 py3 的python3的虚拟环境
	
	> `conda create -n py3 python=3.10`
3. 激活虚拟环境py3
	
	> `conda activate py3`
4. py3中Python的位置
	
	> `which python`

##### Playwright安装、配置，使用

1. 为当前的虚拟环境安装playwright包

  > * 查看此时要用的pip在哪个环境
  >
  >   > 详见[Python 周边环境](Sai_FootPrint/1_PythonEnvironment.md)
  >   >
  >   > `pip3 -V`
  >   >
  >   > `conda install pip3`
  >
  > * `pip3 install pytest-playwright`

2. 为playwright安装浏览器

  > `playwright install`

##### VScode配置，使用

4、第一个爬虫工具
5、第一个自动化操作工具：鼠标、键盘