# Errors and instructions of openpose installation
## 1. CUDA8.0安装
参考：http://blog.csdn.net/zhyj3038/article/details/52494892  
- NVIDIA官网下载.deb安装,.run安装有下面问题:  
	(1) `Error: X server is running`; 解决:tty下$ init 3命令可以kill X server再进行安装  
	(2) 各种关闭X server尝试过后继续`Error: Reboot required to continue`；重启后什么也没发生......  
	- [　] 待研究．．．
- NVIDIA官网下载安装.deb:	成功
- 校验测试是否安装成功  
	(1) 编译`samples`时目录与教程稍有不同，注意  
	(2) 个别`sample`编译出错，没深究，大部分过了:(  
	(3) 不死心，重新搜了检查CUDA是否安装成功　参考：http://blog.csdn.net/u010480194/article/details/54287335  
	(4) `Result=pass`
## 2. cuDNN安装
参考：http://blog.csdn.net/zhyj3038/article/details/52494892
- 顺利
## 3. caffe安装
参考：http://www.linuxidc.com/Linux/2016-09/135034.htm
 - 最后一步`import caffe` 出错　`ImportError: No module named google.protobuf.internal`；　解决：依赖库不够  
```C 
$ sudo apt-get install python-numpy python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags Cython ipython  
$ sudo apt-get update
```
## 4. openpose安装 
参考：https://github.com/CMU-Perceptual-Computing-Lab/openpose  
- `caffe` 和 `openpose`可以同时安装，或单独安装，见参考安装说明
- 运行`demo` 出错　
```C
Starting pose estimation demo.
Starting thread(s)
F0508 10:39:36.013202  6215 cudnn_conv_layer.cpp:53] Check failed: status == CUDNN_STATUS_SUCCESS (6 vs. 0)  CUDNN_STATUS_ARCH_MISMATCH
*** Check failure stack trace: ***
    @     0x7f24cadd45cd  google::LogMessage::Fail()
    @     0x7f24cadd6433  google::LogMessage::SendToLog()
    @     0x7f24cadd415b  google::LogMessage::Flush()
    @     0x7f24cadd6e1e  google::LogMessageFatal::~LogMessageFatal()
    @     0x7f24c8eeef73  caffe::CuDNNConvolutionLayer<>::LayerSetUp()
    @     0x7f24c9051b83  caffe::Net<>::Init()
    @     0x7f24c90549b0  caffe::Net<>::Net()
    @     0x7f24cb0927ae  op::NetCaffe::initializationOnThread()
    @     0x7f24cb0624ef  op::PoseExtractorCaffe::netInitializationOnThread()
    @     0x7f24cb10dd31  op::SubThread<>::initializationOnThread()
    @     0x7f24cb10e320  op::Thread<>::initializationOnThread()
    @     0x7f24cb11318d  op::Thread<>::threadFunction()
    @     0x7f24ca8dec80  (unknown)
    @     0x7f24ca3fa6ba  start_thread
    @     0x7f24ca13082d  clone
    @              (nil)  (unknown)
已放弃 (核心已转储)
```
- 搜了一圈，简单讲：就是GPU的加速性能不够，CUDNN只支持CUDA Capability 3.0以上的GPU加速；笔记本上的GT520M的CUDA Capability是2.1,而官方的cudnn加速是不支持3.0以下的版本的．
- 解决：换电脑！！！最后还是败给了穷.
## 总结：年轻人不要用这么老的本！
