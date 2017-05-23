## ScanNet调研报告

### ScanNet是什么

	ScanNet是一个针对3D深度学习的基于（RGB-D)的视频数据集，包含有707个场景下的
	2.5M个RGB-D图片，这些图片均带有3D相机位姿标注、外观重建、语义分割。

	[官方网站](http://www.scan-net.org/)

### ScanNet应用场景

	ScanNet数据集主要用于3D环境感知相关深度学习算法的训练，论文中提到了3个可应用该数据集的方向为：
	- 3D 物体分类
	- 语义体素标记(Semantic Voxel Labeling)
	- 3D对象检索
	论文针对上述三种类型任务使用该数据集进行训练测试，并提供benchmark，声称获得了
	state-of-the-art的性能表现。

### ScanNet数据获取方式

	数据集中的数据获取相对比较简单易行，过程如下述图片:

![ScanNetData](../resources/Image/ScanNetData.png)

	- 首先使用ipad+一个RGB-D相机录取场景信息
	- 然后上传至服务器，服务器上对视频中的场景进行重建及分割
	- 最后通过亚马逊的“众包”平台分发任务，让工作者通过提示进行最后语义标记等任务。
	
### ScanNet数据集的使用需要提交信息申请
