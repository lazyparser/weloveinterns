# Iterative Pruning研究报告

研究的主要目标是在资源有限的平台上运行深度模型。这就要求对模型进行压缩。本次实验的主要依据是是韩松的论文[Learning both Weights and Connections for Efficient Neural Networks](https://arxiv.org/abs/1506.02626)。目前尚处在初步阶段，在mnist上获得了较好的效果。见[这里](https://github.com/nephashi/DeepCompression)。

实验比较顺利，存在的主要问题是tensorflow对稀疏运算的支持不太好。导致目前只能支持对全连接层的剪枝。好在Alexnet，VGG等模型都存在全连接层，而全连接层的参数数量往往占较大比重。

## 剪枝概述

剪枝的思想比较简单。首先照常训练模型，之后设定一阈值，将低于该阈值的连接剪去，然后重新训练模型以校准。迭代剪枝-校准的过程可以寻求最大化的模型压缩。

## 实现

实现遇到的主要问题是tensorflow对稀疏运算的支持较差，甚至没有直接支持稀疏矩阵相乘的方法。Google之后发现embedding_lookup_sparse方法可以用来实现稀疏矩阵和密集矩阵的乘法，尽管这个函数的本意并非用于这个目的。我基于这个方法封装了创建稀疏矩阵乘密集矩阵的op（node in tensorflow graph）的[方法](https://github.com/nephashi/DeepCompression/blob/master/mnist_iterative_pruning/sparse_op.py)，可以方便以后复用。在封装性和使用上，这个方法并不完美，但我没有找到更好的方案。[这里](https://github.com/nephashi/learntensorflow/blob/master/sparsetensor.md)提供了关于tensorflow中SparseTensor和embedding_lookup_sparse方法的一些解释。但我猜你一定不会想要搞明白这些东西（滑稽）。

## 实验

我在mnist上训练了一个简单的卷积网络。结构大概是这样的。

- input: 28\*28\*1 (input height, input width, channel) 
- conv1: 5\*5\*1\*32 (kernel height, kernel width, input channel, output channel)
- maxpool1: 2\*2 
- (here the input become 14\*14\*32)
- conv2: 5\*5\*32\*64 (kernel height, kernel width, input channel, output channel)
- maxpool2: 2\*2 
- (here the input become 7\*7\*64)
- fc1: 3136\*1024 (3136: flat output of maxpool2, 7\*7\*64=3136)
- fc2: 1024\*10
- softmax

应该不难看懂吧！这其实就是tensorflow教程里面的网络。注意同样用于mnist，这个网络比LeNet5大很多，说明mnist识别任务并不需要这么大的capacity。

实验结果还是比较理想的。剪掉99.77%的权重之后，精确率仍能保持在98.7%。同时在剪枝过程中准确率一度有提升。或许可以认为剪枝降低了模型的过拟合。

|weight kept ratio|accuracy|
|-----------------|--------|
|1                |0.99    |
|0.7              |0.991   |
|0.49             |0.993   |
|0.24             |0.994   |
|0.117            |0.993   |
|0.057            |0.994   |
|0.013            |0.993   |
|0.009            |0.992   |
|0.0047           |0.99    |
|0.0023           |0.987   |
|0.0016           |0.889   |
|0.0011           |0.886   |
|0.00079          |0.677   |
|0.00056          |0.409   |

关于时间性能，结果非常的奇怪。我的实现是，先以二维数组的结构存储每层的权重，再对其剪枝，在将其转换成稀疏表示。

- 在剪枝前的二维数组上的inference时间：0.644
- 在剪枝后的稀疏二维数组上的inference时间：1.572
- 在转换后进行稀疏运算的inference时间：0.692

理论上稀疏矩阵的乘法一定是比密集矩阵要快的，但是并没有得到预期的表现，还需要研究。
