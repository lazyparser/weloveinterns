
# openpose_install
openpose_install_errors_instructions
1. CUDA8.0安装 参考：http://blog.csdn.net/zhyj3038/article/details/52494892
> - NVIDIA官网下载.deb安装,.run安装有下面问题:  
 >>>(1) Error: X server is running; 解决:tty下$ init 3命令可以kill X server再进行安装  
 >>>(2) 各种关闭X server尝试过后继续Error: Reboot required to continue；重启后什么也没发生......
> - 曲线救国NVIDIA官网下载安装.deb:  
 >>>嗯，什么也没有发生，安装完了！
> - 校验测试是否安装成功  
 >>>(1) 编译sample时目录与教程稍有不同，注意  
 >>>(2) 个别sample编译出错，没深究，大部分过了:(  
 >>>(3) 不死心，重新搜了检查CUDA是否安装成功　参考：http://blog.csdn.net/u010480194/article/details/54287335  
 >>>(4) Result=pass!
2. cuDNN安装 参考：http://blog.csdn.net/zhyj3038/article/details/52494892
>- 顺利
3. caffe安装 参考：http://www.linuxidc.com/Linux/2016-09/135034.htm
> - 最后一步import caffe出错　ImportError: No module named google.protobuf.internal；　解决：依赖库不够  
``$sudo apt-get install python-numpy python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags Cython ipython  
$ sudo apt-get update``
4. 按openpose安装的	https://github.com/CMU-Perceptual-Computing-Lab/openpose
