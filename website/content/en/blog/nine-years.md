---
title: Nine years of one repository
date: 2026-10-31T10:00:00+08:00
sub: From robotics assignments to a RISC-V talent system — this is how the line grew
description: From a 2017 wiki of robotics assignments to the 2026 Five-Colour Stone Project, the weloveinterns repository has carried four signboards and seen several teams come and go over nine years; the only continuity is people.
aliases: ["/story/"]
tags: ["Retrospective"]
---

## Prologue: a wiki's birth certificate

On 2 May 2017 the repository held three things: a README, a Home page and a sidebar. What it recorded then was a group of interns doing robotics: ROS navigation and mapping, grasping with the XBot robot, MACE and GluonCV inference running on Android, an opencv.js browser demo, YOLO ported to phones, notes on trying TensorRT, and speech recognition experiments with PocketSphinx.

One detail in those files captures the context particularly well: the coding-conventions directory was called `droid_coding_norm`, and inside were `droid_cpp_template.cpp`, `droid_py_template.py` and `ros_package_template.xml`. "droid" was not the robotics droid but the English name of **Zhongke Chongde**. The repository's author worked there at the time — on his later CV, the company for that period is written as "Zhongke Chongde".

In 2017 the repository produced 254 commits, the busiest year in its history. One person, one wiki, a group of interns doing robotics — that is how the repository's first year was filled.

## Chapter one: 2019, PLCT Lab and a strange grading system

In 2019 Wu Wei had a new signboard: **PLCT Lab** (Programming Language and Compilation Technology Laboratory) at the Institute of Software, Chinese Academy of Sciences. The repository's centre of gravity shifted with it — `plct-interns.md` appeared, and robotics reports slowly gave way to compilers and toolchains.

Also on 14 March that year, the repository published for the first time something very short that would later have a deep influence: "How we grade interns' capability". It borrowed the setting of Tokiwadai Middle School in *A Certain Scientific Railgun* and split interns into six levels, **LV0 to LV5**:

- **LV5 Super Ability** — can break a problem down and marshal resources independently, lead a development group and guarantee delivery;
- **LV4 Great Ability** — can take on module-level development independently, and debug, locate and fix large systems such as LLVM on their own; can notice and point out mistakes made by LV4 and above;
- **LV3 Strong Ability** — the bar is written concretely: **"able to analyse a bug or crash independently"**;
- **LV2 Esper** — can use git to collaborate with a team and complete development tasks assigned by a mentor within a week; this is the default recruitment bar;
- **LV1 / LV0** — offers are generally not made.

This grading is assessed by the lead as a "benevolent dictator", with input from mentors and LV4+ interns. There is one criterion: can you complete the day-to-day development work of a joint-programme host — **"abilities the joint internship host does not need are outside the assessment"**.

A document in 2019 dared to write this because there was a real building site behind it: GCC, Binutils, LLVM, QEMU, glibc, V8, Gem5, Gentoo, Arch Linux, openEuler. The levels are not certificates; they are a division of labour.

## Chapter two: 2022, "let glory fall on the blade's edge"

On 27 March 2022 the repository published a new category: **senior interns**. The first of the reasons given is nine characters long:

> Let glory fall on the blade's edge.

The second and third reasons are more practical, and show the manager's anxiety more clearly: the existing "monthly observation of externally visible delivery" can see code and PRs but cannot see invisible output such as **peer mentoring, cross-team help and maintaining relationships**; and what the team really needs is to move people who have already proved themselves out of "simple work that produces a result in a month" and into work that is hard, slow and may not show a result that month.

So what senior interns receive is not an honorary title but a promise: **the monthly stipend is never below the baseline, only above it**.

In the same period an ecosystem grew up in the studio that is hard to reproduce today: the TARSIER operating system team, the simulator team, the Arch team, the Gentoo team, the LLVM team, the GCC team, the CAAT team, the oerv team, the Aya team… and a club that called itself the "Wenwen News Agency" (`bunbun.md`), working on the Aya programming language and a theorem prover, with a recruitment notice that read like a technical blog and a club flyer at once: "Only by implementing a feature and then using it to write code ourselves can we build an intuitive sense of whether the thing is 'any use'."

This group later became the LV5 and LV4+ names on the list: maintainers of large numbers of packages on Arch Linux RISC-V, the author of the LuaJIT RISC-V port, the lead of RustSBI, the person who submitted mainline kernel support for the K230, the person who made eunomia-bpf a community.

## Chapter three: 2023, gathering and scattering

In June 2023 PLCT Lab went through its first big layoff since founding and entered a long period of financial contraction. The consequences are written directly in the repository:

- **Kubuds** was founded. Two co-founders: Li Weiwei from PLCT's simulator team, Wang Junqiang from the TARSIER operating system team — both disbanded first, then set out again.
- The **TARSIER team** disbanded between June and August 2023.
- On 15 September 2023, a commit was titled "Remove non-PLCT content, simplify README and related internship process description".

This is the most honest thing about the repository: it does not pretend to be a curve that only goes up. Teams form, swell, disband, form again, and each time leaves a seam in git. After the seam, the repository is still there, and the recruitment is still there.

## Chapter four: 2024, Project Jiachen

On 8 June 2024 Project Jiachen announced a new project: **joint open-source internship recruitment and training**. In the original words, "member organisations accelerate the RISC-V ecosystem work that matters to their own business with the smallest possible spend of money and management resources"; from the Jiachen Dragon year, more than 2,000 internship places open each year.

On 19 July 2024 weloveinterns added an introduction to Project Jiachen. From then on it was no longer just PLCT's recruitment page but the entrance to the whole of Project Jiachen — positions from dozens of member organisations go out through this repository.

On 12 October that year the repository did a subtraction: 253 files were deleted, intern reports from 2021 and earlier were gathered up, including the whole `archives/` from the Zhongke Chongde period. The sentence left in the README reads a little movingly today:

> If you are interested, or want to find a report you submitted, you can clone this repository and `git checkout -b old-happy-time 664048d`.

`old-happy-time` — the good old days.

## Chapter five: 2025 to 2026, from "screening" to "training"

In December 2025 the PLCT Lab brand was retired. A name used for six years left the stage; recruitment and training did not stop, but continued under Project Jiachen.

On the first day of the Bingwu Horse year, 2026, Project Jiachen announced the **Five-Colour Stone Project**: the RISC-V Global Leadership Training Programme. Taking its meaning from Nüwa smelting five-colour stones to mend the sky, it works on a ten-year cycle, upgrading from "finding and screening talent" to "training talent systematically and over the long term".

In September 2026 the position numbers in the repository reached `K181`–`K185`: openEuler robotics package maintenance, openKylin embodied-intelligence cases, RT-Thread embedded, FlagOS RISC-V, RISC-V robot design. All five descriptions carry the same sentence:

> This position is part of the Five-Colour Stone Project.

The wiki that held robotics assignments nine years ago is now the registration desk for a complete ten-year talent system.

## Epilogue: why "only lazyparser is still in the same place"

Of 779 commits, 500 come from one person. It is not that he has no other identities — member of the RISC-V International Technical Steering Committee, chair of the ISA Infra HC, board member of the LLVM Foundation, founder and lead of Project Jiachen — but on this line his role has never changed: the person who reads CVs, arranges mentors, counts externally visible delivery at the end of the month, and then signs off the stipend.

Organisations scatter, brands retire, companies lay people off. What can remain in a repository is two other things:

One is **rules**: "we do not care about 985 or 211, or about your major or year ranking; selection is based entirely on ability and potential"; "we believe in women's potential in STEM and reserve at least 30% of internship places for women applicants"; the monthly stipend is assessed on externally visible output, and exceptional output is not capped. These sentences have been written from 2019 to now and have never been deleted.

The other is **by-lines**: every intern willing to be public has their name written in this repository, and now on this website. Glory is not given to abstract people; glory is given to specific people — falling on the blade, falling on those merged PRs.

The joint programme is made of iron; the interns flow through it. Those who flowed through are now maintaining your compiler.
