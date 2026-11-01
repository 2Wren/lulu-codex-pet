<div align="center">

# Codex 水豚噜噜桌宠

**简体中文 · [English](./README.en.md)**

一只为 Codex 打造的水豚噜噜桌面宠物 · Capybara Lulu Codex pet

</div>

## 动画预览

<div align="center">

<table>
  <tr>
    <td align="center"><strong>待机</strong><br /><img src="./lulu/previews/idle.png" width="160" alt="噜噜待机动画" /><br /><code>idle</code> · 6 帧</td>
    <td align="center"><strong>招手</strong><br /><img src="./lulu/previews/waving.png" width="160" alt="噜噜招手动画" /><br /><code>waving</code> · 4 帧</td>
    <td align="center"><strong>跳跃</strong><br /><img src="./lulu/previews/jumping.png" width="160" alt="噜噜跳跃动画" /><br /><code>jumping</code> · 5 帧</td>
  </tr>
  <tr>
    <td align="center"><strong>向左移动</strong><br /><img src="./lulu/previews/running-left.png" width="160" alt="噜噜向左移动" /><br /><code>running-left</code> · 8 帧</td>
    <td align="center"><strong>执行任务</strong><br /><img src="./lulu/previews/running.png" width="160" alt="噜噜执行任务动画" /><br /><code>running</code> · 6 帧</td>
    <td align="center"><strong>向右移动</strong><br /><img src="./lulu/previews/running-right.png" width="160" alt="噜噜向右移动" /><br /><code>running-right</code> · 8 帧</td>
  </tr>
  <tr>
    <td align="center"><strong>等待输入</strong><br /><img src="./lulu/previews/waiting.png" width="160" alt="噜噜等待输入动画" /><br /><code>waiting</code> · 6 帧</td>
    <td align="center"><strong>完成待查看</strong><br /><img src="./lulu/previews/review.png" width="160" alt="噜噜完成待查看动画" /><br /><code>review</code> · 6 帧</td>
    <td align="center"><strong>失败或阻塞</strong><br /><img src="./lulu/previews/failed.png" width="160" alt="噜噜失败或阻塞动画" /><br /><code>failed</code> · 8 帧</td>
  </tr>
</table>

### 注视方向

<p align="center">
  <img src="./lulu/previews/look-directions.png" width="192" alt="噜噜的 16 个注视方向" /><br />
  <code>look directions</code> · 16 个方向
</p>

</div>

## 安装

> [!NOTE]
> 宠物保存在你的 ChatGPT 账号里，Codex 桌面端和 ChatGPT 共用同一份，在一处装好，另一处也能选。

### 方式一：让 Codex 用 Pets 插件安装（推荐）

在 Codex 里对它说：

> 用 Pets 插件帮我安装水豚噜噜：下载 <https://github.com/2Wren/lulu-codex-pet> 里的 `lulu/spritesheet.webp`，这是已经做好并校验过的精灵表，直接上传，不要重新生成或修改。名字用「水豚噜噜」，描述用 `lulu/pet.json` 里的 `description`，创建后选中它。

### 方式二：手动放进宠物文件夹

1. 克隆仓库：

   ```bash
   git clone https://github.com/2Wren/lulu-codex-pet.git
   ```

2. 打开 Codex App，进入 **Settings → Pets → Custom pets → Open folder**。
3. 将仓库中的 `lulu` 文件夹复制到打开的目录。
4. 返回 Codex App，点击 **Refresh**，然后选择水豚噜噜。

命令行安装（macOS / Linux）：

```bash
git clone https://github.com/2Wren/lulu-codex-pet.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/pets/lulu"
cp -R lulu-codex-pet/lulu/. "${CODEX_HOME:-$HOME/.codex}/pets/lulu/"
```

命令行安装（Windows PowerShell）：

```powershell
git clone https://github.com/2Wren/lulu-codex-pet.git
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$petDir = Join-Path $codexHome "pets\lulu"
New-Item -ItemType Directory -Force $petDir | Out-Null
Copy-Item ".\lulu-codex-pet\lulu\*" $petDir -Recurse -Force
```

> [!TIP]
> Codex 第一次读到这个文件夹时，会把噜噜上传到你的账号，之后显示的是账号里那份。以后再改文件夹里的文件不会同步过去，更新请看下一节。

### 方式三：只用 ChatGPT 网页版

在 **Settings → Personalization → Pet → Upload pet** 中上传 [`lulu/spritesheet.webp`](./lulu/spritesheet.webp)。上传框支持 `1536 × 2288` 的 v2 精灵表。

## 更新到新版本

拉取仓库的最新版本后，在 Codex 里对它说：

> 用 Pets 插件把我的「水豚噜噜」的精灵表更新为 `<仓库路径>/lulu/spritesheet.webp`。直接用这个文件，不要重新生成或修改，宠物 ID 保持不变。

## 文件结构

```text
lulu/
├── pet.json
├── spritesheet.webp
└── previews/
    ├── idle.png
    └── …
```

- `pet.json`：桌宠元数据（名字、描述）
- `spritesheet.webp`：v2 动画精灵表（`1536 × 2288`，8 列 × 11 行，共 73 帧），Codex 桌面端和 ChatGPT 通用
- `previews/`：README 预览图片，不影响桌宠运行

## 自己重新生成

噜噜的精灵表最初用 Codex 内置的 `$hatch-pet` 技能生成。现在官方的做法是 Codex 的 **Pets 插件**（`create-pet` / `update-pet`），格式相同。`scripts/release.py` 按 Pets 插件的规范校验精灵表，并导出 README 里的预览图：

```bash
python3 scripts/release.py --source <含 pet.json 和 spritesheet.webp 的目录>
```

## 版权声明

水豚噜噜的角色形象及相关权利归其原作者 / 权利方所有。本仓库是非官方的粉丝作品，仅供个人学习和交流使用，请勿用于商业用途；如权利方认为不妥，请联系删除。

本仓库的脚本和文档使用 [MIT License](LICENSE)；角色美术素材不在 MIT 授权范围内。
