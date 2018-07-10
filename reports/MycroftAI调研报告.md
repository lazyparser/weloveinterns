MycroftAI调研报告
====
##Mycroft是什么？<br> 
--------
  Mycroft是世界上第一个开源的，开放硬件的人工智能语音平台。<br> 
  它区别于Siri，Alexa和Cortana这些大公司商业化的智能语音助手平台，这是一个基于Raspberry Pi3和Arduino － 世界上最受欢迎的两个开放式硬件的开发平台。<br> 
它允许发明者、小型开发商和制造商充分展示自己的创意，让他们成为现实。Mycroft 团队开源了 Adapt Intent Parser，这是一段能够将自然语言转换成机器可以理解的
指令的代码。更清楚的描述它的话，它可以通过手机或者电脑等设备上的一个程序将用户说的话转换成可以解释执行的命令。Adapt Intent Parser 已经开源，这意味着它 
可以被任何项目任何人使用，同时也可以将它变得更好。除此之外，它还是一个轻量级的解决方案，它允许用户在有限的硬件条件下集成它。简而言之，你不需要桌面电脑那
样强大的运算能力就能运行它。<br> 

Mycroft能做什么？<br> 
----------
   Mycroft的创始人蒙哥马利说：“Mycroft的创意受到星际迷航中电脑的启发。”他想创建可以控制家里每个电器的人工智能语音平台，并应用于开源环境。达到反应灵敏，
简单好用，功能很赞的地步。<br> Mycroft 家居AI控制器配置Raspberry Pi 2和Arduino控制器，支持Wi-Fi。你下命令，如“锁前门”或者“打开走廊灯”，它就会控制家里的电
器完成任务。Mycroft还可以通过连接Netflix、YouTube、Pandora和Spotify播放媒体，支持的输出设备有Roku和Chromecast。类似于Amazon Echo，你可以询问天气更
新或者新闻头条，也可以询问单词拼写和数学辅导，或者让其给你讲个笑话。Mycroft配置ARM Cortex-A7四核处理器，1GB内存。你可以无线连接你的无线路由器，或者用
网线连接。Mycroft还有一个159美元的版本，这个版本含有背面板，可以轻松访问Raspberry Pi 2的HDMI接口、USB 2.0接口和GPIO口。Mycroft不支持蓝牙、Z-Wave或
者Zigbee，因此你需要SmartThings Hub或者WeMo Link这些网关设备把它连接到其他不用Wi-Fi的设备。<br> 
![](https://github.com/willionZS/picture/blob/master/2.png)

Mycroft如何运转？<br> 
--------
GitHub上有mycroftAI 的开源文件：https://github.com/MycroftAI。我们可以`clone or download`它的mycroft-core文件到本地来使用。<br>

操作如下：<br>
   `cd ~/`<br>
   `git clone --depth=1 https://github.com/MycroftAI/mycroft-core.git`<br>
   `cd mycroft-core`<br>
   `bash dev_setup.sh`<br>
dev_setup.sh脚本设置了依赖关系和virtualenv，在ubuntu下需要先运行dev_setup.sh来安装相关的软件包。<br>
安装过程中，我出现过网络端口被占用的情况，简单粗暴重启后就行了，还出现一次安装运行不成功的情况，指令：git init即可解决。<br>
安装完成后，如下执行即可运行Mycroft：<br>
•	cd ~/mycroft-core<br>
•	./start-mycroft.sh debug<br>
“debug”命令将启动后台服务（麦克风监听器，技能，messagebus和音频子系统），并启动一个基于文本的命令行界面（CLI），您可以使用该命令行与Mycroft交互并查看各种日志。或者，您可以运行./start-mycroft.sh all以在没有命令行界面的情况下开始服务。稍后，您可以使用CLI调出./start-mycroft.sh cli。
后台服务可以作为一个组停止：<br>
•	./stop-mycroft.sh<br>

Mycroft的产品如何使用？<br> 
--------
Mycroft入门<br>
在这里，我们将逐步介绍每个Mycroft平台或设备的第一步 – 简称设备为机箱（device） - 并让您发布简单的话语，从而调用技能。然后，加入我们的  论坛和聊天来寻求友好的建议和帮助，继续与Mycroft一起学习。<br>
1.创建一个Mycroft Home帐户<br>
无论您使用的是哪种平台或机箱（device），您的第一步就是在Mycroft Home上创建一个帐户。Mycroft Home是您管理所有安装了Mycroft的设备的地方。<br>
2.安装Mycroft并将您的设备与Mycroft Home配对<br>
下载并安装Mycroft<br>
在mycroft.ai下载页面的链接有每个平台或机箱的安装说明。如果您在安装过程中卡住了，请加入我们的聊天室或论坛，或与我们联系以获取更多帮助。<br>
此外你可能会喜欢阅读《入门手册》（PDF，290Kb）<br>
将您的设备与Mycroft Home帐户配对<br>
一旦你安装了你的平台或成功设置了你的机箱，Mycroft应该给你一个6个字母的配对代码。每个Mycroft设备都需要与Mycroft Home帐户配对。您的Mycroft Home账户可为您的设备提供详细信息，例如您的一般位置，例如天气等技能，以及您对诸如温度等测量的偏好。<br>
这些术语是什么意思？<br>
当您开始使用Mycroft时，您会看到一些可能不熟悉的短语 - 所以我们在下面解释它们。<br>
•	设备：您安装了Mycroft的平台。这可能是使用Enclosure（如Mark 1）或Raspberry Pi，或者它可能位于Linux桌面上。在使用之前，每台设备都需要与Mycroft Home帐户配对。<br>
•	唤醒单词：唤醒单词是您用来告诉Mycroft您即将发出命令的短语。您可以在Mycroft Home帐户中配置唤醒词。<br>
•	话语：一个话语是你如何与迈克罗夫特互动。话语是一个命令或问题 - 例如“堪萨斯城的天气如何？”或“告诉我关于彭布罗克威尔士柯基犬”。<br>
•	技巧：当Mycroft听到唤醒词，然后是话语时，Mycroft将尝试找到与话语相匹配的技能。该技能可以获取一些数据，或者播放一些音频，或说话，或显示一些信息。如果Mycroft找不到与话语相匹配的技能，他会告诉你他不了解。
3.开始使用默认技能，然后安装更多与Mycroft一起安装的默认技能<br>
Mycroft安装了许多默认技能，例如设置闹钟，提供天气或告诉时间。尝试以下基本示例开始：<br>
•	“嘿Mycroft，现在几点？”<br>
•	“嘿Mycroft，在巴黎几点钟？”<br>
•	“嘿Mycroft，墨尔本现在几点？”<br>
•	“嘿Mycroft，天气怎么样？”<br>
•	“嘿Mycroft，设置闹钟30分钟。”<br>
•	“嘿Mycroft，我的IP地址是什么？”<br>
•	“嘿Mycroft，给我开个玩笑吧。”<br>
•	“嘿Mycroft，告诉我关于巧克力的事。”<br>
•	“嘿Mycroft，告诉我关于Linux的事情。”<br>
安装其他技能<br>
一旦您对基础知识感到满意，您可以安装其他技能。这很简单 - 只需告诉Mycroft你想安装的技能。<br>
•	“嘿Mycroft，安装技能日常冥想”。<br>
•	“嘿Mycroft，安装技能复活节彩蛋”。<br>
浏览社区贡献技能列表，查找您想尝试的其他人。<br>
4.参与进来<br>
这仅仅是个开始。无论您是否具备技术技能，您都可以为Mycroft做出贡献。<br>

我的看法<br>
--------
Mycroft是一款很棒的生活服务软件设备，在生活中使用它，可以迅速的完成用户的要求，为使用者的生活带来便利。同时，它还可以把家庭里的家具连接在一起，通过用
户的声音来给智能家居分配任务。它主要的功能偏向于家居，能够为人类生活带来很好的便利。<br>
后续可能的工作和计划<br> 

后续的工作<br>
--------
我认为Mycroft可以把汽车导航，用户数据迁移和备份，远程服务结合起来。比如用户去外地旅游，只需要一键登录自己的Mycroft，就可以在其他地方继续
沿用在自己家里的习惯和服务，以及通过数据迁移，可以在其它的用户下，复制一份自己原本的mycroft数据信息。以及，在即将回家的途中，通过给Mycroft远程发布消息
让它提前为自己准备好热水，地热，暖气，冷气等服务。<br>
