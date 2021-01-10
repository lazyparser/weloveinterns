## ROS程序包创建

`catkin_create_pkg pkg_name std_msgs roscpp rospy OTHER_PACKAGE`

使用该指令创建一个新的程序包之后，会在指令运行目录下生成pkg_name的文件夹，即ROS程序包的基础模板。

## package.xml文件标准模板

使用者可以参考ros 包的package.xml文件的模板：

[ros_package_template](https://yt.droid.ac.cn/beijing/weloveinterns/blob/master/droid_coding_norm/ros_package_template.xml)

```xml
<?xml version="1.0"?>
<package format="2">
  <name>package_name</name>
  <version>1.0.0</version>
  <description>此处对该ROS程序包做一个简单的描述</description>

  <!-- One maintainer tag required, multiple allowed, one person per tag -->
  <!-- Example:  -->
  <!-- <maintainer email="jane.doe@example.com">Jane Doe</maintainer> -->
  <!-- 必须有维护者，因为上传ROS后其CI会通过该邮箱联系维护者 -->
  <maintainer email="wangpeng@droid.ac.cn">rocwang</maintainer>


  <!-- One license tag required, multiple allowed, one license per tag -->
  <!-- Commonly used license strings: -->
  <!--   BSD, MIT, Boost Software License, GPLv2, GPLv3, LGPLv2.1, LGPLv3 -->
  <!-- 必须有，否则不通过ROS的CI -->
  <license>BSD</license>


  <!-- Url tags are optional, but multiple are allowed, one per tag -->
  <!-- Optional attribute type can be: website, bugtracker, or repository -->
  <!-- Example: -->
  <!-- 可选，一般链接到所创建的wiki ros 包页面 -->
  <url type="website">http://wiki.ros.org/package_name</url>


  <!-- Author tags are optional, multiple are allowed, one per tag -->
  <!-- Authors do not have to be maintainers, but could be -->
  <!-- Example: -->
  <!-- 可选，不一定是维护者 -->
  <author email="wangpeng@droid.ac.cn">rocwang</author>


  <!-- The *depend tags are used to specify dependencies -->
  <!-- Dependencies can be catkin packages or system dependencies -->
  <!-- Examples: -->
  <!-- Use depend as a shortcut for packages that are both build and exec dependencies -->
  <!--   <depend>roscpp</depend> -->
  <!--   Note that this is equivalent to the following: -->
  <!--   <build_depend>roscpp</build_depend> -->
  <!--   <exec_depend>roscpp</exec_depend> -->
  <!-- Use build_depend for packages you need at compile time: -->
  <!--   <build_depend>message_generation</build_depend> -->
  <!-- Use build_export_depend for packages you need in order to build against this package: -->
  <!--   <build_export_depend>message_generation</build_export_depend> -->
  <!-- Use buildtool_depend for build tool packages: -->
  <!--   <buildtool_depend>catkin</buildtool_depend> -->
  <!-- Use exec_depend for packages you need at runtime: -->
  <!--   <exec_depend>message_runtime</exec_depend> -->
  <!-- Use test_depend for packages you need only for testing: -->
  <!--   <test_depend>gtest</test_depend> -->
  <!-- Use doc_depend for packages you need only for building documentation: -->
  <!--   <doc_depend>doxygen</doc_depend> -->


  <!-- 以下根据自己的包实际依赖更改 -->

  <!-- buildtool_depend -->
  <buildtool_depend>catkin</buildtool_depend>


  <!-- build computer language depend -->
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>

  
  <!-- build ros tool depend -->
  <build_depend>nodelet</build_depend>
  <build_depend>pluginlib</build_depend>
  <build_depend>message_filters</build_depend>
  <build_depend>actionlib</build_depend>
  <build_depend>kdl_conversions</build_depend>
  
  <!-- build msg depend -->
  <build_depend>std_msgs</build_depend>
  <build_depend>nav_msgs</build_depend>
  <build_depend>geometry_msgs</build_depend>
  <build_depend>actionlib_msgs</build_depend>
  <build_depend>xbot_msgs</build_depend>


  <!-- build ecl depend   -->
  <build_depend>ecl_threads</build_depend>
  <build_depend>ecl_geometry</build_depend>
  <build_depend>ecl_linear_algebra</build_depend>



  <!-- build export computer language depend -->
  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>rospy</build_export_depend>

  
  <!-- build export ros tool depend -->
  <build_export_depend>nodelet</build_export_depend>
  <build_export_depend>pluginlib</build_export_depend>
  <build_export_depend>message_filters</build_export_depend>
  <build_export_depend>actionlib</build_export_depend>
  <build_export_depend>kdl_conversions</build_export_depend>
  
  <!-- build export msg depend -->
  <build_export_depend>std_msgs</build_export_depend>
  <build_export_depend>nav_msgs</build_export_depend>
  <build_export_depend>geometry_msgs</build_export_depend>
  <build_export_depend>actionlib_msgs</build_export_depend>
  <build_export_depend>xbot_msgs</build_export_depend>


  <!-- build export ecl depend   -->
  <build_export_depend>ecl_threads</build_export_depend>
  <build_export_depend>ecl_geometry</build_export_depend>
  <build_export_depend>ecl_linear_algebra</build_export_depend>



  <!-- exec computer language depend -->
  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>

  
  <!-- exec ros tool depend -->
  <exec_depend>nodelet</exec_depend>
  <exec_depend>pluginlib</exec_depend>
  <exec_depend>message_filters</exec_depend>
  <exec_depend>actionlib</exec_depend>
  <exec_depend>kdl_conversions</exec_depend>
  
  <!-- exec msg depend -->
  <exec_depend>std_msgs</exec_depend>
  <exec_depend>nav_msgs</exec_depend>
  <exec_depend>geometry_msgs</exec_depend>
  <exec_depend>actionlib_msgs</exec_depend>
  <exec_depend>xbot_msgs</exec_depend>


  <!-- exec ecl depend   -->
  <exec_depend>ecl_threads</exec_depend>
  <exec_depend>ecl_geometry</exec_depend>
  <exec_depend>ecl_linear_algebra</exec_depend>

  



  <!-- The export tag contains other, unspecified, tags -->
  <export>
    <!-- Other tools can request additional information be placed here -->
    <!-- 如果使用到ros nodelet封装，则需要这个以及该目录下的文件 -->
    <nodelet plugin="${prefix}/plugins/nodelet_plugins.xml"/>
  </export>
</package>
```


记得重命名该文件为package.xml并替换所创建的pkg_name项目内部的同名文件，替换后修改文件对应部分的内容。

## 内容要求

* 给出程序包版本

* 给出程序包的简单介绍

* 给出维护者邮箱信息，有公司邮箱的必须填写公司邮箱

* 填写license，公司默认开源软件使用BSD协议，闭源软件则按实际情况填写

* 修改作者信息，可以与维护者不同

* 注意修改build depend等内容，按照实际ROS包的需要修改。

## gitlab CI建议

建议按照以上规则验证所有上传代码的信息，不符合要求者打回更改。

以上规则是对[ROS官方平台对编码规范要求](http://wiki.ros.org/DevelopersGuide)的补充。


## 参考规范

[ROS官方平台对编码规范要求](http://wiki.ros.org/DevelopersGuide)
