# Git学习

#### 初次使用Git的配置

> Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址

1. 配置用户名  `git config --global user.name 'will'`

2. 配置邮箱  `git config --global user.email 'jiangsai0502@163.com'`

4. 查看配置  `git config --list`



### Git 基本概念

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200129060459.png)

* **工作区 Workspace**

  > 工作区是本地能看到的目录，平时修改代码和文件的地方

  * 将变更的文件提交到暂存区  `git add .`
  * 将远程仓库的数据拉到当前分支并合并  `git pull`
  * 切换分支  `git checkout [branch-name]`

* **暂存区 Index**

  > 暂存区是用  `git init`  初始化工作区**时产生的一个叫 `index` 文件（.git/index），该文件存储的是即将提交到Git仓库的代码变更信息

  * 将变更的文件提交到 Git 仓库的当前分支  `git commit -m '提交说明'`

* **Git 仓库 Repository**

  > 是用  `git init`  命令**初始化工作区**时产生的一个叫 `.git` 的文件夹，存放所有提交过的代码，Head指针指向的是最终提交的版本

  * 将 Git 仓库的 `master`  /   `sai_branch` 分支提交到本地名为 `githubtestgit` 的远程仓库 

    `git push githubtestgit master`

    `git push githubtestgit sai_branch`

  * 将远程仓库的  `githubtestgit.git`  仓库 clone 到本地，只有  `master`  分支

    `git clone git@github.com:jiangsai0502/githubtestgit.git`

* **远程仓库 Remote**

  > github 网站提供的仓库



| Git的工作流程                                       | Git管理的文件的状态                                          |
| --------------------------------------------------- | ------------------------------------------------------------ |
| 在**工作区 Workspace**中增删改文件                  | **已修改**的状态是 **Modified**                              |
| 将文件放入**暂存区 Index**                          | **已暂存**，即执行 `git add .` 之后的状态是 **Staged**       |
| 将**暂存区 Index**文件提交到**Git 仓库 Repository** | **已提交**，即执行 `git commit -m "提交说明"` 之后的状态是 **Committed** |



### Git 全流程

1. 创建一个 Git 本地目录  `mkdir ~/Documents/testGit && cd ~/Documents/testGit`

2. 初始化一个空仓库  `git init`

   > 1. testGit 目录下生成一个 `.git` 目录，即 **Git 仓库**，用于 Git 来管理 testGit 目录下所有文件的版本迭代
   > 2. `.git` 目录下的 `index` 文件就是**暂存区 stage (Index)**

3. 创建一个项目说明文档  `touch README.md && vi README.md`

4. 增删改文件后，查看 testGit 目录下所有文件的状态  `git status`

   > 显示哪些文件有变更，但没有具体变更信息

5. 查看变更文件的具体变更信息  `git diff`  或  `git diff README.md`

   > 1. `git diff`  
   >
   >    会一行一行显示所有文件具体改动了什么
   >
   > 2. `git diff README.md`
   >
   >    会一行一行显示 README.md 具体改动了什么
   >    
   > 3. `q`
   >
   >    跳出

6. 将变更后的文档提交到暂存区  `git add .`   或  `git add <文件名.扩展名>`

   > 1. `git add .`  添加工作区所有变更文件到暂存区
   > 2. `git add <文件名.扩展名>`  添加指定文件到暂存区

7. 撤销上一次`git add`：`git reset HEAD`

8. 提交文件到暂存区后，查看 testGit 目录下所有文件的状态  `git status`

   > 1. 显示暂存区有哪些文件可以被提交到本地 Git 仓库

9. 将暂存区的文件提交到本地 Git 仓库  `git commit -a -m 'add sai readme'`

10. 查看过去提交到本地 Git 仓库的历史  `git log`  或  `git log --pretty=oneline`

   > 1. `git log`  查看详细历史信息
   > 2. `git log --pretty=oneline`  查看格式飘落的历史信息
   >
   > ```bash
   > 4a1ea4412792f230a83aadc6f9e544350acb2434 (HEAD -> master) 第三次操作
   > edbe103f0d63e6697afb2e03323bc739ebf75439 第二次操作
   > d14d1a6c1bbb74ebb3eeb58b1dbdd814379a97c4 第一次操作
   > 7b43dd08294cd9155d059b43fb8458226635a258 清空操作
   > 356bd841b878d9059c9050c355d69ebaa25ef86f 测试二
   > 8bb7b664dd2109e2de3bb389a6f4b1052d2fecea 测试一
   > ```
   >
   > 1. 4a1ea4412792f230a83aadc6f9e544350acb2434 (HEAD -> master) 第三次操作
   >
   >    > * 4a1ea4412792f230a83aadc6f9e544350acb2434 是提交的版本号  `commit-hash-id`
   >    > * (HEAD -> master) 说明这是本地 Git 仓库的当前版本
   >    > * "第三次操作" 是提交该版本时的备注

11. 撤销上一次`git commit`：`git reset --soft HEAD^`

12. 将本地 Git 仓库的当前版本回滚到之前的指定版本  `git reset --hard <commit-hash-id>`

    > git reset --hard 7b43dd08294cd9155d059b43fb8458226635a258
    >
    > ```base
    > 7b43dd08294cd9155d059b43fb8458226635a258 (HEAD -> master) 清空操作
    > 356bd841b878d9059c9050c355d69ebaa25ef86f 测试二
    > 8bb7b664dd2109e2de3bb389a6f4b1052d2fecea 测试一
    > ```

13. 新建一个 `sai_branch` 分支，并切换过去  `git checkout -b sai_branch`

14. 列出所有本地分支  `git branch`

    >   ```bash
    >   master
    > * sai_branch
    >   ```

15. 切换回主分支  `git checkout master`

16. 删除 `sai_branch` 分支  `git branch -d sai_branch`

17. 查看其它分支和当前分支的差异  `git diff <current_branch> <other_branch>`

18. 合并其他分支到你的当前分支  `git merge <other_branch> `  或  `git pull`

    > 如果合并时有冲突 conflicts ，则需要手动合并以避免冲突
    >
    > 1. 发现冲突
    >
    >    > 1. 查看哪些文件冲突  `git status -sb`
    >
    > 2. 解决冲突
    >
    >    > 1. 依次打开每个冲突的文件，搜索 4 个等号 ====
    >    > 2. 在等号上下两部分中选择要保留的部分
    >    > 3. 完成后，删除 ==== >>>> <<<< 这些标记
    >    > 4. 将刚才修改的文件提交到暂存区  `git add <文件>`
    >    > 5. 再次执行  `git status -sb`  解决下一个冲突
    >    > 6. 解决完所有冲突后，执行  `git commit`  (注意后面不需要参数)

19. 将本地 Git 仓库发布到远端 Git 仓库

    > 1. 先去 Github 新建一个绝对空的仓库（ README.md 都不要）
    >
    > 2. 然后本地切换到 master/sai_branch 分支，任何分支都行
    >
    > 3. 给远程仓库 testgit 取一个本地名称 githubtestgit
    >
    >    `git remote add githubtestgit git@github.com:jiangsai0502/testgit.git`
    >
    >    > 1. 将本地 Git 仓库的 master 分支推送到远程仓库的 master 分支
    >    >
    >    >     `git push -u githubtestgit master`
    >    >
    >    >    此时本地 Git 仓库的 **master** 分支与远程仓库的 **master** 分支就对应起来了
    >    >
    >    > 2. 将本地 Git 仓库的 sai_branch 分支推送到远程仓库的 sai_branch 分支
    >    >
    >    >    `git push -u githubtestgit sai_branch`
    >    >
    >    >    此时本地 Git 仓库的 **sai_branch** 分支与远程仓库的 **sai_branch** 分支就对应起来了
    >    >
    >    > 第一次推送时需要加上参数 -u ,之后推送就可以去掉参数 -u
    >    >
    >    > `git push  githubtestgit master`
    >    >
    >    > `git push githubtestgit sai_branch`

20. 从远程拉取最新数据

    1. 直接合并最新数据到本地：`git pull`

       1. 遇到commit your changes or stash them before you can merge，

          解决方案：放弃本地更改`git reset --hard`

    2. 更安全的做法：拉取最新数据到临时分支，比较临时分支与自己的区别，再合并
       1. 查看远程仓库：`git remote -v`
       2. 拉取`origin`远程仓库的最新数据到temp临时分支：`git fetch origin master:temp`
       3. 查看temp分支与本地原有分支的不同：`git diff temp`
       4. 将temp分支和本地的master分支合并：`git merge temp`
       5. 删除temp分支：`git branch -d temp`



#### GIT 获取指定历史版本代码

1. 首先拉去最新代码

   `git clone https://github.com/lalor/headlines.git`

   ![eKSEeZ](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/eKSEeZ.png)

2. GitHub查看作者commit记录

   ![3r9weq](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/3r9weq.png)

3. 获取指定的历史版本代码

   `git checkout 789f31871230c53c909df7f22721abc91d71d00a`


