# graph ransform tool(GTT)
## 0.keng
![](imgs/20180723-214749.png)
解决方法
<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/graph_transforms>
将这个里边的工具包靠近你的tensorflow文件，这样就可以运行其中的build文件，在bazel中这个要自己建立，还有	WORKSPACE文件，这是表明此文件夹是一个bazel的工作区，也可以自己手动创建一个空的，`touch WORKSPACE`。
## 1.path of tensorflow
pip安装后的tensorflow路径
/usr/local/lib/python2.7/dist-packages/tensorflow/
## 2.simple case  Inception V3 graph
<http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz>
## 3.transform_graph
GTT的一种基本的使用方法如下所示，其中地址要写到0.keng中的tensorflow文件。

    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul:0' \
    --outputs='softmax:0' \
    --transforms='
    strip_unused_nodes(type=float, shape="1,299,299,3")
    remove_nodes(op=Identity, op=CheckNumerics)
    fold_old_batch_norms
    '
### 4.summarize_graph
如果在转化时不知道inputs和outputs，可以使用summarize_graph

    bazel build tensorflow/tools/graph_transforms:summarize_graph
    bazel-bin/tensorflow/tools/graph_transforms/summarize_graph --in_graph=tensorflow_inception_graph.pb
### 5. Optimizing for Deployment
去除无用的节点，以达到压缩的目的
 
     bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul' \
    --outputs='softmax' \
    --transforms='
      strip_unused_nodes(type=float, shape="1,299,299,3")
      remove_nodes(op=Identity, op=CheckNumerics)
      fold_constants(ignore_errors=true)
      fold_batch_norms
      fold_old_batch_norms'
### 6.Fixing Missing Kernel Errors on Mobile
解决丢失核的错误
    
    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul' \
    --outputs='softmax' \
    --transforms='
      strip_unused_nodes(type=float, shape="1,299,299,3")
      fold_constants(ignore_errors=true)
      fold_batch_norms
      fold_old_batch_norms'
### 7.Shrinking File Size  round_weights
您可以调整NUMYSTATE参数以控制每个权重缓冲器被舍入到多少值，较低的数字将以准确性的代价增加压缩。 

    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul' \
    --outputs='softmax' \
    --transforms='
      strip_unused_nodes(type=float, shape="1,299,299,3")
      fold_constants(ignore_errors=true)
      fold_batch_norms
      fold_old_batch_norms
      round_weights(num_steps=256)'
作为进一步的步骤，您可以直接将权重存储为eight-bit 值： 
    
    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul' \
    --outputs='softmax' \
    --transforms='
      strip_unused_nodes(type=float, shape="1,299,299,3")
      fold_constants(ignore_errors=true)
      fold_batch_norms
      fold_old_batch_norms
      quantize_weights'
简化上述步骤，使用obfuscate_names transform,出了inputs outputs都可以代替:

    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul:0' \
    --outputs='softmax:0' \
    --transforms='
      obfuscate_names'
### 8.Eight-bit Calculations
有时eight-bit的计算方式要比浮点型更好, 可以按如下方式将模型转化为量化形式

    bazel build tensorflow/tools/graph_transforms:transform_graph
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
    --in_graph=tensorflow_inception_graph.pb \
    --out_graph=optimized_inception_graph.pb \
    --inputs='Mul' \
    --outputs='softmax' \
    --transforms='
      add_default_attributes
      strip_unused_nodes(type=float, shape="1,299,299,3")
      remove_nodes(op=Identity, op=CheckNumerics)
      fold_constants(ignore_errors=true)
      fold_batch_norms
      fold_old_batch_norms
      quantize_weights
      quantize_nodes
      strip_unused_nodes
      sort_by_execution_order'
### 9.example
第3小节的实例应用
如开始所说，首先下载graph transform tools ，在其所在的目录运行

    bazel build tensorflow/tools/graph_transforms:transform_graph
经过漫长的等待后，
    
    bazel-bin/tensorflow/tools/graph_transforms/transform_graph \
     --in_graph=~/rm/inception-2015-12-05/classify_image_graph_def.pb \
     --out_graph=~/mace/tensorflow/optimized_classify_graph.pb \
    --inputs='Mul:0' \
    --outputs='softmax:0' \
    --transforms='
    strip_unused_nodes(type=float, shape="1,299,299,3")
    remove_nodes(op=Identity, op=CheckNumerics)
    fold_old_batch_norms
    '
其中`in_graph`表示你的模型文件所在位置，`out_graph` 表示你所优化后模型的位置，名称等。结果如下图
![](imgs/20180724-191221.png)