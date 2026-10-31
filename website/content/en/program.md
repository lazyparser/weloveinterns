---
title: How the joint programme works
sub: An on-machine test, mentor pick, LV grading, externally visible delivery and the stipend
description: "The full process of Project Jiachen's joint open-source internship programme: from sending a CV to the on-machine test, mentor pick, monthly output review and promotion."
---

## The one-sentence version

This is an internship system **with the mentor as its load-bearing wall**: positions are not issued to headcount, they are issued to a specific mentor; an internship exists only if a master is willing to pick you.

## Step one: application and first confirmation

Send your CV to `wuwei@rv2036.org` with the subject line "**position number - name - phone number - school**" (write "part-time" if you have already graduated). The body should contain a self-introduction of no more than 300 words related to the position, and a PDF CV is mandatory.{{< cite "repo" >}}

Once it arrives, four things are confirmed first: which position you are applying for, which LV you assess yourself at, the start and end dates of the internship, and what you want that is not on the CV (which company you hope to join later, or whether you plan to continue studying).

## Step two: remote on-machine test

Every technical category is tested by default: ssh into a remote Linux host, enter tmux, and solve three basic C/C++ programming problems. **If you cannot get into the test environment, you fail.**

This rule had an important update in September 2026, in these words:

> As AI coding ability has become widespread, the cultivation of coding ability is no longer emphasised; instead, we assess whether you can complete a task with AI assistance.

That is, the test no longer measures "syntax you have memorised" but **whether you can deliver with AI**.

## Step three: mentor pick (the core step)

After passing the machine test, you go into a conversation with mentors directly. This is a **two-way choice**: an internship follows a master, and the contract exists only once a master accepts you. Not being picked is not a disgrace — you can try again with another position or another mentor.

Mentors look for different things, usually including: what you want from the internship, your existing technical background, the fundamentals (networking, operating systems, compilers), and "how you want to write your CV after the internship".

## Step four: technical report and community trial

Most mentors ask candidates to prepare a 20–30 minute technical talk, attended by supervisors who ask questions; usually a week is given to prepare.

Some positions (most often LLVM-related) ask you to take a real task in the target open-source community and submit a PR; **once it is merged, the offer follows automatically**.

## Step five: contract, stipend and output review

- The internship is paid, under a labour contract; an internship certificate can be issued at the end;
- Each month your **externally visible output** is counted, the stipend for that month is agreed with your mentor, and it is paid around the 25th of the following month;
- The range is 0–5k, with normal output usually **2k–3k** before tax; exceptional output is not capped at 5k;
- Interns must be current university or college students (with a CHSI enrolment certificate); after leaving school it is called part-time and requires social insurance including work-injury cover.

"Externally visible delivery" is the key phrase of this system: it requires your work to be visible in public repositories, mailing lists or upstream communities — that is why it can be decoupled from academic credentials and tied to ability.

## LV0–LV5: how capability is graded

Grading borrows the "espers" setting of Tokiwadai Middle School and is assessed by the lead (Wu Wei, @lazyparser) as a **benevolent dictator**, with input from mentors and LV4+ interns. There is one criterion: **can you complete the day-to-day development work of a joint-programme host?**

| Level | Key requirement |
| --- | --- |
| **LV5 Super Ability** | Can analyse and break down a problem and marshal resources independently; can guide LV4 and below, lead a development team independently and guarantee delivery; in some situations is given decision-making authority |
| **LV4 Great Ability** | Can take on module-level development independently; **can debug, trace and fix large systems such as LLVM independently**; can give technical talks independently; can point out mistakes made by LV4 and above; can open up a technical direction for the team from zero to one |
| **LV3 Strong Ability** | Can take on more than a week of development independently; **can analyse a bug or crash independently (this is the entry bar for LV3)**; fluent in one main language plus a scripting language; can give public technical talks fluently |
| **LV2 Esper** | Understands data structures, algorithms and computer architecture; **can use git for team collaboration**; can complete development and testing within a week under a mentor's guidance. This is the default recruitment bar |
| **LV1 / LV0** | Offers are generally not made |

Two other markers exist: **[probationary]** means ability sits between two levels (e.g. "LV3 probationary" is above LV2 but does not fully meet LV3); **[M]** means the highest rating is based on organisational and management ability, and technical ability may be below that M level.

LV4 is the default level for hiring full-time employees — **an intern who reaches LV4 can receive an offer**.

## senior interns: paying more to people who have already proved themselves

A category added on 27 March 2022. Of the three reasons given, the first is "**let glory fall on the blade's edge**"; the second openly admits a blind spot in the system:

> The current system for observing externally visible delivery cannot observe invisible output within the team, including peer mentoring, cross-team help and maintaining relationships.

Entry conditions: more than 3 months of internship and a renewal, stable externally visible output, technical ability at LV3 or above, and taking on some decision-making and mentoring duties in the team.

## This system has been revised four times

- **2019-03-14, first version made public**: six levels established;
- **2019-12-27, second version**: raised the demand for "solving problems independently";
- **2020-06-01, third version**: wrote debugging and fault analysis into the LV3 bar;
- **2024-04-21, fourth version**: removed outdated robotics team information, softened the LV2 requirements and simplified the text.{{< cite "repo" >}}
