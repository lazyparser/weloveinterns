# EWayBot MoRo 测试报告
- 安装SDK
## FunSDK说明
Function分为两个功能层：HighLevelAI获取机器人检测消息；LowLevelAI获得机器人运动控制，主要由以下实现机制：  
**1. Message机制**  
所有消息（包含HighLevelAI检测到的周边数据，LowLevelAI发送的运动数据以及Function内部的Timer数据、自定义消息数据）均按到达时间及优先级加入一个消息队列，每个Function内部均存在在一个消息处理线程，该线程读取此消息列表，串行处理各消息。  
**2. Feature机制**   
Feature主要用于向HighLevelAI请求某项识别、检测功能。 

1） 首先调用RequestFeature请求Feature；  

2） 调用CheckMessageCode回调询问处理方式；  

3） 调用Proc系列函数处理。  

目前支持的FeatureCode如下： 
- SysCom_ID_Vision_Marker （51）  视觉Marker数据
- SysCom_ID_Vision_Object （52） 视觉物体识别数据
- SysCom_ID_Vision_Face （53） 视觉人脸识别数据
- SysCom_ID_Voice_Speech （9050） 听觉语音识别数据
- SysCom_ID_LMsg_Obst （10052） 障碍检测传感器数据
- SysCom_ID_LMsg_RobPos （10053） 机器人位置变化
- SysCom_ID_LMsg_ArmPos （10054） 机器人手臂位置变化
- SysCom_ID_LMsg_HeadPos （10055） 机器人头部位置变化  

**3. Initialize机制**  
Function在启动时必须要初始化资源，等资源初始化完成之后，系统会调入JobStart函数，开始Function真正的工作。初始化需要做的工作就是注册所用Feature和肢体控制列表，即FeatureList和LimbList。  

**4. Command机制**  
Command为Function向LowLevelAI发送运动指令，控制机器人运动所使用。 发送接口为Send***系列函数。首先检查权限，权限正常后及发送返回值至Function，运动函数返回，此时机器人还未开始运动，之后LowLevelAI开始规划运动轨迹，发送电机指令控制机器人运动。当指令发送完毕，等待下位机执行结束后，LowLevelAI会发送CommandDone消息至Function，通知Function该指令执行完毕  

**5. 子Function机制**  （尚未仔细研究）  
Function可编译成lib和app,当编译为lib库时，该Function可作为子Function被其它Function调用（app及lib均可）。调用方式为父Function调用AddChildFun函数，参数传入被调用lib库名去掉lib前缀及.so后缀。框架会自动实例化该子Function模块，将其连入HighLevelAI及LowLevelAI，子Function可获取消息数据，可发送肢体控制指令控制机器人运动。  

**6. Timer机制**  
ms定时，ProcTimer处理。

## 实例测试
**1. 新建工程**  
安装完SDK之后，使用命令：emake [参数1] [参数2] [参数3] [参数4]  //我这里生成fapp ip 192.168.8.100
**参数列表**  
1) -t 指定生成工程类型，目前支持fapp及flib两种。  
fapp： 生成Function应用程序，此项目可运行在操作系统为ubuntu16.04的电脑上，通过wifi连接MoRo HighLevelAI及LowLevelAI，可获取Sensor数据、调用FuncInterface中相关接口发送命令控制机器人运动以及调用他人FunctionLib库。此类程序不可上传至MoRo本地运行。  
flib：生成FunctionLib程序，此项目生成为一个MoRo Function动态库，Function库可被其它Function程序加载，加载后可获取Sensor数据、调用FuncInterface中相关接口发送命令控制机器人运动以及调用他人FunctionLib库。Function库可通过WebUI上传至MoRo本地运行。  
2) -n 指定生成工程的名称，名称必须以字母开头，中间不可出现除字母及数字之外字符。  
3) -i 设置MoRo IP地址。  
4) -v 显示emake版本号  
5) -h 显示emake帮助信息  
6) -u 升级emake  

**2. Qt打开工程**  
1） 生成的工程文件结构  

![](images/文件结构.png)
