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

## 手动安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/2Wren/lulu-codex-pet.git
   ```

2. 打开 Codex App，进入 **Settings → Pets → Custom pets → Open folder**。
3. 将仓库中的 `lulu` 文件夹复制到打开的目录。
4. 返回 Codex App，点击 **Refresh**，然后选择水豚噜噜。

### 命令行安装

#### macOS / Linux

```bash
git clone https://github.com/2Wren/lulu-codex-pet.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/pets/lulu"
cp -R lulu-codex-pet/lulu/. "${CODEX_HOME:-$HOME/.codex}/pets/lulu/"
```

#### Windows PowerShell

```powershell
git clone https://github.com/2Wren/lulu-codex-pet.git
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$petDir = Join-Path $codexHome "pets\lulu"
New-Item -ItemType Directory -Force $petDir | Out-Null
Copy-Item ".\lulu-codex-pet\lulu\*" $petDir -Recurse -Force
```

## 关于 Web 端

> [!NOTE]
> Codex 桌面端与 ChatGPT Web 端的自定义宠物分开管理；安装到桌面端的噜噜无法同步到 Web 端。

Web 端请下载 [`lulu/web-spritesheet.png`](./lulu/web-spritesheet.png)，然后在 **Settings → Personalization → Pet → Upload pet** 中上传。该文件是 Web 端所需的 `1536 × 1872` 透明 PNG；桌面端使用的 `spritesheet.webp`（`1536 × 2288`）不能直接上传到 Web 端。

也可让 Codex 直接帮你上传：

> 请帮我把水豚噜噜设置为 ChatGPT Web 宠物：<https://github.com/2Wren/lulu-codex-pet>。下载仓库中的 `lulu/web-spritesheet.png`，然后在我已登录的 ChatGPT Web 中进入 **Settings → Personalization → Pet → Upload pet**，完成上传并启用噜噜，最后告诉我结果。

## 文件结构

```text
lulu/
├── pet.json
├── spritesheet.webp
├── web-spritesheet.png
└── previews/
    ├── idle.png
    └── …
```

- `pet.json`：桌宠元数据
- `spritesheet.webp`：Codex v2 动画精灵表
- `web-spritesheet.png`：ChatGPT Web 端上传素材
- `previews/`：README 预览图片，不影响桌宠运行

## 自己重新生成

噜噜的精灵表由 Codex 内置的 `$hatch-pet` 技能生成，再用 `scripts/release.py` 校验并导出 Web 端素材和预览图。

## 版权声明

水豚噜噜的角色形象及相关权利归其原作者 / 权利方所有。本仓库是非官方的粉丝作品，仅供个人学习和交流使用，请勿用于商业用途；如权利方认为不妥，请联系删除。

本仓库的脚本和文档使用 [MIT License](LICENSE)；角色美术素材不在 MIT 授权范围内。
