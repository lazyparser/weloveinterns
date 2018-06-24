# 零基础使用qemu模拟器搭建arm

### 简介
#### qemu介绍
>QEMU是一套由法布里斯·贝拉(Fabrice Bellard)所编写的以GPL许可证分发源码的模拟处理器，在GNU/Linux平台上使用广泛。Bochs，PearPC等与其类似，但不具备其许多特性，比如高速度及跨平台的特性，通过KQEMU这个闭源的加速器，QEMU能模拟至接近真实电脑的速度。

#### 搭建的必要性
如果想做arm+Linux的嵌入式开发，或者对内核机制很感兴趣，关心arm架构的相关功能,想使用qemu进行开发，搭建qemu+arm的执行环境就很有必要了。
### 开发环境
Ubuntu16.04 模拟arm vexpress A9开发板。
### 搭建步骤
#### 下载Linux内核
1. 方法一：git下载

		git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

2. 方法二：下载linux3.16源代码包

		wget https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.16.tar.xz
		
##### 编译Linux内核
1. 生成vexpress开发板的config文件

		make CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm vexpress_defconfig
		
2. 编译，生成内核镜像zImage

		make CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
		
##### 下载和安装qemu模拟器
* 高版本qemu源码下载：

		wget http://wiki.qemu-project.org/download/qemu-2.0.2.tar.bz2
		
* 安装依赖
	* `sudo apt-get install zlib1g-dev`
	* `sudo apt-get install libglib2.0-0`
	* `sudo apt-get install libglib2.0-dev`
	
* 配置qemu

		./configure --target-list=arm-softmmu --audio-drv-list=
		
* 编译和安装
	* `make`
	* `sudo make install`
	
#### 测试内核能否执行成功
测试指令：（注意路径是镜像所在路径）

`qemu-system-arm -M vexpress-a9 -m 512M -kernel /home/**your file PATH**/arch/arm/boot/zImage -nographic -append "console=ttyAMA0"`

如果看到内核启动过程中的打印，说明之前的搭建都是成功的。
#### 制作根文件系统
在上一步的测试中，内核报panic，由于内核找不到根文件，无法启动init进程，所以要自己制作根文件系统
##### 下载、编译和安装busybox
1. 源码下载

`wget http://www.busybox.net/downloads/busybox-1.20.2.tar.bz2`

2. 编译安装

	* `make defconfig`
	* `make CROSS_COMPILE=arm-linux-gnueabi-`
	* `make install CROSS_COMPILE=arm-linux-gnueabi-`
	
安装完毕后。会在busybox文件夹下生成_install文件夹。该文件夹下的程序就是单板执行所须要的命令。
##### 形成根文件夹结构
1.   创建rootfs文件夹（根文件夹）

	* sudo mkdir rootfs
	* cd rootfs
	* sudo mkdir dev
	* sudo mkdir lib
	
2.  拷贝busybox命令到根文件夹下

	* sudo cp busybox-1.20.2/_install/* -r rootfs/
	
3. 从工具链中拷贝执行库到lib文件夹下

	* sudo cp -P /usr/arm-linux-gnueabi/lib/* rootfs/lib/
	
4. 创建4个tty端终设备

	* sudo mknod rootfs/dev/tty1 c 4 1
	* sudo mknod rootfs/dev/tty2 c 4 2
	* sudo mknod rootfs/dev/tty3 c 4 3
	* sudo mknod rootfs/dev/tty4 c 4 4
	
##### 制作根文件系统镜像
1. 生成32M大小的镜像
`dd if=/dev/zero of=a9rootfs.ext3 bs=1M count=32`
2. 格式化成ext3文件系统
`mkfs.ext3 a9rootfs.ext3`
3. 将文件复制到镜像中

	* `sudo mkdir tmpfs`
	* `sudo mount -t ext3 a9rootfs.ext3 tmpfs/ -o loop`
	* ` cp -r rootfs/*  tmpfs/`
	* `sudo umount tmpfs`
	
##### 系统启动执行
启动qemu来模拟vexpress开发板:

`qemu-system-arm -M vexpress-a9 -m 512M -kernel /home/**your file PATH**/arch/arm/boot/zImage -nographic -append "root=/dev/mmcblk0  console=ttyAMA0" -sd a9rootfs.ext3`

###### 出现命令提示符，标志着搭建成功！

#### 参考链接
1. [从零使用qemu模拟器搭建arm执行环境](https://www.cnblogs.com/mfmdaoyou/p/6934098.html)
2. [开源Cortex-M模拟器QEMU的使用方法](https://blog.csdn.net/zoomdy/article/details/50582557)
3. [QEMU blog](https://abiaog.github.io/blog/2017/01/18/QEMU.html)

###### The author：anchuanxu 2018/6/22
	