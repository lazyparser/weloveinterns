---
title: Five-Colour Stone Project
sub: It starts with one sentence — "in an age of rapid AI progress, give young people a hand"
description: The origins of the Five-Colour Stone Project, its causal link to the contraction of entry-level positions, and its place in Project Jiachen's support system — every external fact carries a source.
---

## 1. The exact words on that slide

On 16 August 2026, at the CCF Open Source Software Conference, one slide of a 56-page talk carried only two lines:

> **The Five-Colour Stone Project's positioning:**
> **In an age of rapid AI progress, give young people a hand**

Four months earlier, on 5 April 2026, at the opening ceremony of the QEMU training camp, the same thing was put another way, and more concretely:

> You're right about all of it, but right now I'm missing the first opportunity, the first stepping stone.
> "You don't know how many CVs you have to send now before you get one interview."
> "You don't know how many interviews you have to go through now before there is a chance to discuss salary."

{{< cite "ccf-deck" >}}{{< cite "gotc-deck" >}} Put the two passages together and the project's origin is complete: **it is not "AI is here, so we must train AI talent", it is "AI has narrowed the entrance, so we build young people a stepping stone".**

Below, that sentence is broken into three parts that can be checked.

## 2. Judgement one: entry-level positions really are contracting

The Stanford Digital Economy Lab has followed ADP payroll data through June 2026; its August 2026 update gives a set of ugly numbers:

- In occupations highly exposed to AI, employment for **22–25-year-olds** is **19% lower** than it would have been had they grown in step with less-exposed peers of the same age; the gap was 15% in the July 2025 data, so it widened within a year;
- Experienced workers show no comparable gap;
- Employment of 22–25-year-olds in the two most-exposed quintiles **fell by about 11%** from November 2022 to June 2026, while their peers in the three least-exposed quintiles **rose by about 10%**;
- The change comes **mainly from slower hiring, not from more layoffs**.{{< cite "stanford-canaries" >}}

Anthropic's own research is more cautious: it did not see a systematic rise in unemployment in highly exposed occupations, but it likewise acknowledges that "hiring of young workers has slowed in affected occupations".{{< cite "anthropic-labor" >}}

The two accounts look inconsistent but point to the same movement: **the stock has barely moved; the entrance is narrowing.** For a 22-year-old, the difference between those two things is "do I still get a first chance". What this site offers here is a judgement, not a conclusion from the data: slower hiring is quieter than layoffs, because it produces no news, only a batch of people who have sent many CVs and heard nothing.

## 3. Judgement two: what got cheap is not "code" but the ticket that says "can write code"

In Stack Overflow's 2025 survey, 84% of respondents are using or planning to use AI tools in their development workflow, up from 76% a year earlier; 51% of professional developers use them daily.{{< cite "so-survey-2025" >}}

Accounts from the industry are more direct: coding AI has made writing code extremely cheap and convenient; the bottleneck in product development has moved from **implementation** to **review**; the number of prototypes has exploded; the traditional waterfall from requirements document to code no longer exists; two new roles have appeared — "builder" and "reviewer" — and "to stay competitive, everyone has to adopt coding AI".{{< cite "hwchase17" >}}

This means: what a newcomer can get in exchange for "I can write code in some language" is shrinking. And what is scarce at the other end is put like this in the talk:

> Developers who can handle software complexity are scarce worldwide (open-source community leaders are the scarcest of the scarce).
> And we do not know how to train these people effectively at scale either.

{{< cite "gotc-deck" >}}

This admission matters — it concedes "we don't know either". So the Five-Colour Stone is not a proven answer but a public experiment.

## 4. Judgement three: the gap is not an argument, it is that first stepping stone

Bring the scene to China: the 2026 cohort of ordinary higher-education graduates is projected at **12.7 million**, up 480,000 year on year.{{< cite "moe-1270" >}}

So "give a hand" in this context is not abstract encouragement. The list the talk offers young people is plain: treat AI as a tool and a partner, treat yourself as a brand and a platform, do not expect to stay at one company until retirement, the half-life of knowledge is shrinking, and "curiosity really matters".{{< cite "gotc-deck" >}}

Beyond those points, the one thing that can actually change someone's situation is: **a first internship with a mentor, a real upstream task and output**. That is the stepping stone, and it is the one thing this repository has been producing at scale for nine years.

## 5. So the Five-Colour Stone exists: three different choices

On the first day of the Bingwu Horse year, 2026, Project Jiachen formally announced the **Five-Colour Stone Project** (full name: Project Jiachen RISC-V Global Leadership Training Programme).{{< cite "jiachen-wucai-shi" >}} Compared with the usual "talent training programme", it differs in three obvious ways:

**The time scale is ten years, split into four stages.** 2026–2028: complete three cohorts and formally hire and train more than 50 people; 2029–2030: train 2,000 people, and build core-developer and successor pipelines with more than 50 open-source communities worldwide; 2031–2033: more than 5,000 people and more than 500 resident mentors; 2034–2036: 10,000 people and more than 2,000 mentors.

**It starts in the first or second year of university.** Not people looking for an internship three months before graduation, but people who have just entered university and still have four years to grow. The curriculum runs from computer fundamentals and chip design to open-source software development and community operations.

**The relationship is "agent-like", strict in, loose out, and free.** In the announcement's words: after a strict admission screen, once in the training track a student may "withdraw freely at any time, with no binding constraint and no penalty clause"; no agency fee is charged during study or for ten years after graduation. For ten years after graduation it also provides career planning, position upgrades and high-end headhunting introductions.

Together, these three answer the most uncomfortable question in judgement one: if the entrance is narrowing, **move the preparation earlier and extend the service period later**.

## 6. The name: Nüwa smelts five-colour stones to mend the sky

The announcement's explanation of the name is worth quoting in full:

> Legend has it that in remote antiquity the sky collapsed and the earth cracked, the four pillars failed and the nine provinces split… Nüwa smelt five-colour stones to mend the blue sky, and cut the legs of the giant turtle to set up the four pillars… The story first appears in the *Huainanzi*, "Lanming xun", of the Western Han… In the RISC-V era we borrow its meaning: through systematic training, to fill the "hole in the sky" of global open-source talent.

And what the "hole in the sky" means is made clear in the same paragraph: the new generation of technical talent should "fill the gap left by the **ageing maintainer community** of the global open-source ecosystem".{{< cite "jiachen-wucai-shi" >}}

That sentence is where this project meets what I care about most. This repository has a group of interns from 2019–2022 who are now upstream maintainers, community core members, technical leads at other companies. When they grow old, or no longer have time, if no one comes up behind them, what is missing is not labour but the people who **remember why it was written this way**.

## 7. Where it stands: four cornerstones, one loop

Project Jiachen has broken talent training into four cornerstones that each work on their own; the Five-Colour Stone Project connects them into one loop:

{{< stones >}}

The four cornerstones are (structure from page 44 of the CCF talk):{{< cite "ccf-deck" >}}

- **Public free training courses** — RISC-V technical courses across all categories, free for anyone to study
- **Development board drifting** — free RISC-V development boards for learning and experiments (project repository: `rv2036/riscv-board-wandering`)
- **Joint open-source internship programme** — RISC-V open-source internship positions, **with a mentor and with pay**
- **Project Jiachen talent endorsement** — public endorsement, internship and job referrals for outstanding students (endorsement number 0 is self-signed by the lead; all are publicly verifiable on GitHub)
- **Five-Colour Stone Project** — further integrates the four above, "helping fresh graduates and young people survive in the AI era"

Under Project Jiachen, member organisations have also launched other projects: the RuyiSDK developer environment, the RISC-V documentation wiki project, RVSPOC, the new 32-bit RV, the RISC-V chip security challenge, and the Tushan Project (using AI to design a high-performance RISC-V processor for laptops, targeting CPU/GPU performance per watt at the level of Apple M1, with a thousand units to be delivered before Chinese New Year 2029, the Jiyou year).{{< cite "ccf-deck" >}}

## 8. Observable commitments

The Five-Colour Stone has published three numbers that can be checked against, over ten years:

1. **Awareness** — make more than 1 million people worldwide aware of the RISC-V open-source ecosystem;
2. **Training** — attract more than 10,000 university students to sign into the training system;
3. **Leadership output** — train more than 1,000 people to become core maintainers, founders or BDFLs of well-known global open-source projects.

Admission is layered too: reaching PLCT intern level **LV3** or above, or "One Student One Chip" CBAS grade **B** or above, gets you into the candidate pool; reaching **LV4** or above (or CBAS B or above) and passing an interview assessment organised by the lead lasting no more than 3 months gets you into the training track. Once in the track, no fewer than 2 internships or collaboration opportunities at well-known companies or research institutions each year, and sponsorship for no fewer than 2 technical exchange events in China or in Japan/Korea + Southeast Asia each year.{{< cite "jiachen-wucai-shi" >}}

The LV3 bar is written very concretely in the repository: "able to analyse a bug or crash independently". That is, the ticket is not an exam score, it is **that you have once tracked a real problem to its root**.

## 9. Where this website stands

Open `open-internships.md` in the weloveinterns repository and, in the September 2026 position descriptions, one sentence is repeated five times: **"This position is part of the Five-Colour Stone Project."**{{< cite "repo" >}}

So this website's place is clear: it is a side chain of the Five-Colour Stone Project — not a prospectus (that is in the repository), but **an account that lays out the people and the years along this chain**. If what the Five-Colour Stone wants to do is "train a thousand leaders over the next ten years", this site is responsible for "in the previous nine years, more than a thousand people have already passed through here".
