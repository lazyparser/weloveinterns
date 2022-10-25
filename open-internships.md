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

(Next Job ID: 73)

### BJ72 eunomia-bpf intern

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

### BJ71 RT-Thread 社区实习生
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

### BJ70 Aya 全套生态开发实习生

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

### BJ69 Deepin RISC-V 操作系统构建实习生（8 个名额）

**工作内容**

从事 Linux 发行版的软件包构建、测试、分析工作。

**要求**

- LV2+；喜欢从事开源软件开发工作。

需要在提交简历之前，请完成以下工作：

- 在 amd64 或其他架构操作系统架构使用 qemu-user 启动 Ubuntu/Debian riscv 发行版 并输出 `neofetch` 截图
- 在此基础上，使用 `apt source neofetch` 下载对应源码并完成升级版本号 并打包安装上 然后输出 `apt policy neofetch` 截图

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

即便微软开源了 dotNet 环境， Mono 系统在 Linux 开源生态中依然占有重要的位置。还有很多事情需要做。具体可以从 [1] 中看到。 PLCT实验室新设置的岗位就是为了让 RISC-V 在不远的未来（2025年之前）成为 Mono 的 Tier-1 支持平台而存在。我们招募看到 RISC-V 发展的同学来一起为开源社区添砖加瓦。

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

### BJ38 LuaJIT 开发实习生

目标：将 LuaJIT 移植到 RV64G 平台。
背景参考：https://github.com/plctlab/plctlab.github.io/issues/9

入职要求：
LV4+，能进行英语交流，对编译技术有基本了解。如果事先了解过ELF格式、RISC-V或其他指令集、相关ABI文档，那么都算是加分项。
远程实习，不需要坐班。


### BJ68 OpenWrt RISC-V 移植及观测实习生【已满】

### BJ67 操作系统RISC-V成熟度观测实习生（跟踪所有国内外知名Linux发行版）【已满】

### BJ66 科技文档翻译实习生（日语、韩语）【已满】

### BJ60 开源技术社区运营经理实习生（1-2名）【已满】

### BJ59 开源软件项目经理实习生（1-2名）【已满】

### BJ33 Spidermonkey 开发实习生【取消】

### NJ55 开源EDA实习生【取消】

### BJ39 Web 前端开发实习生【已满】

### NJ53a openEuler RISC-V 操作系统构建实习生【已满】
