# website/ —— weloveinterns.org

故事站。Hugo 构建，部署到 GitHub Pages。中文单语，明暗双主题，零第三方素材。

## 目录

```
website/
├── hugo.toml
├── assets/css/main.css          # 全站样式（明暗两套 CSS 变量，系统字体栈）
├── data/
│   ├── people.yaml              # 社区导师 + 杰出实习生（含 GitHub 头像直链与背书编号）
│   ├── projects.yaml            # 开源项目：甲辰计划共建 / 推荐上手
│   ├── sources.yaml             # 引用登记表：id / 出处 / URL / 用法 / 许可
│   ├── timeline.yaml            # 时间线 19 个节点，每条带证据（提交号或文件名）
│   └── stats.yaml               # 首页数字看板
├── content/
│   ├── _index.md                # 首页「关于这个站」正文
│   ├── blog/                    # 博客：_index.md + nine-years.md（一个仓库的九年）
│   ├── history.md               # 时间线页（layout: timeline）
│   ├── shise-stone.md           # 五色石工程：初衷、佐证、目标（站点主线）
│   ├── interns.md               # LV4+ / LV5 / senior interns 完整名单
│   ├── program.md               # 联合培养计划怎么运转（LV 分级、mentor pick、实习费）
│   ├── join.md                  # 怎么加入
│   └── sources.md               # 来源与许可（layout: sources）
├── layouts/
│   ├── index.html               # 首页：甲辰计划 / 联合培养 / 实习生 / 导师 / 五色石 / 项目 / 博客 / 加入 / 关于
│   ├── blog/{list,single}.html
│   ├── 404.html
│   ├── _default/{baseof,single,timeline,sources,rss}.html
│   ├── partials/{header,footer,stones,timeline,cite,avatar}.html
│   └── shortcodes/{cite,stones}.html
└── static/favicon.svg           # 自绘
```

## 本地构建

```sh
make site          # 构建到 website/public
make site-serve    # 本地预览 http://localhost:1314/
make site-check    # 构建后自检：站内链接、引用角标、来源登记条数
```

依赖：Hugo **0.147.9 extended**（与 CI 同版本）。无 Node、无 Python 依赖（自检脚本只用标准库）。

## 加一条引用

1. 在 `data/sources.yaml` 里加一项，`id` 用短横线小写；
2. 正文里写 `{{< cite "your-id" >}}`，会渲染成带上标的编号链接，指向 `/sources/#your-id`；
3. `make site-check` 会检查是否有角标指向了未登记的 id（有则 exit 1）。

编号按 YAML 里的顺序自动生成，插入新条目会让后面的编号顺移 —— 这是件小事，不用手管。

## 加一条时间线

在 `data/timeline.yaml` 里加一项：`date` / `title` / `desc` / `kind`（repo|org|program|people，决定圆点颜色）/ `evidence`（提交号、文件名或公告）。**没有证据的节点不要加** —— 这个站点的立身之本就是"能指到具体提交"。

## 素材与许可

- 页面上的图表（支撑体系闭环、favicon）全部自绘 SVG，**不放第三方图片、截图与网络字体**；
- 需要引入第三方素材时，先在仓库根的 `3rd-party/README.md` 登记 URL + SPDX + 抓取日期 + 用途，未登记不得进主分支；
- 站点正文以 **CC BY-SA 4.0** 发布，与仓库 `LICENSE` 一致（注意是 BY-SA，不是 BY）。

## 部署

`.github/workflows/pages.yml`：推 `master`/`main` 且命中 `website/**`、`scripts/**`、`3rd-party/**` 时触发，Hugo 构建 → 自检 → deploy-pages。

首次启用：GitHub 仓库 Settings → Pages → Source 选 **GitHub Actions**；Custom domain 填 `weloveinterns.org`，DNS 侧 CNAME 指向 `<用户名>.github.io`，勾选 Enforce HTTPS。未配域名前会部署在 `https://<用户名>.github.io/<仓库名>/`，`baseURL` 由 `configure-pages` 自动适配。
