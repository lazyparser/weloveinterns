# 翻译交付规范（六语站点）

本文件是给译者的作业单。中文原稿是唯一事实来源，**只翻译，不新增任何事实、不新增任何链接、不改数字**。

仓库根：`/Users/hermes/weloveinterns`，站点根：`/Users/hermes/weloveinterns/website`

语言代码（目录名必须逐字一致，大小写敏感）：
`zh-Hant`（繁體中文，台灣用語） · `en`（English） · `ja`（日本語） · `ru`（Русский） · `ko`（한국어）

---

## 一、必须产出的三组文件

### 1. `website/i18n/<lang>.toml`

- 以 `website/i18n/zh.toml` 为模板，**键名与段落顺序完全一致，一个都不能少**
- 只翻译 `other = "..."` 里的字符串；保留 TOML 的 `[section.key]` 结构与双引号
- 字符串里出现的 `→`、`（`、`）`、`·` 按目标语言习惯处理（例如英文用 ` →`、半角括号）
- 示例（英文）：

```toml
[nav.interns]
other = "Interns"
```

### 2. `website/content/<lang>/` 下的 11 个 markdown 文件

对应中文原稿（`website/content/zh/` 为源）：

| 目标文件 | 中文源 |
| --- | --- |
| `_index.md` | `content/zh/_index.md` |
| `history.md` | `content/zh/history.md` |
| `interns.md` | `content/zh/interns.md` |
| `join.md` | `content/zh/join.md` |
| `mentors.md` | `content/zh/mentors.md` |
| `program.md` | `content/zh/program.md` |
| `shise-stone.md` | `content/zh/shise-stone.md` |
| `sources.md` | `content/zh/sources.md` |
| `blog/_index.md` | `content/zh/blog/_index.md` |
| `blog/nine-years.md` | `content/zh/blog/nine-years.md` |
| `blog/joint-recruitment-2024.md` | `content/zh/blog/joint-recruitment-2024.md` |

front matter 规则：

- **键名逐字保留**（`title` / `sub` / `description` / `layout` / `date` / `aliases` / `weight` 等），只翻译**值**里的人话
- `layout:`、`aliases:`、`date:`、`slug:` 的值**原样不动**
- `title` / `sub` / `description` 必须翻译（它们会出现在导航、页头、RSS 与搜索结果里）
- 正文里的短代码 `{{< cite "some-id" >}}` **原样保留、位置不动**（它渲染成来源角标，id 对应 `data/i18n/<lang>/sources.yaml`）
- 正文里的所有 URL、commit hash、GitHub handle、LV 等级、数字、日期**逐字不动**

### 3. `website/data/i18n/<lang>/` 下的 5 个 YAML

| 目标文件 | 中文源 | 要翻的字段 |
| --- | --- | --- |
| `stats.yaml` | `data/i18n/zh/stats.yaml` | 全部值（都是短语） |
| `people.yaml` | `data/i18n/zh/people.yaml` | `role` / `org` / `work` / `endorse` / `history` / `note` / `bio` / `links[].note` / `tags`（tags 保留英文技术名） |
| `projects.yaml` | `data/i18n/zh/projects.yaml` | `desc`；`name` / `url` / `tag` 不动 |
| `timeline.yaml` | `data/i18n/zh/timeline.yaml` | `title` / `desc` / `evidence` 里的描述部分；`date` / `kind` / `evidence` 中的提交号与文件名逐字保留 |
| `sources.yaml` | `data/i18n/zh/sources.yaml` | `usage` / `note`；`id` / `url` / `date` / `license` / `author` / `title` 保持原样（外部材料标题不译） |

**YAML 结构必须与中文源逐键一致**：键的顺序、列表长度、每项键集合都不能变，只改值。检查方法见第四节。

---

## 二、术语表（必须统一）

| 中文 | en | ja | ru | ko | zh-Hant |
| --- | --- | --- | --- | --- | --- |
| 甲辰计划 | Project Jiachen | 甲辰計画 | Проект Цзячэнь (Project Jiachen) | 지아천 프로젝트 | 甲辰計畫 |
| 开源实习生联合培养 | joint open-source internship programme | オープンソースインターン共同養成 | совместная программа стажировок | 오픈소스 인턴 공동 양성 | 開源實習生聯合培養 |
| 五色石工程 | Five-Colour Stone Project | 五色石プロジェクト | проект «Пятицветный камень» | 오색석 프로젝트 | 五色石工程 |
| 社区导师 / mentor | mentor | メンター | наставник | 멘토 | 社群導師 |
| 实习生 | intern | インターン | стажёр | 인턴 | 實習生 |
| 实习费 / 津贴 | stipend | インターン手当 | стипендия | 인턴 수당 | 實習津貼 |
| 能力分级 LV0–LV5 | capability levels LV0–LV5 | レベル LV0–LV5 | уровни LV0–LV5 | 레벨 LV0–LV5 | 能力分級 LV0–LV5 |
| 维护者 | maintainer | メンテナ | мейнтейнер | 메인테이너 | 維護者 |
| 上游 | upstream | 上流 | upstream | 업스트림 | 上游 |
| 让荣光落于刀锋之上（站训） | Let glory fall on the blade's edge | 栄光を刃の上に | Пусть слава ляжет на лезвие | 영광은 칼날 위에 | 讓榮光落於刀鋒之上 |

专有名词一律**不译**：`PLCT 实验室`（PLCT Lab）、`苦芽科技`（Kubuds）、`中科重德`（Zhongke Chongde）、`lazyparser`、`RISC-V`、`Fedora`、`LLVM`、`QEMU`、`GCC`、`MoonBit`、`openEuler`、`RT-Thread`、`RuyiSDK`、`openGauss`、`deepin`、`eunomia-bpf`、`bpftime`、`wasm-bpf`、所有人名与 GitHub handle。

---

## 三、语气

- 中文原稿的风格：克制、具体、把可核对的事实摆出来，不喊口号。译文必须保持同样的克制，**不要**加形容词、不要加感叹、不要营销腔、不要补原文没有的因果。
- 原稿里刻意保留的钝感、短句、破折号结构，尽量保留。
- 数字与日期格式跟随目标语言习惯（英文 `8 June 2024` 或 `2024-06-08` 均可，但全篇统一）。

---

## 四、交付前必须自检（用 python，把结果贴进最终报告）

```python
import yaml, glob, os, unicodedata
lang = "<你的语言代码>"
base = "/Users/hermes/weloveinterns/website"

# 1) YAML 与中文源逐键对比
for name in ["stats","people","projects","timeline","sources"]:
    zh = yaml.safe_load(open(f"{base}/data/i18n/zh/{name}.yaml", encoding="utf-8"))
    tr = yaml.safe_load(open(f"{base}/data/i18n/{lang}/{name}.yaml", encoding="utf-8"))
    def shape(o):
        if isinstance(o, dict):  return {k: shape(v) for k, v in o.items()}
        if isinstance(o, list):  return [shape(v) for v in o]
        return None
    assert shape(zh) == shape(tr), f"{name}.yaml 结构不一致"
    print(f"  ok {name}.yaml 结构一致")

# 2) i18n 键集合必须与 zh.toml 完全相同
import tomllib
zh_keys = set()
for sec, kv in tomllib.load(open(f"{base}/i18n/zh.toml","rb")).items():
    if isinstance(kv, dict):
        zh_keys |= {f"{sec}.{k}" for k in kv}
tr_keys = set()
for sec, kv in tomllib.load(open(f"{base}/i18n/{lang}.toml","rb")).items():
    if isinstance(kv, dict):
        tr_keys |= {f"{sec}.{k}" for k in kv}
missing = zh_keys - tr_keys
assert not missing, f"i18n 缺键: {sorted(missing)}"
print(f"  ok i18n 键齐全 ({len(tr_keys)} 个)")

# 3) 11 个 md 都在，且 front matter 能解析
need = ["_index.md","history.md","interns.md","join.md","mentors.md","program.md",
        "shise-stone.md","sources.md","blog/_index.md","blog/nine-years.md","blog/joint-recruitment-2024.md"]
for f in need:
    p = f"{base}/content/{lang}/{f}"
    assert os.path.exists(p), f"缺文件 {f}"
    t = open(p, encoding="utf-8").read()
    assert t.startswith("---"), f"{f} 没有 front matter"
    fm = t.split("---",2)[1]
    yaml.safe_load(fm)
print(f"  ok 11 个页面齐全，front matter 均可解析")

# 4) 拉丁/西里尔/韩文页面里不应残留大段中文（专有名词除外）
if lang in ("en","ru","ko"):
    bad = []
    for f in need:
        t = open(f"{base}/content/{lang}/{f}", encoding="utf-8").read()
        han = sum(1 for ch in t if '\u4e00' <= ch <= '\u9fff')
        if han > 40: bad.append((f, han))
    print("  中文字符统计:", bad if bad else "无异常")
```

第 4 项如果报出某页中文字符很多，通常是整段没翻或复制粘贴漏改，必须回去重翻。

---

## 五、绝对不要做的事

- 不要 `git add` / `commit` / `push` / 建分支 —— 提交由主控统一做
- 不要运行 `hugo` / `make` —— 构建由主控统一做
- 不要改 `website/layouts/**`、`website/hugo.toml`、`website/assets/**`、`website/static/**`
- 不要改 `content/zh/**`、`data/i18n/zh/**`、`i18n/zh.toml`（中文是事实来源）
- 不要碰别的语言目录（`content/en` 只归英文译者，等等）
- 不要为了「读起来更顺」删掉原稿里有的事实句，也不要合并段落

## 六、最终报告要求

返回：语言代码、写了哪些文件（绝对路径或相对仓库路径）、上面自检脚本的真实输出、以及任何你拿不准的译法（列出来，别自己改事实）。
