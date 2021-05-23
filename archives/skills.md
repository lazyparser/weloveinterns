# 实习生技能列表

更新日期：**20191129** 。欢迎继续提交PR

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

## kanban&& scrum

了解Kanban和Scrum,了解Scrum和Kanban的异同：

|  | Scrum | Kanban |
|------|:----------:|-----:|
| 迭代 | 要求定时迭代 | 没有指定定时迭代，可以分开计划、发布、过程改进，可以事件驱动而不是限定时限 |
| 承诺|团队在每个迭代承诺一定数目的工作 |承诺不是必须的|
|度量数据|以速度（Velocity）作为计划和过程改进的度量数据|使用开发周期作为计划和过程改进的度量数据|
|团队|指定跨功能团队|没有指定跨功能团队，也容许专门团队|
|工作大小|工作任务细分，可于一个迭代中完成|没有指定工作任务大小|
|图表|指定使用燃烧图|没有指定任何图表|
|工作限制|间接限制开发中工作（每个迭代）|设定开发中工作的限制（每个工作流程状态）|
|估算|规定估算过程|没有指定任何估算方式|
|任务变更|在迭代中不能加入新工作任务|只要生产力容许，可以随时添加工作任务|
|是否跨团队|由单一团队负责 Sprint Backlog|多个团队和成员分享看板|
|团队角色|指定三个角色（产品负责人/ScrumMaster/团队）|没有指定任何团队角色|
|看板周期|Scrum board在每个迭代后重设|看板反应持久开发情况|
|优先级|规定优化的product backlog|优先级是非必须的|

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

##### 字体：

- 加粗： 要加粗的文字左右分别用两个\*号包起来, **例如** 

- 斜体：要倾斜的文字左右分别用一个\*号包起来, *例如*

- 斜体加粗：要倾斜和加粗的文字左右分别用三个\*号包起来， ***例如***

- 删除线：要加删除线的文字左右分别用两个\~\~号包起来, ~~例如~~

- 插入图片：`![图片alt](图片地址 ''图片title'')`

- 插入超链接：`[超链接名](超链接地址 "超链接title")`

- 插入表格：\`\`\`

```ruby
表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容
```

- 插入代码：上下各三点。

​```
代码
代码
代码
​```
## 在小组技术讨论中保持建设性和高效

- 积极踊跃发言，表达自己；
- 疑问和困惑及时表达，寻求帮助；
- 及时分享学习到的技能和自己对某方面的见解；
- 敢于质疑，勤于验证别人的结论。

## 技术报告的表达能力

- 清晰的表达，语言流畅，逻辑清晰；
- 表达有条理；
- 突出重点，论证严谨；
- 总结到位；

## python 语言编程能力

- 会python环境的搭建；
- 熟悉python的基本的语法和数据结构；
- 关键字、标识符和内置函数；
- 熟悉列表、元组、字典和集合的用法；
- 熟悉文件操作；
- 熟悉异常处理；
- 熟悉面向对象技术；
- 熟悉构建正则表达式；

## 网络组建及部署 (Optional)

- 熟悉网络的TCP/IP、OSI及五层协议体系结构；
- 了解IPV4报文结构；
- 熟悉五类地址各自范围、私网IP地址及网络地址转换
- 会计算：子网掩码与CIDR；
- 熟悉中继器、集线器、网桥、交换机和路由器的作用及原理；
- 了解ARP、DHCP与ICMP协议；
- 了解IPV6报文结构及特点
- 了解路由协议RIP、OSPF和ICMP原理
- 熟悉TCP与UDP协议各自特点
- 熟悉DNS与FTP协议工作原理
- service network-manager stop:关闭网络服务
- service network-manager restart: 重启网络服务
- sudo ps -e | grep ssh:ps是查看进程 |是管道 grep用于查找文件里符合条件的字符串
- ctrl+h:显示linux下的隐藏文件夹
- ping IP:用来测试主机之间网络的连通性。执行ping指令会使用ICMP传输协议，发出要求回应的信息，若远端主机的网络功能没有问题，就会回应该信息，因而得知该主机运作正常。
- ifconfig：用来查看和配置网络设备。lo 是表示主机的回坏地址，这个一般是用来测试一个网络程序，但又不想让局域网或外网的用户能够查看，只能在此台主机上运行和查看所用的网络接口.

远程控制电脑的方式：

- 1）ssh
- 2）teamviewer(图形化界面控制)
- 3）anydesk（teamviewer的加强版）
- 4）配置主从机


## ROS (Optional)

- 学习并掌握ROS-wiki教程 http://wiki.ros.org/ROS/Tutorials
- 了解核心组件RVIZ框架结构，并修改修改订阅信息 https://github.com/Keyinme/rviz
- 学习掌握柴长坤老师的《机器人操作系统入门》，并运行所有课程示例

## Android (Optional)

- 掌握一款Android IDE工具的使用（比如：Android Studio或Eclipse ID）；
- 掌握Android 应用程序的组件（Activities、Services、Broadcast Receivers和Content Providers等）；
- 熟悉Andriod基础入门路线；
- 熟悉Andriod系统特性与平台架构；
- 相关术语的解释：

1. Dalvik： Android特有的虚拟机,和JVM不同,Dalvik虚拟机非常适合在移动终端上使用!
2. AVD： (android virtual machine):安卓虚拟设备,就是安卓的模拟器
3. ADT： (android development tools)安卓开发工具
4. SDK：(software development kit)软件开发工具包,就是安卓系统,平台架构等的工具集合,如adb.exe
5. DDMS：(dalvik debug monitor service)安卓调试工具
6. adb：安卓调试桥,在sdk的platform-tools目录下,功能很多,命令行必备
7. DX工具：将.class转换成.dex文件
8. AAPT：(android asset packing tool),安卓资源打包工具
9. R.java文件：由aapt工具根据App中的资源文件自动生成,可以理解为资源字典
10. AndroidManifest.xml：app包名 + 组件声明 + 程序兼容的最低版本 + 所需权限等程序的配置文件

- 熟悉APP程序打包与安装的流程；
- 熟悉Android项目的目录结构；

## linux sysadmin (Optional)

- `$grep`：查找；
- `$sed`：文本编辑；
- `$awk`: 文本分析工具；
- `$cat/tail`: 文本输出命令；
- `$ifconfig`: 网卡配置查询命令；
- `$vi`: 文本编辑指令；
- `$ping`: 检测主机互通性
- `$systemctl`: 系统服务管理器指令
- `$ ssh usrname@serverip` 远程登录
- `$ lsof -i:port` 看某一端口的占用情况
- `$ arp -a `查看ARP表
- `$ uname -a` 查看系统内核
- `$ cat /etc/issue`查看系统版本
- `$ cat /proc/cpuinfo` 查看CPU信息
- `$ cat /proc/meminfo` 查看内存信息

#### linux目录结构：

##### 第一层根目录：/
##### 第二层：bin、boot、dev、home、opt、usr、、、

- /bin:存放二进制可执行文件（ls、 cat 、mkdir)等常用命令
- /etc:存放系统管理和配置文件
- /home:存放所有用户文件的根目录
- /usr:存放系统应用程序 ，/usr/local为本地系统管理员软件安装目录
- /opt:额外安装的可选应用程序包的位置，比如ROS
- /dev:设备文件存放地
- /lib: 存放和文件系统中的程序运行所需要的共享库和内核模块

#### linux命令/apt-get

在ubuntu中，安装应用程序的三种方法：

- sudo apt-get install ×××, 安装位置在/usr/bin
- sudo dpkg -i package.deb ,安装类型为deb的包，安装位置在/opt

```
//源码安装 git clone URL 
cd package 
mkdir build
 cd build
 cmake .. 
 make
 sudo make install
```

- sudo apt-get remove ×××:卸载×××
- sudo apt-get update : 更新软件源列表
- sudo apt-get upgrade: 更新软件

## iOS programming (Optional)

- 熟悉IOS环境搭建；
- 熟悉Objective C基础知识；

## Testing Automation (Optional)

- 熟悉Docker
...

