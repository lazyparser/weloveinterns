# CNNDroid尝试报告
CNNDroid是一个开源的，把神经网络移植到Android上的框架。它把在性能良好的机器上训练好的模型转换成为自己的格式，并且在移动设备上使用。[这里是它的Github地址。](https://github.com/ENCP/CNNdroid)

Github根目录里面有一个CNNdroid Complete Developers Guide and Installation Instruction.pdf，详细的说明了框架的用法。首先你要用项目提供的python脚本把原来的CNN模型（支持caffe，Theano，Torch，没有TensorFlow）转换成框架需要的格式。之后调用框架的API去加载模型做出预测。Github上提供了几个训练并且转换好的模型，我就没有做第一步。框架封装的很好，调用非常简单。但是我还是踩了几个坑，在这里说一说。

第一个大坑！Github上提供了一些Demo，但是这些Demo都是运行不了的。问题大概出在Android的调用上，并非框架本身的问题。我花了好几天调试这些Demo，蛋痛的很。后来自己写了一个，放在[Gtihub](https://github.com/nephashi/cnndroid_demo)上。在AVD里跑大概长这样。

![image](/resources/Image/CNNDroid/demo_appearance.png)

不要嫌我的UI丑TAT。这是用CIFAR10模型预测图片的示例。点一下Start加载参数，点一下compute从资源里加载一张静态图片并且预测，输出预测结果。运行这个demo之前，先把框架给出的Data_Cifar10文件夹放到sdcard根目录下，确保能读到这些文件。

配套我这个Demo，稍微讲解一下调用好了。首先是Start的按钮的Listener。据说把加载模型的代码直接放里面会炸，我就放在asyncTask里跑。这个类是Android的类，在这里是主活动的内部类。提供异步的执行功能，防止耗时的运算阻塞UI线程。具体调用百度一下就知道啦。大概理解就是开个线程，加载参数，完成。嗯。


```
startAsyButton.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        prepareModel asyncTask = new prepareModel();
        asyncTask.execute();
    }
});
```


```
private class prepareModel extends AsyncTask<RenderScript, Void, CNNdroid> {

    @Override
    protected void onPreExecute() {
        textView.setText("加载网络模型参数中");
    }

    @Override
    protected CNNdroid doInBackground(RenderScript... params) {
        loadTime = System.currentTimeMillis();
        try {
            //myConv是主活动的成员变量
            myConv = new CNNdroid(myRenderScript, "/sdcard/Data_Cifar10/Cifar10_def.txt");
        } catch (Exception e) {
            e.printStackTrace();
        }
        loadTime = System.currentTimeMillis() - loadTime;
        return myConv;
    }

    @Override
    protected void onPostExecute(CNNdroid model) {
        textView.setText("加载结束");
    }
}
```

接下来是预测的代码。这段代码是我从框架自带的Demo里抄的。大概就是读图片，搞成三通道的形式，然后预测。


```
computeButton.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Bitmap img = getImgRes("bird");
        Bitmap scaled = Bitmap.createScaledBitmap(img, 32, 32 ,false);

        ParamUnpacker pu = new ParamUnpacker();
        float[][][] mean = (float[][][]) pu.unpackerFunction("/sdcard/Data_Cifar10/mean.msg", float[][][].class);

        float[][][][] inputBatch = new float[1][3][32][32];
        for (int j = 0; j < 32; ++j)
            for (int k = 0; k < 32; ++k) {
                int color = scaled.getPixel(j, k);
                inputBatch[0][0][k][j] = (float) (blue(color)) - mean[0][j][k];
                inputBatch[0][1][k][j] = (float) (green(color)) - mean[1][j][k];
                inputBatch[0][2][k][j] = (float) (red(color)) - mean[2][j][k];
            }

        float[][] output = (float[][]) myConv.compute(inputBatch);
        textView.setText(accuracy(output[0], labels, 3));
    }
});
```

我遇到的第二个坑是关于Android文件系统的。如果和我一样以前没玩过Android，这个可能对你有用。Android的文件系统分内存和外存，外存也就是sdcard。Demo里的模型文件是放在外存里的。

首先要在Android Studio AVD管理器里配置好sdcard。其次Android Studio没有提供管理文件系统的功能。需要在虚拟手机上下一个se文件管理器。从虚拟手机导出和导入文件也需要使用adb工具。另外关于路径引用的问题，Android sdcard引用路径千奇百怪的，但一般可以用两种方法拿到sdcard文件：

```
File file = new File("/sdcard/Data_Cifar10/labels.txt");
```

```
File file = new File(Environment.getExternalStorageDirectory(),"Data_Cifar10/labels.txt");
```
如果你对得到的对象调用getAbsolutePath()，得到的可能和你的输入参数不一样。

还有一个大坑，就算你在AndroidManifest里配置了读写权限，有的手机还需要在setting里手动授权！
