# 实习生岗位

全职员工的招聘可以 从 [PLCT-Weekly 仓库找到](https://github.com/plctlab/PLCT-Weekly/blob/master/Jobs.md)。

如果你是即将毕业的应届生，欢迎按照下属方式投递简历，应届生也可以走实习生的招聘通道。

## 如何正确的投递简历

在投递简历之前最好对我们有更多一点了解。以下是阅读材料：

- [极简项目管理](https://github.com/lazyparser/minimalist-team-leader) 是目前PLCT实验室的管理方式，实习生也在管理范围内。请先阅读。
- [我们如何进行实习生招聘](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-interview-interns.md)
- [我们如何对实习生进行能力评定和培养](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)
- [实习生生存手册](https://github.com/lazyparser/survivial-manual-for-interns) 目前还在断断续续的撰写中，欢迎围观和贡献PR (Pull Requests)

阅读之后，接下来就可以发邮件了。以下内容请认真阅读。不符合条件邮件不会收到回复。

有意者请投递简历至：
**吴老师 wuwei2016@iscas.ac.cn**

邮件标题请注明：
**岗位编号 - 姓名 - 手机号码 - 学校**

（兼职实习的伙伴可以用【兼职】取代【学校】）

邮件正文请:
**进行跟应聘职位相关的自我介绍**，不超过300字。

邮件必须附带简历。**没有PDF格式简历的邮件不保证会收到回复**。

## 实习生共性要求和注意事项

开放岗位的入职要求（教学助理等非技术类的同学只需要满足前两条）：

1. 良好的沟通理解能力、能够观察和感知他人的态度和观点。能够主动沟通、遇到计划外或坏消息能够大声的说出来。
2. 知道如何陈述bugs/issues以及向其他人求助，如何不浪费同事的时间，将复现bug需要的信息提供完整。
3. 能力值评定一般要求达到LV2级别及以上。参见：[我们如何面试实习生](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-interview-interns.md)，[我们如何给实习生评级](https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)。
4. 热爱编程，经常写代码。C/C++/Java/JavaScript 任何一种常见语言都可以。
5. 熟练使用 Linux 命令行；会一点 Python/Bash 脚本进行自动化。
6. 熟练使用 Google 搜索引擎、流畅高清看油管。
7. 熟练使用 Git，能够自己 rebase 解决 conflicts。
8. （加分）自学了 RISC-V 指令集，包括 RV32GC 和 RV64GC。在自己的电脑上部署运行起来QEMU-RISCV64以及Spike模拟器。
9. （加分）对于网络知识有基本了解并熟练使用，例如SSH任意端口登陆、Port Forwarding、反向链接、ProxyCommand 等配置自行掌握。
10. 自律性强，能够独立展开工作。PLCT实验室全员远程工作，不需要坐班，也没有工位提供。
11. 需要注意开源社区都是个人出道，所有的行为都是公开的，要有一颗大心脏。
12. 劳务费每个月根据产出浮动，浮动区间 0k - 5k，正常产出一般是税前 2k-3k 之间。厉害的产出/任务另算。

其他说明：所有岗位默认都是远程实习，支持全球实习工资支付（中国学生必须是国内银行卡，与软件所北京本部签约需要建设银行卡）。实习随时可以开始随时可以暂停随时可以结束（如果超过一周旷工、或八周没有外部可见产出会被劝退）。

## PLCT Lab 的实习生岗位

PLCT全称是程序语言与编译技术实验室，隶属于中科院软件所智能软件研究中心（ISRC），致力于成为编译技术领域的开源领导者，推进工具链及运行时系统等软件基础设施的技术革新， 具备主导开发和维护重要基础设施的技术及管理能力。与此同时，致力于培养一万名编译领域尖端人才，推动先进编译技术在国内的普及和发展。

(Next Job ID: 110)

### OC109 QtRVSim 开发实习生（远程，2-3名）

岗位介绍：

为 https://github.com/cvut/qtrvsim 添砖加瓦。PLCT实验室与该开源项目作者建立了初步的合作联系。

实习内容：

注意部分内容有可能已经完成了，请务必在开始之前联系PLCT实验室进行沟通。

- https://github.com/cvut/qtrvsim/issues/1
- https://github.com/cvut/qtrvsim/issues/2

TL;DR of the topics (in random order):

- finish porting more complex unit tests and extend them
- compressed ISA support
- 64bit ISA support in gui (it is hard to fit it there)
- DWARF location display (when C code is simulated)
- declarative specification of (at least simple) pseudoinstructions (for both encoding and decoding). Right now, it is a special case for compilation only.
- detail view of instruction encoding
- recording of pipeline utilization with visualization like this (https://image.slidesharecdn.com/chapter4theprocessor-100520050519-phpapp01/95/chapter-4-the-processor-55-728.jpg?cb=1274344463)
- time travel debugging ("step back" ability, probably for basic components only, not memory, peripherals...)

岗位要求：

1. LV3及以上。
2. 熟练英文文字交流。
3. 懂得礼貌友好的进行英文社区沟通。

### BJ108 RISC-V 测试实习生（北京坐班，名额5人）

岗位介绍：

中国科学院软件研究所PLCT团队开发和维护着包括 openEuler RISC-V 在内的多个 Linux 发行版。为了保证 RISC-V 平台用户的使用体验，在操作系统的自动化测试之外，需要大量的进行物理设备上的测试验证。本岗位的工作内容是借助于 ISCAS RISC-V Lab 中丰富的 RISC-V 开发板和计算机，对包括 openEuler、 RevyOS、 RT-Thread 在内的多种操作系统进行实际的安装、使用、测试，并验证浏览器、办公软件等常用软件在 RISC-V 上的运行稳定性。

实习内容：

1. 根据测试要求，将 openEuler 等多款操作系统安装在 Pioneer Box、 LicheePi 4A 等 RISC-V 设备上，并测试功能可用性、稳定性、性能。
2. 评审和修改完善相关的技术文档。
3. 参与测试用例的撰写，包括手工测试用例和自动化测试脚本等。
4. 参与技术分享，包括中文和英文会议的发言等。
5. 工作突出的同学有机会代表测试小队在各类 RISC-V 会议上进行演讲。

岗位要求和说明：

1. 需要达到 LV2 能力等级，并且没有在软件所实习过。
2. 做事细心不浮躁，写文档有耐心。
3. 在投递简历之前，需要已经自学过 RISC-V 是什么，并且能够在 Linux 环境下的 QEMU 上跑起来 openEuler RISC-V。
4. 要求北京学校在校大学生，可以来软件所北京本部坐班，工作日每周至少2天。实习生费用按照出勤天数（100元/天）+外部可见产出（可变）叠加的方式。
5. 注意不提供住宿和任何补助，北京以外其他城市同学可以看看其他岗位信息，基本都是可以远程的。

### BJ107 DynamoRIO RISC-V 移植开发实习生（1 人）

岗位介绍：

DynamoRIO 是一个运行时的二进制动态插桩系统，广泛地用于程序的分析、模拟、优化以及性能评估等等。目前 DynamoRIO 的核心模块已经支持 RISC-V，但仍有大量工作需要推进。

实习内容：

和 mentor 一起参与 DynamoRIO for RISC-V 的开发，并将自己的工作直接提交到上游。

岗位要求：

1. 基础能力 Lv2 及以上；
2. 对 RISC-V 指令集有一定了解；
3. 可以流畅书写和阅读英文；
4. 投递简历之前，我们希望你已经了解并尝试使用过 DynamoRIO。

### BJ106 openEuler RISC-V 操作系统开发实习生

岗位介绍:

参与 openEuler 官方 risc-v sig 的维护工作，包含 compiler sig 的 LLVM 平行宇宙计划 RISC-V 方向实习生。

实习内容：

1. 跟踪 openEuler 在 RISC-V 架构的软件包构建情况并进行修复
2. 参与以 llvm 构建发行版的「LLVM 平行宇宙计划」的软件包构建情况、进行尝试性修复与提交
3. 协助 maintainer 调研并解决 oerv 系统 issue
4. 构建并丰富openEuler软件生态，参加社区 SIG 组开源运作
5. 调研分析操作系统领域最新动向和前沿技术，结合产品场景应用落地

岗位要求:
1. 基础能力 Lv2 及以上。
2. 对 linux 发行版有一定使用经验。
3. 掌握中文普通话、英文[通常要求 CET4/6 通过]。
4. 微信响应速度快，每周7天中至少能够有3天、工作时间有至少连续3个小时在线一起工作。

### BJ105 ART 虚拟机性能评测实习生

岗位介绍：
本岗位是 PLCT 实验室与 OPPO 开源及产学研合作等团队合作招募的岗位。

实习内容介绍：

1. 建立开源的ART虚拟机性能benchmark套件，对标google不开源的golem。希望在分析主流app的负荷之后，依据重要性和热度逐渐建立各项测试指标。大体上可以拆分成两个阶段。第一个阶段就单纯是分析，合作厂商列一些核心应用的核心场景，先调研当前ART虚拟机的性能状态，涉及的哪些功能、基础库会影响到性能表现。第二个阶段，再根据第一阶段的结果，根据重要性来写对应的benchmark。
2. 性能对比分析。扩展https://github.com/dsrg-uoft/LangBench使其支持swift，对比swfit、java on ART和java on OpenJdk三者的性能(对比方法和粒度参考https://www.usenix.org/conference/atc22/presentation/lion)
3. LLVM编译VM语言代码能力调研。对比分析 llvm中statepoint机制的代码生成结果 和 ART虚拟机的代码生成结果，给出LLVM当前支持VM语言的功能和性能状态。


岗位要求：
- 基础能力 LV3 及以上。

### BJ104 SG2042 数据库移植实习生（20230912 开放 10 名）

岗位介绍：
SG2042 是一款高性能  RISC-V 处理器，具有 64 个 RISC-V 核心。 该岗位招募实习生帮助移植常见的数据库系统到基于 SG2042 的 Pioneer Box 等设备上。

工作内容：
- 构建、移植、测试运行在 Pioneer Box 上的各类开源数据库，包括
  - TiDB (≥1)
  - OceanBase (≥1)
  - GaussDB (≥1)
  - TDSQL (≥1)
  - MySQL (1) 测试为主
  - PostgreSQL (1) 测试为主
- 建立维护CI测试监控体系，及时检测和处理软硬件适配问题和软件依赖问题等。
- 撰写社区宣传文章、开源活动申请书等。
- 组织社区会议和活动，开源项目每周同步 / 社区伙伴月度分享。

岗位要求：
- 基础能力 LV3 及以上。
- 掌握中文普通话、英文。
- 具备数据库理论知识（本科优等水平）。
- 微信响应速度快，每周7天中至少能够有3天、工作时间有至少连续3个小时在线一起工作。

### BJ103 SG2042 操作系统开发实习生（20230912 开放 50 名）

岗位介绍：
SG2042 是一款高性能  RISC-V 处理器，具有 64 个 RISC-V 核心。 该岗位招募实习生帮助移植常见的操作系统到基于 SG2042 的 Pioneer Box 等设备上。

工作内容：
- 构建、移植、测试运行在 Pioneer Box 上的各类操作系统，包括
  - Arch Linux (10)
  - RevyOS (Debian) (10)
  - Gentoo (5)
  - Fedora (5)
  - Deepin, UOS (5)
  - openEuler (3)
  - openKylin (3)
  - OpenAnolis (3)
  - 中标麒麟 (3)
  - FreeBSD and others (3)
- 建立维护CI测试监控体系，及时检测和处理软硬件适配问题和软件依赖问题等。
- 撰写社区宣传文章、开源活动申请书等。
- 组织社区会议和活动，开源项目每周同步 / 社区伙伴月度分享。

岗位要求：
- 本岗位面向首次实习的新人。已经在PLCT实验室或TARSIER实习过的同学请挑战其他更难的岗位。
- 基础能力 LV2 及以上。
- 掌握中文普通话、英文。
- 微信响应速度快，每周7天中至少能够有3天、工作时间有至少连续3个小时在线一起工作。
- 遵守良好的社交礼仪，在开源社区交流中能够高度自律，不引战，不应战；遇到计划外坏消息及时团队同步应对。
- 请知悉本岗位的招募评价标准按照每个发行版细分方向有各自独立的 mentor 考核要求。

### BJ102 Buddy Compiler 开源社区运营助理实习生

工作内容：
- 跟踪 Buddy Compiler PR 和 Issue 信息，保障社区仓库的稳定性和响应实时性。
- 建立维护监控体系，及时检测和处理软硬件适配问题和软件依赖问题等。
- 每周围绕 MLIR 和 RISC-V 进行全网资料收集和情报整理。
- 撰写社区宣传文章、开源活动申请书等。
- 组织社区会议和活动，开源项目每周同步 / 社区伙伴月度分享。

岗位要求：
- 基础能力 LV2 及以上。
- 掌握中文普通话、英文。
- 微信响应速度快，每周至少能够有3天、工作时间有至少连续4个小时在线一起工作。

### BJ101 FORCE-RISCV 开发实习生（20230909 开放 3 名）

**工作内容描述**

基于 FORCE-RISCV 动态指令发生器的 litmus 用例编译工具链。

FORCE-RISCV 是 RISC-V 领域重要的动态指令集发生器，提供大型 server 级别 cpu 的完整验证交付能力。Litmus 是 memory model 架构探索的重要工具，是多核 memory model 方面的核心工具。本任务基于 FORCE-RISCV 前端 Python API，建立编译工具链，将 litmus test 转译到 FORCE-RISCV 平台上。

**岗位职责**

基于FORCE-RISCV前端Python API，建立编译工具链，将litmus test转译到FORCE-RISCV平台上：
1. 负责编译python编译工具链，将litmus用例转译为FORCE-RISCV的templates
2. 负责相关regression管理工具的开发

**岗位要求**

0. 基础能力 LV3 及以上
1. 对编译原理有基本了解
2. 熟悉python编程
3. 熟悉CPU验证基本流程
4. 对CPU验证工具、指令发生器有经验者优先

### BJ100 RISC-V nettle 开发实习生 (20230901 开放 3 名)

工作内容：
- 建立性能测评环境并进行持续跟踪（后续合并进入 PLCT RISC-V PTS）。
- 给 nettle 补充 RISC-V 支持，使用 Crypto Scalar 和 Vector 等扩展指令进行加速，并且尝试进行 upstream。
- 搭建 for RISC-V 的回归测试环境。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。（LV2）

岗位要求：
- 基础能力 LV3 及以上。
- C/C++、计算机本科各类基础课原理扎实，自学掌握能力强。

### BJ99 RISC-V OpenSSL 开发实习生 (20230901 开放 2 名)

工作内容：
- 建立性能测评环境并进行持续跟踪（后续合并进入 PLCT RISC-V PTS）。
- 基于openssl算法库，对加解密算法 aes、rsa、sm2、 sm3、 sm4、 md5、 sha、 des、 使用 crypto vector 扩展指令进行加速，并且尝试进行 upstream。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。（LV2）

岗位要求：
- 基础能力 LV3 及以上。
- C/C++、计算机本科各类基础课原理扎实，自学掌握能力强。

### BJ98 Flutter RISC-V 开发实习生 (20230901 开放 2 名)

工作内容：
- 调研分析 Flutter 在 RISC-V Linux 下的适配现状和缺失能力部分，及其应用辐射范围（LV2）
- 进行必要的 RISC-V Porting （LV4+）
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。（LV2）

岗位要求：
- 基础能力 LV3 及以上。
- C/C++、计算机本科各类基础课原理扎实，自学掌握能力强。

### BJ97 Milk-V Duo IDE 开发实习生（20230809 开放 3 名）

工作内容：
- 基于 VSCode 进行二次（插件）开发，为 Milk-V Duo 提供常用的编辑、编译、调试、管理、配置能力。
- 开发扩展 Duo 相关的代码示例。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- C/C++、计算机本科各类基础课原理扎实，自学掌握能力强。
- （加分）玩过各种嵌入式小物件；最好是摸过电焊（大学课程里的也算）；最好是调试过多线程程序或者内核。
- （加分）有设计或美工软件使用的经验（画了点图标、P过自己照片都算）。
- 微信响应速度快、自驱力强。

### BJ96 Milk-V Duo SDK 开发实习生（20230809 开放 3 名）

工作内容：
- 整理目前 Duo 相关的文档和 Demo，进行验证和完善、扩充。
- 探索 Duo 中大小核的各类玩法，输出 Demo 和技术分享。
- MicroPython 支持； RT-Thread 支持。
- 参与英文会议，跟全球社区开发者 battle。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- C/C++、计算机本科各类基础课原理扎实，自学掌握能力强。
- （加分）玩过各种嵌入式小物件；最好是摸过电焊（大学课程里的也算）；最好是调试过多线程程序或者内核。
- 微信响应速度快、自驱力强、自己喜欢写 Kernel 代码。

### BJ95 Milk-V Duo Linux Kernel 开发实习生（20230809 开放 1 名）

工作内容：
- 写代码，帮助 Milk-V Duo / CV1800 进入 Linux Kernel 主线
- 写文档、做技术分享和讨论。
- 参与英文会议，跟全球社区开发者 battle。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- 玩过 kernel 代码，熟练 debugging。
- 微信响应速度快、自驱力强、自己喜欢写 Kernel 代码。

额外说明事项：
- 劳务费每个月根据产出浮动，浮动区间 0k - 5k，正常产出一般是税前 2k-3k 之间。不算高。 **完成牛x的 upstream 任务另外以 1w 为单位叠加**

### BJ94 Milk-V Duo Buildroot 开发实习生（20230809 开放 1 名）

工作内容：
- 写代码，帮助 Milk-V Duo / CV1800 进入 Buildroot 主线。
- 写文档、做技术分享和讨论。
- 参与英文会议，跟全球社区开发者 battle。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- 在投递简历之前已经尝试玩过 Buildroot， 在 RISC-V 设备上跑起来 Buildroot 构建的系统， 尝试修改过一点代码。
- 微信响应速度快、自驱力强、自己喜欢倒腾。


### BJ93 Milk-V Duo Yocto 开发实习生（20230809 开放 1 名）

工作内容：
- 写代码，帮助 Milk-V Duo / CV1800 进入 Yocto 主线。
- 写文档、做技术分享和讨论。
- 参与英文会议，跟全球社区开发者 battle。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- 在投递简历之前已经尝试玩过 Yocto， 在 RISC-V 设备上跑起来 Yocto 构建的系统， 尝试修改过一点代码。
- 微信响应速度快、自驱力强、自己喜欢倒腾。

### BJ92 Milk-V Duo OpenWRT 开发实习生（20230809 开放 1 名）

工作内容：
- 写代码，帮助 Milk-V Duo / CV1800 进入 OpenWRT 主线。
- 写文档、做技术分享和讨论。
- 参与英文会议，跟全球社区开发者 battle。
- 根据自己的兴趣参与本地或同城高校的 RISC-V 技术交流推广活动。

岗位要求：
- 基础能力 LV3 及以上。
- 在投递简历之前已经尝试将 OpenWRT 在 RISC-V 设备上跑起来。
- 微信响应速度快、自驱力强、自己喜欢写操作系统代码。

### BJ91 开源社区运营助理（LicheePi 4A 等 RISC-V SBC）实习生（20230801开放， 共 1 名）

工作内容：
- 围绕 LicheePi 4A 建设开源社区，每周进行全网资料收集和情报整理。进行测试和验证。
- 中译英、英译中；为新闻稿撰写摘要（缩写文章）；
- 每个月偶尔组织线上会议，或者（更为少见的）自己本校区/城市范围内的 meetup。

岗位要求：
- 基础能力 LV2 及以上。
- 掌握中文普通话、英文。
- 微信响应速度快，每周至少能够有3天、工作时间有至少连续4个小时在线一起工作。

### BJ90 开源社区运营助理（SG2042 and Duo）实习生（20230801开放， 共 3 名）

工作内容：
- 围绕 SG2042 开源社区，每周进行全网资料收集和情报整理，汇总为 [SG2042 Newsletter](https://github.com/sophgocommunity/SG2042-Newsletter)，每周五发布一次。
- 中译英、英译中；为新闻稿撰写摘要（缩写文章）；
- 参与社区技术人员沟通，收集反馈信息、发放问卷等（中英双语）；
- 每个月偶尔组织线上会议，或者（更为少见的）自己本校区/城市范围内的 meetup。

岗位要求：
- 基础能力 LV2 及以上。
- 掌握中文普通话、英文。
- 加分：掌握日语、韩语、俄语、德语、法语、西班牙语中的任何一个。
- 加分：掌握闽南语、吴语、上海话等方言。
- 微信响应速度快，每周至少能够有3天、工作时间有至少连续4个小时在线一起工作。

### BJ89 编译器功能支持实习生（2人）

岗位名称：
编译器功能支持实习生

工作内容：
完成rvv0.7.1 汇编器以及intrinsic功能支持。具体：

- 需要根据rvv0.7.1 spec在llvm的riscv后端完成汇编器支持。
- 根据rvv0.7.1 intrinsic 标准，完成llvm和clang的intrinsic支持.
- 完成功能开发阶段的单元测试编写，改写目前rvv-intrinsic-doc的测试用例使之适用于rvv0.7.1。

报名要求：
1. LV3及以上；熟练使用脚本语言，shell/python 等。
2. 熟悉 LLVM 编译器，熟悉 riscv 架构。
3. 了解rvv指令集，以及intrinsic.
3. 有过intrinsic开发经验的优先。

### BJ88 RISC-V SAIL 开发实习生【暂停招聘】

工作内容：

- 参与PLCT实验室在SAIL等相关开源项目的开发。在开源社区直接提交代码。

入职要求：

- LV3+，对RISC-V形式化模型的内部实现有兴趣。
- 远程实习，不需要坐班。


### BJ87 RISC-V ACT 开发实习生【暂停招聘】

工作内容：

- 参与PLCT实验室在ACT（riscv-arch-test）等相关开源项目（包括riscof/riscv-isac/riscv-ctg等）的开发。在开源社区直接提交代码。

入职要求：

- LV2+，对RISC-V架构测试有兴趣。
- 远程实习，不需要坐班。

### HZ86 CXL开源硬件IP开发【暂停招聘】

(NOTE: 这是由 DatenLord 提供外部 mentor 支持的联合培养实习岗位）

岗位职责
参与CXL协议开源硬件IP开发：
1. 负责CXL.io、CXL.cache、CXL.mem协议的RTL实现；
2. 负责开源IP的综合与原型验证；
3. 撰写相关设计和接口文档（英文）。

岗位要求：

基本要求：
1. 熟悉数字IC的开发工具链；
2. 熟悉Bluespec、SpinalHDL、Chisel或Clash等新一代HDL语言；
3. 熟练掌握Verilog、SystemVerilog或VHDL语言；
4. 熟悉SystemVerilog Assertion的使用；
5. 熟练掌握TCL脚本语言；
6. 具有很强的学习能力，自我驱动以及团队合作意识。

加分项：
1. 熟悉CXL、PCIe、AXI、ACE、CHI、NVMe等协议接口开发优先；
2. 熟悉基于Python的仿真测试工具Cocotb优先；
3. 有形式化验证相关经验优先；
4. 有硬件敏捷开发和验证相关经验优先；
5. 能长期实习优先。

简历投递：pwang@datenlord.com cc wuwei2016@iscas.ac.cn


### HZ85 CXL软硬件联合开发【暂停招聘】

(NOTE: 这是由 DatenLord 提供外部 mentor 支持的联合培养实习岗位）

岗位职责
参与CXL软硬件联合开发与仿真测试：
1. 负责CXL协议接口的硬件仿真实现；
2. 负责CXL协议的相关Linux驱动开发；
3. 负责实现CXL相关软硬件联合调试与自动化测试。

岗位要求
基本要求：
1. 熟悉SystemC等高层次系统建模语言；
2. 熟悉Linux内核模块、驱动的开发；
3. 熟悉基于QEMU的软硬件联合调试工具链；
4. 具有很强的学习能力，自我驱动以及团队合作意识。

加分项：
1. 有RTL开发经验优先；
2. 熟悉CXL、PCIe、AXI、ACE、CHI、NVMe等协议接口开发优先；
3. 熟悉Rust for Linux开发内核模块、驱动；
4. 能长期实习优先。

简历投递：pwang@datenlord.com cc wuwei2016@iscas.ac.cn

### BJ84 RVWhl Python Package 开发实习生【暂停招聘】

【工作内容】
1. 编译以及构建 Python Wheel Package, 目前主要集中在 Linux 平台
2. 开发维护 RVWhl 系统(语言为 Python)
3. 提交 Wheel Package 第三方依赖的兼容 RISC-V 补丁(涉及多种编程语言以及多种编译软件)

【岗位要求】
1. 一年以上 Linux 开发经验，C 语言或 RUST 语言开发经验
2. 熟悉计算机组成原理以及编译原理
3. 了解 Python 语言, 熟悉 Python Package 机制
4. 了解 RISC-V 架构
5. 实习期每个月不少于 14 天的工作日

### BJ83 openEuler操作系统实习开发工程师【暂停招聘】

【工作内容】
1. Linux内核/用户态OS热补丁特性开发
2. OS热补丁特性多架构支持，如RISC-V
3. 构建并丰富openEuler软件生态，参加社区SIG组开源运作
4. 调研分析操作系统领域最新动向和前沿技术，结合产品场景应用落地

【岗位要求】
1. 一年以上Linux开发经验，C语言或RUST语言开发经验
2. 熟悉计算机组成原理以及编译原理
3. 了解Linux内核驱动开发
4. 了解RISC-V架构
5. 实习期三个月以上

### BJ82 实现基于 LoongArch 架构的 RISC-V 模拟器 LARVa 【暂停招聘】

(本岗位为外部社区联合贡献岗位，mentor来自 loongson 社区。)

项目地址：https://github.com/xen0n/larva

工作内容：
- 与 mentor 协作开发基于 LoongArch 架构的 RISC-V 模拟器 LARVa。
- 该项目目前使用 Rust 语言开发，需要有一定 Rust 基础。由于 LoongArch 在 Rust 上游支持很新（截至该职位发布时甚至不完整），有很大机率涉及直接向 Rust 上游贡献适配代码。
- 目前路线图上的短期目标包括实现一个不依赖 LoongArch 的解释执行后端，用于校验 RISC-V 模拟语义，因此暂时没有 LoongArch 知识或硬件也 okay。
- 在 Rust 上游支持开发 LoongArch UEFI 应用之前，工作重心会放在实现 linux-user 模拟上。否则会开始基于 RustSBI 实现完整的 RISC-V 系统级模拟。（这也可能通过一定的方式先在 Linux 环境模拟，但目前没有这方面想法。）
- mentor 会和你一同学习制作架构模拟器。

岗位要求：
- LV3及以上。
- 对指令集架构模拟、虚拟化等技术有基本的了解。
- 对二进制翻译技术、相关的编译原理内容有基本的了解。
- 有一定的 Rust 语言基础。

加分项：

- 读过 LoongArch 手册、相关文档。
- 了解 QEMU、Box64 等类似项目做事情的方式。

### BJ81 RISC-V科研实习生：P扩展在 Linux Kernel 中对解压缩算法等模块的加速可能性研究及原型实现 【暂停招聘】

工作内容：
- 在 Linux Kernel 内核中寻找可以用 P 扩展进行加速的模块（第一步是解压缩模块）
- 根据分析调研的结果，基于香山等开源RISC-V处理器进行扩展，做软硬件协同优化。
- 撰写论文（英文优先）并投递学术杂志发表。

岗位要求：
- LV3及以上。
- 面试之前已经阅读过 RVP 标准草案，可以是 0.5.2 也可以是 0.9.x 的版本。
- 自己编译过 Linux （架构不限），自己做过 LFS 或 CLFS 实践。

论文说明：
- 如果是1位实习生solo，那么该实习生一作；如果是多位实习生，则提前根据分工排序，并根据每个阶段的观测结果决定是否需要调整。
- 通讯作者需要是负责研究思路确定、审稿把关的软件所研究人员（员工）。
- 论文发表前需要软件所作为第一单位审核并确认基金号支持。

### Android(AOSP) RISC-V 移植开发实习生 BJ77~BJ80 【暂停招聘】

基本要求：
- 熟悉 C/C++，熟悉 Shell/Python。
- 对 RISC-V 指令集以及汇编编程有一定了解。
- 对安卓系统基本架构有所了解，了解安卓 build system 和镜像制作等
- 自我能力评定是 [LV3+](https://github.com/plctlab/weloveinterns/blob/master/how-do-we-rank-interns.md)

以下按方向分

- BJ77 LLVM/Clang 方向
  - 对编译链接技术感兴趣。
  - 了解 LLVM / Clang 相关技术。
  - 在 LLVM 上开发过 Clang 和相关组件或者调试过相关问题。

- BJ78 嵌入式开发方向
  - 对 Linux / U-boot / 模拟器 VirtIO 技术等感兴趣。
  - 有过一定的嵌入式开发基础，譬如编译过内核和 U-boot 等。

- BJ79 虚拟机方向
  - 熟悉 Java 语言，对 Java 虚拟机实现原理感兴趣。
  - 了解 OpenJDK 或者 Android ART 内部实现者优先。

- BJ80 底层库性能优化
  - 对性能优化感兴趣，譬如多媒体加速、数据格式压缩、数学浮点运算加速等。
  - 有过 X86(SSEx)/ARM(NEON) 架构相关指令级别优化经验优先。

### BJ76 OpenCV RISC-V P 扩展移植实习生（进行中，名额 2）

工作内容：

- 参与 PLCT 实验室 OpenCV for RISC-V 相关项目的开发，主要包括面向 RVP 扩展的 Universal Intrinsic 后端开发和针对现有 SIMD 优化算法的移植。

入职要求：

- LV2+，熟悉 C++语言，喜欢从事开源软件开发工作。
- 对 RISC-V 指令集和 P 扩展有一定的了解
- 加分项：具有开源项目开发经验，为 OpenCV 或其他开源社区提交过代码
- 加分项：了解SIMD编程模型，使用Intrinsic编写过向量化代码（SSE / AVX / NEON / RVV 等）

### BJ75 OpenJDK 实习生（Lilliput、RISC-V）（进行中，名额 1）

ISCAS Intern Job Description

Add support for Openjdk Lilliput on 64-bit RISC-V

Openjdk Lilliput Project: https://openjdk.org/projects/lilliput/

The goal of this Project is to explore techniques to downsize Java object headers in
the Hotspot JVM from 128 bits to 64 bits or less, reducing Java's memory footprint.
Improved performance across most, if not all, workloads is also expected.

Currently only supports x64 and aarch64 platforms.

Target:
- Port this feature to Linux RISC-V 64-bit platform.
- Pass jtreg tier1-4 regression tests on Linux RISC-V 64-bit HiFive Unmatched board.
- Demonstrate effect on CPU and/or memory usage for Java benchmarks like SPECjvm2008, SPECjbb2015, etc.

报名要求：
1. LV3+
2. 熟练构建 OpenJDK，看过 OpenJDK 内部实现，调研 Lilliput。

### BJ74 编译器性能评测实习生【暂停招聘】

岗位名称：
编译器性能评测实习生

mentor：
廖春玉 等。

工作内容：
搜集开源 benchmarks，用 GCC 和 LLVM 分别编译 benchmark，对比 benchmark 的性能数据。具体：

- 需要使用 GCC 和 Clang 编译 benchmark，对比 benchmark 的指令数和 codesize 等指标。
- 每日用 Clang 编译 benchmark，完善CI；分析自动化脚本的输出，如果指令数和 codesize 比前一天的有所增加提示具体 benchmark 的信息，并保留 log 和 Clang 的 commit IDs.
- 根据需要配置不同版本和配置的本地工具链，随时手动复现结果并进行汇编或 trace 级别的分析。

报名要求：
1. LV3及以上；熟练使用脚本语言，shell/python 等。
2. 熟悉 GCC 和 LLVM 编译器。 能够成功编译并读懂测试集输出的数据。（例如 git@github.com:llvm/llvm-test-suite.git ）
3. 了解 benchmark 的方法学，熟悉创建测试集，比如 spec cpu 2006, coremark 等。
4. 熟练使用 llvm-test-suite，对其实现过外部 benchmark 扩展功能支持的优先。

### BJ73 SystemVerilog编译器工程师(slang to mlir), （进行中，名额 1）

(NOTE: 这是由兆松科技提供外部mentor支持的联合培养实习岗位）

注意：申请者至少需要保证每周投入到项目的时间不少于20小时，不少于半年的连续投入。

职位描述：

- 评估CIRCT框架当中Moore dialect等方言的设计，以及对SystemVerilog的支持情况。
- 基于开源SystemVerilog编译器slang的前端，设计可以生成CIRCT项目当中Moore dialect(或者自定义dialect)的编译器前端。
- 参考CIRCT Moore编译器(rust)的实现，在slang编译器当中实现Moore dialect(或者自定义dialect)的代码生成。


任职要求：

- 扎实的数据结构基础知识，熟练掌握C++，熟练使用C++ STL，最好了解STL实现原理。
- 熟练使用Linux，会编写shell脚本。
- 学习过数字电路，以及最好有编译原理基础知识。
- 足够自信的英语阅读和书写能力，需要和上游无障碍沟通。
- 有LLVM/CIRCT/MLIR开发经验者优先考虑。
- LV3+ 及以上能力等级。

参考信息：

- slang仓库: https://github.com/MikePopoloski/slang
- Moore仓库: https://github.com/fabianschuiki/moore
- CIRCT: https://circt.llvm.org/



### BJ72 eunomia-bpf intern （进行中，名额 2）

(本岗位为外部社区联合贡献岗位，mentor来自 eunomia-bpf 社区。)

[eunomia-bpf](https://github.com/eunomia-bpf/eunomia-bpf) 是一个开源的 eBPF 动态加载运行时和开发工具链，是为了简化 eBPF 程序的开发、构建、分发、运行而设计的基于 libbpf 的轻量级开发框架。使用 eunomia-bpf ，可以在编写 eBPF 程序或工具时只编写内核态代码，自动获取内核态导出信息，或使用 WASM 进行用户态交互程序的开发，在 WASM 虚拟机内部控制整个 eBPF 程序的加载和执行。eunomia-bpf 可以将预编译的 eBPF 程序打包为通用的 JSON 或 WASM 模块，跨架构和内核版本进行分发，无需重新编译即可动态加载运行。

我们已经测试了在 x86、ARM 等不同架构、不同内核版本的 Linux 系统上，对于一个基于 eBPF 的工具或模块，eunomia-bpf 框架都可以使用同一个预编译 eBPF 程序二进制，从云端一行命令获取到本地之后直接运行，不需要类似 BCC 一样再使用 LLVM/Clang 进行本地编译，也能嵌入其他应用中作为插件运行且具有良好的隔离性。我们希望能尝试在 RISC-V 系统上完成移植和测试，实现架构无关的 eBPF 工具的移植和运行。

工作内容:

1. 将 eunomia-bpf 的运行时模块移植到 RISC-V 系统上（主要是 Webassembly 运行时和 libbpf 库）
2. 将 [BCC](https://github.com/iovisor/bcc) 中基于 libbpf 的工具移植到 Webassembly 并进行测试，尝试让编译产物在 RISC-V、x86、ARM 或其他指令集的内核上都可以正常运行；
3. 尝试移植更多 eBPF 的开发框架和工具到 WebAssembly，并为基于 Webassembly 的 eBPF 程序开发和运行提供更多的用户态开发库和工具链；
4. 尝试进行更多基于 eBPF 和 WebAssembly 的相关探索和实现，重构现有的开发框架和工具链，和 WebAssembly、eBPF 相关上游社区进行交流和推进；目前的核心代码量其实很少（~2k），主要使用 C/C++ 完成，我们希望接下来使用 Rust 完成一些重构和重新设计的工作，支持更多的 eBPF 程序类型和相关 API；

岗位要求:

1. 对 WebAssembly 和 eBPF 技术感兴趣，对二者有一些初步的了解或者有一些 demo 尝试（花个一两天看看就好）
2. 了解 C/C++，对于操作系统有一些了解（按照我们在 ARM 上面的经验来说，完成移植工具和测试工作应该不是很困难，预计 LV2 就够？）
3. 了解 BTF 格式信息，了解 Rust 语言，对于 eBPF 的实现机制或 WebAssembly 相关生态有一些深入的理解（可选）

### BJ71 RT-Thread 社区实习生 （3个名额）
RT-Thread诞生于2006年，是一款以开源、中立、社区化发展起来的物联网操作系统。 RT-Thread主要采用 C 语言编写，浅显易懂，且具有方便移植的特性（可快速移植到多种主流 MCU 及模组芯片上）。RT-Thread社区是一个开放、开源的社区。RT-Thread拥有非常丰富的软件包，基于这些软件包可以快速构建产品原型。并且拥有较好的POSIX接口支持，可方便的移植Linux应用。为了更好的服务蓬勃发展的RISC-V生态，我们期望可以将RT-Thread已有的软件生态都很好的对接到RISC-V平台上。同时，RT-Thread Smart微内核系统支持用户态应用程序，rootfs等的构建程序，后面也会积极推进Smart for riscv 版本,也欢迎大家积极参与进来！

RT-Thread相关的工作可以分为三类：A类（MCU）、B类(Smart)、C类(libc)

#### A类（MCU）-工作内容：
- 维护RT-Thread的代码；
- 开发或完善RISC-V架构相关的BSP及驱动；
- 开发或完善测试用例，提升RT-Thread的可维护性；
- 在RISC-V平台上构建良好的POSIX生态，测试并完善POSIX接口支持；
- 在RISC-V平台上构建良好的软件包生态，测试并完善软件包对RISC-V平台上的支持；
- 在RISC-V上搭建基于RT-Thread的Arduino生态；
- 编写文档来介绍RT-Thread&&RISC-V相关的知识，当前的文档在：https://www.rt-thread.org/document/site/#/

#### B类(Smart)-工作内容：
- 参与并推进 RT-Thread Smart for riscv;
- 开发或完善RISC-V架构相关的BSP及驱动；
- 完善应用支持，迁移更多的GNU应用到 RT-Thread Smart for riscv 平台上；
- 完善 Smart for riscv 的 GUI 生态，移植LVGL、Wayland及终端Terminal软件；
- 编写文档来介绍RT-Thread Smart&&RISC-V相关的知识，当前的文档在：https://www.rt-thread.org/document/site/#/

#### C类(libc)-工作内容：
- 一个国际的开源项目：开发维护一套 riscv mcu 下的 mlibc 库;
- 小型化的 libc 库，针对体积做特殊优化;
- 使用这个 mlibc 出一份 riscv 工具链；

#### 岗位要求：
- 电子、计算机、通信、自动控制等专业；
- c语言基础扎实，熟悉计算机体系结构；
- 熟悉一种或数种嵌入式CPU软硬件平台，例如STM32，RISC-V等；
- 有强烈的学习能力和学习新知识的欲望；

### BJ70 Aya 全套生态开发实习生【暂停招聘】

**工作内容**

PLCT Aya 小队致力于研发划时代的类型论实现，包括如何更好地通过元编程技术和约束求解算法来实现程序和证明的自动化生成、如何「正确」地设计一些在学界前沿尚有争议的问题、如何利用当代 OpenJDK 的生态来为这一切打下基石。

0. 实现并参与实现 Aya 的各种语言特性、标准库、工具链（IDE、包管理等）。
2. 追踪相关领域的研究，调研世界上存在的广大竞品（Lean、Arend、Agda、Coq、Idris2 还有蝉语等），并向它们学习、与它们的作者交流。
3. 向 PLCT 输出我们学到的知识，可以是博客或者周会报告的形式。
4. 尽可能解决 Aya 的用户遇到的问题。

**能力要求**

0. 强制要求：PLCT 实习生评级 LV3·强能力者 (https://github.com/lazyparser/weloveinterns/blob/master/how-do-we-rank-interns.md)
  + 对具体编程语言的要求可灵活处理，因为 Aya 的开发也不涉及 Python 等语言。
  + 强制要求：英语读写能力、调试查错能力。
2. 对编程语言理论、函数式编程有一定了解，熟悉至少两门函数式编程语言。
3. 熟悉面向对象编程基本概念、常见设计模式。

*加分项*

0. 阅读编程语言领域的论文，并将相关研究融入 Aya 的实现中。
1. PLCT 实习生评级 LV4·大能力者。
2. 熟悉 JVM 相关技术，包括 IntelliJ 平台、性能调优、字节码生成等。
3. 对文学编程有自己的理解。
4. 对代码质量要求高，对重构持乐观态度。

### BJ69 Deepin RISC-V 操作系统构建实习生【暂停招聘】

**工作内容**

从事 Linux 发行版的软件包构建、测试、分析工作。

**要求**

- LV3+；喜欢从事开源软件开发工作。

需要在提交简历之前，请完成以下工作：

- 在 amd64 或其他架构操作系统架构使用 qemu-user 启动 deepin riscv 发行版 并输出 `neofetch` `bash --version` 截图
- 在此基础上，使用 `apt source bash` 下载对应源码并完成升级版本号 打包并安装 然后输出 `apt policy bash` 与 `bash --version` 截图
  - Tips:
    - 请使用 dpkg-buildpackage 的方式从源码编译 并且需要做到 `可重复构建` 即输出的 `dsc` 也可以再次构建
    - 打包源码 `dsc` 的命令为 `dpkg-source` / 升级deb包版本 `changelog` 的命令为 `dch`
    - 可以参考 [Debian New Maintainers' Guide](https://www.debian.org/doc/manuals/maint-guide/)
- 展示更新 `bash` 的 patch 并输出截图

### BJ65 DynamoRIO 开发实习生（负责 RISC-V 移植及优化）【暂停招聘】

**工作内容**

DynamoRIO 是很优秀的一款开源开发工具。PLCT实验室在2021年初吹的牛/立的FLAG，到2022年下半年还没圆上。围观地址：

https://github.com/DynamoRIO/dynamorio/issues/3544

现在我们很高兴的宣布已经有了全职的员工在这个项目中工作了一段时间，准备开始招募实习生了。实习生的工作就是让 DynamoRIO 移植到 RISC-V 架构， x86 和 arm 有的，我们希望 RISC-V 也有。

**岗位要求**

第一个实习生，需要有 LV4 及以上的等级，能够直接与我们的员工一起直接贡献 upstream。第二个实习生开始需要 LV3 能力等级，能够自发的进行模块的分析和开发。

在投递简历之前，我们希望你已经看过 DynamoRIO 这个项目，下载了代码，在自己的机器上构建了一次。

### BJ64 Mono 系统开发实习生（负责 RISC-V 移植及优化）【暂停招聘】

**工作内容**

即便微软开源了 dotNet 环境， Mono 系统在 Linux 开源生态中依然占有重要的位置。还有很多事情需要做。具体可以从 [1] 中看到。 PLCT实验室新设置的岗位就是为了让 RISC-V 在不远的未来（2025年之前）成为 Mono 的 Tier-1 支持平台而存在。我们招募看到 RISC-V 发展的同学来一起为开源社区添砖加瓦。

**岗位要求**

目前PLCT实验室没有全职投入在 Mono 系统的 mentor，因此需要第一位实习生有高度的自驱能力，至少要求达到LV4或以上；第二名之后的实习生要求达到 LV3 或更高级别。

远程实习，支持全球实习工资支付（中国学生必须是国内银行卡）。实习随时可以开始随时可以暂停随时可以结束（如果超过一周旷工、或八周没有外部可见产出会被劝退）。

[1] https://github.com/mono/mono/blob/main/docs/riscv.md

### BJ63 Maple-C 编译器 Linux 构建验证及 RISC-V 移植实习生【暂停招聘】

2019年下半年开源的方舟编译器（Maple）系列，在移动端的Java虚拟机领域进展并不顺利。 Maple-C 是 Maple 编译架构面向C语言的编译系统。源代码保存在[1]中。

时至今日，PLCT实验室依然看重 Maple 编译框架的价值，并且希望能够完成两个长期目标：
1. Maple-C 编译器能够支持 RISC-V 架构，包括 RV64GC 和 RV32GC 等常用的指令集组合。
2. Maple-C 编译器能够替换 GCC 和 Clang 对流行的 Linux 发行版进行整体构建（Linux Kernel 除外）。

欢迎有志向有能力的小伙伴加入我们。道阻且长，需要自行探索的路径非常多。要求能力在LV3以上，并且能够有着高度的自驱能力。

[1] https://gitee.com/openarkcompiler/OpenArkCompiler

### BJ61 蝉语实习生【暂停招聘】

(本岗位为外部社区联合贡献岗位，mentor来自蝉语社区。岗位信息来自 [cicada-internships](https://github.com/cicada-lang/cicada-internships))

**蝉语实习生 / Cicada Internships**

[蝉语](https://github.com/cicada-lang) 是一个开源程序语言设计团队。

主要项目 [Cicada](https://github.com/cicada-lang/cicada)
是一个 Dependently Typed 程序语言（类似 Coq、Agda、Idris 和 Lean），
可以用来辅助证明数学定理，并却作为形式化的数学基础。

想要设计一个实用的计算机辅助证明系统的同时，这个语言也是大家学习与尝试新想法的基础。

程序语言设计就像 Web App 的设计一样，也分为 _前端_ 与 _后端_，
前端包括语法设计与类型系统设计，后端主要在于代码生成与编译器优化。
我们的工作偏重于程序语言设计的前端。

工作内容：

- 维护 [Cicada](https://github.com/cicada-lang/cicada) 的代码。
  - 由 TypeScript 实现，OOP 编程风格。
- 编写文档来介绍我们的语言，以普及 _机器辅助证明_ 与 _形式化数学基础_ 相关的知识。
  - 当前的文档在：https://cicada-lang.org/docs
- 探索类型系统的功能与实现方式。
  - 例如 Inductive datatype、递归函数、子类型关系等等。
  - 我们读类型论相关的书籍与论文，然后以研讨会和博客的形式分享。
  - 中文 Telegram 讨论群：https://t.me/CicadaLanguageCN

入职要求：

- 能读英文。
- 对 _程序语言设计_ 与 _类型系统设计_ 感兴趣。

说明：

- 目前 [Cicada](https://github.com/cicada-lang/cicada)
  的代码有 10000 行左右（包括 REPL，以及模块系统）。
  良好的代码结构在于容易理解（因而容易修改），
  我们努力注意保持良好的代码结构，
  但是代码中还是有很多有待改进的地方。
  也许通过讲解与讨论实现方式，
  我们能获得清晰的理解与更好的代码结构。

### BJ58 libcxx-simd 项目实习生招聘（进行中，名额 1）

工作内容：
 参与 libcxx-simd 项目开发与测试相关工作。 experimental/simd 是一个为 C++ 显式数据并行编程提供零开销 C++ 类型的库，该库已经被包含进GCC官方的 libstdc++ 库。PLCT正尝试将其移植到 Clang/LLVM 官方的 libcxx 库中。

要求：
- 熟练使用C++，熟悉C++模板元编程及C++11/14/17新特性。
- 了解libstdc++/libc++库的使用与开发流程。
- 具备SIMD指令集相关基础知识，了解至少一种SIMD指令集及其intrinsic（SSE、AVX、AVX512、Arm Neon、PowerPC AltiVec）。
- 具备基本的Linux操作基础和基本的git操作基础。

远程实习。要求LV3及以上能力。

### NJ53 软件测试实习生（这是测试岗位）【暂停招聘】

（这是目前唯一只需要LV1+的岗位）

工作内容：
- 为 PLCT 正在开发或维护的开源软件提供QA服务，包括最新的软件的构建、测试、分析、报告和技术交流分享。
- 能够理解测试组长的需求，阅读分析现有测试用例/测试集/测试过程的不足，按照一些通用的测试评价指标（覆盖率等）进行测试用例的补充和设计。

要求：
1. LV1+ 即可，不需要通过上机编程考试。
2. 具有一定的软件测试的理论基础（上过软件测试或者软件工程的课）。
3. 具备基本的 Linux 操作的基础，例如会在命令行使用 cd/ps/mkdir/make 等。
4. （加分）具备基本的 git 操作基础，会使用 git clone，知道有 submodule 的概念。
5. （加分）能够有比较好的英语的阅读和书写能力。英语的口头表达能力不要求。

### NJ52 测试开发实习生（这是开发岗位）【暂停招聘】

工作内容：
- 通过测试流程设计、自动化脚本编写、框架或系统开发等方式，为 RISC-V Linux 发行版的测试工作的生产力提高提供帮助。
- 能够理解测试组长的需求，阅读分析现有测试用例/测试集/测试过程的不足，按照一些通用的测试评价指标（覆盖率等）进行测试用例的补充和设计，并通过程序或脚本的形式来批量的实现。
- 为 PLCT 正在开发或维护的开源软件提供QA服务，包括最新的软件的构建、测试、分析、报告和技术交流分享。
- 跟 Jenkins、GitHub Actions、Gitlab Runners、Ansible Playbooks 等打交道，还有可能写 Web UI，写 expect/lit 自动化回归测试脚本。

要求：
1. LV2+；需要通过上机考试。
2. 熟练使用至少两种脚本语言，包括但不限于 python、bash、perl、PHP 等。
3. 具备基本的软件测试的流程和思想，具备基本的调试代码的能力。

### BJ15 QEMU/Spike 开源模拟器开发实习生（进行中，名额 1）

工作内容：
- 参与PLCT实验室在QEMU、Spike等相关开源项目的开发。在开源社区直接提交代码。

入职要求：
- LV3+，对模拟器的内部实现有兴趣。
- 远程实习，不需要坐班。

### BJ32 Dart for RISC-V 开发实习生【暂停招聘】

PLCT实验室2022年路线图中包含了移植DartVM到RISC-V架构，但是一直没有招募到合适的勇者（非常稀缺的LV4+实习生），所以一直在咕。但～是～！前不久，Google Dart Team 最新的版本中已经包含了初步的RISC-V支持！于是乎我们从躺平中惊坐起，觉得**难度大幅度降低，LV3+的实习生也可以开始参与了**！

工作内容：
- 就像将 V8 移植到 RISC-V 平台一样，将 Dart 移植到 RISC-V 平台。负责跟 Dart 上游交流，将移植工作 upstream。路线上先从 RV64GC 开始做。

入职要求：
- 这份工作目前没有正式员工在做，需要一位能力在LV3及以上的同学，与PLCT实验室的mentor和DartVM上游协作（默认mentor是 V8 RISC-V 的maintainer）。
- 学习了 Dart 语言（现学3天的水平即可）。
- 基本了解 DartVM 的内部实现（至少学了一周，看过文档、看过技术分享视频、看过源代码、编译运行起来了）。
- 熟悉语言虚拟机的内部实现（看过书，知道解释器、字节码、JIT、GC、锁、线程等等）
- 脸皮厚。能跟外国人直接英语对线。

### BJ37 GCC 开发实习生（进行中，名额 3）

工作内容
- 最近PLCT实验室在参与RISC-V国际基金会的相关新指令扩展的工作，具体内容是为 unratified extensions （就是还在制定中的扩展指令集）进行 GNU Toolchain 的实现，用于验证草案本身在设计上是否存在遗漏缺失、是否在功能或性能上有改进的空间。目前面向大学生及研究生招募开发者，以PLCT实验室实习生的身份，直接参与到RISC-V基金会管理下的GCC工具链开发中，并有可能后续直接将代码（patch）提交到上游（upstream）。最近开始有业界一线的大佬指导和review实习生的代码，是非常难得的学习机会。
- 与此同时，实习生岗位 BJ18 Clang/LLVM 开发实习生以及 BJ15 QEMU/Spike 开发实习生同样持续招聘。一个完整扩展指令参考实验和验证包括编译器、二进制工具、模拟器，都是需要的。

入职要求：
- LV3+，能进行英语交流，对编译技术有基本了解。如果事先了解过ELF格式、RISC-V或其他指令集、相关ABI文档，那么都算是加分项。
- 远程实习，不需要坐班。

### (被BJ78-BJ80替代) NJ57 Android(AOSP) RISC-V 移植开发实习生【暂停招聘】

**工作内容**

由阿里巴巴平头哥主导的 AOSP RISC-V 移植项目已经有了比较大的进展，初步的工作已经开源到了GitHub上。
Android Open Source Project 是一个非常宏大的项目，要完成移植工作需要非常多的贡献者的努力。
PLCT Lab 是最早开始公开进行 AOSP RISC-V 移植的团队， 并在平头哥开源更为完整的 AOSP 移植工作之后， 跟平头哥一起加入到了 RISC-V 国际基金会协调下的 AOSP 移植工作组（Android SIG）。
我们希望招募看好RISC-V长远发展的同学，参与到 AOSP RISC-V 项目中来。

**岗位要求**

1. 熟悉 C/C++，熟悉 Shell/Python。
2. 对 RISC-V 指令集以及汇编编程有一定了解。
3. 对安卓系统基本架构有所了解，了解安卓 build/make 系统和镜像制作等
4. 对 Android Framework 底层库性能优化感兴趣，譬如手机上的 audio、图片处理相关等
5. 对虚拟机开发感兴趣，譬如 ART，可以做一些简单的优化工作。
6. 熟悉 Linux 内核和驱动开发，会对 Kernel 驱动进行配置。
7. 对嵌入式开发感兴趣，了解过一些嵌入式接口开发，有一些裸机开发和驱动开发调试经验。
8. 对底层偏硬件开发感兴趣，了解 BSP，HAL 开发。

远程实习，支持全球实习工资支付（中国学生必须是国内银行卡，国际学生可以用境外卡支付）。实习随时可以开始随时可以暂停随时可以结束。

### BJ47 Gentoo RISC-V 操作系统构建实习生（进行中，名额 2）

要求：LV2或以上。日常使用 Gentoo。【没有用过Gentoo的同学请勿投递。】

```
Requirement:

0) eager to contribute to open source
1) self-motivated, self-learning
2) enough *time* to contribute
3) good english communication skills
     at least able to do good online communication
4) familiar with Linux Distro
     have experience with Gentoo would be great++

Note:
 sophisticated programming skill is not a must,
 but do prefer computer/science (or related) background

works:
 help ARCH=riscv in Gentoo Linux - (test, maintain, fix, improve)
 work on Gentoo based binary distro/binhost project

```

### NJ51 Arch Linux RISC-V 操作系统构建实习生【暂停招聘】

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV3及以上；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### NJ50 Debian/Ubuntu RISC-V 操作系统构建实习生【暂停招聘】

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV2+；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### NJ49 Fedora RISC-V 操作系统构建实习生【暂停招聘】

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV2+；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### HZ48 Chisel 开发实习生 【暂停招聘】

工作内容：
加入 Chisel 小队，从事 Chisel 的开发工作。

要求：
- LV2+
- 已经自学了 Chisel。

### BJ17 V8 开发实习生（进行中，名额 1）

工作内容：
- 参与PLCT实验室 V8 for RISC-V 相关项目的开发。在开源社区直接提交代码。

入职要求：
- LV4及以上，熟练的英语交流。
- C++ 要熟练。新特性了然于胸。
- 需要已经看过 V8 的源代码，自行构建 riscv64 后端成功。
- 需要熟悉 JavaScript 语言。如果看过 WebAssembly 加分。
- 远程实习，不需要坐班。

### BJ45 MLIR 开源开发实习生【暂停招聘】

我们相信MLIR将会成为未来编译器框架的实施标准。因此从2021年开始，PLCT实验室将 MLIR 列入了「关键开源基础设施」名单，已经跟 LLVM、GCC 一样成为PLCT实验室的长期管理对象。

工作内容：
- 参与PLCT实验室 MLIR 相关开源项目的开发。

入职要求：
- LV3+，能进行英语交流，对编译技术有很好的了解。对 MLIR 项目有浓厚的兴趣。
- 远程实习，不需要坐班。


### BJ34 OpenJDK 开发实习生（进行中，名额 1）

工作内容：
- 参与PLCT实验室 OpenJDK for RISC-V 相关项目的开发。帮助 RISC-V 社区将 Java 执行速度提高 100x 以上。

入职要求：
- LV3+，能进行英语交流，对编译技术有基本了解。对 Java 虚拟机感兴趣。
- 远程实习，不需要坐班。

### BJ18 Clang/LLVM 开发实习生（进行中，名额 7）

工作内容：
参与PLCT实验室 Clang/LLVM 相关项目的开发、技术分析、报告撰写。在开源社区直接提交代码。

入职要求：
LV3+，能进行英语交流，对编译技术有基本了解。
远程实习，不需要坐班。

### BJ38 LuaJIT 开发实习生【暂停招聘】

目标：将 LuaJIT 移植到 RV64G 平台。
背景参考：https://github.com/plctlab/plctlab.github.io/issues/9

入职要求：
LV4+，能进行英语交流，对编译技术有基本了解。如果事先了解过ELF格式、RISC-V或其他指令集、相关ABI文档，那么都算是加分项。
远程实习，不需要坐班。


### BJ68 OpenWrt RISC-V 移植及观测实习生【暂停招聘】

### BJ67 操作系统RISC-V成熟度观测实习生（跟踪所有国内外知名Linux发行版）【暂停招聘】

### BJ66 科技文档翻译实习生（日语、韩语）【暂停招聘】

### BJ60 开源技术社区运营经理实习生【暂停招聘】

### BJ59 开源软件项目经理实习生【暂停招聘】

### BJ33 Spidermonkey 开发实习生【暂停招聘】

### NJ55 开源EDA实习生【暂停招聘】

### BJ39 Web 前端开发实习生【暂停招聘】

### NJ53a openEuler RISC-V 操作系统构建实习生【暂停招聘】
