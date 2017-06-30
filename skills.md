# 实习生技能列表

实习生第一个月一般用来进行内部培训，在内部培训结束之后实习生会（必须）掌握以下技能或知识：

## git
学习《Git Pro》 https://git-scm.com/book/en/v2 ，基本掌握git仓库克隆、同步更新、修改、推送、新建分支、分支合并等基本操作。
- ```git init```:初始化仓库
- ```git add file_name``` :跟踪一个文件
- ```git rm file_name``` :移除一个文件
- ```git mv file_name1 file_name2``` :重命名一个文件
- ```git status``` :查看状态
- ```git commit``` :提交更改， ```-a```：提交所有更改，```-m```：添加说明
- ```git log``` :倒序列出提交历史，```-p -2```列出近两次区别，```--stat```简略信息，```--pretty=format：“”```控制日志格式
- ```git config --global alias.ss status``` :自定义别名参数
- ```git config --global user.name user_name``` ```git config --global user.email email``` :设置github用户名邮箱
- ```git remote -v``` :列出远程服务器名```git remote add name URL``` :添加远程服务器名
- ```git fetch remote-name``` :拉取远程仓库
- ```git push remote-name branch-name``` :推送远程仓库某分支
- ```git checkout -b branch-name``` :新建分之并切换至该分支，无```-b```仅切换分支
- ```git branch``` :列出本地分支，```-a```列出所有分支，包括远程分支，```-v```分支最后一次提交

## github
- 掌握 Fork-Clone-Push， pull request
- 保持与fork源同步，即更新: 
>> ```git remote add upstream URL``` 添加upstream
>> ```git fetch upstream``` 更新本地
>> ```git merge upstream/master``` 合并
>> ```git push origin``` 推送
- ```git clone -b name URL```：clone指定分支
- 重命名分支：
>> ```git push --delete origin name``` 删除远程分支
>> ```git branch -m origin_name new_name``` 重命名本地分支
>> ```git push origin``` 推送

## slack
基本掌握聊天操作、查看任务接受任务、分享、@等操作。

## kanban

TODO 技能掌握程度的描述

## scrum

TODO 技能掌握程度的描述

## linux command line
学习《The Linux Command Line》 掌握Linux基本命令
- `$date`:查看时间
- `$cal`:查看日历
- `$df`:查看磁盘
- `$cd`:返回Home
- `$cd -`:返回上一目录
- `$cd ..`:返回上一级目录
- `$cd ./xxx`:相对路径
- `$pwd`:当前所在目录
- `$file` xxx:确定文件类型
- `$ls`:显示当前目录内容，`-a`显示全部包括隐藏，`-l`长格式显示，`-t`按时间显示，`S`按文件大小显示
- `$cp`:复制
- `$mv`:移动
- `$mkdir`:新建目录
- `$rm`:删除

## wiki & markdown

- 标题：一级标题：#，二级标题：##，三级标题：###
- 突出标记：×斜体×，××粗体××
- 列表：一级标题：×，-
- 块引用：>
- 行间代码：``
- 多行代码：``````
- 任务列表与标记：`-[]`，`-[x]`
- 表格：```Header|Header```
- 划线：`～～划线～～`

## 在小组技术讨论中保持建设性和高效

TODO 技能掌握程度的描述

## 技术报告的表达能力

TODO 技能掌握程度的描述

## python 语言编程能力

TODO 技能掌握程度的描述

## 网络组建及部署 (Optional)

TODO 技能掌握程度的描述

## ROS (Optional)

- 学习并掌握ROS-wiki教程 http://wiki.ros.org/ROS/Tutorials 
- 了解核心组件RVIZ框架结构，并修改修改订阅信息 https://github.com/Keyinme/rviz 

## Android (Optional)

TODO 技能掌握程度的描述

## linux sysadmin (Optional)

TODO 技能掌握程度的描述

## iOS programming (Optional)

TODO 技能掌握程度的描述

## Testing Automation (Optional)

TODO 技能掌握程度的描述


