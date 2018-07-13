MycroftAI调研报告
====
##Mycroft是什么？<br> 
--------
  Mycroft是世界上第一个开源的，开放硬件的人工智能语音平台。<br> 
  它区别于Siri，Alexa和Cortana这些大公司商业化的智能语音助手平台，这是一个基于Raspberry Pi3和Arduino － 世界上最受欢迎的两个开放式硬件的开发平台。<br> 
它允许开发商、制造商和使用者充分展示自己的创意，亲自动手编程。Mycroft 团队开源了 Adapt Intent Parser，这是一段能够将自然语言转换成机器可以理解的
指令的代码。即它可以通过手机或者电脑等设备上的程序将用户说的话转换成可以执行的命令。Adapt Intent Parser 已经开源，这意味着它 
可以被任何任何人使用，同时也可以它变得越来越强大。此外，它还允许用户在有限的硬件条件下集成它。简而言之，它是一款方便，轻便的AI语音平台。<br> 

Mycroft能做什么？<br> 
----------
   Mycroft的创始人蒙哥马利说：“Mycroft的创意受到星际迷航中电脑的启发。”他想创建可以控制家里每个电器的人工智能语音平台，并应用于开源环境。达到反应灵敏，
简单好用，功能很赞的地步。<br> Mycroft 家居AI控制器配置Raspberry Pi 2和Arduino控制器，支持Wi-Fi。你下命令，如“锁门”或者“打开走廊灯”，它就会控制家里的电
器完成任务。Mycroft还可以通过连接Netflix、YouTube、Pandora和Spotify播放媒体，支持的输出设备有Roku和Chromecast。类似于Amazon Echo，你可以询问天气更
新或者新闻头条，也可以询问单词拼写和数学辅导，或者让其给你讲个笑话。Mycroft配置ARM Cortex-A7四核处理器，1GB内存。你可以无线连接你的无线路由器，或者用
网线连接。Mycroft还有一个159美元的版本，这个版本可以轻松访问Raspberry Pi 2的HDMI接口、USB 2.0接口和GPIO口。Mycroft不支持蓝牙、Z-Wave或
者Zigbee，因此你需要SmartThings Hub或者WeMo Link这些网关设备把它连接到其他不用Wi-Fi的设备。<br> 
![](https://github.com/willionZS/picture/blob/master/2.png)

Mycroft开源demo简单使用<br> <br> <br> 
===========
准备环境<br> <br>
------------
首先，获取Mycroft的源代码程序，可以直接clone或者git（git如下）：<br> 
`cd ~/`<br> 
`git clone --depth=1 https://github.com/MycroftAI/mycroft-core.git` <br> 
`cd mycroft-core`<br>  
`bash dev_setup.sh`<br> 
![bash](https://github.com/willionZS/history/blob/master/mycroft-picture/1bash.png)<br><br>
bash完成如下
![bashed](https://github.com/willionZS/history/blob/master/mycroft-picture/2bashed.png)<br><br>
dev_setup.sh这个脚本为安装依赖项，在ubuntu下，直接bash它等待完成安装即可，其他系统需要根据提示手动安装软件包 <br> <br> <br>


运行Mycroft <br><br>
-------------
Mycroft包里有start-mycroft.sh这个脚本，可以用来启动这个demo，运行如下： <br>
`cd ~/mycroft-core` <br>
`./start-mycroft.sh debug` <br>
![start](https://github.com/willionZS/history/blob/master/mycroft-picture/3start-mycroft.png)<br><br>
"debug"为命令启动后台服务（麦克风，skill模块，消息，音频等系统）以及文本命令行界面(CLI)，你可以使用CLI和Mycroft进行交互，
并查看交互内容和log日志内容 <br>
或者，您可以运行./start-mycroft.sh all以在没有命令行界面的情况下开始服务。稍后您可以使用CLI启动CLI ./start-mycroft.sh cli，后台停止服务如下： <br>
`./stop-mycroft。sh`<br>
启动后，程序会自动连接服务器，如果网速不好，或者没有代理的情况下会显示链接不成功，因此翻墙是必要的，而且速度不能太差
（亲测代理ms达到300之后就会连接失败），启动成功,界面如下：<br>
![sign](https://github.com/willionZS/history/blob/master/mycroft-picture/4sign.png)<br><br>
如图所示，Mycroft会给你提供一个6位数字与字母组合而成的激活码，一长串句子，打引号的字母和数字就是激活码，
你需要使用这个激活码登录到home.mycroft.ai来为你的设备配对然后才能使用：<br>
你可以使用谷歌账号在它的官网登录，然后配对，也可以使用其它账号，在线配对如下：<br>

![sign](https://github.com/willionZS/history/blob/master/mycroft-picture/5online.png)<br><br>
配对成功后，配对网站在线显示如下，并会给你几个示例问题：<br>
![sigin](https://github.com/willionZS/history/blob/master/mycroft-picture/6had.png)<br><br>
点击finish按钮，就可以看到你刚才在线设置好的，属于自己的mycroft：<br>
![thus](https://github.com/willionZS/history/blob/master/mycroft-picture/thus.png)<br><br>
然后这边运行界面，就会有如下提示:now,I am ready for use，表示你的设备以及可以正常运行了：<br><br>
![pair](https://github.com/willionZS/history/blob/master/mycroft-picture/7paired.png)<br><br>
下面是我在使用过程的几个示例，可以问它的名字，你会发现它已经默认自己名字为你刚注册时给它取的名字，以及他还可以唱歌，读新闻，帮你google维基百科<br>
![used](https://github.com/willionZS/history/blob/master/mycroft-picture/8used.png)<br><br>
![sing](https://github.com/willionZS/history/blob/master/mycroft-picture/9sing.png)<br><br>

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
