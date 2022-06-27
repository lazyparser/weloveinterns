# 实习生岗位

包含三个团队的岗位。请注意编号。
全职员工的招聘可以 从 [PLCT-Weekly 仓库找到](https://github.com/plctlab/PLCT-Weekly/blob/master/Jobs.md)。

如果你是即将毕业的应届生，欢迎按照下属方式投递简历，应届生也可以走实习生的招聘通道。

目录：
+ [如何正确的投递简历](#如何正确的投递简历)
+ [PLCT Lab 的实习生岗位](#plct-lab-的实习生岗位)
+ [机器人团队的实习生岗位](#机器人团队的实习生岗位)
+ [工业仿真组的实习生岗位](#工业仿真组的实习生岗位)
+ [文文新闻报社的实习生岗位](#文文新闻报社的实习生岗位)

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

## 所有实习生共性要求（技术类）

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

其他说明：所有岗位默认都是远程实习，支持全球实习工资支付（中国学生必须是国内银行卡，与软件所北京本部签约需要建设银行卡）。实习随时可以开始随时可以暂停随时可以结束（如果超过一周旷工、或八周没有外部可见产出会被劝退）。

## PLCT Lab 的实习生岗位

PLCT全称是程序语言与编译技术实验室，隶属于中科院软件所智能软件研究中心（ISRC），致力于成为编译技术领域的开源领导者，推进开源工具链及运行时系统
等软件基础设施的技术革新，具备主导开发和维护重要基础设施的技术及管理能力。与此同时，努力成为编译领域培养尖端人才的黄埔军校，推动先进编译技术在国
内的普及和发展。

(Next Job ID: 66)

### BJ65 DynamoRIO 开发实习生（负责 RISC-V 移植及优化）

**工作内容**

DynamoRIO 是很优秀的一款开源开发工具。PLCT实验室在2021年初吹的牛/立的FLAG，到2022年下半年还没圆上。围观地址：

https://github.com/DynamoRIO/dynamorio/issues/3544

现在我们很高兴的宣布已经有了全职的员工在这个项目中工作了一段时间，准备开始招募实习生了。实习生的工作就是让 DynamoRIO 移植到 RISC-V 架构， x86 和 arm 有的，我们希望 RISC-V 也有。

**岗位要求**

第一个实习生，需要有 LV4 及以上的等级，能够直接与我们的员工一起直接贡献 upstream。第二个实习生开始需要 LV3 能力等级，能够自发的进行模块的分析和开发。

在投递简历之前，我们希望你已经看过 DynamoRIO 这个项目，下载了代码，在自己的机器上构建了一次。

### BJ64 Mono 系统开发实习生（负责 RISC-V 移植及优化）

**工作内容**

即便微软开源了 dotNet 环境， Mono 系统在 Linux 开源生态中依然占有重要的位置。还有很多事情需要做。具体可以从 [1] 中看到。 PLCT实验室新设置的岗位就是为了让 RISC-V 在不愿的未来（2025年之前）成为 Mono 的 Tier-1 支持平台而存在。我们招募看到 RISC-V 发展的同学来一起为开源社区添砖加瓦。

**岗位要求**

目前PLCT实验室没有全职投入在 Mono 系统的 mentor，因此需要第一位实习生有高度的自驱能力，至少要求达到LV4或以上；第二名之后的实习生要求达到 LV3 或更高级别。

远程实习，支持全球实习工资支付（中国学生必须是国内银行卡）。实习随时可以开始随时可以暂停随时可以结束（如果超过一周旷工、或八周没有外部可见产出会被劝退）。

[1] https://github.com/mono/mono/blob/main/docs/riscv.md

### BJ63 Maple-C 编译器 Linux 构建验证及 RISC-V 移植实习生

2019年下半年开源的方舟编译器（Maple）系列，在移动端的Java虚拟机领域进展并不顺利。 Maple-C 是 Maple 编译架构面向C语言的编译系统。源代码保存在[1]中。

时至今日，PLCT实验室依然看重 Maple 编译框架的价值，并且希望能够完成两个长期目标：
1. Maple-C 编译器能够支持 RISC-V 架构，包括 RV64GC 和 RV32GC 等常用的指令集组合。
2. Maple-C 编译器能够替换 GCC 和 Clang 对流行的 Linux 发行版进行整体构建（Linux Kernel 除外）。

欢迎有志向有能力的小伙伴加入我们。道阻且长，需要自行探索的路径非常多。要求能力在LV3以上，并且能够有着高度的自驱能力。

[1] https://gitee.com/openarkcompiler/OpenArkCompiler

### BJ61 蝉语实习生

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

### BJ60 开源技术社区运营经理实习生（1-2名）

随着 openEuler RISC-V (简称OERV) 社区规模的扩大，项目经理已经忙不过来了。因此希望招募新同学来帮助OERV项目经理完成开源技术社区运营的部分工作，并在这个过程中，逐渐培养出优秀的社区运营经理。同时这个工作本身有技术要求，同时具有技术和管理属性，适合对技术感兴趣的小伙伴参加。

**工作内容：**
- 搜集 RISC-V 领域（不仅是OERV）的各类新闻和八卦，进行整理和汇总。尤其是各个流行的 Linux 发行版在 RISC-V 平台上的适配进展。
- 帮助 OERV 社区撰写公众号文章或B站分享，向更多的人介绍 openEuler RISC-V，吸引更多的伙伴加入。
- 帮助 OERV 社区收集和统计国内外 openEuler RISC-V 相关使用、测试、测评的新闻动向，并积极邀请和联系新伙伴参与到社区中来。
- 代表 OERV 社区在开源技术会议或沙龙中进行分享。
- 代表 OERV 社区参加各类线下技术展示。

**岗位要求：**
- 为人正直；能够放低自己的姿态，谦卑且勇敢；并且能够积极的看待这个世界。（开源社区是一个社会的缩影，内心需要足够强大才能长期面对所有的社会面。）
- 具备良好的倾听能力、理解能力和共情能力。
- 知晓 “非暴力沟通”、“关键冲突”、“关键对话” 等沟通原则或技能。 （在面试前，请务必确保自己阅读过至少1本）
- 良好的自学能力；熟练使用搜索引擎。（能够使用Google搜索者加分。）
- 主动观测、主动收集、主动沟通、主动反馈。
- 不骄傲，有担当；在出现错误时勇于承认自己的错误并补救。
- 不怯场的英语口语和写作能力。（常用英语600句那种水平，不需要6级，关键是脸皮要厚，并善于使用自动语法检查工具。）

**其它工作说明：**
- 远程岗位，不需要坐班，需要在线，及时响应社区伙伴的 ping/at。
- 期待每周会有4天在线，每次至少在线2小时；其中至少1天是在周末的时候能在线，最好是周末2天都在线。
- 不需要LV评定。
- 实习工资默认税前 2k/mo，会根据产出和工作量上浮。

### BJ59 开源软件项目经理实习生（1-2名）

随着 openEuler RISC-V (简称OERV) SIG 参与的贡献者数量和移植工作量的增加，项目经理已经忙不过来了。因此希望招募新同学来帮助OERV项目经理完成部分日常工作，并在这个过程中，逐渐培养出能够独当一面的开源项目经理。同时这个工作本身有技术要求，同时具有技术和管理属性，适合对技术感兴趣的小伙伴参加。

**工作内容：**
- 每日查看 OERV 开源项目仓库和OBS构建工程的状态，收集和更新统计信息。这项工作确保了能够每天看到 OERV 移植工作的进度和潜在问题。
- 帮助项目经理完成新加入的伙伴的 pre-task 和 task-0 的指导和辅助。 pre-task 和 task-0 是进去项目开发的准入门槛。要求项目经理实习生本人也能够熟练的掌握上述技能。
- 每两周帮助项目经理汇总和统计各个伙伴的外部可见产出，并与开发伙伴进行不定期沟通，有计划外坏消息及时同步和处理。这构成了付费团队成员的费用支付的依据。
- 代表 OERV SIG 与 openEuler 的其它 SIG 组沟通，并跟进各项工作的进展。
- 代表 OERV SIG 在开源技术会议或沙龙中进行分享。
- 代表 OERV SIG 参加各类线下技术展示。

**岗位要求：**
- 为人正直；能够放低自己的姿态，谦卑且勇敢；并且能够积极的看待这个世界。（开源社区是一个社会的缩影，内心需要足够强大才能长期面对所有的社会面。）
- 具备良好的倾听能力、理解能力和共情能力。
- 知晓 “非暴力沟通”、“关键冲突”、“关键对话” 等沟通原则或技能。 （在面试前，请务必确保自己阅读过至少1本）
- 良好的自学能力；熟练使用搜索引擎。（能够使用Google搜索者加分。）
- 主动观测、主动收集、主动沟通、主动反馈。
- 不骄傲，有担当；在出现错误时勇于承认自己的错误并补救。
- 能够完成 openEuler RISC-V 的 pre-task 和 task-0 项目。
- 不怯场的英语口语和写作能力。（常用英语600句那种水平，不需要6级，关键是脸皮要厚，并善于使用自动语法检查工具。）
- 广州地区高校的同学优先。（因为项目经理在北京，有些广州地区的活动希望实习项目经理参加。）
- 大学或大专的同学优先。（因为研究生阶段时间精力就有限了。）

**其它工作说明：**
- 远程岗位，不需要坐班，需要在线，及时响应社区伙伴的 ping/at。
- 期待每周会有4天在线，每次至少在线2小时；其中至少1天是在周末的时候能在线，最好是周末2天都在线。
- 不需要LV评定。
- 实习工资默认税前 2k/mo，会根据产出和工作量上浮。

### BJ58 libcxx-simd 项目实习生招聘

工作内容：
 参与 libcxx-simd 项目开发与测试相关工作。 experimental/simd 是一个为 C++ 显式数据并行编程提供零开销 C++ 类型的库，该库已经被包含进GCC官方的 libstdc++ 库。PLCT正尝试将其移植到 Clang/LLVM 官方的 libcxx 库中。

要求：
- 熟练使用C++，熟悉C++模板元编程及C++11/14/17新特性。
- 了解libstdc++/libc++库的使用与开发流程。
- 具备SIMD指令集相关基础知识，了解至少一种SIMD指令集及其intrinsic（SSE、AVX、AVX512、Arm Neon、PowerPC AltiVec）。
- 具备基本的Linux操作基础和基本的git操作基础。

远程实习。要求LV3及以上能力。

### NJ53 软件测试实习生（这是测试岗位）

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

### NJ52 测试开发实习生（这是开发岗位）

工作内容：
- 通过测试流程设计、自动化脚本编写、框架或系统开发等方式，为 RISC-V Linux 发行版的测试工作的生产力提高提供帮助。
- 能够理解测试组长的需求，阅读分析现有测试用例/测试集/测试过程的不足，按照一些通用的测试评价指标（覆盖率等）进行测试用例的补充和设计，并通过程序或脚本的形式来批量的实现。
- 为 PLCT 正在开发或维护的开源软件提供QA服务，包括最新的软件的构建、测试、分析、报告和技术交流分享。
- 跟 Jenkins、GitHub Actions、Gitlab Runners、Ansible Playbooks 等打交道，还有可能写 Web UI，写 expect/lit 自动化回归测试脚本。

要求：
1. LV2+；需要通过上机考试。
2. 熟练使用至少两种脚本语言，包括但不限于 python、bash、perl、PHP 等。
3. 具备基本的软件测试的流程和思想，具备基本的调试代码的能力。

### BJ15 QEMU/Spike 开源模拟器开发实习生

工作内容：
- 参与PLCT实验室在QEMU、Spike等相关开源项目的开发。在开源社区直接提交代码。

入职要求：
- LV3+，对模拟器的内部实现有兴趣。
- 远程实习，不需要坐班。

### NJ53a openEuler RISC-V 操作系统构建实习生

工作内容：
从事 Linux 发行版 openEuler 在 RISC-V 上的软件包构建、测试、升级、分析工作。

openEuler 是国内的又一个 Linux 发行版社区。起初由华为发起，中科院软件所是最早一批和可能目前最活跃的社区贡献单位。去年主要是软件所的OS团队在进行贡献。2021年7月开始，PLCT实验室开始与华为的工程师一起负责 RISC-V 平台上的 oE 的构建和维护工作。目前老板已经到位，项目经理已经就绪，测试团队已经组建，CI基础设施订单已下。软硬件环境都已经准备好，就差你来干活了。

要求：
- LV2及以上；喜欢倒腾新技术、喜欢编译尝试开源软件的同学们优先。
- 需要先去 gitee 上逛逛 oE RISC-V 的有关信息，看看会议纪要，构建的状态等。
- **需要在提交简历之前，在 oE/RV 社区提交一个 MR 修复一个包。**
- 不管是否决定来实习，都欢迎加老板微信 fangzhang1024 先拉你到 oE RISC-V SIG 的群里。每两周开会，各种讨论事项都很公开。来感受下业界的脉搏，说不定以后毕业未来的面试官/老板就在群里😄

### BJ32 Dart for RISC-V 开发实习生

PLCT实验室2022年路线图中包含了移植DartVM到RISC-V架构，但是一直没有招募到合适的勇者（非常稀缺的LV4+实习生），所以一直在咕。但～是～！前不久，Google Dart Team 最新的版本中已经包含了初步的RISC-V支持！于是乎我们从躺平中惊坐起，觉得**难度大幅度降低，LV3+的实习生也可以开始参与了**！

工作内容：
- 就像将 V8 移植到 RISC-V 平台一样，将 Dart 移植到 RISC-V 平台。负责跟 Dart 上游交流，将移植工作 upstream。路线上先从 RV64GC 开始做。

入职要求：
- 这份工作目前没有正式员工在做，需要一位能力在LV3及以上的同学，与PLCT实验室的mentor和DartVM上游协作（默认mentor是 V8 RISC-V 的maintainer）。
- 学习了 Dart 语言（现学3天的水平即可）。
- 基本了解 DartVM 的内部实现（至少学了一周，看过文档、看过技术分享视频、看过源代码、编译运行起来了）。
- 熟悉语言虚拟机的内部实现（看过书，知道解释器、字节码、JIT、GC、锁、线程等等）
- 脸皮厚。能跟外国人直接英语对线。

### BJ37 GCC 开发实习生

工作内容
- 最近PLCT实验室在参与RISC-V国际基金会的相关新指令扩展的工作，具体内容是为 unratified extensions （就是还在制定中的扩展指令集）进行 GNU Toolchain 的实现，用于验证草案本身在设计上是否存在遗漏缺失、是否在功能或性能上有改进的空间。目前面向大学生及研究生招募开发者，以PLCT实验室实习生的身份，直接参与到RISC-V基金会管理下的GCC工具链开发中，并有可能后续直接将代码（patch）提交到上游（upstream）。最近开始有业界一线的大佬指导和review实习生的代码，是非常难得的学习机会。
- 与此同时，实习生岗位 BJ18 Clang/LLVM 开发实习生以及 BJ15 QEMU/Spike 开发实习生同样持续招聘。一个完整扩展指令参考实验和验证包括编译器、二进制工具、模拟器，都是需要的。

入职要求：
- LV3+，能进行英语交流，对编译技术有基本了解。如果事先了解过ELF格式、RISC-V或其他指令集、相关ABI文档，那么都算是加分项。
- 远程实习，不需要坐班。

### NJ57 Android(AOSP) RISC-V 移植开发实习生

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

### BJ47 Gentoo RISC-V 操作系统构建实习生

要求：LV2或以上。

```
Requirement:

0) have interest in open source
1) self-motivated, self-learning
2) have *time* to contribute
3) good english communication skill at least capable of writing
4) familiar with Linux Distro
have experience with Gentoo would be great++

Note:
 sophisticated programming skill is not a must,
 but do prefer computer science (or related) background

works:
testing packages for ARCH=riscv in Gentoo Linux
 a) if fail
   *) file bugs (https://bugs.gentoo.org)
   *) report to upstream
   +) help to fix (not a must)
 b) or success
   *) keywording packages and send PR

Testing Xfce4, KDE, Gnome, your choice!?
```

### NJ51 Arch Linux RISC-V 操作系统构建实习生

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV2+；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### NJ50 Debian/Ubuntu RISC-V 操作系统构建实习生

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV2+；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### NJ49 Fedora RISC-V 操作系统构建实习生

工作内容：
从事 Linux 发行版的软件包构建、测试、分析工作。

要求：
- LV2+；喜欢从事开源软件开发工作。
- **需要在提交简历之前，在社区提交一个PR，为 RISC-V 修复一个包。**

### HZ48 Chisel 开发实习生

工作内容：
加入 Chisel 小队，从事 Chisel 的开发工作。

要求：
- LV2+
- 已经自学了 Chisel。

### BJ17 V8 开发实习生

工作内容：
- 参与PLCT实验室 V8 for RISC-V 相关项目的开发。在开源社区直接提交代码。

入职要求：
- LV3+，熟练的英语交流。
- C++ 要熟练。新特性了然于胸。
- 需要已经看过 V8 的源代码，自行构建 riscv64 后端成功。
- 需要熟悉 JavaScript 语言。如果看过 WebAssembly 加分。
- 远程实习，不需要坐班。

### BJ45 MLIR 开源开发实习生

我们相信MLIR将会成为未来编译器框架的实施标准。因此从2021年开始，PLCT实验室将 MLIR 列入了「关键开源基础设施」名单，已经跟 LLVM、GCC 一样成为PLCT实验室的长期管理对象。

工作内容：
- 参与PLCT实验室 MLIR 相关开源项目的开发。

入职要求：
- LV3+，能进行英语交流，对编译技术有很好的了解。对 MLIR 项目有浓厚的兴趣。
- 远程实习，不需要坐班。

### BJ39 Web 前端开发实习生

目标：
- 改进PLCT各类web页面。
- 开发和维护包括 [RISC-V 软件生态状态跟踪数据库](https://github.com/isrc-cas/riscv-ecosystem-tracking) 在内的 PLCT Lab 开发维护的各类 Web 页面。包括 HTML/CSS/JS。推荐和鼓励使用最新的前端框架。

入职要求：
- LV2+
- 熟练 Web 前端开发，熟悉这两年最新的开发框架
- （加分）懂一点 nodejs/php/perl/ruby/go。

远程实习，不需要坐班。遵循每个月1号和16号的外部可见交付物报告制度。

### BJ34 OpenJDK 开发实习生

工作内容：
- 参与PLCT实验室 OpenJDK for RISC-V 相关项目的开发。帮助 RISC-V 社区将 Java 执行速度提高 100x 以上。

入职要求：
- LV3+，能进行英语交流，对编译技术有基本了解。对 Java 虚拟机感兴趣。
- 远程实习，不需要坐班。

### BJ18 Clang/LLVM 开发实习生

工作内容：
参与PLCT实验室 Clang/LLVM 相关项目的开发、技术分析、报告撰写。在开源社区直接提交代码。

入职要求：
LV3+，能进行英语交流，对编译技术有基本了解。
远程实习，不需要坐班。

### BJ33 Spidermonkey 开发实习生

工作内容：
- 就像将 V8 移植到 RISC-V 平台一样，将 Spidermonkey 移植到 RISC-V 平台。跟 mentor 一起将工作提交到 Mozilla upstream。

入职要求：
- LV3+ 级别。能够进行英文的交流。
- 提交简历时已经看过 Spidermonkey 源代码，自己尝试构建过 Spidermonkey 或 Firefox。
- 远程实习，不需要坐班。

### NJ55 开源EDA实习生

**岗位特别说明**

需要提醒同学们注意的是，PLCT实验室目前并没有员工（mentor）在为开源EDA项目贡献代码，目前PLCT实验室也没有承接有关EDA的工程项目。本实习岗位是纯粹的开源社区培育岗位，隶属于PLCT实验室内部的兴趣培养计划，目的是提供一个相互鼓励和支持的学习环境，为已经对开源EDA工具感兴趣的同学提供支持。所以，这要求应聘的同学本身已经有兴趣并且开始看相关的知识，并直接在相关的开源社区中进行交流和提问。

**工作内容：**

- （暂缓）LV2 Chisel-DSP调研学习报告（1个月）->LV3 基于RoCC的RISC-V DSP-Extension开发
  - 前置课程：数字电路/信号处理/体系结构
  - 收获：学会高性能使用Chisel开发DSP，并理解协处理器工作流程
- （暂缓）LV2 RISCV Debug调研学习报告（1个月）->LV4 RocketChip Debug v0.13调研学习报告（2个月）->LV4 基于Diplomacy的Debug Spec v1.0开发设计
  - 前置课程：体系结构/数字电路
  - 收获：掌握软硬RISCV Debug流程，掌握SoC中Debug/Trace模块的开发
- （暂缓）LV3 Rocket/Boom微架构调研学习报告（3个月）-> 基于Rocket的硬件算法设计（1个月）
  - 前置课程：体系结构
  - 收获：学会Chisel 熟悉Rocket
- （暂缓）LV3 Formal Verification调研学习报告 -> LV4 FIRRTL SMT backend的调研->LV4基于SMTLib的Formal框架的调研学习报告->被Formal验证的高性能硬件算法设计
  - 前置课程：Chisel/Model Checking
  - 收获：进阶Chisel验证方法学/Paper
- LV3 Verilator学习报告（1个月） -> LV4 EmitC/Scheduler源码分析（2个月） -> LV5 Verilator 在 CIRCT 的重实现（3个月）
  - 前置课程：C++ LLVM
  - 收获：下一代高性能仿真器的设计/Paper
- LV3+ Berkeley-ABC 学习报告（3个月）
  - 前置课程： C 数理逻辑 Model Checking
  - 收获：深刻理解电路综合最难的部分

**共享基本要求：**

- 熟练Git，了解GitHub协作流程
- 熟练Linux系统
- 已经解决好了自己的网络问题，速度很快的下载配置环境和访问Google
- 先学再问

### BJ38 LuaJIT 开发实习生

目标：将 LuaJIT 移植到 RV64G 平台。
背景参考：https://github.com/plctlab/plctlab.github.io/issues/9

入职要求：
LV4+，能进行英语交流，对编译技术有基本了解。如果事先了解过ELF格式、RISC-V或其他指令集、相关ABI文档，那么都算是加分项。
远程实习，不需要坐班。


## 机器人团队的实习生岗位

### ROS021 ROS RISC-V 移植开发

工作内容：
- 让 ROS 可以流畅的运行在 RISC-V 硬件上。需要逐一验证核心软件包和主要软件模块在 RISC-V 上的可用性并进行必要的移植。

入职要求：
- LV3+。熟悉 ROS。看过 RISC-V 的相关文档。
- 玩过 deb 或 rpm 包构建。

## 工业仿真组的实习生岗位

无。

## 文文新闻报社的实习生岗位

见[相关文档](bunbun.md)。
